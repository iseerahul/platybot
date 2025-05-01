from flask import Flask, render_template, request, jsonify, session
from platy import ask_platy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session management

@app.route("/")
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template("index.html", chat_history=session['chat_history'])

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = ask_platy(user_message)
    
    # Store in session history
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    chat_entry = {
        'message': user_message,
        'reply': bot_reply,
        'timestamp': datetime.now().isoformat()
    }
    session['chat_history'].insert(0, chat_entry)
    
    # Keep only last 10 conversations
    session['chat_history'] = session['chat_history'][:10]
    
    return jsonify({
        "reply": bot_reply,
        "timestamp": chat_entry['timestamp']
    })

@app.route("/clear", methods=["POST"])
def clear_history():
    session['chat_history'] = []
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
