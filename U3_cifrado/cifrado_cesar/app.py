from flask import Flask, render_template, request

ALPHABET = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%&()+-*/=:,."]

def cifrar_texto(texto, clave):
    return "".join([ALPHABET[(ALPHABET.index(letra) + clave) % len(ALPHABET)] for letra in texto.upper() if letra in ALPHABET])


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cifrar", methods=["POST"])
def cifrar():
    texto = request.form["texto"]
    clave = int(request.form["clave"]) 
    
    resultado = cifrar_texto(texto, clave)
    
    return render_template("index.html", resultado=resultado, texto=texto, clave=clave)

if __name__ == "__main__":
    app.run(debug=True)