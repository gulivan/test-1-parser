import os
from typing import List
import psycopg2


def create_db_connection():
    api_config = {
        'host': os.getenv("POSTGRES_HOST", "localhost"),
        'port': os.getenv("POSTGRES_PORT", "5432"),
        'dbname': os.getenv("POSTGRES_DB", "weather_data"),
        'user': os.getenv("POSTGRES_USER", "postgres"),
        'password': os.getenv("POSTGRES_PASSWORD", "postgres")
    }
    conn = psycopg2.connect(**api_config)
    return conn


def execute_ddl(path_to_query: str):
    """
    Executes a DDL query to create the table.
    :param path_to_query:
    :return:
    """
    with open(path_to_query, 'r') as query_file:
        query = query_file.read()
    conn = create_db_connection()
    with conn.cursor() as cursor:
        cursor.execute(query)
    conn.commit()
    conn.close()


def insert_data(query_template_path: str, data: List):
    """
    Inserts data into the database.
    :param query_template_path:
    :param data:
    :return:
    """
    with open(query_template_path, 'r') as query_file:
        query = query_file.read()
    conn = create_db_connection()
    with conn.cursor() as cursor:
        cursor.executemany(query, data)
        conn.commit()
    conn.close()


def load_csv(path_to_csv: str) -> List:
    """
    Loads a csv into the database.
    :param path_to_csv:
    :param table_name:
    :return:
    """
    with open(path_to_csv, 'r') as csv_file:
        csv_data = csv_file.readlines()[1:]
    data = []
    for row in csv_data:
        row_data = row.rstrip().rstrip(',').split(",")
        data.append(row_data)
    return data


if __name__ == "__main__":
    execute_ddl("queries/create_table_weather.sql")
    data = load_csv("weather.csv")
    insert_data("queries/insert_weather_data.sql", data)
    os.remove("weather.csv")
