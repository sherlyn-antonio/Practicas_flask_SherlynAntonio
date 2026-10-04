from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    perimetro = None

    if request.method == 'POST':
        radio = float(request.form['radio'])

        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

    return render_template(
        'circulo.html',
        area=area,
        perimetro=perimetro
    )


if __name__ == '__main__':
    app.run(debug=True)