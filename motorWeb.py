from flask import Flask, render_template_string
import base64

app = Flask(__name__)

@app.route('/')
def index():
    with open("motor.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return render_template_string('''
        <html>
        <head>
            <title>Mi Ventana</title>
            <style>
                body {
                background-color: white;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            #imagen {
                display: block;
                margin-bottom: 20px;
            }

            #buttons {
                display: flex;
                flex-direction: row;
                justify-content: center;
                gap: 5px;
            }
            </style>
        </head>
        <body>
            <img id="imagen" src="data:image/png;base64,{{ imagen }}">
            <div id="buttons">
                <button onclick="rotar_izquierda()">Rotar Izquierda</button>
                <button onclick="parar_rotacion()">Parar</button>
                <button onclick="rotar_derecha()">Rotar Derecha</button>
            </div>
            <script>
                var anguloRotacion = 0;
                var rotacionActiva = false;
                var intervaloRotacion;

                var imagenElement = document.getElementById('imagen');

                function rotar_imagen(angulo) {
                    anguloRotacion += angulo;
                    imagenElement.style.transform = 'rotate(' + anguloRotacion + 'deg)';
                }

                function rotar_izquierda() {
                    if (!rotacionActiva) {
                        rotacionActiva = true;
                        intervaloRotacion = setInterval(function() {
                            rotar_imagen(-10);
                        }, 100);
                    }
                }

                function rotar_derecha() {
                    if (!rotacionActiva) {
                        rotacionActiva = true;
                        intervaloRotacion = setInterval(function() {
                            rotar_imagen(10);
                        }, 100);
                    }
                }

                function parar_rotacion() {
                    rotacionActiva = false;
                    clearInterval(intervaloRotacion);
                }
            </script>
        </body>
        </html>
    ''', imagen=encoded_string)

if __name__ == '__main__':
    app.run(debug=True)
