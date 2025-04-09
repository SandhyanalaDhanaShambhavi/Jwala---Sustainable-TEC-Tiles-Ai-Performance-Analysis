from flask import Flask, render_template, request, send_file
from utils.predict import make_prediction
from utils.pdf_gen import generate_pdf
from utils.plot_graph import create_performance_plot
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        data = {
            "Doping_Level": float(request.form["doping"]),
            "Temp_Gradient": float(request.form["temp_gradient"]),
            "Seebeck_Coefficient": float(request.form["seebeck"]),
            "Thermal_Conductivity": float(request.form["thermal"]),
            "Electrical_Conductivity": float(request.form["electrical"])
        }
        result = make_prediction(data)
        generate_pdf(data, result)
        create_performance_plot()
    return render_template("index.html", result=result)

@app.route("/download")
def download():
    return send_file("report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)