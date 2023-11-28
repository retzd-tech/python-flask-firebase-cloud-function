from firebase_functions import https_fn
from flask import Flask
app = Flask(__name__)

@app.route('/health-check', methods=['POST'])
def generate_article():
    return "Server OK"

# nama function nya articles, ini bisa diganti dengan id atau nama student
# nama ini untuk integrasi flask ke cloud function
@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()