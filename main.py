from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Formulario de cálculo de compras
@app.route('/calculo-compras', methods=['GET', 'POST'])
def calculo_compras():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        
        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro
        
        # Calcular descuento según edad
        if edad < 18:
            porcentaje_descuento = 0
        elif 18 <= edad <= 30:
            porcentaje_descuento = 15
        else:  # edad > 30
            porcentaje_descuento = 25
        
        descuento = total_sin_descuento * (porcentaje_descuento / 100)
        total_con_descuento = total_sin_descuento - descuento
        
        return render_template('calculo-compras.html', 
                             resultado=True,
                             nombre=nombre,
                             total_sin_descuento=total_sin_descuento,
                             descuento=descuento,
                             total_con_descuento=total_con_descuento)
    
    return render_template('calculo-compras.html', resultado=False)

# Formulario de inicio de sesión
@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        # Usuarios válidos con sus roles
        usuarios = {
            'juan': {'password': 'admin', 'rol': 'administrador'},
            'pepe': {'password': 'user', 'rol': 'usuario'}
        }
        
        if nombre in usuarios and usuarios[nombre]['password'] == password:
            rol = usuarios[nombre]['rol']
            return render_template('inicio-sesion.html', 
                                 resultado=True,
                                 exito=True,
                                 nombre=nombre,
                                 rol=rol)
        else:
            return render_template('inicio-sesion.html', 
                                 resultado=True,
                                 exito=False)
    
    return render_template('inicio-sesion.html', resultado=False)

if __name__ == '__main__':
    app.run(debug=True)