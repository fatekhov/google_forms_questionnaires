from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

import pandas as pd

file_name = r'tests.xlsx' # excel file name
tests = pd.read_excel(file_name,
     engine='openpyxl',
     sheet_name= 0 ) # don't forget to change the sheet if needed!!!
strings = tests['question'].tolist()

title_name = 'Опросник Шулера (1994)' # Title of the form 


SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)

form_service = discovery.build('forms', 'v1', http=creds.authorize(
    Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

# Request body for creating a form
NEW_FORM = {
    "info": {
        "title": title_name,
    }
}

# Creates the initial form
result = form_service.forms().create(body=NEW_FORM).execute()

for num, text_name in enumerate(strings):

    NEW_QUESTION = {
    "requests": [{
        "createItem": {
            "item": {
                "title": text_name,
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "Абсолютно не согласен"},
                                {"value": "Не согласен"},
                                {"value": "Нейтрален"},
                                {"value": "Согласен"},
                                {"value": "Абсолютно согласен"}   
                            ],
                            "shuffle": False
                        }
                    }
                },
            },
            "location": {
                "index": num
            }
        }
    }]
}



    # Adds the question to the form
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

    # Prints the result to show the question has been added
    get_result = form_service.forms().get(formId=result["formId"]).execute()
    print(get_result)