from flask import Flask, render_template, request

ALPHABET = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%&()+-*/=:,."]

def cesar(text, key, mode):
    return "".join([ALPHABET[(ALPHABET.index(char) + (key * mode)) % len(ALPHABET)] for char in text.upper() if char in ALPHABET])


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/do_cesar", methods=["POST"])
def do_cesar():
    text = request.form["text"]
    key = int(request.form["key"])
    mode = int(request.form["mode"])
    
    result = cesar(text, key, mode)
    
    return render_template("index.html", result=result, text=text, key=key, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)