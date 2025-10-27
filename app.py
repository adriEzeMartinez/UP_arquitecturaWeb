from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Datos de Homero X
citas = [
    "¡D'oh!",
    "¡Mmm... rosquillas!",
    "No soy un hombre de plegarias, pero si estás ahí arriba... ¡Sálvame Superman!",
    "Hable más fuerte que tengo una toalla.",
    "¡Lisa, en esta casa obedecemos a las leyes de la termodinámica!"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cita')
def cita():
    return jsonify({"cita": random.choice(citas)})
    
    respuesta = random.choice(respuestas)
    return jsonify({"respuesta": respuesta})
if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    print(port)
    url = "http://127.0.0.1:{0}".format(port)
    print(url)
    app.run(use_reloader=False, debug=True, port=port)
