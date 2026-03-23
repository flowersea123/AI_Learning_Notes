# AI 学习笔记

一位内地大一学生的尝试，建立自己的代码仓库（？）。
仅用来记录AI学习的过程

## 项目结构

```
.
├── src/                  # 源代码目录
│   ├── __init__.py      # 包初始化
│   ├── main.py          # 主程序入口
│   └── utils.py         # 工具函数
├── tests/               # 测试目录
│   ├── __init__.py
│   └── test_utils.py    # 单元测试
├── requirements.txt     # 依赖配置
├── .gitignore          # Git忽略文件
└── README.md           # 本文件
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行程序

```bash
python -m src.main
```

## 运行测试

```bash
python -m pytest tests/
```

或者使用unittest:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 代码检查和格式化

```bash
# 代码格式化
black src/ tests/

# 代码检查
pylint src/
```