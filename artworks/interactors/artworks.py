"""Artworks interactors.
~~~~~~~~~~~~~~~~~~~~~~~~
"""
import csv
from collections import defaultdict
from typing import Dict, List

from artworks.constants import BATCH_SIZE
from artworks.interactors import remove_punctuation
from artworks.adapters.mongodb import insert_many_artworks, get_artworks


def format_artwork_doc(artwork_rows):
    """Transform the rows associated to the same artwork to a dictionary with the requested format.

    Args:
        artwork_rows: the rows associated to the same artwork

    Returns:
        Dictionary with the requested format
    """
    titles = []
    title_types = []
    base_row = artwork_rows[0]

    for k_row, v_row in base_row.items():
        if "TITLE" in k_row and v_row:
            titles.append(v_row)
            title_type = "OriginalTitle" if k_row == "ORIGINAL TITLE" else "AlternativeTitle"
            title_types.append(title_type)

        # keep only unique combinations of (title, title_type)
        titles_unique = {f'{title}#{title_type}' for title, title_type in zip(titles, title_types)}

    artwork_doc = {
        "_id": int(base_row["ID SOCIETY"]),
        "iswc": remove_punctuation(base_row["ISWC"]),
        "titles": [
            {"title": t.split('#')[0], "type": t.split('#')[1]}
            for t in titles_unique
        ],
        "right_owners": [
            {"name": row["RIGHT OWNER"], "role": row["ROLE"], "ipi": row["IPI NUMBER"].zfill(11)}
            for row in artwork_rows
        ],
    }

    return artwork_doc


def read_artworks_from_csv(filename: str) -> None:
    """Parse csv file defined by filename and insert the data in MongoDB dataset with the format requested.

    Args:
        filename: Name of the CSV file to parse
    """
    artworks_raw: Dict = defaultdict(list)
    last_id = None

    with open(filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if len(artworks_raw) == BATCH_SIZE and row["ID SOCIETY"] != last_id:
                artwork_docs = [format_artwork_doc(x) for x in artworks_raw.values()]
                insert_many_artworks(artwork_docs)
                artworks_raw = defaultdict(list)

            artworks_raw[row["ID SOCIETY"]].append(row)
            last_id = row["ID SOCIETY"]

    artwork_docs = [format_artwork_doc(x) for x in artworks_raw.values()]
    insert_many_artworks(artwork_docs)


def get_right_owners_by_iswc(iswc: str) -> List:
    """Get right owners metadata for the queried artwork by ISWC.

    Args:
        iswc: ISWC code to filter artwork

    Returns:
        A list with the right owners metadata.
    """
    docs = get_artworks({'iswc': iswc})
    return docs[0].get('right_owners', [])


def get_all_artworks() -> List:
    """Get all the artwork documents in MongoDB collection.

    Returns:
        A list of artwork documents.
    """
    return get_artworks()
