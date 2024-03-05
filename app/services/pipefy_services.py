import requests

PIPEFY_API_URL = "https://api.pipefy.com/graphql"
PIPEFY_API_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MDk1MzEyMDEsImp0aSI6ImFmNzRkZTA3LWYzMDMtNDdlMy1iZGQwLWI1YzFkMzcwZjUzOCIsInN1YiI6MzAxOTkwMjQzLCJ1c2VyIjp7ImlkIjozMDE5OTAyNDMsImVtYWlsIjoicGF1bG9AbWFwc2NyZWRpdG8uY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDMyODU5Miwic2NvcGVzIjpbXX0sImludGVyZmFjZV91dWlkIjpudWxsfQ.gvsgXtEbiRXI0cI4HjrQsKx-vzE9A8eUmZV_4rjl7mcYV7dUyzXc1-vVE43un4wzYvNUS25_vNgI2Hs_J9e5HA"
def create_pipefy_card(data):
    headers = {
        'Authorization': f'Bearer {PIPEFY_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    # Extract data from the request
    tipo_de_pessoa = data.get('tipo_de_pessoa')
    nome_raz_o_social = data.get('nome_raz_o_social')
    cpf = data.get('cpf')
    estado_civil = data.get('estado_civil')
    telefone = data.get('telefone')
    e_mail = data.get('email')
    valor_total_da_compra = data.get('valor_total_da_compra')
    qual_tipo_de_im_vel = data.get('qual_tipo_de_im_vel')
    cep = data.get('cep')
    endere_o = data.get('endere_o')
    n_mero = data.get('n_mero')
    bairro = data.get('bairro')
    cidade = data.get('cidade')
    estado = data.get('estado')
    qual_valor_do_im_vel = data.get('qual_valor_do_im_vel')
    qual_o_valor_do_empr_stimo = data.get('qual_o_valor_do_empr_stimo')
    prazo_para_pagamento = data.get('prazo_para_pagamento')
    indica_o = data.get('indica_o')
    assessor_respons_vel = data.get('301990243')
    pol_tica_de_privacidade = data.get('Li e concordo com a Política e Privacidade')


    # Prepare the request payload
    payload = {
        "query": f"""
            mutation {{
              createCard(input: {{
                pipe_id: "303394377",
                title: "HOME EQUITY",
                fields_attributes: [
                  {{ field_id: "tipo_de_pessoa", field_value: "{data.get('tipo_de_pessoa')}" }},
                  {{ field_id: "nome_raz_o_social", field_value: "{data.get('nome_raz_o_social')}" }},
                  {{ field_id: "cpf", field_value: "{data.get('cpf')}" }},
                  {{ field_id: "estado_civil", field_value: "{'Solteiro(a)'}" }},
                  {{ field_id: "telefone", field_value: "{data.get('telefone')}" }},
                  {{ field_id: "e_mail", field_value: "{data.get('e_mail')}" }},
                  {{ field_id: "valor_total_da_compra", field_value: "{data.get('valor_total_da_compra')}" }},    
                  {{ field_id: "qual_tipo_de_im_vel", field_value: "{data.get('qual_tipo_de_im_vel')}" }},
                  {{ field_id: "cep", field_value: "{data.get('cep')}" }},
                  {{ field_id: "endere_o", field_value: "{data.get('endere_o')}" }},
                  {{ field_id: "n_mero", field_value: "{data.get('n_mero')}" }},
                  {{ field_id: "bairro", field_value: "{data.get('bairro')}" }},
                  {{ field_id: "cidade", field_value: "{data.get('cidade')}" }},
                  {{ field_id: "estado", field_value: "{data.get('estado')}" }},
                  {{ field_id: "qual_valor_do_im_vel", field_value: "{data.get('qual_valor_do_im_vel')}" }},
                  {{ field_id: "qual_o_valor_do_empr_stimo", field_value: "{data.get('qual_o_valor_do_empr_stimo')}" }},
                  {{ field_id: "prazo_para_pagamento", field_value: "{data.get('prazo_para_pagamento')}" }},
                  {{ field_id: "indica_o", field_value: "{'Não'}" }},
                  {{ field_id: "assessor_respons_vel", field_value: "{'301990243'}" }},
                  {{ field_id: "pol_tica_de_privacidade", field_value: "{'Li e concordo com a Política e Privacidade'}" }}
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
    return response.json()
    # Check if the request was successful


