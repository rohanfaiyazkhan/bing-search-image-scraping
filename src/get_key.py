from tokenize import Name
import yaml

def get_key(path="secret.yaml") -> str:
    with open(path, "r") as stream:
        try:
            contents = yaml.safe_load(stream)
            
            if contents["azure_secret_key"] is None:
                raise KeyError("azure_secret_key could not be found")

            return contents["azure_secret_key"]
        except KeyError as e:
            raise KeyError(e)

if __name__ == "__main__":
     print(get_key("secret.yaml"))