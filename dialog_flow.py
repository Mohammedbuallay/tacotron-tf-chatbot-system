import dialogflow, os

def send_to_dialogflow(text_to_be_analyzed):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'new-drphfu-289d9a316551.json'
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path('new-drphfu', 'en-US')
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code='en')
    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

print (send_to_dialogflow("hi"))    