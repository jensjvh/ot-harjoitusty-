from build import build
import os


def pytest_configure():
    build()
    print(f"DATABASE_PATH: {os.getenv('DATABASE_FILENAME')}")