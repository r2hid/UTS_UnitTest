import unittest
from entity.anime import Anime

class TestAnimeEntity(unittest.TestCase):
    def test_create_anime(self):
        anime = Anime(1, "Naruto", "Action", 220)
        self.assertEqual(anime.title, "Naruto")

    def test_anime_repr(self):
        anime = Anime(2, "Bleach", "Action", 366)
        self.assertIn("Bleach", repr(anime))

    def test_anime_fields(self):
        anime = Anime(3, "One Piece", "Adventure", 1000)
        self.assertEqual((anime.id, anime.genre, anime.episodes), (3, "Adventure", 1000))