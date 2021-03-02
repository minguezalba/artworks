"""Package-wide test fixtures."""
from typing import Iterator

from app import app
from flask.testing import FlaskClient
import pytest

from artworks.constants import COLLECTION_TEST
from artworks.adapters.mongodb import db


@pytest.fixture
def client() -> Iterator[FlaskClient]:
    """Fixture for using test app."""
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def create_clean_test_collection() -> Iterator:
    db.create_collection(COLLECTION_TEST)
    yield
    db[COLLECTION_TEST].drop()


@pytest.fixture
def create_fill_clean_test_collection() -> Iterator:

    test_docs = [
        {'_id': 11111, 'iswc': 'T12345',
         'titles': [{'title': 'test_artwork_orig_title', 'type': 'OriginalTitle'},
                    {'title': 'test_artwork_alt_title', 'type': 'AlternativeTitle'}],
         'right_owners': [{'name': 'test_owner_1', 'role': 'test_role_1', 'ipi': '00011111111'},
                          {'name': 'test_owner_2', 'role': 'test_role_2', 'ipi': '00000222222'}]},
        {'_id': 22222, 'iswc': 'T98765',
         'titles': [{'title': 'test_artwork_orig_title', 'type': 'OriginalTitle'},
                    {'title': 'test_artwork_alt_title', 'type': 'AlternativeTitle'}],
         'right_owners': [{'name': 'test_owner_3', 'role': 'test_role_3', 'ipi': '00033333333'},
                          {'name': 'test_owner_4', 'role': 'test_role_4', 'ipi': '00000444444'}]}
    ]

    db.create_collection(COLLECTION_TEST)
    db[COLLECTION_TEST].insert_many(test_docs)
    yield
    db[COLLECTION_TEST].drop()
