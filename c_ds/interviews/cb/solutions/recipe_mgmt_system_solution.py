"""Solution for the in-memory Recipe Management System."""
from __future__ import annotations

from copy import deepcopy
from typing import Dict, List


class RecipeManagementSystem:
    def __init__(self) -> None:
        self.recipes: Dict[str, Dict[str, str | int]] = {}
        self.users: Dict[str, Dict[str, str]] = {}
        self.versions: List[Dict[str, object]] = []
        self.version_seq = 0

    def add_recipe(self, recipe: Dict[str, str | int]) -> bool:
        recipe_id = str(recipe["recipeId"])
        if recipe_id in self.recipes:
            return False
        self.recipes[recipe_id] = dict(recipe)
        self._record_version(f"add_recipe:{recipe_id}")
        return True

    def update_recipe(self, recipe_id: str, **fields: str | int) -> bool:
        if recipe_id not in self.recipes:
            return False
        self.recipes[recipe_id].update(fields)
        self._record_version(f"update_recipe:{recipe_id}")
        return True

    def get_recipe(self, recipe_id: str) -> Dict[str, str | int] | None:
        recipe = self.recipes.get(recipe_id)
        return dict(recipe) if recipe else None

    def delete_recipe(self, recipe_id: str) -> bool:
        if recipe_id not in self.recipes:
            return False
        del self.recipes[recipe_id]
        self._record_version(f"delete_recipe:{recipe_id}")
        return True

    def search_recipes(self, query: str) -> List[Dict[str, str | int]]:
        needle = query.lower()
        results = [recipe for recipe in self.recipes.values() if needle in recipe["name"].lower()]
        results.sort(key=lambda recipe: (recipe["name"].lower(), recipe["recipeId"]))
        return [dict(recipe) for recipe in results]

    def list_recipes(self, sort_by: str) -> List[Dict[str, str | int]]:
        if sort_by == "name":
            key_fn = lambda recipe: (recipe["name"].lower(), recipe["recipeId"])
        elif sort_by == "size":
            key_fn = lambda recipe: (recipe["size"], recipe["recipeId"])
        else:
            raise ValueError("sort_by must be 'name' or 'size'")
        ordered = sorted(self.recipes.values(), key=key_fn)
        return [dict(recipe) for recipe in ordered]

    def add_user(self, user: Dict[str, str]) -> bool:
        user_id = user["userId"]
        if user_id in self.users:
            return False
        self.users[user_id] = dict(user)
        self._record_version(f"add_user:{user_id}")
        return True

    def version_history(self) -> List[Dict[str, str]]:
        return [{"version_id": entry["version_id"], "action": entry["action"]} for entry in self.versions]

    def rollback(self, version_id: int) -> bool:
        snapshot = next((entry for entry in reversed(self.versions) if entry["version_id"] == version_id), None)
        if snapshot is None:
            return False
        self.recipes = deepcopy(snapshot["recipes"])
        self.users = deepcopy(snapshot["users"])
        index = self.versions.index(snapshot)
        self.versions = self.versions[: index + 1]
        self.version_seq = version_id
        return True

    def _record_version(self, action: str) -> None:
        self.version_seq += 1
        snapshot = {
            "version_id": self.version_seq,
            "action": action,
            "recipes": deepcopy(self.recipes),
            "users": deepcopy(self.users),
        }
        self.versions.append(snapshot)
