#!/usr/bin/env python3

from typing import List

import asyncio
from . import async_generator  # Import from the previous module


async def async_comprehension() -> List[int]:
    """
    Collects 10 random numbers using an async comprehension over the
    async_generator and returns them as a list.
    """

    return [async_num async for async_num in async_generator()]
