import re

from dotenv import load_dotenv
load_dotenv() 
import os 
from openai import AzureOpenAI

AZURE_OPENAI_API_ENDPOINT = os.getenv("AZURE_OPENAI_API_ENDPOINT", "")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "")
AZURE_OPENAI_API_MODEL = os.getenv("AZURE_OPENAI_API_MODEL", "")
AZURE_OPENAI_API_GPT_35_MODEL = os.getenv("AZURE_OPENAI_API_GPT_35_MODEL", "")
AZURE_OPENAI_API_GPT_4o_MODEL = os.getenv("AZURE_OPENAI_API_GPT_4o_MODEL", "")
client = AzureOpenAI(
azure_endpoint=AZURE_OPENAI_API_ENDPOINT,  
api_key=AZURE_OPENAI_API_KEY,  
api_version= AZURE_OPENAI_API_VERSION,
)

def get_completion(prompt: str, system_prompt="", prefill="", json_mode=False, model=AZURE_OPENAI_API_MODEL):
    print(f"==================LLM {model} response======================")
    payload = {
        "temperature":0.7,
        "top_p":0.1,
        "model": model,
        "stream": False,
        "max_tokens": 1000,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
        "messages" :  [ 
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": prefill}

        ]
    }
    if json_mode:
        payload["response_format"] =  { "type": "json_object" }
    res =  client.chat.completions.create(**payload)
    response = res.choices[0].message.content
    return response

def get_completion_with_structured_output(prompt: str, system_prompt="", output_format=None):
    print(f"==================LLM {AZURE_OPENAI_API_GPT_4o_MODEL} response======================")
    completion = client.beta.chat.completions.parse(
    model= AZURE_OPENAI_API_GPT_4o_MODEL,
    messages= [ 
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": prompt}
        ],
    response_format=output_format,
    )
    response = completion.choices[0].message.parsed
    return response

def extract_llm_response(text: str, tag: str):
    if text is None or text == "":
        print(f"text is None or empty")
        return ""
    match = re.search(fr'<{re.escape(tag)}>(.*?)</{re.escape(tag)}>', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # If tag is not found, try to match ```tag code blocks
    match = re.search(fr'```{re.escape(tag)}\s*(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # If no matches are found, return the original text
    return text.strip()
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content
