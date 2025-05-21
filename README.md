# MovieSearchProject

A console-based Python application that allows users to search for movies from the Sakila database by genre, release year, or keyword.

## Features

- 🔍 Search movies by:
  - Genre (by number or name)
  - Release year (e.g., 2006–2020)
  - Keyword in the title
- 📊 View top 10 most popular search queries
- 🗂 Log each search into a MySQL database
- ✅ Handles missing or incorrect input gracefully

## Technologies Used

- Python 3
- MySQL (Sakila and log databases)
- PrettyTable (for console tables)
- mysql-connector-python

## Project Structure

MovieSearchProject/
├── config.py # Database configs
├── database_utils.py # DB connection logic
├── log_queries.py # Search logging and popular queries
├── main.py # Main program file
├── search_movies.py # Core search logic
└── .gitignore # Files to be excluded from Git tracking

## How to Run

1. Set up **MySQL** and import the **Sakila** database.
2. Create a separate **logging** database.
3. Add your database credentials in `config.py`.
4. (Optional) Create the table by running `create_table_search_log_EF()` from `log_queries.py`.
5. Run `main.py` to start the application:

```bash
python main.py
```

