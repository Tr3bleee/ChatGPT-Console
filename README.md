# ChatGPT
This code utilizes OpenAI's GPT-3 language model to create a conversational chatbot called ChatGPT. It allows users to interact with the chatbot by entering messages, and the chatbot generates responses based on the input using the GPT-3 model.

# Requirements
1. OpenAI Python module: You need to have the OpenAI Python module installed to use this code. You can install it using pip by running pip install openai.

2. OpenAI API key: You also need to have a valid OpenAI API key. You can obtain an API key from OpenAI's website (https://platform.openai.com/).

# Usage
1. Set your OpenAI API key: Replace the 'Token' string in the openai.api_key line with your actual API key obtained from OpenAI.

2. Start chatting: Run the chatgpt() function to start the chatbot. It will display a welcome message and prompt you to enter messages. Type your messages as if you're having a conversation with a chatbot.

3. Exit: To exit the chat, simply type 'exit'. The chatbot will print a goodbye message and terminate the program.

# How it works
1. Messages: The chatbot uses a list called messages to keep track of the conversation. Each message is stored as a dictionary with two keys: 'role' (which can be either 'user' or 'assistant') and 'content' (which contains the text of the message).

2. generate_response() function: This function takes a list of messages as input and uses the GPT-3 model to generate a response. It sets various parameters like model (the GPT-3 model to use), max_tokens (the maximum length of the generated response), frequency_penalty (to discourage repeated phrases), presence_penalty (to discourage irrelevant responses), and temperature (to control randomness of the output).

3. chatgpt() function: This function implements the main loop of the chatbot. It takes user input, adds it to the messages list, calls generate_response() to generate a response, prints the response, and adds it to the messages list as an assistant's message. It continues to loop until the user enters 'exit' to terminate the chat.


Note: The code uses a simple input/output mechanism, where the user enters text input and the chatbot responds with text output. You can customize and extend the functionality of the chatbot by modifying the generate_response() function or by adding additional logic to the chatgpt() function. Please refer to OpenAI's documentation for more information on using the GPT-3 model and its capabilities.
