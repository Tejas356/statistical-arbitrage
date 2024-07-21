from flask import Flask, request, render_template, jsonify
from matched_betting import * 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    odds1 = convert_odds(data['odds1'])
    odds2 = convert_odds(data['odds2'])
    bet_amount = float(data['bet_amount'])
    if odds1 is None or odds2 is None:
        return jsonify(result="Invalid odds format. Please enter odds as a decimal or fraction.")
    result = twoWayBets(odds1, odds2, bet_amount)
    if len(result) == 0:
        formatted_result = "No possible positive outcome"
    else:
        formatted_result = {
            k: (f"{v[0]:.2f}", f"{v[1]:.2f}") for k, v in result.items()
        }
    return jsonify(result=formatted_result)

if __name__ == "__main__":
    app.run(debug=True)
