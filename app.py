from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_status():

    transaction_id = request.form["transaction_id"]

    connection = sqlite3.connect("payment.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM payments WHERE transaction_id = ?",
        (transaction_id,)
    )

    payment = cursor.fetchone()

    connection.close()

    if payment:

        return render_template(
            "result.html",
            transaction_id=payment[1],
            customer_name=payment[2],
            amount=payment[3],
            status=payment[4]
        )

    else:
        return "Transaction not found"


@app.route("/health")
def health():

    return {
        "status": "UP",
        "application": "Payment Status Monitoring"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)