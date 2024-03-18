#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
mandatory
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random function n times

    Args:
        n (int): number of times wait_random should be called.
        max_delay (int): maximum delay period

    Returns:
        List[float]: List of all the delays in sorted order
    """
    # gather with an unpacked list of awaitables
    res = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    # Sort result in ascending order
    res.sort()

    return res
