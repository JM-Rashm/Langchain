import openai
import os
from langchain.llms import OpenAI

class GenerativeAIService:
    def __init__(self) -> None:
        openai.api_key = os.getenv("VROC_OPENAI_API_KEY")
        self.llm = OpenAI(model_name="text-davinci-003")
        
    def generate_response(self, input):
        our_query = f"What is the funny fact about " + input
        print(our_query)
        response = self.llm(our_query)
        return response
    
    