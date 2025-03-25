from flask import Flask, render_template, request

ALPHABET = "ABCDEFGHIJKLMNIOPQRSTUVWXYZ"

def vigenere(text=str, key=list, mode=int):
    return "".join([ALPHABET[(ALPHABET.index(text[i]) + int(key[i]) * mode) % len(ALPHABET)] for i in range(len(text))])


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/do_vigenere", methods=["POST"])
def do_cesar():
    text = request.form["text"].upper()
    key = request.form["key"].split(",")
    mode = int(request.form["mode"])
    
    result = vigenere(text, key, mode)
    
    return render_template("index.html", result=result, text=text, key=key, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)