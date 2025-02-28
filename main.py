from flask import Flask, request, jsonify
import openai  # Change this if using another AI model

app = Flask(__name__)

# Configure OpenAI API Key (or replace with Ollama if running locally)
openai.api_key = "YOUR_OPENAI_API_KEY"

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
