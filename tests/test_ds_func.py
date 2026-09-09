import unittest

from src.study1.DS_func import (
    ListNode,
    Queue,
    binary_search,
    bubble_sort,
    factorial,
    is_valid_parentheses,
    length_of_linked_list,
    merge_sort,
    quick_sort,
    reverse_linked_list,
)


class DSFuncSmokeTests(unittest.TestCase):
    def test_binary_search(self):
        values = [1, 3, 5, 7]
        self.assertEqual(binary_search(values, 5), 2)
        self.assertEqual(binary_search(values, 4), -1)

    def test_bubble_sort_small_input(self):
        values = [2, 1]
        result = bubble_sort(values)
        self.assertIs(result, values)
        self.assertEqual(result, [1, 2])

    def test_linked_list_helpers(self):
        head = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual(length_of_linked_list(head), 3)

        reversed_head = reverse_linked_list(head)
        self.assertEqual(
            [reversed_head.val, reversed_head.next.val, reversed_head.next.next.val],
            [3, 2, 1],
        )
        self.assertIsNone(reversed_head.next.next.next)

    def test_parentheses(self):
        self.assertTrue(is_valid_parentheses("a({[]})"))
        self.assertFalse(is_valid_parentheses("([)]"))

    def test_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertIsNone(queue.dequeue())

    def test_merge_sort(self):
        values = [4, 1, 3, 2]
        result = merge_sort(values, 0, len(values))
        self.assertIs(result, values)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)

    def test_quick_sort_observed_input(self):
        values = [3, 1, 2]
        result = quick_sort(values, 0, len(values) - 1)
        self.assertIsNone(result)
        self.assertEqual(values, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
