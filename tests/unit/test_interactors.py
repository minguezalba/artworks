"""Unit tests for artworks interactors."""
from typing import List, Dict

from pytest import mark

from artworks.interactors.artworks import format_artwork_doc


@mark.parametrize(
    'artwork_rows,expected',
    [
        (
            [{'ISWC': 'test_iswc',
              'ORIGINAL TITLE': 'test_artwork_orig_title',
              'ALTERNATIVE TITLE 1': 'test_artwork_alt_title',
              ' ALTERNATIVE TITLE 2': '',
              'ALTERNATIVE TITLE 3': '',
              'RIGHT OWNER': 'test_ownwer_1',
              'ROLE': 'test_role_1',
              'IPI NUMBER': 'test_ipi_1',
              'ID SOCIETY': 'test_id_society_1'},
             {'ISWC': 'test_iswc',
              'ORIGINAL TITLE': 'test_artwork_orig_title',
              'ALTERNATIVE TITLE 1': 'test_artwork_alt_title',
              ' ALTERNATIVE TITLE 2': '',
              'ALTERNATIVE TITLE 3': '',
              'RIGHT OWNER': 'test_ownwer_2',
              'ROLE': 'test_role_2',
              'IPI NUMBER': 'test_ipi_2',
              'ID SOCIETY': 'test_id_society_1'}],
            {'_id': 'test_id_society_1', 'iswc': 'test_iswc',
             'titles': [{'title': 'test_artwork_orig_title', 'type': 'OriginalTitle'},
                        {'title': 'test_artwork_alt_title', 'type': 'AlternativeTitle'}],
             'right_owners': [{'name': 'test_ownwer_1', 'role': 'test_role_1', 'ipi': 'test_ipi_1'},
                              {'name': 'test_ownwer_2', 'role': 'test_role_2', 'ipi': 'test_ipi_2'}]
             }
        ),
    ],
)
def test_format_artwork_doc(artwork_rows: List, expected: Dict) -> None:
    """Test format artwork doc function."""
    artwork_doc = format_artwork_doc(artwork_rows)
    titles = artwork_doc.pop('titles')
    expected_titles = expected.pop('titles')
    assert expected == artwork_doc
    assert sorted(expected_titles, key=lambda k: k['title']) == sorted(titles, key=lambda k: k['title'])
