from flask import Flask, render_template, jsonify
import numpy as np
from requests import request


app = Flask(__name__)
i = 1
random_decimal = np.random.rand()


@app.route('/')
def homepage():
    return render_template('index.html', x=random_decimal)


@app.route('/update_DecimalNumber', methods=['POST'])
def update():
    random_decimal = np.random.rand()
    return jsonify('', render_template('random_decimal_model.html', x=random_decimal, contador=i))


if __name__ == '__main__':
    app.run(debug=True)
