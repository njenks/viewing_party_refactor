import pytest
from viewing_party.movie import Movie 

def test_create_person():
    # Arrange
    title = "shrek 2"
    genre = "comedy"
    rating = 4
    host = "netflix"

    # Act
    movie = Movie(title, genre, rating, host)

    # Assert
    assert movie.title == title 