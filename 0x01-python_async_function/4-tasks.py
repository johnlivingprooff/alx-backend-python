#!/usr/bin/env python3
"""altering wait_n to use Task"""
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """returns a asyncio task"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return asyncio.create_task(tasks)
