#!/usr/bin/env python3
""""
Implementation for method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        find the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        dataset = self.dataset()
        number_pages = math.ceil(len(dataset) / page_size)

        if page > number_pages:
            return []
        indexes = index_range(page=page, page_size=page_size)
        self.dataset()
        return self.__dataset[indexes[0]: indexes[1]]
