from pathlib import Path

project_dir = Path(__file__).parent  # Путь к текущей папке проекта

target_files = ["main.py", "log_queries.py", "database_utils.py"]

replacements = {
    "Ошибка подключения": "Connection error",
    "Создаёт подключение к базе данных": "Establishes a database connection",
    "Создаёт таблицу search_logs_EF, если её нет": "Creates the table search_logs_EF if it doesn't exist",
    "Ошибка при создании таблицы": "Error creating the table",
    "Сохраняет параметры поиска в таблицу": "Saves search parameters to the table",
    "Ошибка при сохранении запроса": "Error saving the query",
    "Выводит 10 самых популярных поисковых запросов": "Displays top 10 popular search queries",
    "Проверка: выполняется get_popular_queries": "Running get_popular_queries",
    "SQL-запрос для популярных запросов": "SQL query for popular queries",
    "Результаты запроса": "Query results",
    "Популярные запросы отсутствуют в базе": "No popular queries found in the database",
    "Ошибка при выполнении SQL-запроса": "Error executing SQL query",
    "Получает минимальный и максимальный год выпуска фильмов в базе данных": "Gets the min and max release year from database",
    "Ошибка при получении диапазона годов": "Error retrieving year range",
    "Выберите действие": "Choose an action",
    "Поиск фильмов": "Search movies",
    "Популярные запросы": "Popular queries",
    "Выход": "Exit",
    "Введите номер": "Enter a number",
    "Введите параметры поиска (нажмите Enter, чтобы пропустить)": "Enter search parameters (press Enter to skip)",
    "Доступные жанры": "Available genres",
    "Введите номера жанров": "Enter genre numbers",
    "Жанра с номером": "Genre number",
    "не существует": "does not exist",
    "Жанр": "Genre",
    "не найден": "not found",
    "Некорректные жанры": "Invalid genres",
    "Поиск будет без учёта жанра": "Search will be without genre filter",
    "Год выпуска": "Release year",
    "Введите год или нажмите Enter, чтобы пропустить": "Enter year or press Enter to skip",
    "Год должен быть в диапазоне": "Year must be in range",
    "Попробуйте снова": "Try again",
    "Некорректный ввод": "Invalid input",
    "Ключевое слово в названии": "Keyword in title",
    "Поиск по жанру": "Search by genre",
    "Неверный ввод. Попробуйте снова": "Invalid input. Please try again",
    "Выход": "Exit"
}

# Перебираем и заменяем
for file_name in target_files:
    file_path = project_dir / file_name
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
        for rus, eng in replacements.items():
            content = content.replace(rus, eng)
        file_path.write_text(content, encoding="utf-8")

print("✅ Русские фразы успешно заменены на английские.")
