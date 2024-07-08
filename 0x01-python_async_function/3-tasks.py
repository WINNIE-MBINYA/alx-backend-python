#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio.Task for wait_random.
"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for wait_random with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
