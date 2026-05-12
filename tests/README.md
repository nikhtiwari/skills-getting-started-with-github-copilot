# Running Backend Tests

This project uses `pytest` for backend testing.

## How to run the tests

1. Make sure you have all dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Run all tests from the project root:
   ```bash
   pytest
   ```

- Do **not** use `python tests.py` — there is no such file, and tests are discovered and run by `pytest`.

## Test File Structure
- All test files are in the `tests/` directory and should be named `test_*.py`.
- Example: `tests/test_app.py`

## More info
- See https://docs.pytest.org/ for more options and usage.
