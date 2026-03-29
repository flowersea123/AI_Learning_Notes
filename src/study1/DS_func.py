class ListNode:  # 先定义链表节点（考试必写）
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def binary_search(nums, target):
    """
    二分查找：在有序数组中查找目标值的位置
    :param nums: 有序数组
    :param target: 目标值
    :return: 目标值在数组中的索引，如果不存在返回 -1
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
    return -1


def bubble_sort(nums):
    """
    冒泡排序：对数组进行升序排序
    :param nums: 待排序数组
    :return: 排序后的数组
    """
    n = len(nums)
    for i in range(n - 1):
        flag = False
        for j in range(i, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break
    return nums


def reverse_linked_list(head):
    """
    反转单链表
    :param head: 链表头节点
    :return: 反转后的链表头节点
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # 保存下一个节点
        curr.next = prev  # 反转当前节点指向
        prev = curr  # prev后移
        curr = next_node  # curr后移
    return prev  # 新表头


def length_of_linked_list(head):
    """
    计算链表长度
    :param head: 链表头节点
    :return: 链表长度
    """
    count = 0
    p = head
    while p:
        count += 1
        p = p.next
    return count


def is_valid_parentheses(s):
    """
    检查括号是否匹配
    :param s: 包含括号的字符串
    :return: True 如果匹配，否则 False
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char not in "()[]{}":
            continue
        if char in mapping and stack:
            top = stack.pop()
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return len(stack) == 0


class Queue:
    """
    队列类，使用列表实现
    """
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        """
        入队
        :param item: 要入队的元素
        """
        self.items.append(item)

    def dequeue(self):
        """
        出队
        :return: 出队的元素，如果队列为空返回 None
        """
        if self.is_empty():
            return None
        res = self.items[self.front]
        self.front += 1
        return res

    def is_empty(self):
        """
        检查队列是否为空
        :return: True 如果为空，否则 False
        """
        return self.front >= len(self.items)


def merge_sort(nums, l, r):
    """
    归并排序
    :param nums: 待排序数组
    :param l: 左边界
    :param r: 右边界
    :return: 排序后的数组
    """
    if l < r - 1:
        mid = (l + r) // 2
        merge_sort(nums, l, mid)
        merge_sort(nums, mid, r)
        merge(nums, l, r, mid)
    return nums


def merge(nums, l, r, m):
    """
    归并两个有序子数组
    :param nums: 数组
    :param l: 左边界
    :param r: 右边界
    :param m: 中间点
    """
    arr = []
    lp, rp = l, m
    while lp < m and rp < r:
        if nums[lp] < nums[rp]:
            arr.append(nums[lp])
            lp += 1
        else:
            arr.append(nums[rp])
            rp += 1
    arr.extend(nums[lp:m])
    arr.extend(nums[rp:r])
    for i in range(l, r):
        nums[i] = arr[i - l]


def factorial(n):
    """
    计算阶乘
    :param n: 非负整数
    :return: n 的阶乘
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


def quick_sort(nums, l, r):
    """
    快速排序
    :param nums: 待排序数组
    :param l: 左边界
    :param r: 右边界
    """
    if l >= r - 1:
        return
    p = nums[l]
    i, j = l, r
    while i < j:
        while i < j and nums[j] >= p:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= p:
            i += 1
        nums[j] = nums[i]
    nums[i] = p
    quick_sort(nums, l, i)
    quick_sort(nums, i + 1, r)
