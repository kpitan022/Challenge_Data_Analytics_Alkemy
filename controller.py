from get_csv import get_csv
from my_data import dataframes
from  variables import list_category, list_urls
from db_connect import craete_table
from variables import list_cinemas
from logs import my_log

logger=my_log('controller')

def main():
    logger.info('Running script')
    try:
        for i in map(get_csv, list_category, list_urls):
            i
    except Exception as e:
        logger.info(e)


def records(register):
    try:
        # Cantidad de registros totales por categoría
        categories_records=register.groupby('categoria').size().to_frame(name = 'registros_por_categoria')

        # Cantidad de registros totales por fuente
        source_records=register.groupby(['categoria','fuente']).size().to_frame(name = 'registros_por_fuente')

        # Cantidad de registros por provincia y categoría
        province_records=register.groupby(['categoria','provincia']).size().to_frame(name='registros_por_provincia')

        # Total de datos conjuntos por provincia, fuente y categoría
        total_records_cat_source=categories_records.merge(source_records, how='outer', left_index=True, right_index=True)
        total_records=total_records_cat_source.merge(province_records, how='outer',left_index=True, right_index=True)
        total_records.reset_index(inplace=True)
        total_records=total_records[['categoria','registros_por_categoria','fuente','registros_por_fuente','provincia','registros_por_provincia']]
        return total_records
    except Exception as e:
        logger.info(e)
        exit(1)


def info_cinemas(cinemas):
    try:
        cinemas[list_cinemas[3]]=cinemas[list_cinemas[3]].replace({'si': 1, 'SI': 1,'Si': 1, 'No': 0, 'no': 0, 'NO': 0, '0': 0}).fillna(0)
        cinemas=cinemas.astype({list_cinemas[3]:'int64'})
        cinemas_group=cinemas.groupby(list_cinemas[0])[[list_cinemas[1], list_cinemas[2],list_cinemas[3]]].sum()
        return cinemas_group
    except Exception as e:
        logger.error(e)
        logger.info('error in the column [espacio_incaa], contains non-numeric values')
        exit(1)



if __name__ == '__main__':
    main()
    
    concat,register,cinemas=dataframes()
    
    craete_table(concat,"total_normalizer")
    logger.info('Created table total_normalizer')

    craete_table(records(register),"total_records")
    logger.info('Created table total_records')
    
    craete_table(info_cinemas(cinemas),"info_cinemas")
    logger.info('Created table info_cinemas')
    logger.info('Stop script')