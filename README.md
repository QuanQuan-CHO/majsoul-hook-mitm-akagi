# majsoul-hook-mitm

mhm 使用 Proxinject 在雀魂客户端中注入 Socks5 代理

拦截 WebSocket 连接并使用 Protobuf 进行解析

通过修改和转发数据以实现以下功能：

- [x] 兼容小助手
- [x] 本地全皮肤
- [ ] 本地昵称
- [ ] 本地寻觅
- [x] 随机星标皮肤
- [x] 支持[Akagi](https://github.com/shinkuan/Akagi)
- [x] 自动打牌
- [x] 自动开下局

## 用前须知

> _魔改千万条，安全第一条。_
>
> _使用不规范，账号两行泪。_
>
> _本插件仅供学习参考交流，_
>
> _请使用者于下载 24 小时内自行删除，不得用于商业用途，否则后果自负。_

## 支持平台

- 雀魂客户端

- 雀魂网页端

## 使用方法

安装配置 mhm 需求 Python >= 3.10

同步仓库

```bash
git clone https://github.com/lqgl/majsoul-hook-mitm.git && cd majsoul-hook-mitm

```

配置国内镜像源（可选）

```bash
python -m pip config set global.index-url https://mirror.nju.edu.cn/pypi/web/simple
```

安装依赖

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

使用 Akagi

> 到 [Discord](https://discord.gg/Z2wjXUK8bN) 下载 Akagi 提供的 bot.zip。 注: 网盘中除 v2 版本均可用，任选一个下载。解压获取 **mortal.pth** 文件，放置到 bot 文件夹中。

> 注: 3p 的 mortal.pth 及对应的 libriichi3p 文件需捐赠 Akagi 进行获取.

启动 mhm

```bash
python -m mhm
```

安装 mitmproxy 证书

> 首次启动 mhm 成功后，关闭它。
> 然后到用户目录 ~/.mitmproxy 安装证书

## 配置文件

首次启动 mhm 会自动生成配置文件 mhmp.json

可以编辑此文件以根据需求自定义设置，以下表格解释了 hook 可用的配置选项：

| 释义         | 键               | 可用值        |
| ------------ | ---------------- | ------------- |
| 启用全皮肤   | enable_skins     | true \| false |
| 启用小助手   | enable_aider     | true \| false |
| 启用伪寻觅   | enable_chest     | true \| false |
| 随机星标皮肤 | random_star_char | true \| false |

以下表格解释了 autoNextGame 可用的配置选项：

| 释义           | 键                    | 可用值                                   |
| -------------- | --------------------- | ---------------------------------------- |
| 启用自动开下局 | enable_auto_next_game | true \| false                            |
| 游戏段位场     | next_game_Rank        | copper \| silver \| gold \| jade \| king |
| 游戏人数       | next_game_number      | 4p \| 3p                                 |
| 游戏房间       | next_game_rounds      | south \| east                            |

### 有关代理模式

mhm.json 中默认代理模式为 `"mode": ["regular"]`。

使用 steam 雀魂客户端, 修改为: `"mode": ["socks5"]`, `"proxinject": { "name": "jantama_mahjongsoul", "set-proxy": "127.0.0.1:7878"}`, 这里的 7878 端口是`mitm`监听的端口。

网页加载慢可尝试使用上游代理，可以更改为 `"mode": ["upstream:http://127.0.0.1:7890/"]`, 示例为 clash 的 7890 端口。

## 特别感谢

- [Akagi](https://github.com/shinkuan/Akagi)
- [Avenshy](https://github.com/Avenshy/mahjong-helper-majsoul-mitmproxy)
- [PragmaTwice](https://github.com/PragmaTwice/proxinject)
- [747929791](https://github.com/747929791/majsoul_wrapper)
- [EndlessCheng](https://github.com/EndlessCheng/mahjong-helper)

## 更新内容说明

本项目是 [majsoul-hook-mitm](https://github.com/anosora233/majsoul-hook-mitm) 和 [Akagi](https://github.com/shinkuan/Akagi) 的聚合版本。在 **majsoul-hook-mitm** 项目的基础上增加了对 **Akagi** 项目中 mortal 模型的支持与自动打牌功能支持，与 **Akagi** 项目中的不同是无美观好看的终端界面。

## Discord 交流群

- [majsoul-hook-mitm](https://discord.gg/NTXFtuRK)

- [Akagi](https://discord.gg/Z2wjXUK8bN)