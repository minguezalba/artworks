"""Artworks routes.
~~~~~~~~~~~~~~~~~~~~~~~~
"""
from typing import Dict, Tuple

from flask import Blueprint

from artworks.interactors.artworks import get_right_owners_by_iswc

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
