# AI 学习笔记

这是一个记录 AI 学习与练习过程的 Python 项目，主要用来整理知识点、实践算法和积累项目经验。

- 作者：内地大一学生
- 目标：构建可运行、可测试的学习型代码仓库
- 主要技术栈：Python、pytest、black、pylint

## 项目结构

```
.
├── src/                  # 源代码目录
│   ├── __init__.py      # 包初始化
│   ├── main.py          # 主程序入口
│   ├── tools_for_test.py # 编程练习辅助模块
│   └── study1/          # 学习代码示例
│       └── guess_number.py # 猜数字小游戏
├── tests/               # 测试目录
│   ├── __init__.py
│   └── test_utils.py    # 单元测试
├── requirements.txt     # 依赖配置
├── .gitignore           # Git忽略文件
└── README.md            # 本文件
```

## 环境准备

建议使用虚拟环境：

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# 或 macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 运行程序

```bash
python -m src.main
```

如果需要运行练习代码（如猜数字）：

```bash
python -m src.study1.guess_number
```

## 运行测试

```bash
pytest tests/
```

或使用 unittest:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## 代码检查与格式化

```bash
# 代码格式化
black src/ tests/

# 静态分析
pylint src/
```

## 贡献指南

欢迎提交 Issue 或 PR：

1. Fork 本仓库
2. 新建分支: `feat/xxx` 或 `fix/xxx`
3. 完成功能/修复并补充测试
4. 提交 PR 并描述修改内容

## 许可证

MIT License，详见 `LICENSE`（若不存在，可根据需要添加）。

> 以上内容均由AI生成。

