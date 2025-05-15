from interface.anime_repository import AnimeRepository
from entity.anime import Anime

class AnimeController(AnimeRepository):
    def __init__(self):
        self.db = []

    def browse(self):
        return self.db

    def read(self, anime_id):
        for a in self.db:
            if a.id == anime_id:
                return a
        return None

    def add(self, anime):
        self.db.append(anime)

    def edit(self, anime):
        for i, a in enumerate(self.db):
            if a.id == anime.id:
                self.db[i] = anime
                return

    def delete(self, anime_id):
        self.db = [a for a in self.db if a.id != anime_id]