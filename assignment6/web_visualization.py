
import os
from flask import Flask
from flask import request
from flask import render_template
from temperature_CO2_plotter import Climate

app = Flask(__name__)   # Create Flask instance that later runs the server
os.system("pydoc -w temperature_CO2_plotter")            # Generate HTML-file with documentation
os.system("mv temperature_CO2_plotter.html templates/")  # Move HTML-file into templates folder

default_temp_params = ["January", 1816, 2012, -5.4, 1.0]    # Define default params for temp
default_co2_params = [1751, 2012, 0, 10000]                 # Define default params for CO2
default_co2_by_country_params = [2010, 10.0, 30.0]  # Define default params for CO2-by-country

climate = Climate("temperature.csv", "co2.csv", "CO2_by_country.csv")   # Initiate Climate object
climate.plot_temperature(*default_temp_params)                          # Generate default plot
climate.plot_CO2(*default_co2_params)                                   # Generate default plot
climate.plot_CO2_by_country(*default_co2_by_country_params)             # Generate default plot

@app.route("/", methods = ["GET", "POST"])
def visualize_data():
    """
    Function that, based on user submitted parameters from the web page
    visualize_page.html, generates new plots using the Climate class and
    furthermore updates the web page with these new plots as the user wants.
    """
    if (request.method == "POST"):
        current_temp_params = [request.form["month"], int(request.form["syear temp"]),
            int(request.form["eyear temp"]), float(request.form["ymin temp"]),
            float(request.form["ymax temp"])]
        current_co2_params = [int(request.form["syear co2"]), int(request.form["eyear co2"]),
            float(request.form["ymin co2"]), float(request.form["ymax co2"])]
        current_co2_by_country_params = [int(request.form["year"]),
            float(request.form["ltreshold"]), float(request.form["utreshold"])]

        # Only plot temp if non-deafult parameters are submitted
        if (current_temp_params != default_temp_params):
            climate.plot_temperature(*current_temp_params)

        # Only plot CO2 if non-deafult parameters are submitted
        if (current_co2_params != default_co2_params):
            climate.plot_CO2(*current_co2_params)

        # Only plot CO2-by-country if non-deafult parameters are submitted
        if (current_co2_by_country_params != default_co2_by_country_params):
            climate.plot_CO2_by_country(*current_co2_by_country_params)


    return render_template("visualization_page.html")   # Display HTML-page with new plots

@app.route("/help")
def show_help():
    return render_template("temperature_CO2_plotter.html")

app.run(debug = True)   # Run server and initiate web page