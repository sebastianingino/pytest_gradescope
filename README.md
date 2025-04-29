# Gradescope Pytest Library

A package for producing Gradescope-compatible results.json files with Pytest tests.

Forked from [ucsb-gradescope-tools/pytest_utils](https://github.com/ucsb-gradescope-tools/pytest_utils) to bring it to parity with the latest version of the [Gradescope Python Autograder](https://github.com/gradescope/gradescope-utils/) (which uses unittest).

## Usage

At the top of the file where you define your tests, put:

```python
import pytest_gradescope
from pytest_gradescope.decorators import weight, visibility, tags, ...
```

Then annotate your tests using the provided decorators.

### weight

To set the weight for a test:

```python
@weight(value)
def test_a():
```

Where `value` is a numeric value.

### number

To optionally set the number for a test (used for ordering on Gradescope):

```python
@number(value)
def test_a():
```

Where `value` is a numeric value.

### visibility

To optionally set the visibility of a test:

```python
@visibility(value)
def test_a():
```

Where `value` is 'visible', 'hidden', 'after_due_date', or 'after_published.' Default value is 'visible.'

### hide_errors

To optionally hide the errors for a test:

```python
@hide_errors(msg)
def test_a():
```

Where `msg` is a message to display instead of the error. Default value is 'Test failed'.

### tags

To optionally add extra tags to a test:

```python
@tags(value)
def test_a():
```

Where `value` is a string array. Default value is an empty array.

### leaderboard

To optionally set the leaderboard for a test:

```python
@leaderboard(column_name, sort_order="desc")
def test_a(set_leaderboard_value = None):
    set_leaderboard_value(value)
```

Where `column_name` is the name of the leaderboard column and `sort_order` is either 'asc' or 'desc', and `set_leaderboard_value` is a function that can be called to set the value for the leaderboard. If `set_leaderboard_value` is not called, the test will not contribute to the leaderboard.

### partial_credit

To optionally set partial credit for a test:

```python
@partial_credit(weight)
def test_a(set_score=None):
    set_score(partial_score)
```

Where `weight` is the weight of the test and `set_score` is a function that can be called to set the score for the test. If `set_score` is not called, the test will receive full credit if it passes, or no credit if it fails.

## Running Locally

To run locally:

```bash
> git clone https://github.com/ucsb-gradescope-tools/pytest_utils.git
> cd pytest_utils
> pip3 install -e .
```

Then, in the directory where your `test_assignment.py` lives:

```bash
> pytest
```

The results will be written to results.json.

## Example

The assignment is to create a file called `assignment.py` with a function `hello()` which returns "hello". The `test_assignment.py` file is:

```python
import pytest_utils
from pytest_utils.decorators import weight, visibility, tags
from assignment import *

class TestAssignment(object):
    @weight(10)
    def test_one(self):
        assert(hello() == "hello")
```
