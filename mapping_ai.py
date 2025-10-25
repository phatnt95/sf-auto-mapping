from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_ENDPOINT")
def suggest_mapping(csv_columns, sf_metadata):
    client = OpenAI(api_key=api_key, base_url=base_url)
    sf_fields = [f"{f['label']} ({f['api_name']})" for f in sf_metadata]

    prompt = f"""
    You are a Salesforce data mapping assistant.
    Given CSV columns: {csv_columns}
    and Salesforce fields: {sf_fields},
    suggest the best mapping between them.
    Return a JSON object like:
    {{
        "CSV Column": "Salesforce Field API Name"
    }}.
    Return only valid JSON without markdown or explanations.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"}
    )

    print(response.choices[0].message.content)
    try:
        mapping = json.loads(response.choices[0].message.content)
    except Exception as e:
        mapping = {"error": str(e)}

    return mapping
