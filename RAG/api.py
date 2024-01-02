#Getting The Interfact to Get the Quetion
from flask import Flask, request
#from answer_generator import generate_answer

app = Flask(__name__)

@app.route('/answer', methods=['POST'])
def get_answer():
    if request.method == 'POST':
        question = request.json.get('question')  # Assumes JSON input with 'question' key

        if question:
            #answer = generate_answer(question)
            answer="This is the answer"
            return {'answer': answer}
        else:
            return {'error': 'Question not provided.'}, 400

if __name__ == '__main__':
    app.run(debug=True)
