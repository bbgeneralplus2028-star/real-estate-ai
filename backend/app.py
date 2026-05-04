from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Property System Running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    P = float(data["purchase"])
    ARV = float(data["arv"])
    sqft = float(data["sqft"])
    cost_per_ft = float(data["condition"])
    months = float(data["months"])

    RC = sqft * cost_per_ft
    EC = RC * 0.10
    TC = months * 2000
    CC = (RC + EC) * 0.15

    TP = RC + EC + TC + CC
    total = P + TP
    profit = ARV - total

    if profit > 80000:
        strategy = "FLIP"
    elif profit > 30000:
        strategy = "MINIMAL REHAB"
    elif profit > 0:
        strategy = "SECTION 8 / OWNER FINANCE"
    else:
        strategy = "WALK AWAY"

    return jsonify({
        "repair": RC,
        "equipment": EC,
        "holding": TC,
        "contingency": CC,
        "transformation": TP,
        "total": total,
        "profit": profit,
        "strategy": strategy
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
