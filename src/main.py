from search_images import ImageSearch
from pathlib import Path

OUTPUT_DIRECTORY = Path("data")
DEFAULT_SECRET_PATH = "secret.yaml"

if __name__ == "__main__":
    instance = ImageSearch(DEFAULT_SECRET_PATH, OUTPUT_DIRECTORY)
    instance.search_and_download_into_folder("lottery winner", max_images=150, page=1)