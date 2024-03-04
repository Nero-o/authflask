import requests

PIPEFY_API_URL = "https://api.pipefy.com/graphql"
PIPEFY_API_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MDk1MzEyMDEsImp0aSI6ImFmNzRkZTA3LWYzMDMtNDdlMy1iZGQwLWI1YzFkMzcwZjUzOCIsInN1YiI6MzAxOTkwMjQzLCJ1c2VyIjp7ImlkIjozMDE5OTAyNDMsImVtYWlsIjoicGF1bG9AbWFwc2NyZWRpdG8uY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDMyODU5Miwic2NvcGVzIjpbXX0sImludGVyZmFjZV91dWlkIjpudWxsfQ.gvsgXtEbiRXI0cI4HjrQsKx-vzE9A8eUmZV_4rjl7mcYV7dUyzXc1-vVE43un4wzYvNUS25_vNgI2Hs_J9e5HA"
def create_pipefy_card(data):
    headers = {
        'Authorization': f'Bearer {PIPEFY_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    # Extract data from the request
    tipo_pessoa = data.get('tipo_pessoa')
    nome = data.get('nome')
    cpf_cnpj = data.get('cpf_cnpj')
    estado_civil = data.get('estado_civil')
    telefone = data.get('telefone')
    email = data.get('email')
    renda_mensal = data.get('renda_mensal')
    tipo_terreno = data.get('tipo_terreno')
    cep = data.get('cep')
    endereco = data.get('endereco')
    numero = data.get('numero')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    estado = data.get('estado')
    valor_propriedade = data.get('valor_propriedade')
    valor_emprestimo = data.get('valor_emprestimo')
    prazo_pagamento = data.get('prazo_pagamento')

    # Prepare the request payload
    payload = {
        "query": f"""
            mutation {{
              createCard(input: {{
                pipeId: "303394377",
                title: "HOME EQUITY",
                fieldsAttributes: [
                  {{ fieldId: "tipo_pessoa_field_id", fieldValue: "{data.get('tipo_pessoa')}" }},
                  {{ fieldId: "nome_field_id", fieldValue: "{data.get('nome')}" }},
                  {{ fieldId: "cpf_cnpj_field_id", fieldValue: "{data.get('cpf_cnpj')}" }},
                  {{ fieldId: "estado_civil_field_id", fieldValue: "{data.get('estado_civil')}" }},
                  {{ fieldId: "telefone_field_id", fieldValue: "{data.get('telefone')}" }},
                  {{ fieldId: "email_field_id", fieldValue: "{data.get('email')}" }},
                  {{ fieldId: "renda_mensal_field_id", fieldValue: "{data.get('renda_mensal')}" }},
                  {{ fieldId: "tipo_terreno_field_id", fieldValue: "{data.get('tipo_terreno')}" }},
                  {{ fieldId: "cep_field_id", fieldValue: "{data.get('cep')}" }},
                  {{ fieldId: "endereco_field_id", fieldValue: "{data.get('endereco')}" }},
                  {{ fieldId: "numero_field_id", fieldValue: "{data.get('numero')}" }},
                  {{ fieldId: "bairro_field_id", fieldValue: "{data.get('bairro')}" }},
                  {{ fieldId: "cidade_field_id", fieldValue: "{data.get('cidade')}" }},
                  {{ fieldId: "estado_field_id", fieldValue: "{data.get('estado')}" }},
                  {{ fieldId: "valor_propriedade_field_id", fieldValue: "{data.get('valor_propriedade')}" }},
                  {{ fieldId: "valor_emprestimo_field_id", fieldValue: "{data.get('valor_emprestimo')}" }},
                  {{ fieldId: "prazo_pagamento_field_id", fieldValue: "{data.get('prazo_pagamento')}" }}
                ]
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

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        if 'data' in result and 'createCard' in result['data'] and 'card' in result['data']['createCard']:
            card_data = result['data']['createCard']['card']
            return card_data
        else:
            # Handle missing data
            return None
    else:
        # Handle API error
        return None


def fetch_pipe_fields(pipe_id):
    # Construct the GraphQL query to fetch fields for the specified Pipe
    query = f"""
        {{
          pipe(id: "{303394377}") {{
            phases {{
              name
              fields {{
                id
                label
              }}
            }}
          }}
        }}
        """

    # Make a request to the Pipefy API to fetch the fields
    response = requests.post(
        "https://api.pipefy.com/graphql",
        json={"query": query},
        headers={
            'Authorization': f'Bearer {PIPEFY_API_TOKEN}',
            'Content-Type': 'application/json'
        }

    )

    # Parse the response
    if response.status_code == 200:
        data = response.json()
        fields = data["data"]["pipe"]["phases"][0]["fields"]  # Assuming you're fetching fields from the first phase
        field_names = [field["label"] for field in fields]
        return field_names
    else:
        return None

def fetch_card_fields(card_id):
    query = f"""
           {{
             card(id: "{759461116}") {{
                 fields {{
                   id
                 }}
             }}
           }}
           """

    response = requests.post(
        "https://api.pipefy.com/graphql",
        json={"query": query},
        headers={
            'Authorization': f'Bearer {PIPEFY_API_TOKEN}',
            'Content-Type': 'application/json'
        }
    )

    # Parse the response
    if response.status_code == 200:
        data = response.json()
        fields = data["data"]["card"]["fields"]
        field_names = [field["id"] for field in fields]
        return field_names
    else:
        return None