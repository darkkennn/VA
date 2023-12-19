from flask import Flask, request, jsonify;
from flask_cors import CORS;

app = Flask(__name__);
CORS(app);

@app.route('/processAudio', methods=['POST'])
def processAudio():
    audioData = request.form.get('audio');
    print(audioData)
    return jsonify(audioData);


@app.route('/processChat', methods=['POST'])
def processChat():
    chatData = request.form.get('chat');
    print(chatData)
    return jsonify(chatData);

if __name__ == '__main__':
    app.run(debug = True)



