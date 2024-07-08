# 0x01. Python - Async

## Description
This project involves working with asynchronous programming in Python using `asyncio`. The tasks include writing asynchronous coroutines, measuring runtime, and creating and handling tasks.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- All files must be executable
- The length of the files will be tested using `wc`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules should have a documentation
- All functions should have a documentation

## Tasks

### Task 0: The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer argument (`max_delay`, with a default value of 10) and waits for a random delay between 0 and `max_delay` seconds before returning the delay.

### Task 1: Let's execute multiple coroutines at the same time with async
Write an async routine `wait_n` that takes two integer arguments: `n` and `max_delay`. It spawns `wait_random` n times with the specified `max_delay` and returns a list of all the delays.

### Task 2: Measure the runtime
Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

### Task 3: Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

### Task 4: Tasks
Modify `wait_n` to create `task_wait_n`, which uses `task_wait_random`.

## Usage
### Running the code
```sh
# Ensure the files are executable
chmod +x 0-basic_async_syntax.py 1-concurrent_coroutines.py 2-measure_runtime.py 3-tasks.py 4-tasks.py

# Run the main files for each task to see the output
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
