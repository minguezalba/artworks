"""Artworks routes.
~~~~~~~~~~~~~~~~~~~~~~~~
"""
from typing import Dict, Tuple

from flask import Blueprint

from artworks.interactors.artworks import get_all_artworks, get_right_owners_by_iswc

api = Blueprint('Artworks', __name__)


@api.route('/artworks/<string:iswc>/right-owners', methods=['GET'])
def get_right_owners(iswc: str) -> Tuple[Dict, int]:
    """Get list of right owners associated to the requested iswc.
    ---

    tags:
        - Artworks

    parameters:
        - name: iswc
          in: path
          type: string
          description: ISWC code to get right owners metadata from
    definitions:
      RightOwner:
        type: object
        properties:
          name:
            type: string
            description: Agent who have rights over the musical work.
          role:
            type: string
            description: Role of the right owner.
          ipi:
            type: string
            description: International identification number assigned to the right owner.
    responses:
        200:
            description: List of right owners associated to the requested iswc.
            schema:
              type: object
              properties:
                right_owners:
                  type: array
                  items:
                    $ref: '#/definitions/RightOwner'
    """
    right_owners = get_right_owners_by_iswc(iswc)
    return {'right_owners': right_owners}, 200


@api.route('/artworks', methods=['GET'])
def get_artworks() -> Tuple[Dict, int]:
    """Get list of all artwork documents existing in the collection.
    ---

    tags:
        - Artworks

    definitions:
      Title:
        type: object
        properties:
          title:
            type: string
            description: Title of the artwork
          type:
            type: string
            description: Title type, can be OriginalTitle or AlternativeTitle
      ArtworkDoc:
        type: object
        properties:
          _id:
            type: integer
            description: The primary key, a identifier assigned by the society.
          iswc:
            type: string
            description: ISWC code.
          titles:
            type: array
            description: List with the titles information
            items:
              $ref: '#/definitions/Title'
          right_owners:
            type: array
            description: List with right owner information.
            items:
              $ref: '#/definitions/RightOwner'

    responses:
        200:
            description: List of all artwork documents.
            schema:
              type: object
              properties:
                artworks:
                  type: array
                  items:
                    $ref: '#/definitions/ArtworkDoc'
    """
    artworks = get_all_artworks()
    return {'artworks': artworks}, 200
