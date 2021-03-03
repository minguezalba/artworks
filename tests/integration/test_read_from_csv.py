"""Integration tests for read from csv."""

import pytest
from unittest.mock import patch

from flask.testing import FlaskClient
from pymongo.errors import BulkWriteError  # type: ignore

from artworks.constants import COLLECTION_TEST
from artworks.interactors.artworks import read_artworks_from_csv


@patch('artworks.adapters.mongodb.COLLECTION', COLLECTION_TEST)
def test_read_from_csv(client: FlaskClient, create_clean_test_collection) -> None:
    """Test read from CSV and insert in MongoDB dataset."""
    filename = 'files/artworks_test.csv'
    read_artworks_from_csv(filename)

    rv = client.get('/artworks')

    assert [{"_id": 2141219,
             "iswc": "T0420889173",
             "titles": [{"title": "MALA YERBA",
                         "type": "OriginalTitle"}],
             "right_owners": [{"name": "RAFAEL MENDIZABAL ITURAIN",
                               "role": "Autor",
                               "ipi": "00200703727"},
                              {"name": "JOSE CARPENA SORIANO",
                               "role": "Autor",
                               "ipi": "00222061816"},
                              {"name": "FRANCISCO MARTINEZ SOCIAS",
                               "role": "Compositor",
                               "ipi": "00222084113"}]
             }] == rv.json['artworks']


@patch('artworks.adapters.mongodb.COLLECTION', COLLECTION_TEST)
def test_error_read_from_csv(client: FlaskClient, create_clean_test_collection) -> None:
    """Test read from CSV and insert in MongoDB dataset."""
    filename = 'files/artworks_test.csv'

    with pytest.raises(BulkWriteError):
        read_artworks_from_csv(filename)
        read_artworks_from_csv(filename)
