"""Practice tests for designing a pagination helper."""
from __future__ import annotations

from typing import Any, List

import pytest


class OffsetPaginator:
    """Simple offset-based paginator over an in-memory list."""

    def __init__(self, items: List[Any], page_size: int):
        raise NotImplementedError

    def get_page(self, page_number: int) -> dict:
        raise NotImplementedError


def make_paginator(items: List[Any], page_size: int) -> OffsetPaginator:
    try:
        from solutions.pagination_solution import OffsetPaginator as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = OffsetPaginator
    return cls(items, page_size)


def test_pagination_edges() -> None:
    paginator = make_paginator(list(range(7)), page_size=3)
    assert paginator.get_page(1) == {"page": 1, "items": [0, 1, 2], "next_page": 2, "total_pages": 3}
    assert paginator.get_page(3) == {"page": 3, "items": [6], "next_page": None, "total_pages": 3}


def test_invalid_inputs() -> None:
    paginator = make_paginator(["a"], page_size=1)
    assert paginator.get_page(1)["items"] == ["a"]
    with pytest.raises(ValueError):
        make_paginator(["a"], page_size=0)
    with pytest.raises(ValueError):
        paginator.get_page(2)
