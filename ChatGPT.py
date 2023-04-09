import openai

openai.api_key = 'Token'

messages = []


def generate_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        max_tokens=2500,
        frequency_penalty=0,
        presence_penalty=0,
        temperature=0.7
    )
    answer = response['choices'][0]['message']['content']
    return answer


def chatgpt():
    print("Welcome to ChatGPT. You can start chatting with ChatGPT. To exit, type 'exit'.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        messages.append({"role": "user", "content": user_input})
        response = generate_response(messages)
        print("ChatGPT:", response)
        messages.append({"role": "assistant", "content": response})


chatgpt()
