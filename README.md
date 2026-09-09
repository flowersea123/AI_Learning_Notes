# DS_func

本仓库以 [`src/study1/DS_func.py`](src/study1/DS_func.py) 为核心，保存一组基础数据结构与算法实现。核心文件保留其现有代码、注释、编码和换行格式，不在仓库整理过程中修改。

## 内容

`DS_func.py` 不导入第三方库，也没有命令行入口或顶层执行逻辑。它公开以下类和函数：

| 名称 | 代码可确认的行为 |
| --- | --- |
| `ListNode` | 保存 `val` 和 `next` 的单链表节点 |
| `binary_search(nums, target)` | 在升序序列中查找目标值，返回索引或 `-1` |
| `bubble_sort(nums)` | 尝试原地升序排序，并返回同一个列表 |
| `reverse_linked_list(head)` | 原地反转单链表链接并返回新表头 |
| `length_of_linked_list(head)` | 返回链表节点数 |
| `is_valid_parentheses(s)` | 检查圆括号、方括号和花括号是否匹配；忽略其他字符 |
| `Queue` | 基于列表和前端索引实现的先进先出队列 |
| `merge_sort(nums, l, r)` | 原地归并排序半开区间 `[l, r)`，并返回列表 |
| `merge(nums, l, r, m)` | 合并两个相邻的有序半开区间 `[l, m)` 和 `[m, r)` |
| `factorial(n)` | 递归计算非负整数的阶乘 |
| `quick_sort(nums, l, r)` | 原地快速排序实现；返回 `None` |

## 环境与依赖

- Python 3（最低兼容版本：待补充）
- 第三方运行依赖：无

无需安装 `requirements.txt`。建议在项目根目录运行示例和测试，以便 Python 能找到 `src.study1.DS_func`。

## 使用示例

```python
from src.study1.DS_func import binary_search, merge_sort

numbers = [1, 3, 5, 7]
position = binary_search(numbers, 5)

values = [4, 1, 3, 2]
merge_sort(values, 0, len(values))
```

`DS_func.py` 本身只定义 API，直接运行文件不会输出结果。

## 测试

测试仅使用 Python 标准库，不会发起网络请求、写入外部系统或修改真实数据：

```bash
python -m unittest discover -s tests -v
```

## 已知限制

- 函数没有统一的类型注解或参数校验；调用方需要满足各函数的输入前提。
- `bubble_sort` 当前循环边界可能使部分未排序输入无法被完整排序。
- `quick_sort` 的边界参数约定没有在原文件中明确说明，且部分短区间不会被处理。修改这些行为需要改动核心文件，因此本次整理不修复。
- 项目的作者、背景和目标使用场景：待补充。

## 许可证

待补充：仓库目前没有可核验的 `LICENSE` 文件，请由维护者确认许可证后再添加。
