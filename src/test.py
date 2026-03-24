"""主程序入口"""

from src.utils import greet, add_numbers


def main():
    """主函数"""
    print("=" * 50)
    print("欢迎来到 AI 学习笔记")
    print("=" * 50)
    
    # 示例 1: 问候消息
    name = "AI Learner"
    greet(name)
    
    # 示例 2: 数学计算
    result = add_numbers(10, 20)
    print(f"\n10 + 20 = {result}")
    
    print("\n" + "=" * 50)
    print("程序执行完成")
    print("=" * 50)


if __name__ == "__main__":
    main()
