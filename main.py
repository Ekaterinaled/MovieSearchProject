from log_queries import create_table_search_log_EF, get_popular_queries
from search_movies import search_movies
from prettytable import PrettyTable

if __name__ == "__main__":
   from database_utils import connect_db, SAKILA_DB_CONFIG
from search_movies import search_movies
from log_queries import create_table_search_log_EF, get_popular_queries

# 🔹 Функция для получения диапазона годов
def get_year_range():
    """Gets the min and max release year from database."""
    connection = connect_db(SAKILA_DB_CONFIG)
    if connection is None:
        return 1990, 2024  

    cursor = connection.cursor()
    query = "SELECT MIN(release_year), MAX(release_year) FROM film;"
    
    try:
        cursor.execute(query)
        min_year, max_year = cursor.fetchone()
        return min_year, max_year
    except Exception as e:
        print(f"❌ Error retrieving year range: {e}")
        return 1990, 2024
    finally:
        cursor.close()
        connection.close()

# 📌 Список жанров с номерами
GENRES = {
    1: "Action", 2: "Animation", 3: "Children", 4: "Classics",
    5: "Comedy", 6: "Documentary", 7: "Drama", 8: "Family",
    9: "Foreign", 10: "Games", 11: "Horror", 12: "Music",
    13: "New", 14: "Sci-Fi", 15: "Sports", 16: "Travel"
}

# 🔹 Запуск приложения
if __name__ == "__main__":
    create_table_search_log_EF()
    min_year, max_year = get_year_range()

    while True:
        print("\n📌 Choose an action:")
        print("1. 🔎 Search movies")
        print("2. 📊 Popular queries")
        print("3. ❌ Exit")

        choice = input("Enter a number: ").strip()

        if choice == '1':
            print("\n📌 Enter search parameters (press Enter to skip):")

            # 📌 Вывод списка жанров перед вводом
            print("\n🎭 Available genres:")
            for num, name in GENRES.items():
                print(f"{num}. {name}")

            # 📌 Получение ввода от пользователя
            genres_input = input("\nEnter a numberа жанров (через запятую) или их названия: ").strip()

            # 📌 Обработка жанров
            genres = []
            if genres_input:
                genres_list = [g.strip() for g in genres_input.split(",")]

                for g in genres_list:
                    if g.isdigit():
                        genre_number = int(g)
                        genre_name = GENRES.get(genre_number)
                        if genre_name:
                            genres.append(genre_name)
                        else:
                            print(f"⚠️ Genre number {genre_number} does not exist.")
                    elif g in GENRES.values():
                        genres.append(g)
                    else:
                        print(f"⚠️ Genre '{g}' not found.")

                if not genres:
                    print("⚠️ Invalid genres. Search will be without genre filter.")
                    genres = None
            else:
                genres = None

            # 📌 Ввод года с проверкой
            year = None
            while True:
                print(f"📅 Release year (от 1990 до 2024):")
                year_input = input("Enter year or press Enter to skip: ").strip()

                if not year_input:
                    break

                if year_input.isdigit():
                    year = int(year_input)
                    if 1990 <= year <= 2024:
                        break
                    else:
                        print(f"⚠️ Year must be in range 1990-2024. Try again.")
                else:
                    print("⚠️ Invalid input. Введите число или оставьте поле пустым.")

            # 📌 Ввод ключевого слова
            keyword = input("🔎 Keyword in title: ").strip() or None

            # 📌 Запуск поиска
            selected_genre = genres[0] if genres else None
            print(f"🔍 Search by genre: {selected_genre}")  

            search_movies(genre=selected_genre, year=year, keyword=keyword)

        elif choice == '2':
            get_popular_queries()

        elif choice == '3':
            print("👋 Exit")
            break

        else:
            print("⚠️ Неверный ввод. Try again.")

