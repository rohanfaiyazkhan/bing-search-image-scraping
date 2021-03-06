# Scrape Images using Bing Search API

## Requirements

You'll need a Azure account and a Bing Search Resource to make this work. Once you have those, you need to get your API key, create a `secret.yaml` file in the root of the project with this information:

`secret.yaml`
```yaml
azure_secret_key: "your API key"
```

Install all dependencies:

```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run

`src/main.py` features an example of the script in use. 

```python
from search_images import ImageSearch

instance = ImageSearch(DEFAULT_SECRET_PATH, OUTPUT_DIRECTORY)
instance.search_and_download_into_folder("search_query", max_images=150, page=1)
```

By default `DEFAULT_SECRET_PATH` is `secret.toml` and `OUTPUT_DIRECTORY` is `data`. Data will get downloaded as `count.jpg`.