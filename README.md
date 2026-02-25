# Jubeat List

一个用于爬取和整理 jubeat 音乐游戏歌曲数据的 Python 工具。

## 功能

- 从 [atwiki jubeat 维基](https://w.atwiki.jp/jubeat/) 爬取歌曲信息
- 解析歌曲的标题、作曲家、BPM、各难度等级和 Note 数
- 导出多种格式的数据文件（JSON、CSV、Excel）
- 按难度等级分类提取 Lv9 和 Lv10 的谱面

## 项目结构

```
jubeat_list/
├── main.py              # 主程序入口
├── script/
│   ├── parser.py        # 网页爬取与解析
│   ├── export_suzuchan.py   # 按谱面导出数据
│   ├── Extract_10.py    # 提取 Lv10+ 谱面
│   └── Extract_9.py     # 提取 Lv9 谱面
├── output/              # 输出文件目录
│   ├── jubeat_list.json
│   ├── jubeat_list.csv
│   ├── jubeat_list_per_chart.csv
│   ├── jubeat_lv10.csv
│   ├── jubeat_lv10_by_level.xlsx
│   ├── jubeat_lv9.csv
│   └── jubeat_lv9_by_level.xlsx
└── wikipage_files/      # 缓存的网页文件
```

## 依赖

```
pandas
cloudscraper
beautifulsoup4
openpyxl
```

## 安装

```bash
pip install pandas cloudscraper beautifulsoup4 openpyxl
```

## 使用方法

运行主程序即可自动爬取数据并生成所有输出文件：

```bash
python main.py
```

## 输出说明

| 文件 | 说明 |
|------|------|
| `jubeat_list.json` | 完整歌曲列表（JSON格式） |
| `jubeat_list.csv` | 完整歌曲列表（CSV格式） |
| `jubeat_list_per_chart.csv` | 按单个谱面展开的列表 |
| `jubeat_lv10.csv` | Lv10+ 谱面列表 |
| `jubeat_lv10_by_level.xlsx` | Lv10+ 谱面（按等级分 Sheet） |
| `jubeat_lv9.csv` | Lv9 谱面列表 |
| `jubeat_lv9_by_level.xlsx` | Lv9 谱面（按等级分 Sheet） |

## 数据字段

- `title` - 歌曲标题
- `artist` - 作曲家
- `bpm` - BPM
- `bsc_level` / `adv_level` / `ext_level` - BSC/ADV/EXT 难度等级
- `bsc_note` / `adv_note` / `ext_note` - 各难度 Note 数

## 数据来源

- https://w.atwiki.jp/jubeat/pages/2334.html
- https://w.atwiki.jp/jubeat/pages/2333.html
