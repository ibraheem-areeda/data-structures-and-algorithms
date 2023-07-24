import pytest
from hashmap_repeated_word.hashmapRepeatedWord import repeated_word

def test_repeated_word_middle():
    string = "This is a test string with repeated word test in the middle."
    assert repeated_word(string) == "test"

def test_repeated_word_beginning():
    string = "test this is a test string with a repeated word at the beginning."
    assert repeated_word(string) == "test"

def test_repeated_word_end():
    string = "This is test string with a repeated word at the end test."
    assert repeated_word(string) == "test"

def test_repeated_word_no_repetition():
    string = "This is a test string with no repeated words."
    assert repeated_word(string) == "No Repetition"

def test_repeated_word_empty_string():
    string = ""
    assert repeated_word(string) == "No Repetition"
