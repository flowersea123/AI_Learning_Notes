# 测试输入输出是否能正常显示
print("测试成功！欢迎来到 study1/guess_number.py\n")

# ==================== 学习笔记2：猜数字小游戏 ====================
# 用到知识点：随机数、循环、条件判断（新手进阶必学）

# 导入随机数工具（系统自带，直接用）
import random

# 程序生成1-10之间的随机数字
secret_num = random.randint(1, 10)

print("========= 猜数字游戏 =========")
print("规则:我想了一个1~10的数字,你来猜!")

# 循环：一直猜，直到猜对为止
while True:
    # 获取用户输入的数字
    guess = int(input("请输入你猜的数字："))

    # 判断数字大小
    if guess > secret_num:
        print("❌ 猜大了！再试试")
    elif guess < secret_num:
        print("❌ 猜小了！再试试")
    else:
        print("🎉 恭喜你！猜对了！数字就是：", secret_num)
        break  # 结束循环

print("\n✅ 小游戏运行完成！")
