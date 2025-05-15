class Anime:
    def __init__(self, id, title, genre, episodes):
        self.id = id
        self.title = title
        self.genre = genre
        self.episodes = episodes

    def __repr__(self):
        return f"Anime(id={self.id}, title='{self.title}', genre='{self.genre}', episodes={self.episodes})"