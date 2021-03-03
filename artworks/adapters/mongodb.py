"""MongoDB adapter
~~~~~~~~~~~~~~~~~~~~~~~~
"""

from typing import Dict, List
import logging

from pymongo import MongoClient  # type: ignore
from pymongo.errors import BulkWriteError  # type: ignore

from artworks.constants import MONGODB_URL, DATASET, COLLECTION

client = MongoClient(MONGODB_URL)
db = client[DATASET]


def insert_many_artworks(artwork_docs: List) -> None:
    """Insert artwork documents into MongoDB collection

    Args:
        artwork_docs: artwork documents to insert
    """
    try:
        db[COLLECTION].insert_many(artwork_docs)
    except BulkWriteError as error:
        logging.error(error)
        raise


def get_artworks(filter_fields: Dict = dict()):
    """Get all artwork documents from MongoDB collection. Optionally, you can filter them by iswc code.

    Args:
        filter_fields: (Optional) Filters in a key-value format.

    Returns:
        List of all artworks (or artworks which iswc is in iswc_filter list)
    """
    cursor = db[COLLECTION].find(filter_fields)
    return [doc for doc in cursor]
