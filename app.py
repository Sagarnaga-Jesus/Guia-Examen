from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)



@app.route("/prueba")
def prueba ():
    return

@app.route("/")
def formulario ():
    return render_template("formulario.html")

@app.route("/resultado", methods = ["Get", "POST"])
def resultado():
    if request .method == "POST":
        edad = request.form["edad"]
        altu = request.form["altu"]
        peso = request.form["peso"]
        genero = request.form["genero"]
        actividad = request.form["activi"]
        
        tbm = 0
        get = 0
        nivel = 0
        altura = float(altu)*100
        
        if actividad == "sedentario":
            nivel = 1.2
        else:
            if actividad == "ligera":
                nivel = 1.375
            else:
                if actividad == "moderada":
                    nivel=1.55
                else:
                    if actividad == "alta":
                        nivel = 1,725
        
        if genero == "hombre":
            tbm = 10*float(peso)+6.25*float(altura)-5*float(edad)+5
        else:
            if genero == "mujer":
                tbm = 10*float(peso)+6.25*float(altura)-5*float(edad)-161
        
        get = tbm * nivel
        
    return render_template("resultado.html",get=get,tbm=tbm,)


if __name__ == "__main__":
    app.run(debug=True)