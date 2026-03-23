"""工具函数集合"""


def greet(name: str) -> None:
    """
    问候函数
    
    Args:
        name: 用户名
    """
    print(f"您好，{name}！欢迎使用本项目。")


def add_numbers(a: int, b: int) -> int:
    """
    计算两个数的和
    
    Args:
        a: 第一个数
        b: 第二个数
        
    Returns:
        两个数的和
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """
    计算两个数的积
    
    Args:
        a: 第一个数
        b: 第二个数
        
    Returns:
        两个数的积
    """
    return a * b
