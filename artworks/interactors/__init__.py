"""Interactors package."""
import string


def remove_punctuation(text: str):
    """Remove punctuations characters"""
    table_ = str.maketrans('', '', string.punctuation)
    return text.translate(table_)
