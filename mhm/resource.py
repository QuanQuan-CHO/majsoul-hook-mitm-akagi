from collections import defaultdict
from typing import Literal

from google.protobuf.json_format import MessageToDict
from google.protobuf.message import Message

from .proto import config_pb2, sheets_pb2

SheetNames = Literal[
    "item_definition_loading_image",
    "item_definition_character",
    "item_definition_title",
    "item_definition_skin",
    "item_definition_item",
    "character_emoji",
    "chest_preview",
]


class ResourceManager:
    RENAME_SCROLL = 302013
    VIEW_CATEGORY = 5

    def __init__(self, lqbin: bytes, version: str, no_cheering_emotes) -> None:
        self.no_cheering_emotes = no_cheering_emotes
        self.sheets_table: dict[SheetNames, list] = defaultdict(list)
        self.version = version
        
        config_table = config_pb2.ConfigTables()
        config_table.ParseFromString(lqbin)

        for data in config_table.datas:
            klass_words = f"{data.table}_{data.sheet}".split("_")
            klass_key = "_".join(klass_words)

            if klass_key in SheetNames.__args__:
                klass_name = "".join(n.capitalize() for n in klass_words)
                klass: Message = getattr(sheets_pb2, klass_name)

                for buffer in data.data:
                    message: Message = klass()
                    message.ParseFromString(buffer)

                    message_dict = MessageToDict(
                        message,
                        including_default_value_fields=True,
                        preserving_proto_field_name=True,
                    )

                    self.sheets_table[klass_key].append(message_dict)

    def build(self):
        self.skin_map = defaultdict(list)
        for row in self.sheets_table["item_definition_skin"]:
            self.skin_map[row["character_id"]].append(row["id"])
        self.skin_rows = [n for m in self.skin_map.values() for n in m]

        self.extra_emoji_map = defaultdict(list)
        for row in self.sheets_table["character_emoji"]:
            self.extra_emoji_map[row["charid"]].append(row["sub_id"])
        if self.no_cheering_emotes:
            exclude = set(range(13, 19))
            for emotes in self.extra_emoji_map.values():
                emotes[:] = sorted(set(emotes) - exclude)

        self.character_map = {
            m["id"]: {
                "charid": m["id"],
                "skin": m["init_skin"],
                "extra_emoji": self.extra_emoji_map[m["id"]],
                "level": 5,
                "exp": 1,
                "is_upgraded": True,
                "rewarded_level": [],
                "views": [],
            }
            for m in self.sheets_table["item_definition_character"]
        }
        self.character_rows = list(self.character_map.values())

        self.item_rows = [ResourceManager.RENAME_SCROLL]
        for row in self.sheets_table["item_definition_item"]:
            if row["category"] == ResourceManager.VIEW_CATEGORY:
                self.item_rows.append(row["id"])
        for row in self.sheets_table["item_definition_loading_image"]:
            self.item_rows.append(row["unlock_items"][0])
        self.bag_rows = [{"item_id": m, "stack": 1} for m in self.item_rows]

        self.chest_map = defaultdict(lambda: defaultdict(list))
        for row in self.sheets_table["chest_preview"]:
            self.chest_map[row["chest_id"]][row["type"]].append(row["item_id"])

        self.title_rows = [m["id"] for m in self.sheets_table["item_definition_title"]]
        return self