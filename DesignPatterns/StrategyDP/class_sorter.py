from DesignPatterns.StrategyDP.bubble_sort import BubbleSort
from DesignPatterns.StrategyDP.factory.sorting_factory import SortingFactory
from DesignPatterns.StrategyDP.quick_sort import QuickSort


class Sorter:

    def sort_data(self, data, algo):
        # if algo == 'bubble':
        #     return BubbleSort().sort(data)
        #
        # if algo == 'quick':
        #     return QuickSort().sort(data)

        '''
            We have multiple if conditions here.
            If we need to add new sorting algo, then 
            we need to add more if conditions.
            Hence here OCP is breaking.
            
            Even though we need to add more if conditions 
            that should be managed by us not the client.
            So include a factory that will decide the 
            required algorithm.
        '''

        strategy = SortingFactory.getSortingObj(algo)
        strategy.sort(data)