from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route("/")
def base ():
    return render_template("base.html")

@app.route("/prueba")
def prueba ():
    return

@app.route("/formulario")
def formulario ():
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)