from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    colors = ['red', 'green', 'blue']
    words = ['RED', 'GREEN', 'BLUE']
    stimuli = [f"{color}-{word}" for color in colors for word in words]

    if request.method == 'POST':
        results = request.form
        # Przetwórz wyniki i wyświetl wyniki testu
        return render_template('test.html', results=results)

    # Zmień kolejność wyświetlania bodźców
    random.shuffle(stimuli)

    return render_template('test.html', stimuli=stimuli, colors=colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)