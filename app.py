from flask import Flask, render_template, request
import pandas as pd
from mapping_ai import suggest_mapping
from salesforce_helper import get_metadata_from_api, get_metadata_from_csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map", methods=["POST"])
def map_fields():
    # api_key = request.form["api_key"]
    data_csv = request.files["data_csv"]
    metadata_source = request.form["metadata_source"]

    df = pd.read_csv(data_csv)
    csv_cols = df.columns.tolist()

    if metadata_source == "api":
        username = request.form["username"]
        password = request.form["password"]
        token = request.form["token"]
        object_name = request.form["object_name"]
        metadata = get_metadata_from_api(object_name, username, password, token)
    else:
        metadata_csv = request.files["metadata_csv"]
        metadata = get_metadata_from_csv(metadata_csv)

    mapping = suggest_mapping(csv_cols, metadata)
    return render_template("result.html", mapping=mapping)

if __name__ == "__main__":
    app.run(debug=True)
