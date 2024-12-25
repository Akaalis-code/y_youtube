from ollama import chat
from ollama import ChatResponse


def mth_ask_for_response(para_question):
    response: ChatResponse = chat(model='llama3.2', messages=[
                                                                {
                                                                    'role': 'user',
                                                                    'content': 'In short , '+str(para_question),
                                                                },
                                                            ]
                                )
    return response

var_resp = mth_ask_for_response('hi how are you')
print(var_resp['message']['content'])
# or access fields directly from the response object
#print(var_resp.message.content)