"""Solution for the in-memory task management system."""
from __future__ import annotations

from copy import deepcopy
from typing import Dict, List


class TaskManagementSystem:
    def __init__(self) -> None:
        self.tasks: Dict[str, Dict[str, str | int]] = {}
        self.users: Dict[str, Dict[str, object]] = {}

    def add_task(self, task_id: str, name: str, priority: int) -> bool:
        if task_id in self.tasks:
            return False
        self.tasks[task_id] = {"task_id": task_id, "name": name, "priority": priority}
        return True

    def update_task(self, task_id: str, **fields: str | int) -> bool:
        if task_id not in self.tasks:
            return False
        self.tasks[task_id].update(fields)
        return True

    def get_task(self, task_id: str) -> Dict[str, str | int] | None:
        task = self.tasks.get(task_id)
        return deepcopy(task) if task else None

    def list_top_tasks(self, limit: int) -> List[Dict[str, str | int]]:
        ordered = sorted(self.tasks.values(), key=lambda task: (-int(task["priority"]), task["task_id"]))
        return [deepcopy(task) for task in ordered[:limit]]

    def search_tasks(self, substring: str, limit: int) -> List[Dict[str, str | int]]:
        needle = substring.lower()
        matches = [task for task in self.tasks.values() if needle in task["name"].lower()]
        matches.sort(key=lambda task: (-int(task["priority"]), task["task_id"]))
        return [deepcopy(task) for task in matches[:limit]]

    def add_user(self, user_id: str, quota: int) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = {"quota": quota, "assignments": []}
        return True

    def assign_task(self, user_id: str, task_id: str, start_time: int, ttl: int) -> bool:
        user = self.users.get(user_id)
        task = self.tasks.get(task_id)
        if not user or not task:
            return False
        active_count = sum(1 for assignment in user["assignments"] if _is_active(assignment, start_time))
        if active_count >= user["quota"]:
            return False
        user["assignments"].append(
            {"task_id": task_id, "start": start_time, "ttl": ttl, "completed": False}
        )
        user["assignments"].sort(key=lambda assignment: assignment["start"])
        return True

    def list_active_tasks(self, user_id: str, time: int) -> List[str]:
        user = self.users.get(user_id)
        if not user:
            return []
        return [assignment["task_id"] for assignment in user["assignments"] if _is_active(assignment, time)]

    def complete_task(self, user_id: str, task_id: str, time: int) -> bool:
        user = self.users.get(user_id)
        if not user:
            return False
        active_assignments = [assignment for assignment in user["assignments"] if assignment["task_id"] == task_id and _is_active(assignment, time)]
        if not active_assignments:
            return False
        assignment = min(active_assignments, key=lambda assignment: assignment["start"])
        assignment["completed"] = True
        return True

    def list_expired_tasks(self, user_id: str, time: int) -> List[str]:
        user = self.users.get(user_id)
        if not user:
            return []
        expired = [assignment["task_id"] for assignment in user["assignments"] if _is_expired(assignment, time)]
        return expired


def _is_active(assignment: Dict[str, int | str | bool], time: int) -> bool:
    if assignment["completed"]:
        return False
    return assignment["start"] <= time < assignment["start"] + assignment["ttl"]


def _is_expired(assignment: Dict[str, int | str | bool], time: int) -> bool:
    return (not assignment["completed"]) and time >= assignment["start"] + assignment["ttl"]
