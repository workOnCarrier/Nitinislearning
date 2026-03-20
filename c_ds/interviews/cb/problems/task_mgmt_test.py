"""Practice tests for the in-memory task management system."""
from __future__ import annotations

from typing import Dict, List


class TaskManagementSystem:
    def add_task(self, task_id: str, name: str, priority: int) -> bool:
        raise NotImplementedError

    def update_task(self, task_id: str, **fields: str | int) -> bool:
        raise NotImplementedError

    def get_task(self, task_id: str) -> Dict[str, str | int] | None:
        raise NotImplementedError

    def list_top_tasks(self, limit: int) -> List[Dict[str, str | int]]:
        raise NotImplementedError

    def search_tasks(self, substring: str, limit: int) -> List[Dict[str, str | int]]:
        raise NotImplementedError

    def add_user(self, user_id: str, quota: int) -> bool:
        raise NotImplementedError

    def assign_task(self, user_id: str, task_id: str, start_time: int, ttl: int) -> bool:
        raise NotImplementedError

    def list_active_tasks(self, user_id: str, time: int) -> List[str]:
        raise NotImplementedError

    def complete_task(self, user_id: str, task_id: str, time: int) -> bool:
        raise NotImplementedError

    def list_expired_tasks(self, user_id: str, time: int) -> List[str]:
        raise NotImplementedError


def make_system() -> TaskManagementSystem:
    try:
        from solutions.task_mgmt_solution import TaskManagementSystem as cls
    except ModuleNotFoundError:  # pragma: no cover
        cls = TaskManagementSystem
    return cls()


def test_assignment_flow_and_quota() -> None:
    system = make_system()
    system.add_task("t1", "Write spec", 5)
    system.add_task("t2", "Code", 10)
    system.add_task("t3", "Deploy", 7)
    system.add_user("u1", quota=2)

    assert system.assign_task("u1", "t1", start_time=0, ttl=5) is True
    assert system.assign_task("u1", "t2", start_time=1, ttl=4) is True
    assert system.assign_task("u1", "t3", start_time=2, ttl=3) is False  # quota hit

    assert system.list_top_tasks(2)[0]["task_id"] == "t2"
    assert system.search_tasks("code", 5)[0]["task_id"] == "t2"

    assert sorted(system.list_active_tasks("u1", 2)) == ["t1", "t2"]
    assert system.complete_task("u1", "t1", time=3) is True
    assert system.list_active_tasks("u1", 3) == ["t2"]
    assert system.list_expired_tasks("u1", 10) == ["t2"]

    # Completing earliest active assignment for duplicated task ids
    system.assign_task("u1", "t2", start_time=4, ttl=5)
    system.assign_task("u1", "t2", start_time=6, ttl=5)
    assert system.complete_task("u1", "t2", time=6) is True
    assert len(system.list_active_tasks("u1", 6)) == 1


def test_assignment_expiration_and_missing_entities() -> None:
    system = make_system()
    assert system.assign_task("missing", "t", 0, 1) is False
    system.add_task("t1", "Task", 1)
    system.add_user("u1", quota=1)
    assert system.assign_task("u1", "t1", start_time=0, ttl=1) is True
    assert system.list_expired_tasks("u1", time=2) == ["t1"]
    assert system.complete_task("u1", "t1", time=2) is False
