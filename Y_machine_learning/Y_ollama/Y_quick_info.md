0) sudo apt install python3-pip
1) curl -fsSL https://ollama.com/install.sh | sh     -->> ollama gets installed in your system and starts some services
   http://localhost:11434/                           -->> In this url its saying ollama running , need to figureout how to stop it , 
                                                          other than using systemctl
2) ollama run <your_model_choice>                    -->> Through ollama the model gets downloaded and installed and starts running in your system
   ollama stop <your_model_choice>                   -->> This will stop your running model
3) pip install ollama                                -->> Python library which lets you talk to your local running ollama and your model
4) Next Run this below code in python :
        from ollama import chat
        from ollama import ChatResponse

        response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
        ])
        print(response['message']['content'])
        # or access fields directly from the response object
        print(response.message.content)