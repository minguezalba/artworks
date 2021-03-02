"""MongoDB adapter
~~~~~~~~~~~~~~~~~~~~~~~~
"""

from typing import List, Union

from pymongo import MongoClient  # type: ignore

from artworks.constants import MONGODB_URL, DATASET, COLLECTION

client = MongoClient(MONGODB_URL)
db = client[DATASET]


def insert_many_artworks(artwork_docs: List) -> None:
    """Insert artwork documents into MongoDB collection

    Args:
        artwork_docs: artwork documents to insert
    """
    db[COLLECTION].insert_many(artwork_docs)


def get_artworks(iswc_filter: Union[List, None] = []):
    """Get all artwork documents from MongoDB collection. Optionally, you can filter them by iswc code.

    Args:
        iswc_filter: List od iswc codes to filter artwork documents

    Returns:
        List of all artworks (or artworks which iswc is in iswc_filter list)
    """

    if iswc_filter:
        cursor = db[COLLECTION].find({'iswc': {'$in': iswc_filter}})
    else:
        cursor = db[COLLECTION].find()

    return [doc for doc in cursor]
