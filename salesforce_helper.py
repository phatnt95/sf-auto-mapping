import pandas as pd
from simple_salesforce import Salesforce

def get_metadata_from_api(object_name, username, password, token):
    sf = Salesforce(username=username, password=password, security_token=token)
    fields = sf.__getattr__(object_name).describe()["fields"]
    return [{"api_name": f["name"], "label": f["label"]} for f in fields]

def get_metadata_from_csv(file):
    df = pd.read_csv(file)
    return df.to_dict(orient="records")
