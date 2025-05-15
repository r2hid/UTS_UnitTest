from interface.anime_repository import AnimeRepository
from entity.anime import Anime

class AnimeUseCase:
    def __init__(self, repo):
        self.repo = repo

    def browse(self):
        return self.repo.browse()

    def read(self, anime_id):
        return self.repo.read(anime_id)

    def add(self, anime):
        if self.repo.read(anime.id):
            raise Exception("Anime with this ID already exists")
        self.repo.add(anime)

    def edit(self, anime):
        if not self.repo.read(anime.id):
            raise Exception("Anime not found")
        self.repo.edit(anime)

    def delete(self, anime_id):
        self.repo.delete(anime_id)