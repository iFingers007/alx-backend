#!/usr/bin/env python3
"""Module for 0. Simple helper function"""

import csv
import math
from typing import List, Tuple, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns range of a page
    Args:
    page: Page Number
    page_size: Size of the page
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        """Returns a paginated page of the dataset
        """
        assert isinstance(page, int) and page > 0, "Page must be > 0"
        assert isinstance(page_size, int) and page_size > 0, "Size must be > 0"

        start, end = index_range(page, page_size)

        data = self.dataset()
        return data[start:end] if start < len(data) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:  # noqa
        """returns a dictionary containing the following key-value pairs
        """
        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
