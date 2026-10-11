from flask import Flask, render_template

# Crear instancia Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Ejecutar servidor local
if __name__ == "__main__":
    app.run(debug=True)
