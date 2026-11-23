from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            notas = [nota1, nota2, nota3]
            notas_validas = all(10 <= n <= 70 for n in notas)
            asistencia_valida = 0 <= asistencia <= 100

            if not notas_validas:
                error = "Las notas deben estar entre 10 y 70."
            elif not asistencia_valida:
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = sum(notas) / 3
                aprobado = promedio >= 40 and asistencia >= 75
                resultado = {
                    "promedio": round(promedio, 1),
                    "asistencia": asistencia,
                    "estado": "Aprobado" if aprobado else "Reprobado",
                }
        except ValueError:
            error = "Debes ingresar solo números en todos los campos."

    return render_template("ejercicio1.html", resultado=resultado, error=error)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    error = None

    if request.method == "POST":
        nombres = [
            request.form["nombre1"].strip(),
            request.form["nombre2"].strip(),
            request.form["nombre3"].strip(),
        ]

        if "" in nombres:
            error = "Debes completar los 3 nombres."
        else:
            # Cantidad de letras de cada nombre (sin contar espacios)
            cantidades = [len(n.replace(" ", "")) for n in nombres]
            maximo = max(cantidades)
            ganadores = [
                nombres[i] for i in range(3) if cantidades[i] == maximo
            ]
            resultado = {
                "nombres": ganadores,
                "cantidad": maximo,
                "empate": len(ganadores) > 1,
            }

    return render_template("ejercicio2.html", resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)