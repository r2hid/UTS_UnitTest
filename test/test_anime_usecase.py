import unittest
from infrastructure.anime_controller import AnimeController
from usecase.anime_usecase import AnimeUseCase
from entity.anime import Anime

class TestAnimeUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = AnimeController()
        self.uc = AnimeUseCase(self.repo)
        self.anime = Anime(1, "Naruto", "Action", 220)

    def test_add_anime(self):
        self.uc.add(self.anime)
        self.assertEqual(len(self.repo.browse()), 1)

    def test_add_duplicate_anime(self):
        self.uc.add(self.anime)
        with self.assertRaises(Exception):
            self.uc.add(self.anime)

    def test_edit_anime(self):
        self.uc.add(self.anime)
        updated = Anime(1, "Naruto Shippuden", "Action", 500)
        self.uc.edit(updated)
        self.assertEqual(self.repo.read(1).title, "Naruto Shippuden")

    def test_browse(self):
        self.uc.add(self.anime)
        self.assertIsInstance(self.uc.browse(), list)

    def test_delete_anime(self):
        self.uc.add(self.anime)
        self.uc.delete(self.anime.id)
        self.assertEqual(len(self.uc.browse()), 0)

if __name__ == '__main__':
    unittest.main()