# pylint: disable=W0621
"""Asynchronous Python client for Async IO Modern Forms fan."""  # noqa: D401

import asyncio
from datetime import datetime, timedelta

import aiomodernforms
from aiomodernforms.const import LIGHT_POWER_ON


async def main():
    """Example on controlling your Modern Forms Fan device."""
    async with aiomodernforms.ModernFormsDevice("192.168.3.197") as fan:
        await fan.update()
        print(fan.status)
        await fan.light(
            on=LIGHT_POWER_ON,
            brightness=50,
            sleep=datetime.now() + timedelta(minutes=2),
        )
        print(fan.status)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
