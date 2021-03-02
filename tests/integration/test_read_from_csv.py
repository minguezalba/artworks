"""Integration tests for read from csv."""

from unittest.mock import patch

from artworks.adapters.mongodb import get_artworks
from artworks.constants import COLLECTION_TEST
from artworks.interactors.artworks import read_artworks_from_csv


@patch('artworks.adapters.mongodb.COLLECTION', COLLECTION_TEST)
def test_read_from_csv(create_clean_test_collection) -> None:
    """Test read from CSV and insert in MongoDB dataset."""
    filename = 'files/artworks_test.csv'
    read_artworks_from_csv(filename)
    docs = get_artworks()

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
             }] == docs
