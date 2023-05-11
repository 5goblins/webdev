from flask import Flask, render_template

app = Flask(__name__)

#Rutas de la APP
@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/agregar-donacion.html")
def agregardonacion():
    return render_template("agregar-donacion.html")

@app.route("/agregar-pedido.html")
def agregarpedido():
    return render_template("agregar-pedido.html")

@app.route("/ver-pedidos.html")
def verpedidos():
    return render_template("ver-pedidos.html")

@app.route("/ver-donaciones.html")
def verdonacions():
    return render_template("ver-donaciones.html")

if __name__ == "__main__":
    app.run(debug=True)