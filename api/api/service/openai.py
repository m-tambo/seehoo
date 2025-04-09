from openai import OpenAI
from os import environ

class Client(OpenAI):
    def __init__(self):
        super().__init__(api_key=environ.get('OPEN_AI_API_KEY'))

    def message(self, input):
        try:
            response = self.responses.create(
                model="gpt-4o",
                # TODO: set ^ in env
                input=input
            )
            return response
        except Exception as e:
            return f"Error: {e}"
            
ai = Client()
