#!/usr/bin/env python3
"""intro to async functions"""
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for random delay"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
