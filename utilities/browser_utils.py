import numbers
import asyncio
import time

#asynch method for sleep
async def a_sleep(seconds:numbers):
    await asyncio.sleep(seconds)
#non asynch method for sleep
def sleep(seconds):
    time.sleep(seconds)
#comparing two message types
def message_comparer(actual, expected):
    return expected == str(actual)