# Python Variable Annotations

This project contains a series of tasks to practice Python type annotations and enforce type checking using `mypy`. Each task is designed to enhance the understanding of Python's type system and improve code quality by making it more readable and less prone to errors.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` style (version 2.5)
- All files must be executable
- The length of the files will be tested using `wc`
- All modules should have a documentation string
- All classes should have a documentation string
- All functions (inside and outside a class) should have a documentation string

## Tasks

### 0. Basic annotations - add

File: `0-add.py`

Write a type-annotated function `add` that takes two floats `a` and `b` as arguments and returns their sum as a float.

### 1. Basic annotations - concat

File: `1-concat.py`

Write a type-annotated function `concat` that takes two strings `str1` and `str2` as arguments and returns their concatenated string.

### 2. Basic annotations - floor

File: `2-floor.py`

Write a type-annotated function `floor` that takes a float `n` as an argument and returns the floor of the float.

### 3. Basic annotations - to string

File: `3-to_str.py`

Write a type-annotated function `to_str` that takes a float `n` as an argument and returns the string representation of the float.

### 4. Define variables

File: `4-define_variables.py`

Define and annotate the following variables with the specified values:
- `a`: an integer with a value of `1`
- `pi`: a float with a value of `3.14`
- `i_understand_annotations`: a boolean with a value of `True`
- `school`: a string with a value of `“Holberton”`

### 5. Complex types - list of floats

File: `5-sum_list.py`

Write a type-annotated function `sum_list` which takes a list `input_list` of floats as an argument and returns their sum as a float.

### 6. Complex types - mixed list

File: `6-sum_mixed_list.py`

Write a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

### 7. Complex types - string and int/float to tuple

File: `7-to_kv.py`

Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`, and the second element is the square of the int/float `v` annotated as a float.

### 8. Complex types - functions

File: `8-make_multiplier.py`

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by `multiplier`.

### 9. Let's duck type an iterable object

File: `9-element_length.py`

Annotate the function `element_length`'s parameters and return values with the appropriate types.

### 10. Duck typing - first element of a sequence

File: `100-safe_first_element.py`

Augment the function `safe_first_element` with the correct duck-typed annotations.

### 11. More involved type annotations

File: `101-safely_get_value.py`

Given the parameters and the return values, add type annotations to the function `safely_get_value`.

### 12. Type Checking

File: `102-type_checking.py`

Use `mypy` to validate the given piece of code and apply any necessary changes.

## Usage

To run the tests provided in each main file, use the following commands:

```sh
chmod +x <main_file>
./<main_file>
