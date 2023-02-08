from dotenv import load_dotenv
import openai
import os


load_dotenv()

#openai.api_key = os.getenv('CHATGPT_API_KEY')
openai.api_key = "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"
def chatgpt_response(prompt):
    response = openai.Completion.create(
       engine = "text-davinci:003",
       prompt = prompt,
       temperature = 1,
       max_tokens = 100
       
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response
