import csv
import psycopg2
import logging


# Get logger
def get_logger():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


# Read CSV file
def process_csv(logger):
    file_path = "data/sample.csv"
    mode = "r"
    number_of_rows = 0
    insert_query = """
INSERT INTO people (id, name, age, city)
VALUES (%s, %s, %s, %s)
"""

    conn = postgres_connection()
    cursor = conn.cursor()

    logger.info("reading file...")
    with open(file_path, mode) as csv_file:
        csv_reader = csv.reader(csv_file)
        number_of_rows += 1
        next(csv_reader)  # Skip header row

        for row in csv_reader:

            cursor.execute(insert_query, row)

    logger.info(f"Number of rows processed: {number_of_rows}")
    conn.commit()
    cursor.close()
    conn.close()


# Connect to Postgres
def postgres_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="myuser",
        password="mypassword",
    )
    return conn


# For basic Main setup
def main():
    logger = get_logger()
    logger.info("Starting CSV processing...")
    process_csv(logger)
    logger.info("CSV processing completed.")


if __name__ == "__main__":
    main
