
from flask import Flask
from flask import request
from flask import render_template
from temperature_CO2_plotter import Climate

app = Flask(__name__)

climate = Climate("temperature.csv", "co2.csv", "CO2_by_country.csv")
climate.plot_temperature("January", 1816, 2012, -5.4, 1.0)
climate.plot_CO2(1751, 2012, 0, 10000)
climate.plot_CO2_by_country(2010, 10.0, 30.0)

@app.route("/", methods = ["GET", "POST"])
def render_html_template():
    if (request.method == "GET"):
        pass

    elif (request.method == "POST"):
        print(request.form["start year"])
        climate.plot_temperature(request.form["month"], int(request.form["start year"]),
            int(request.form["end year"]), float(request.form["y_min"]), float(request.form["y_max"]))

    return render_template("visualization_page.html")

app.run(debug = True, host = "0.0.0.0")