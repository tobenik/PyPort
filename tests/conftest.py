import pytest
import os

# Define the custom fixture
@pytest.fixture(autouse=True)
def set_test_mode():
    # Set the environment variable to the test mode value
    os.environ["PYPORT_TEST_MODE"] = "True"
    yield
    # Clean up after the tests (optional)
    os.environ.pop("PYPORT_TEST_MODE")