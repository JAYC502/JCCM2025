from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')

    messages = [
        {"role": "system", "content": "Eres el asistente personalizado del CEO, atento, claro y útil."},
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({'response': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
