"""Practice tests for the recipe management system."""
from __future__ import annotations

from typing import Dict, List

import pytest


class RecipeManagementSystem:
    def add_recipe(self, recipe: Dict[str, str | int]) -> bool:
        raise NotImplementedError

    def update_recipe(self, recipe_id: str, **fields: str | int) -> bool:
        raise NotImplementedError

    def get_recipe(self, recipe_id: str) -> Dict[str, str | int] | None:
        raise NotImplementedError

    def delete_recipe(self, recipe_id: str) -> bool:
        raise NotImplementedError

    def search_recipes(self, query: str) -> List[Dict[str, str | int]]:
        raise NotImplementedError

    def list_recipes(self, sort_by: str) -> List[Dict[str, str | int]]:
        raise NotImplementedError

    def add_user(self, user: Dict[str, str]) -> bool:
        raise NotImplementedError

    def version_history(self) -> List[Dict[str, str]]:
        raise NotImplementedError

    def rollback(self, version_id: int) -> bool:
        raise NotImplementedError


def make_system() -> RecipeManagementSystem:
    try:
        from solutions.recipe_mgmt_system_solution import RecipeManagementSystem as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = RecipeManagementSystem
    return cls()


def test_versioned_crud_flow() -> None:
    system = make_system()
    assert system.add_recipe({"recipeId": "r1", "name": "Soup", "size": 2}) is True
    system.add_recipe({"recipeId": "r2", "name": "Cake", "size": 5})
    system.update_recipe("r2", name="Chocolate Cake")
    system.add_user({"userId": "u1", "userName": "Chef"})

    assert system.get_recipe("r2")["name"] == "Chocolate Cake"
    assert [r["recipeId"] for r in system.list_recipes("name")] == ["r2", "r1"]
    assert [r["recipeId"] for r in system.search_recipes("cake")] == ["r2"]

    history = system.version_history()
    assert history[-1]["version_id"] == 4

    assert system.rollback(history[1]["version_id"]) is True
    assert system.get_recipe("r2")["name"] == "Cake"


def test_invalid_operations_and_rollback_failure() -> None:
    system = make_system()
    assert system.add_recipe({"recipeId": "r1", "name": "Pasta", "size": 3}) is True
    assert system.add_recipe({"recipeId": "r1", "name": "Duplicate", "size": 4}) is False
    assert system.delete_recipe("missing") is False
    with pytest.raises(ValueError):
        system.list_recipes("invalid")
    assert system.rollback(999) is False
