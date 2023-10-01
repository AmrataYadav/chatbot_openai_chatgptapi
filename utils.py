import openai


def get_initial_message():
    messages=[
        {"role":"system", "content": "You are a helpful AI Tutor. Write answer to coding questions in coding syntax"},
        {"role":"user","content":"I want help with python code."},
        {"role":"assistant", "content":"That's awesome, what do you want to do in python"}
        ]

    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model:",model)
    response = openai.ChatCompletion.create(model=model,messages=messages)
    return response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

