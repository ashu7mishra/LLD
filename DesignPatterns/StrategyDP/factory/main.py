from DesignPatterns.StrategyDP.class_sorter import Sorter

if __name__ == "__main__":
    sorted_data = Sorter().sort_data([1,4,3,2,7,9,5,8], 'bubble')
    print(sorted_data)
