"""Unit tests for artworks interactors."""
from typing import List, Dict

from pytest import mark

from artworks.interactors.artworks import format_artwork_doc


@mark.parametrize(
    'artwork_rows,expected',
    [
        (
            [{'ISWC': 'T-12345',
              'ORIGINAL TITLE': 'test_artwork_orig_title',
              'ALTERNATIVE TITLE 1': 'test_artwork_alt_title',
              ' ALTERNATIVE TITLE 2': '',
              'ALTERNATIVE TITLE 3': '',
              'RIGHT OWNER': 'test_owner_1',
              'ROLE': 'test_role_1',
              'IPI NUMBER': '11111111',
              'ID SOCIETY': 11111},
             {'ISWC': 'T-12345',
              'ORIGINAL TITLE': 'test_artwork_orig_title',
              'ALTERNATIVE TITLE 1': 'test_artwork_alt_title',
              ' ALTERNATIVE TITLE 2': '',
              'ALTERNATIVE TITLE 3': '',
              'RIGHT OWNER': 'test_owner_2',
              'ROLE': 'test_role_2',
              'IPI NUMBER': '222222',
              'ID SOCIETY': 11111}],
            {'_id': 11111, 'iswc': 'T12345',
             'titles': [{'title': 'test_artwork_orig_title', 'type': 'OriginalTitle'},
                        {'title': 'test_artwork_alt_title', 'type': 'AlternativeTitle'}],
             'right_owners': [{'name': 'test_owner_1', 'role': 'test_role_1', 'ipi': '00011111111'},
                              {'name': 'test_owner_2', 'role': 'test_role_2', 'ipi': '00000222222'}]
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
