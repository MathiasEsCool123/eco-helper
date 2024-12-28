from flask import Flask, render_template
import random

app = Flask(__name__)

# List of eco-friendly tips
eco_tips = [
    "Apaga las luces cuando salgas de una habitación.",
    "Reduce, reutiliza y recicla siempre que sea posible.",
    "Usa una botella de agua reutilizable en lugar de botellas desechables.",
    "Planta un árbol en tu comunidad.",
    "Opta por el transporte público o el uso compartido de vehículos para reducir las emisiones."
]

# List of random causes
random_causes = [
    "Gases de Efecto Invernadero.",
    " Cambios en el uso del suelo.",
    "Industrialización.",
    "Uso de energía no renovable."
]

@app.route('/')
def home():
    # Renderiza el archivo index.html
    return render_template('index.html')

@app.route('/advice')
def get_advice():
    return random.choice(eco_tips)

@app.route('/cause')
def get_cause():
    return random.choice(random_causes)

if __name__ == '__main__':
    app.run(debug=True)
