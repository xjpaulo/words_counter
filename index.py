#!/usr/bin/env python3
# -*- coding: utf-8 -*

from flask import Flask, jsonify, make_response, render_template, request

app = Flask('__name__')


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/counter/words', methods=['POST'])
def words_counter():
    request_data = request.get_json()
    message = request_data['message']
    words = message.split()
    result = len(words)
    if result == 0:
        return make_response(jsonify({"error": "At least one word is required."}), 400)
    return make_response(jsonify({"result": result}), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')

