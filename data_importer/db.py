import psycopg2
import yaml
import json
import logging
from data_importer.logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)

def get_db_config():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config['database']

def connect_to_db():
    config = get_db_config()
    try:
        connection = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['password'],
            dbname=config['dbname']
        )
        return connection
    except psycopg2.Error as e:
        logger.error(f"Error connecting to the database: {e}")
        return None

def create_table_if_not_exists(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS public.phone (
                phoneid text NOT NULL,
                phone_name text NULL,
                phone_data jsonb NULL,
                CONSTRAINT api_objects_pkey PRIMARY KEY (phoneid)
            );
        """)
        connection.commit()
    except psycopg2.Error as e:
        logger.error(f"Error creating table: {e}")
        connection.rollback()
    finally:
        cursor.close()

def insert_phone_data(phone_data):
    connection = connect_to_db()
    if connection is None:
        return

    create_table_if_not_exists(connection)

    cursor = connection.cursor()
    for phone in phone_data:
        try:
            cursor.execute(
                """
                INSERT INTO public.phone (phoneid, phone_name, phone_data)
                VALUES (%s, %s, %s)
                ON CONFLICT (phoneid) DO NOTHING;
                """,
                (phone['id'], phone['name'], json.dumps(phone['data']))
            )
        except psycopg2.Error as e:
            logger.error(f"Error inserting data into the database: {e}")
            connection.rollback()
        else:
            connection.commit()
    cursor.close()
    connection.close()