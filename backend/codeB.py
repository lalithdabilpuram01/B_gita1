
import openai_helper
from logging_setup import  setup_logger
from openai import OpenAI

import os



logger = setup_logger('codeB')

def ask_gita(query):
    # Initialize OpenAI client with API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", openai_helper.api_key))

    # Get user query about a book



    messages = [

        {"role": "system", "content": "You are an expert guide on the Bhagavad Gita. When a user asks a question, provide a thoughtful and concise answer inspired by the teachings of the Bhagavad Gita. Include relevant verses (with chapter and verse numbers) when appropriate, and explain the meaning in simple, modern language. Stay true to the philosophy of the Gita and avoid adding unrelated information. If a question cannot be directly answered by the Gita, offer a principle or wisdom from the Gita that can provide guidance."},
        {"role": "user", "content": query}
    ]
    logger.info(f'ask_Gita is called . Question : {query}')

    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,  # Limit response length
            temperature=0.7  # Control creativity
        )

        # Extract and return the response
        answer = response.choices[0].message.content

        #print(answer)
        return  answer

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your API key, quota, or internet connection.")

if __name__ == "__main__":
    ask_gita()






