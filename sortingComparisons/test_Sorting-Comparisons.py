import pytest
from sortingComparisons.SortingComparisons import sort_movies_obj_alphabetical , sort_movies_obj_yearly

movies_arr = [
    {
        "title": "spider_man",
        "year": "1990",
        "genres": ["action", "super_hero"]
    },
    {
        "title": "barbe",
        "year": "2022",
        "genres": ["drama", "comedy"]
    },
    {
        "title": "the gero",
        "year": "2015",
        "genres": ["drama", "comedy"]
    }
]

def test_sort_movies_obj_yearly():
    sorted_movies = sort_movies_obj_yearly(movies_arr)
    years = [movie['year'] for movie in sorted_movies]
    assert years == ['1990', '2015', '2022']

def test_sort_movies_obj_alphabetical():
    sorted_movies = sort_movies_obj_alphabetical(movies_arr)
    titles = [movie['title'] for movie in sorted_movies]
    assert titles == ['barbe', 'gero', 'spider_man']
