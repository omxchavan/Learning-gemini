from flask import Flask, request, jsonify, render_template, session
import google.generativeai as genai

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Gemini API
genai.configure(api_key='AIzaSyD_xFrv1YGDJgEJlxkQ3dtxmLgKZJpskGI')

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')  # Frontend for the chatbot interface

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Get the message from AJAX
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response from Gemini
        response = model.generate_content(user_message)
        session['chat_history'] = session.get('chat_history', []) + [
            {'user': user_message, 'gemini': response.text}
        ]
        return jsonify({'user': user_message, 'gemini': response.text})  # Return JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/history')
def history():
    chat_history = session.get('chat_history', [])
    return render_template('history.html', chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
