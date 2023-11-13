from firebase_functions import https_fn
from flask import Flask, request, jsonify
import os
import openai

openai.api_key = os.getenv("OPEN_AI")
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_article():
    data = request.json
    prompt = data['prompt']

    image_url = generate_image_with_dall_e(prompt)
    article = generate_article(prompt)

    result = {
        "image_url": image_url,
        "article": article
    }

    return jsonify(result)

def generate_article(topic):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Write a 3 paragraph of an article about {topic}",
        max_tokens=1024
        )
    return response

def generate_image_with_dall_e(text_prompt):
    response = openai.Image.create(
        prompt=text_prompt,
        n=1,
        size="512x512"
    )
    return response

@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()