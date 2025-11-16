from flask import Flask, render_template, request
from statistics import mean

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/formulario_notas', methods=['POST'])
def formulario_notas():
    # inputs
    notas = [float(request.form['nota1']), float(request.form['nota2']), float(request.form['nota3'])]
    asistencia = float(request.form['asistencia'])
    
    # Calculo
    promedio = mean(notas)
    estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
    
    # Output
    return render_template('ejercicio1.html', 
                         promedio=round(promedio, 2),
                         estado=estado)

@app.route('/cantidad_caracteres', methods=['POST'])
def cantidad_caracteres():
    # inputs
    nombre_1 = request.form['nombre_1']
    nombre_2 = request.form['nombre_2']
    nombre_3 = request.form['nombre_3']

    # Calculo
    nombre_mayor = max([nombre_1, nombre_2, nombre_3], key=len)
    cantidad = len(nombre_mayor)

    # Output
    return render_template('ejercicio2.html', 
                            nombre_mayor=nombre_mayor, 
                            cantidad=cantidad)

if __name__ == '__main__':
    app.run(debug=True)
    