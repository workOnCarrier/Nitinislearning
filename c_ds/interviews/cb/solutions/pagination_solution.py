"""Offset paginator implementation."""
from __future__ import annotations

from math import ceil
from typing import Any, List


class OffsetPaginator:
    def __init__(self, items: List[Any], page_size: int):
        if page_size <= 0:
            raise ValueError("page_size must be positive")
        self.items = list(items)
        self.page_size = page_size
        self.total_pages = ceil(len(self.items) / page_size) if self.items else 1

    def get_page(self, page_number: int) -> dict:
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("page_number out of range")
        start = (page_number - 1) * self.page_size
        end = start + self.page_size
        items = self.items[start:end]
        next_page = page_number + 1 if page_number < self.total_pages and items else None
        return {
            "page": page_number,
            "items": items,
            "next_page": next_page,
            "total_pages": self.total_pages,
        }
