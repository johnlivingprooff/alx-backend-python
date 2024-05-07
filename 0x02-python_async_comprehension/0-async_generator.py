#!/usr/bin/env python3
"""a coroutine called async_generator that takes no arguments."""
import asyncio
import random


async def async_generator():
    """the function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
