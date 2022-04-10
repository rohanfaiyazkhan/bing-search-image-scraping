from tokenize import Name
import yaml

def get_key():
    with open("secret.yaml", "r") as stream:
        try:
            contents = yaml.safe_load(stream)
            
            if contents["azure_secret_key"] is None:
                raise NameError("azure_secret_key could not be found")

            return contents["azure_secret_key"]
        except NameError as e:
            raise NameError(e)

if __name__ == "__main__":
     print(get_key())