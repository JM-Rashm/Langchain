from flask_cors import CORS
from ai.controllers.vr_requests_controller import VRRequestController

def get_routes(app):
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    vr_contrioller = VRRequestController()
    
    # Define a route and view function
    # @app.route('/api')
    # def hello():
    #     return "Hello, Flask!"

    # @app.route("/api", methods=["POST"])
    @app.route('/api', methods=["POST"])
    def vr_request():
        return vr_contrioller.get_response_for_user()