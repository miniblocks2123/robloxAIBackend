from flask import Flask, request, jsonify
import openai  # Change this if using another AI model

app = Flask(__name__)

# Configure OpenAI API Key (or replace with Ollama if running locally)
openai.api_key = "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"

@app.route('/ai-input', methods=['POST'])
def ai_input():
    data = request.json
    game_state = f"Player is at {data['position']}, moving {data['velocity']}, health {data['health']}."
    
    # Query AI Model (Replace with another model if needed)
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": game_state}]
    )
    
    return jsonify({"input": response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
