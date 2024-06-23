# Python Async Functions

Async functions in Python allow you to write asynchronous code that can run concurrently. They are defined using the `async` keyword before the function definition.

To use an async function, you need to await it using the `await` keyword. This allows other code to run while waiting for the async function to complete.

Here's an example of an async function that simulates a network request:

```python

import asyncio

async def fetch_data(url):
    # Simulate network delay
    await asyncio.sleep(1)
    return f"Data fetched from {url}"

async def main():
    url = "https://example.com"
    data = await fetch_data(url)
    print(data)

asyncio.run(main())
```

In the above code, the `fetch_data` function is defined as an async function. It uses the `await` keyword to pause execution while waiting for the `asyncio.sleep(1)` call to complete. This simulates a network delay of 1 second.

The `main` function is also defined as an async function. It calls the `fetch_data` function using `await` and prints the returned data.

To run the async code, we use `asyncio.run(main())`. This will execute the `main` function and wait for it to complete.

Async functions are useful when dealing with I/O-bound operations, such as network requests or file operations, where waiting for the operation to complete would otherwise block the execution of other code.
