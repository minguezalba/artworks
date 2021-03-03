"""Integration tests for testing the api routes"""

from unittest.mock import patch

from flask.testing import FlaskClient

from artworks.constants import COLLECTION_TEST


@patch('artworks.adapters.mongodb.COLLECTION', COLLECTION_TEST)
def test_get_right_owners_metadata(client: FlaskClient, create_fill_clean_test_collection) -> None:
    """Test read from CSV and insert in MongoDB dataset."""
    test_iswc = 'T98765'
    rv = client.get(f'/artworks/{test_iswc}/right-owners')
    assert rv.json['right_owners'] == [{'name': 'test_owner_3', 'role': 'test_role_3', 'ipi': '00033333333'},
                                       {'name': 'test_owner_4', 'role': 'test_role_4', 'ipi': '00000444444'}]
