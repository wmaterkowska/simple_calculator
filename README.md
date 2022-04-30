# simple calculator

These examples are intended to be self-explanatory to a Python developer, with minimal setup - In addition to Python 2.7 or 3.6+, you'll also need `pytest` and the `pytest-mock` plugin installed to use all these examples, which you can install by running:

```
pip install -r requirements.txt
```

In this folder (ideally, inside a virtual environment, to keep this from affecting your local Python libraries).

Once you've got all the requirements in place, you should be able to simply run

```
pytest
```

In this folder, and see 3 items being collected, and 109 tests passing, in each of the example files, in less than a second.

(PyTest will list the names of each test module file that it found, and then a period for each test case that passed, or other symbols for tests that failed, were skipped, etc.)