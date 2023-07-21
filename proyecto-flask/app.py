from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')




@app.route("/")
def get_locales_comida():
    r = requests.get("http://localhost:8000/api/locales_comidas/",
            auth=('d', 'd'))
    data = json.loads(r.content)
    print(data)
    return render_template("LocalesComida.html", data=data)




@app.route("/locales_repuestos")
def get_locales_repuestos():
    r = requests.get("http://localhost:8000/api/locales_repuestos/",
            auth=('d', 'd'))
    data = json.loads(r.content)
    print(data)
    return render_template("LocalesRepuestos.html", data=data)




@app.route("/barrios")
def get_barrios():
    r = requests.get("http://localhost:8000/api/barrios/",
            auth=('d', 'd'))
    data = json.loads(r.content)
    print(data)
    return render_template("Barrios.html", data=data)




@app.route("/personas")
def get_personas():
    r = requests.get("http://localhost:8000/api/personas/",
            auth=('d', 'd'))
    data = json.loads(r.content)
    print(data)
    return render_template("Personas.html", data=data)


app.run()
