import unittest

from sorts.bubble_sort import bubble_sort
from sorts.merge_sort import merge_sort


class BaseSortTest:
    def sort(self, data):
        return data

    def test_negative(self):
        data = [5, -4, 3, -2, 1]
        self.assertEqual(self.sort(data), [-4, -2, 1, 3, 5])

    def test_repeating_elements(self):
        data = [9, 6, 6, 1, 6, 7, 9, 7, 9, 1]
        self.assertEqual(self.sort(data), [1, 1, 6, 6, 6, 7, 7, 9, 9, 9])

    def test_empty_list(self):
        data = []
        self.assertEqual(self.sort(data), [])

    def test_big_numbers(self):
        data = [100, 5678, 34, 445557, 453, 456]
        self.assertEqual(self.sort(data), [34, 100, 453, 456, 5678, 445557])

    def test_zero_elements(self):
        data = [0, -0, 0, -0]
        self.assertEqual(self.sort(data), [-0, -0, 0, 0])

    def test_miracle_elements(self):
        data = [5, -5]
        self.assertEqual(self.sort(data), [-5, 5])


class TestBubbleSorts(unittest.TestCase, BaseSortTest):
    def sort(self, data):
        return bubble_sort(data)


class TestMergeSort(unittest.TestCase, BaseSortTest):
    def sort(self, data):
        return merge_sort(data)
