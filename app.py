from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Fake AI responses based on keywords in the question
def generate_fake_ai_response(question):
    """
    Generates a fake AI response based on keywords in the question.
    This is a simple rule-based approach to simulate AI functionality.
    """
    question = question.lower()
    
    # Responses based on question keywords
    if 'hello' in question or 'hi' in question:
        responses = [
            "Hello there! How can I assist you today?",
            "Hi! Nice to meet you. What can I help with?",
            "Greetings! I'm here to help with your queries."
        ]
    elif 'weather' in question:
        responses = [
            "I don't have real-time weather data, but I suggest checking a weather service!",
            "Weather information requires live data which I can't access.",
            "For accurate weather forecasts, please check dedicated weather websites."
        ]
    elif 'name' in question:
        responses = [
            "I'm your friendly AI assistant for this practice exercise!",
            "You can call me FakeAI, your practice assistant.",
            "I'm an AI simulation created for educational purposes."
        ]
    elif 'help' in question:
        responses = [
            "I can answer simple questions! Try asking about my name, the weather, or just say hello.",
            "I'm here to demonstrate a Flask API with simulated AI responses.",
            "Ask me anything and I'll give you a simulated AI response!"
        ]
    elif 'bye' in question or 'goodbye' in question:
        responses = [
            "Goodbye! Feel free to come back with more questions.",
            "See you later! Thanks for trying out this demo.",
            "Farewell! Hope this was helpful for your practice."
        ]
    else:
        # Default responses for general questions
        responses = [
            "That's an interesting question. In a real implementation, I would analyze this deeply.",
            "Thanks for your query. This is a simulated response for demonstration purposes.",
            "I've processed your question and determined that this is a great learning exercise!",
            "Based on my analysis (just kidding!), I recommend reviewing Flask APIs for real implementations.",
            "As an AI assistant, I appreciate your curiosity. Keep experimenting with code!",
            "I've consulted my vast knowledge base (okay, not really) to provide this response.",
            "This is a placeholder response from our simulated AI. Great job setting up the project!"
        ]
    
    return random.choice(responses)

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Endpoint to ask a question and receive a simulated AI response.
    
    Expected JSON input:
    {
        "question": "Your question here"
    }
    
    Returns:
    {
        "answer": "Simulated AI response"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({'error': 'Missing question in request body'}), 400
        
        question = data['question']
        
        if not question or not question.strip():
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        # Generate a fake AI response
        answer = generate_fake_ai_response(question)
        
        return jsonify({'answer': answer}), 200
    
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint with information about the API
    """
    return jsonify({
        'message': 'Fake AI Flask API',
        'endpoint': '/ask',
        'method': 'POST',
        'request_format': {'question': 'Your question here'},
        'response_format': {'answer': 'Simulated AI response'}
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)