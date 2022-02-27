from pathlib import Path, PurePath
import requests
from tqdm.auto import tqdm

# modules
from get_date import path_year, fecha
from make_dirs import make_dirs
from logs import my_log

logger=my_log(__name__)

def get_csv(category,urls):
    
    chunk_size=1024
    intento=0
    files_path = PurePath.joinpath(Path.cwd(),category,path_year)
    
    while True:
        if intento>=10:
            logger.error(f'failed to download, try again {intento}/10')
            exit(1)
            

        try:
            req= requests.get(urls, stream = True, timeout=15000, allow_redirects=True)
            total_size = int(req.headers.get('content-length'))
            break
        # except Exception as e:
        except TypeError:
            intento+=1
            # logger.critical(e)
            logger.warning(f'failed attempt {intento}/10 in {category}')
    try:
        logger.info('Making directories')
        make_dirs(category,path_year)
        logger.info(f'Downloading file {category}')
        with open(f'{files_path}/{category}-{fecha}.csv','wb') as f:
            for chunk in tqdm(iterable=req.iter_content(chunk_size=chunk_size),total = round(total_size/chunk_size), unit = 'KB'):
                f.write(chunk)
            logger.info(f'Saving the file {category}')

        logger.info(f'File saved in: {files_path}')
    except Exception as e:
        logger.error(e)
