import requests
from fastcore.foundation import L
from fastdownload import download_url
from pathlib import Path

def download_to_folder(index, url, folder=Path('../data')):
    path = folder / f'{index}.jpg'
    download_url(url, path)
    print(f'Downloaded {url} as {path}')

def search_images(key, term, min_sz=128, max_images=150):    
     params = {'q':term, 'count':max_images, 'min_height':min_sz, 'min_width':min_sz}
     headers = {"Ocp-Apim-Subscription-Key":key}
     search_url = "https://api.bing.microsoft.com/v7.0/images/search"
     response = requests.get(search_url, headers=headers, params=params)
     response.raise_for_status()
     search_results = response.json()    
     return search_results['value']

def search_and_download(query, page=1, max_images=150):
    """
    Search for a query and download all results in one pass
    """
    results = search_images(key, query, page=page, max_images=max_images)
    ims = results.attrgot('contentUrl')
    offset = (page - 1) * max_images
    
    if len(ims) > 0:
        for idx, url in enumerate(ims):
            try:
                download_to_folder(idx + offset, url)
            except Exception as e:
                print(f'Unable to save {url}')
                print(e)
    else:
        print(f'No images found using query: {{query}}')

