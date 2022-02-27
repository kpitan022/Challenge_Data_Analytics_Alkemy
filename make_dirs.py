
from pathlib import Path, PurePath
# from get_date import path_year

def make_dirs(category,path_year):
    PurePath.joinpath(Path.cwd(),category,path_year).mkdir(parents=True, exist_ok=True)


