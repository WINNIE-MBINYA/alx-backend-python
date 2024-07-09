# Python Async Comprehension Project

This project demonstrates the use of asynchronous programming in Python using `asyncio` and asynchronous comprehensions. It consists of three main tasks that build on each other to illustrate the concepts of async generators, async comprehensions, and measuring runtime for parallel coroutines.

## Requirements

- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the `pycodestyle` style (version 2.5.x)
  - The length of your files will be tested using `wc`
  - All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
  - A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)
  - All functions and coroutines must be type-annotated

## Tasks

### Task 0: Async Generator

**File:** `0-async_generator.py`

Write a coroutine called `async_generator` that takes no arguments. The coroutine will loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10. Use the `random` module.

**Example Usage:**
```python
#!/usr/bin/env python3

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
