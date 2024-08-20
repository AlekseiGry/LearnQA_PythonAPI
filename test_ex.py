import pytest

def test_short():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, 'Too long phrase'