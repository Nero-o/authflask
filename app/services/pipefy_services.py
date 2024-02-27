# app/services/pipefy_service.py
import requests

PIPEFY_API_URL = "https://api.pipefy.com/graphql"

def create_pipefy_card(data):
    # Extract data from the request
    person_type = data.get('person_type')
    name = data.get('name')
    cpf = data.get('cpf')
    marital_status = data.get('marital_status')
    phone = data.get('phone')
    email = data.get('email')
    monthly_income = data.get('monthly_income')
    property_type = data.get('property_type')
    cep = data.get('cep')
    address = data.get('address')
    number = data.get('number')
    neighborhood = data.get('neighborhood')
    city = data.get('city')
    state = data.get('state')
    property_value = data.get('property_value')
    loan_value = data.get('loan_value')
    payment_term = data.get('payment_term')

    # Prepare the request payload
    payload = {
        "query": """
        mutation {
          createCard(input: {
            pipeId: "your_pipe_id",
            title: "%s",
            fields_attributes: [
              { fieldId: "person_type_field_id", fieldValue: "%s" },
              { fieldId: "name_field_id", fieldValue: "%s" },
              { fieldId: "cpf_field_id", fieldValue: "%s" },
              { fieldId: "marital_status_field_id", fieldValue: "%s" },
              { fieldId: "phone_field_id", fieldValue: "%s" },
              { fieldId: "email_field_id", fieldValue: "%s" },
              { fieldId: "monthly_income_field_id", fieldValue: "%s" },
              { fieldId: "property_type_field_id", fieldValue: "%s" },
              { fieldId: "cep_field_id", fieldValue: "%s" },
              { fieldId: "address_field_id", fieldValue: "%s" },
              { fieldId: "number_field_id", fieldValue: "%s" },
              { fieldId: "neighborhood_field_id", fieldValue: "%s" },
              { fieldId: "city_field_id", fieldValue: "%s" },
              { fieldId: "state_field_id", fieldValue: "%s" },
              { fieldId: "property_value_field_id", fieldValue: "%s" },
              { fieldId: "loan_value_field_id", fieldValue: "%s" },
              { fieldId: "payment_term_field_id", fieldValue: "%s" }
            ]
          }) {
            card {
              id
              title
            }
          }
        }
        """ % (name, person_type, name, cpf, marital_status, phone, email, 
               monthly_income, property_type, cep, address, number, 
               neighborhood, city, state, property_value, loan_value, 
               payment_term)
    }

    # Make the request to Pipefy API
    headers = {
        "Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MDkwMTY1NzIsImp0aSI6Ijg2YjlkMTlhLTNlMDQtNDllZC1iNjJhLTU3N2M1MGQ4NDJiMSIsInN1YiI6MzAxOTkwMjQzLCJ1c2VyIjp7ImlkIjozMDE5OTAyNDMsImVtYWlsIjoicGF1bG9AbWFwc2NyZWRpdG8uY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDMyNjI5OSwic2NvcGVzIjpbXX0sImludGVyZmFjZV91dWlkIjpudWxsfQ.ZjD_-XUqI8ofoGHzBB_lZK-kLb81JSdu0FkXjLNPR_zlGERTtjNMzxVdaKJNLTvh_3QSQtFwWOpyWY-qdJx0aA",
        "Content-Type": "application/json"
    }
    response = requests.post(PIPEFY_API_URL, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        card_data = result['data']['createCard']['card']
        return card_data
    else:
        # Handle API error
        return None