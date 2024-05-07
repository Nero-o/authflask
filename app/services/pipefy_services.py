import requests
import json
PIPEFY_API_URL = "https://api.pipefy.com/graphql"
PIPEFY_API_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MDk1MzEyMDEsImp0aSI6ImFmNzRkZTA3LWYzMDMtNDdlMy1iZGQwLWI1YzFkMzcwZjUzOCIsInN1YiI6MzAxOTkwMjQzLCJ1c2VyIjp7ImlkIjozMDE5OTAyNDMsImVtYWlsIjoicGF1bG9AbWFwc2NyZWRpdG8uY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDMyODU5Miwic2NvcGVzIjpbXX0sImludGVyZmFjZV91dWlkIjpudWxsfQ.gvsgXtEbiRXI0cI4HjrQsKx-vzE9A8eUmZV_4rjl7mcYV7dUyzXc1-vVE43un4wzYvNUS25_vNgI2Hs_J9e5HA"


def create_pipefy_card(data):
    headers = {
        'Authorization': f'Bearer {PIPEFY_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    if 'status' in data:
        del data['status']

    fields_attributes = []
    for key, value in data.items():
        if key == "pol_tica_de_privacidade":
            if value == "Li e concordo com a Política e Privacidade":
                value = ["Li e concordo com a Política e Privacidade"]
        field_value = json.dumps(value) if isinstance(value, list) else json.dumps(value)
        fields_attributes.append({"field_id": key, "field_value": field_value})

    fields_str = ', '.join(
        f'{{ field_id: "{item["field_id"]}", field_value: {item["field_value"]} }}'
        for item in fields_attributes
    )

    payload = {
        "query": f"""
                   mutation {{
                     createCard(input: {{
                       pipe_id: "304097853",
                       title: "HOME EQUITY",
                       fields_attributes: [{fields_str}]
                     }}) {{
                       card {{
                         id
                         title
                       }}
                     }}
                   }}
               """
    }

    response = requests.post(PIPEFY_API_URL, json=payload, headers=headers)
    try:
        return response.json()
    except ValueError:
        return {"error": "Failed to parse response", "status": response.status_code}

