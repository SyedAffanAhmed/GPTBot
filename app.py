from flask import Flask, request, jsonify
from Bot import ChatGPTBotAPI

app = Flask(__name__)

# Initialize the ChatGPTBotAPI with the OpenAI API key
# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
bot_api = ChatGPTBotAPI('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')

@app.route("/")
def home():
    return "Welcome to CHATGPT BOT"

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    """
    Endpoint to create and store a new prompt.
    """
    data = request.get_json()
    prompt = data.get('prompt')
    
    if prompt:
        bot_api.create_prompt(prompt)
        return jsonify({'message': 'Prompt created successfully!'}), 201
    else:
        return jsonify({'error': 'Prompt is required in the request body.'}), 400

@app.route('/get_response', methods=['GET'])
def get_response():
    """
    Endpoint to get the ChatGPT bot's response for a given prompt index.
    """
    prompt_index = request.args.get('prompt_index')

    if prompt_index is None:
        return jsonify({'error': 'Prompt index is required as a query parameter.'}), 400
    
    # Convert the prompt_index to an integer
    try:
        prompt_index = int(prompt_index)
    except ValueError:
        return jsonify({'error': 'Invalid prompt index. Prompt index must be an integer.'}), 400

    response = bot_api.get_response(prompt_index)
    return jsonify({'response': response}), 200

@app.route('/update_prompt', methods=['PUT'])
def update_prompt():
    """
    Endpoint to update an existing prompt at the specified index with a new prompt.
    """
    data = request.get_json()
    prompt_index = data.get('prompt_index')
    new_prompt = data.get('new_prompt')

    if prompt_index is None or new_prompt is None:
        return jsonify({'error': 'Prompt index and new prompt are required in the request body.'}), 400
    
    # Convert the prompt_index to an integer
    try:
        prompt_index = int(prompt_index)
    except ValueError:
        return jsonify({'error': 'Invalid prompt index. Prompt index must be an integer.'}), 400

    bot_api.update_prompt(prompt_index, new_prompt)
    return jsonify({'message': 'Prompt updated successfully!'}), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
