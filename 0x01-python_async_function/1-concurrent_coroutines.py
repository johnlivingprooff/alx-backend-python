#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """execute multiple coroutines at the same time with async"""
    tasks = [wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]