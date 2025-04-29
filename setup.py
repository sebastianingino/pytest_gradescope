from setuptools import setup, find_packages

setup(
    name="pytest_gradescope",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    # the following makes a plugin available to pytest
    entry_points={
        "pytest11": [
            "pytest_gradescope = pytest_gradescope.pytest_plugin",
        ]
    },
    # custom PyPI classifier for pytest plugins
    classifiers=[
        "Framework :: Pytest",
    ],
)
