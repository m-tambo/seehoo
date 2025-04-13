import requests

from ...config import OLLAMA_URL

class Ollama:
    
    @classmethod
    def prompt(prompt, model="llama2", stream=False):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }

        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json()