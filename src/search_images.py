from unittest.mock import DEFAULT
import requests
from fastcore.foundation import L
from fastdownload import download_url
from pathlib import Path
from get_key import get_key

BING_IMAGE_API_URL = "https://api.bing.microsoft.com/v7.0/images/search"
DEFAULT_SECRET_PATH = "secret.yaml"

def download_to_directory(index, url, output=Path('../data')):
    path = output / f'{index}.jpg'
    download_url(url, path)
    print(f'Downloaded {url} as {path}')

def search_images(key, term, min_sz=128, max_images=150, page=1):
    offset = (page - 1) * max_images
    params = {'q':term, 'count':max_images, 'min_height':min_sz, 'min_width':min_sz, 'offset':offset}

    headers = {"Ocp-Apim-Subscription-Key":key}

    search_url = BING_IMAGE_API_URL
    
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()    
    return L(search_results['value'])

def search_and_download(key, query, output_dir, page=1, max_images=150):
    """
    Search for a query and download all results in one pass
    """
    results = search_images(key, query, page=page, max_images=max_images)

    # fetch URLs of all pictures
    ims = results.attrgot('contentUrl')
    offset = (page - 1) * max_images
    
    if len(ims) > 0:
        for idx, url in enumerate(ims):
            try:
                download_to_directory(idx + offset, url, output_dir)
            except Exception as e:
                print(f'Unable to save {url}')
                print(e)
    else:
        print(f'No images found using query: {{query}}')
class ImageSearch:
    def __init__(self, secret_path=DEFAULT_SECRET_PATH, output_dir=None):
        self._key = get_key(secret_path)
        self._output_dir = output_dir

    def set_output_dir(self, output_dir):
        self._output_dir = output_dir

    def search_and_download_into_folder(self, query, page=1, max_images=150):
        if self._output_dir is None:
            raise Exception("No output directory for saving images specified")

        search_and_download(self._key, query, self._output_dir, page=page, max_images=max_images)

    



