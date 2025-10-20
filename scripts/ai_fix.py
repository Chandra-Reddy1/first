from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze_logs():
    data = request.get_json()
    logs = data.get("logs", "")
    context = data.get("context", "")

    prompt = f"""
    You are a DevOps engineer AI assistant. Analyze the following GitHub Actions build logs.
    Identify the root cause and suggest a fix in shell script form if possible.

    Logs:
    {logs}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    suggestion = response.choices[0].message.content
    return jsonify({"suggestion": suggestion})
