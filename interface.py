from flask import Flask, render_template, jsonify, request
# from calculations import get_add
from utils import get_price

app = Flask(__name__)  # Creating an application

#################################################################


@app.route('/')
def hello_flask():
    print("Welcome to Flask")

    return "Hello Flask"


####################################################################

@app.route('/boston/predict_price')
def get_house_price():
    data = request.form
    print("Data :", data)
    price = get_price(data)
    return jsonify({'Price': f"{price} $"})


if __name__ == "__main__":
    app.run()
    # app.run(host= '0.0.0.0', port= 5002, debug=True)
