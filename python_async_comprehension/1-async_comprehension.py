#!/usr/bin/env python3
"""
coroutine that will execute async_comprehension
four times in parallel using asyncio.gathe
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Measure the total runtime and return it"""
    list_numbers = [i async for i in async_generator()]
    return list_numbers
