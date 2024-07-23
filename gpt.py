#!/usr/bin/env python3
import os
import openai
import constants

# Set up the OpenAI API client
api_key = constants.GPT_API_KEY
openai.api_key = api_key

# Define a function to ask GPT-3 a question
def generate_text(query):
    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=[ 
        {"role": "system", 
         "content": "You are a helpful assistant."}, 
         {"role": "user", "content": query} 
        ] 
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    question = str(os.environ["KMVAR_GPTprompt"])
    answer = generate_text(question)
    print(answer)