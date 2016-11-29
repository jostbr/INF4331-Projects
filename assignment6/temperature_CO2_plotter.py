
import os
import seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Climate(object):
    """Add class docstring"""
    def __init__(self, temperature_filename, CO2_filename, CO2_by_country_filename):
        """Add docstring"""
        self.temperature_filename = temperature_filename
        self.CO2_filename = CO2_filename
        self.CO2_by_country_filename = CO2_by_country_filename

        plt.style.use("ggplot")        
        plt.rcParams["figure.figsize"] = (12, 4)

    def plot_temperature(self, month, start_year, end_year, y_min, y_max):
        """Add docstring"""
        plt.Figure()
        plt.hold(False)

        temp_data = pd.read_csv(self.temperature_filename, index_col = "Year")
        temp_data.loc[start_year:end_year, month].plot(
            linewidth = 2, color = (129.0 / 255, 63.0 / 255, 200.0 / 255))

        plt.axis([start_year, end_year, y_min, y_max])
        plt.title("Temperatures for {} in the period {}".format(month,
            str(start_year) + "-" + str(end_year)), fontsize = 18)
        plt.xlabel("Year", fontsize = 16)
        plt.ylabel("Temperature [$^{\circ}C$]", fontsize = 16)

        image_filename = self.temperature_filename.split(".")[0] + ".png"
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight")

    def plot_CO2(self, start_year, end_year, y_min, y_max):
        """Add docstring"""
        plt.Figure()
        plt.hold(False)

        CO2_data = pd.read_csv(self.CO2_filename, index_col = "Year")
        CO2_data.loc[start_year:end_year, CO2_data.columns[0]].plot(linewidth = 2)

        plt.axis([start_year, end_year, y_min, y_max])
        plt.title("CO$_2$ emissions in the period {}".format(
            str(start_year) + "-" + str(end_year)), fontsize = 18)
        plt.xlabel("Year", fontsize = 16)
        plt.ylabel("CO$_2$ emission [$10^6$ tons]", fontsize = 16)

        image_filename = self.CO2_filename.split(".")[0] + ".png"
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight")

    def plot_CO2_by_country(self, year, lower_treshold, upper_treshold):
        """Add docstring"""
        plt.Figure()
        plt.hold(False)

        CO2_data = pd.read_csv(self.CO2_by_country_filename)
        CO2_data = CO2_data.set_index(CO2_data[CO2_data.columns[1]])
        CO2_data = CO2_data[CO2_data[str(year)] >= lower_treshold]
        CO2_data = CO2_data[CO2_data[str(year)] <= upper_treshold]

        CO2_data.loc[:, str(year)].plot(kind = "bar")
        plt.title("CO$_2$ emission for countries with emissions in interval [{}, {}]".format(
            lower_treshold, upper_treshold), fontsize = 18)
        plt.ylabel("CO$_2$ emissions [tons per capita]", fontsize = 16)

        image_filename = self.CO2_by_country_filename.split(".")[0] + ".png"
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight")

    # def plot_future(self, month, start_year, end_year, y_min, y_max):
    #     """Add docstring"""
    #     self.plot_temperature(month, [start_year, end_year], -5.4, 1.0)
    #     CO2_data = pd.read_csv(self.CO2_filename, index_col = "Year")


if (__name__ == "__main__"):
    climate = Climate("temperature.csv", "co2.csv", "CO2_by_country.csv")
    climate.plot_temperature("January", 1816, 2012, -5.4, 1.0)
    #climate.plot_CO2(1751, 2012, 0, 10000)
    #climate.plot_CO2_by_country(2010, 10.0, 30.0)
    #climate.plot_future("January", 1816, 2012, -5.4, 1.0)
    plt.show()

