
import pytest

from application import application

@pytest.fixture
def client():
    application.config['TESTING'] = True
    client = application.test_client()

    yield client

def test_empty(client):
    """test the empty input"""

    rv = client.get('/translate')
    assert b'No text field given. Please add you text input into the text argument.' == rv.data

def test_single_consonant(client):
    """test the various inputs"""

    rv = client.get('/translate?text=pig')
    assert b'igpay' == rv.data

    rv = client.get('/translate?text=latin')
    assert b'atinlay' == rv.data

    rv = client.get('/translate?text=banana')
    assert b'ananabay' == rv.data

def test_multi_consonant(client):
    """test the various inputs"""

    rv = client.get('/translate?text=smile ')
    assert b'ilesmay' == rv.data

    rv = client.get('/translate?text=string')
    assert b'ingstray' == rv.data

    rv = client.get('/translate?text=glove')
    assert b'oveglay' == rv.data

def test_vowel(client):
    """test the various inputs"""

    rv = client.get('/translate?text=eat')
    assert b'eatay' == rv.data

    rv = client.get('/translate?text=omelet')
    assert b'omeletay' == rv.data

    rv = client.get('/translate?text=are')
    assert b'areay' == rv.data

def test_sentece(client):
    """test the various inputs"""

    rv = client.get('/translate?text=Hello, my name is Alice.')
    assert b'Ellohay, ymay amenay isay Aliceay.' == rv.data

    rv = client.get('/translate?text=I wonder how how the sun is, Bob?')
    assert b'Iay onderway owhay owhay ethay unsay isay, Obbay?' == rv.data

    rv = client.get('/translate?text=The goal of this challenge is to build a microservice that takes english text and translates it into Pig Latin.')
    assert b'Ethay oalgay ofay isthay allengechay isay otay uildbay aay icroservicemay atthay akestay englishay exttay anday anslatestray itay intoay Igpay Atinlay.' == rv.data