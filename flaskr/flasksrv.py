from flask import Flask, request, jsonify, redirect, url_for, render_template

from svf_abi import SVF_O5GS

app = Flask(__name__)

received_data_list = []
current_command = None
ogs_api: SVF_O5GS = None # ustawiam to w main.py....

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/set_command", methods=["POST"])
def set_command():
    # global current_command
    # current_command = request.form.get("command")
    # print("Wysłana komenda:", current_command)
    key = ogs_api.get_enc_k("imsi-" + (request.form.get("command") or ""))
    received_data_list.append(key.decode("ascii"))
    return redirect(url_for("home"))

@app.route("/command", methods=["GET"])
def get_command():
    return jsonify({"command": current_command})

@app.route("/data", methods=["POST"])
def receive_data():
    global current_command

    text_data = request.get_data(as_text=True)

    if text_data:
        received_data_list.append(text_data)
        current_command = None  # jednorazowa obsługa
        print("Otrzymany tekst:", text_data)
        return "OK", 200

    return "Brak danych", 400

@app.route("/data_list", methods=["GET"])
def data_list():
    return jsonify(received_data_list)

@app.route("/save", methods=["POST"])
def save_data():
    with open("data.txt", "w", encoding="utf-8") as f:
        for item in received_data_list:
            f.write(item + "\\n\\n")

    print("Dane zapisane do pliku data.txt")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
