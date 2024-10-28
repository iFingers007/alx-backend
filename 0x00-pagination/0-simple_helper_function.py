#!/usr/bin/env python3
"""Module for 0. Simple helper function"""

# from Typing import Tuple

def index_range(page: int, page_size: int) -> tuple:
    """ Returns range of a page
    Args:
    page: Page Number
    page_size: Size of the page
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
