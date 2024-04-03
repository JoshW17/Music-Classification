import sys
sys.path.append("/home/csj7701/Projects/Music-Classification")

from Data import ComparisonData
import os

def DuplicateTest():
    path='../test'
    test=ComparisonData(path)
    test.add_comparison('a','b',5)

    print("\nTesting direct Duplicate:")
    test.add_comparison('a','b',6)

    print("\nTesting out of order Duplicate:")
    test.add_comparison('b','a',8)

if __name__ == "__main__":
    DuplicateTest()
