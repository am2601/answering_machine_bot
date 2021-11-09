from flask import Flask, request

app = Flask(__name__)

previous_text = ''
current_text = ''
answer = ''
received_messages = []

@app.route("/", methods=['POST', 'GET'])
def hi():
    return received_messages

@app.route("/post_aswer", methods=['POST']) # google colab post answer -- 3
def get_answer():
    global answer
    imd = request.args
    imd.to_dict(flat=True)
    answer = imd["answer"]
    # print(f'/post_aswer: {answer}')
    return 'ok'

@app.route("/get_user_text", methods=['GET']) # google colab get users text -- 2
def get():
    global current_text
    global previous_text
    if current_text != previous_text:
        previous_text = current_text[:]
        # print(f'/get_user_text: {current_text}')
        return current_text
    return 'NOTEXT'

@app.route("/post_user_text", methods=['POST']) # java app post users text on server -- 1
def post_text():
    global current_text
    imd = request.args
    imd.to_dict(flat=True)
    current_text = imd["text"]
    # print(f'/post_user_text: {current_text}')
    received_messages.append(current_text)
    return current_text

@app.route("/get_answer", methods=['GET']) # java app get answer from server -- 4
def get_text():
    global answer
    return answer