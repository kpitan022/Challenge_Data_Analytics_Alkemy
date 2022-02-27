from pathlib import Path, PurePath
import requests
from tqdm.auto import tqdm

# modules
from get_date import path_year, fecha
from make_dirs import make_dirs

def get_path(category,urls):
    chunk_size=1024
    intento=0
    files_path = PurePath.joinpath(Path.cwd(),category,path_year)
    print(f'Downloading file {category}')
    # req= requests.get(urls)
    while True:
        try:
            req= requests.get(urls, stream = True, timeout=15000, allow_redirects=True)
            total_size = int(req.headers.get('content-length'))
            break
        except TypeError:
            intento+=1
            print(f'falló intento {intento}')
    print('Making directories')
    make_dirs(category,path_year)
    with open(f'{files_path}/{category}-{fecha}.png','wb') as f:
        print(f'Saving the file {category}')
        for chunk in tqdm(iterable=req.iter_content(chunk_size=chunk_size),total = round(total_size/chunk_size), unit = 'KB'):
            f.write(chunk)

    print(f'File saved in: {files_path}')

# borrar esta parte 

from variables import museos_url as cat_url

if __name__ == '__main__':
    get_path('museos', cat_url)