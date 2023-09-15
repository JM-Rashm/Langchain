
from ai.aiservices.generative_ai_service import GenerativeAIService


class VRRequestService:
    def __init__(self) -> None:
        self.generate_ai = GenerativeAIService()
    
    def get_response_from_ai(self, subject):
        response = self.generate_ai.generate_response(subject)
        return response