import unittest
from infrastructure.anime_controller import AnimeController
from entity.anime import Anime

class TestMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = AnimeController()
        self.anime = Anime(1, "Naruto", "Action", 220)

    def test_add_and_browse(self):
        self.repo.add(self.anime)
        self.assertEqual(len(self.repo.browse()), 1)

    def test_read_success(self):
        self.repo.add(self.anime)
        self.assertEqual(self.repo.read(1).title, "Naruto")

    def test_read_not_found(self):
        self.assertIsNone(self.repo.read(999))

    def test_edit(self):
        self.repo.add(self.anime)
        self.repo.edit(Anime(1, "Naruto Shippuden", "Action", 500))
        self.assertEqual(self.repo.read(1).episodes, 500)

    def test_delete(self):
        self.repo.add(self.anime)
        self.repo.delete(1)
        self.assertEqual(len(self.repo.browse()), 0)