from pathlib import Path, PurePath
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from psycopg2 import errors 
from variables import db_url, tables_list
from get_date import fecha
from logs import my_log

logger=my_log(__name__)

engine = create_engine(db_url)

def craete_table(data,table_name):
    try:
        logger.info('Connecting to database...')
        data.assign(fecha_actualizacion=fecha).to_sql(table_name, con=engine,if_exists="replace")
        logger.info('Connection successfully')

    except (OperationalError, errors.OperationalError ):
        logger.error('Error establishing a database connection')
        quit(1)


def script_craete_table():
    for table in tables_list:
        try:
            with engine.connect() as conn:
                logger.info(f'try to read script {table}')
                file = open( PurePath.joinpath(Path.cwd(),table))
                query = text(file.read())
                logger.info('Connecting to database...')
                conn.execute(query)
                logger.info(f'Table {table} created successfully')
        except (OperationalError, errors.OperationalError ):
            logger.error(f'Error establishing a database connection in {table}')
            quit(1)


if __name__ == '__main__':
    script_craete_table()