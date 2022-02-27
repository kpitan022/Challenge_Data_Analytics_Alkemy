from pathlib import Path, PurePath
import pandas as pd
from get_date import path_year, fecha
from variables import list_category, columns_lower_museos, columns_lower_cines, columns_lower_bibliotecas, df_unique_table, list_register, list_cinemas



def my_data(category,cols):
    return pd.read_csv(f'{PurePath.joinpath(Path.cwd(),category,path_year)}/{category}-{fecha}.csv',header=0, names=cols)

def dataframes():

	df_museos=my_data(list_category[0],columns_lower_museos)

	df_cines=my_data(list_category[1],columns_lower_cines)

	df_bibliotecas=my_data(list_category[2], columns_lower_bibliotecas)
	
	df_concat=pd.concat([df_museos[df_unique_table],df_cines[df_unique_table],df_bibliotecas[df_unique_table]],sort=False)
	
	df_register=pd.concat([df_museos[list_register],df_cines[list_register],df_bibliotecas[list_register]],sort=False)

	df_cinemas=df_cines[list_cinemas]

	return (df_concat, df_register,df_cinemas)

