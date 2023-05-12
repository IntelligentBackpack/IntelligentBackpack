import asyncio


async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)


# done callback function
def handle(task):
    print("task terminated")


async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.

    # We are using the low-level "loop.create_task()" API here because

    # we already have a reference to the event loop at hand.

    # Otherwise we could have just used "asyncio.create_task()".

    task = loop.create_task(
        set_after(fut, 1, '... world'))
    # register a done callback function
    task.add_done_callback(handle)
    fut
    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    # print(await fut)

asyncio.run(main())
