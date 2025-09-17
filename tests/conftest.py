# conftest.py — keeps pytest quiet and friendly for students.
def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")
