#!/usr/bin/env python3
"""intro to async functions"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
