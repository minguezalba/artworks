"""Package-wide test fixtures."""
from typing import Iterator

import pytest

from artworks.constants import COLLECTION_TEST
from artworks.adapters.mongodb import db


@pytest.fixture
def create_clean_test_collection() -> Iterator:
    db.create_collection(COLLECTION_TEST)
    yield
    db[COLLECTION_TEST].drop()
