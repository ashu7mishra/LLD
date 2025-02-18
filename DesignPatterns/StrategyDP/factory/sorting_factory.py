from DesignPatterns.StrategyDP.bubble_sort import BubbleSort
from DesignPatterns.StrategyDP.merge_sort import MergeSort
from DesignPatterns.StrategyDP.quick_sort import QuickSort


class SortingFactory:
    @staticmethod
    def getSortingObj(algo):
        if algo == 'bubble':
            return BubbleSort()

        if algo == 'quick':
            return QuickSort()

        if algo == 'merge':
            return MergeSort()