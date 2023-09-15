from flask import jsonify, request
import http.client
from ai.services.vr_requests_service import VRRequestService

class VRRequestController:
    def __init__(self):
        self.vr_service = VRRequestService()
    
    def get_response_for_user(self):
        data = request.get_json()
        print(data)
        try:
            response_data = self.vr_service.get_response_from_ai(data)
            response_status = http.client.OK
            response_message = "Success"
        except Exception as e:
            response_data = str(e)
            response_status = http.client.INTERNAL_SERVER_ERROR
            response_message = response_data
            
        response = {
            "data": response_data,
            "status": response_status,
            "message": response_message,
        }
        return jsonify(response), response_status