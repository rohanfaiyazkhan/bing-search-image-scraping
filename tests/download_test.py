from os import path
import sys
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from src.search_images import download_url
from pathlib import Path

if __name__ == "__main__":
    download_url('https://www.facebook.com/favicon.ico', Path('data/test.ico'))