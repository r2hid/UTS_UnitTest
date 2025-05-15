from infrastructure.anime_controller import AnimeController
from usecase.anime_usecase import AnimeUseCase
from entity.anime import Anime

def menu():
    print("\n=== Menu Anime (˶ᵔ ᵕ ᵔ˶) ===")
    print("1. Browse")
    print("2. Read by ID")
    print("3. Add")
    print("4. Edit")
    print("5. Delete")
    print("6. Exit")

repo = AnimeController()
anime_uc = AnimeUseCase(repo)

while True:
    menu()
    choice = input("Pilih menu (1-6): ")

    if choice == '1':
        anime_list = anime_uc.browse()
        if not anime_list:
            print("Belum ada anime sayang ¯\_(ツ)_/¯")
        else:
            for anime in anime_list:
                print(anime)

    elif choice == '2':
        anime_id = int(input("Masukkan ID Anime: "))
        anime = anime_uc.read(anime_id)
        print(anime if anime else "Anime tidak ditemukan.")

    elif choice == '3':
        id = int(input("ID: "))
        title = input("Judul: ")
        genre = input("Genre: ")
        eps = int(input("Jumlah Episode: "))
        try:
            anime_uc.add(Anime(id, title, genre, eps))
            print("Anime berhasil ditambahkan.")
        except Exception as e:
            if str(e) == "Anime with this ID already exists":
                print("ID anime sudah ada")
            else: print("Error:", e)

    elif choice == '4':
        id = int(input("ID Anime yang ingin diedit: "))
        title = input("Judul Baru: ")
        genre = input("Genre Baru: ")
        eps = int(input("Jumlah Episode Baru: "))
        try:
            anime_uc.edit(Anime(id, title, genre, eps))
            print("Anime berhasil diupdate.")
        except Exception as e:
            print("Error:", e)

    elif choice == '5':
        anime_id = int(input("Masukkan ID Anime yang ingin dihapus: "))
        anime_uc.delete(anime_id)
        print("Anime berhasil dihapus.")

    elif choice == '6':
        print("Keluar...")
        break

    else:
        print("Pilihan tidak valid.")