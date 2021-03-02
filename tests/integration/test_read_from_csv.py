"""Integration tests for read from csv."""

from unittest.mock import patch

from artworks.adapters.mongodb import get_artworks
from artworks.constants import COLLECTION_TEST
from artworks.interactors.artworks import read_artworks_from_csv


@patch('artworks.adapters.mongodb.COLLECTION', COLLECTION_TEST)
def test_read_from_csv(create_clean_test_collection) -> None:
    """Test read from CSV and insert in MongoDB dataset."""
    filename = 'files/db_works_test.csv'
    read_artworks_from_csv(filename)
    docs = get_artworks()

    assert [{'_id': '2141219', 'iswc': 'T-042088917-3', 'titles': [{'title': 'MALA YERBA', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'RAFAEL MENDIZABAL ITURAIN', 'role': 'Autor', 'ipi': '200703727'},
                              {'name': 'JOSE CARPENA SORIANO', 'role': 'Autor', 'ipi': '222061816'},
                              {'name': 'FRANCISCO MARTINEZ SOCIAS', 'role': 'Compositor', 'ipi': '222084113'}]},
            {'_id': '606989', 'iswc': 'T-042142495-4',
             'titles': [{'title': 'CANCION DEL MOLINO', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'A K M (AUSTRIA)', 'role': 'Compositor', 'ipi': ''},
                              {'name': 'MANUEL LOPEZ QUIROGA MIQUEL', 'role': 'Compositor', 'ipi': '18483968'},
                              {'name': 'SALVADOR VALVERDE LOPEZ', 'role': 'Compositor/Autor', 'ipi': '89546523'},
                              {'name': 'RAFAEL DE LEON ARIAS DE SAAVEDRA', 'role': 'Autor', 'ipi': '17821298'},
                              {'name': 'ANDRE BADET DE', 'role': 'Autor', 'ipi': '1780714'}]},
            {'_id': '91695', 'iswc': 'T-035019001-0',
             'titles': [{'title': 'AL PIE DE MI TUMBA', 'type': 'OriginalTitle'}],
             'right_owners': [{'name': 'VICTOR CORDERO AURRECOECHEA', 'role': 'Compositor/Autor', 'ipi': '6771296'},
                              {'name': 'EDIT MEX DE MUSICA INT S A', 'role': 'Editor', 'ipi': '159586128'}]},
            {'_id': '2595145', 'iswc': 'T-042650830-6', 'titles': [{'title': 'BATIRI RCA', 'type': 'OriginalTitle'},
                                                                   {'title': 'BATIRI', 'type': 'AlternativeTitle'}],
             'right_owners': [{'name': 'MAXIMILIANO MORE BARTOLOME', 'role': 'Compositor/Autor', 'ipi': '68238360'},
                              {'name': 'EDIT MEX DE MUSICA INT S A', 'role': 'Editor', 'ipi': '159586128'}]},
            {'_id': '611321', 'iswc': 'T-042164479-2',
             'titles': [{'title': 'CHA CHA CHA DE BAHIA', 'type': 'OriginalTitle'},
                        {'title': 'CHA CHACHA EN BAHÍA', 'type': 'AlternativeTitle'},
                        {'title': 'CHA CHACHA EN BAHIA', 'type': 'AlternativeTitle'},
                        {'title': 'CHACHACHA EN BAHIA', 'type': 'AlternativeTitle'}],
             'right_owners': [{'name': 'ENRIQUE JESUS JORRIN Y OLEAGA', 'role': 'Compositor/Autor', 'ipi': '15546498'},
                              {'name': 'EDMOND DAVID BACRI', 'role': 'Adaptador', 'ipi': '1772516'}]}] == docs
