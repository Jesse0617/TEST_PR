from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False


@app.route('/hello')
def hello():

    data = [
        {"name": "山田"},
        {"age": 30}
    ]
    return jsonify({
        'status': 'OK',
        'data': data
    })


if __name__ == "__main__":
    app.run(debug=True)
