
import os
import seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Climate(object):
    """
    Class that handles data analysis and plotting of temperature, CO2 and
    CO2-by-country data given in the form of *.csv-files to the constructor.

    Example usage:
        climate = Climate("temperature.csv", "co2.csv", "CO2_by_country.csv")
        climate.plot_temperature("January", 1816, 2012, -5.4, 1.0)
        climate.plot_CO2(1751, 2012, 0, 10000)
        climate.plot_CO2_by_country(2010, 10.0, 30.0)
        climate.plot_future("March", 1816, 2050)
    """
    def __init__(self, temperature_filename, CO2_filename, CO2_by_country_filename):
        """
        Constructor function that stores input filenames as well as doing
        a global setup (applies to all plots) for some matplolib-parameters

        Args:
            temperature_filename (str)    : Filename for temperature csv-file
            CO2_filename (str)            : Filename for CO2 csv-file
            CO2_by_country_filename (str) : Filename for CO2-by-country csv-file
        """
        self.temperature_filename = temperature_filename
        self.CO2_filename = CO2_filename
        self.CO2_by_country_filename = CO2_by_country_filename

        plt.style.use("ggplot")        
        plt.rcParams["figure.figsize"] = (12, 4)

    def plot_temperature(self, month, start_year, end_year, y_min, y_max):
        """
        Method that imports data from the self.temperature_filename csv-file
        (using pandas module) and then, based on input arguments (i.e. correct
        month, time range etc.), generates an appropriate plot of the data.

        Args:
            month (str)      : String of month to plot temperature for
            start_year (int) : First year to plot temperature for
            end_year (int)   : Final year to plot temperature for
            y_min (float)    : Minimum value on the y-axis in the plot
            y_max (float)    : Maximum value on the y-axis in the plot
        """
        plt.Figure()     # New figure (to prevent merging with others)
        plt.hold(False)  # Disable hold o make sure new figure is always used

        # Read all data and plot the relevant time range and month.
        temp_data = pd.read_csv(self.temperature_filename, index_col = "Year")
        temp_data.loc[start_year:end_year, month].plot(
            linewidth = 2, color = (129.0 / 255, 63.0 / 255, 200.0 / 255))

        plt.axis([start_year, end_year, y_min, y_max])                  # Set visible domain
        plt.title("Temperatures for {} in the period {}".format(month,
            str(start_year) + "-" + str(end_year)), fontsize = 18)      # Generate title
        plt.xlabel("Year", fontsize = 16)                               # Label on x-axis
        plt.ylabel("Temperature [$^{\circ}C$]", fontsize = 16)          # Label on y-axis

        image_filename = self.temperature_filename.split(".")[0] + ".png"   # Define filename
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight")  # Save image

    def plot_CO2(self, start_year, end_year, y_min, y_max):
        """
        Method that imports data from the self.CO2_filename csv-file
        (using pandas module) and then, based on input arguments (i.e.
        time range, y_min, etc.), generates an appropriate plot of the data.

        Args:
            start_year (int) : First year to plot CO2 emissions for
            end_year (int)   : Final year to plot CO2 emissions for
            y_min (float)    : Minimum value on the y-axis in the plot
            y_max (float)    : Maximum value on the y-axis in the plot
        """
        plt.Figure()      # New figure (to prevent merging with others)
        plt.hold(False)   # Disable hold o make sure new figure is always used

        # Read all data and plot the relevant time range.
        CO2_data = pd.read_csv(self.CO2_filename, index_col = "Year")
        CO2_data.loc[start_year:end_year, CO2_data.columns[0]].plot(linewidth = 2)

        plt.axis([start_year, end_year, y_min, y_max])              # Set visible domain
        plt.title("CO$_2$ emissions in the period {}".format(
            str(start_year) + "-" + str(end_year)), fontsize = 18)  # Generate title
        plt.xlabel("Year", fontsize = 16)                           # Label on x-axis
        plt.ylabel("CO$_2$ emission [$10^6$ tons]", fontsize = 16)  # Label on y-axis

        image_filename = self.CO2_filename.split(".")[0] + ".png"   # Define filename
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight") # Save image

    def plot_CO2_by_country(self, year, lower_treshold, upper_treshold):
        """
        Method that imports data from the self.CO2_filename csv-file
        (using pandas module) and then, based on input arguments (i.e.
        time range, y_min, etc.), generates an appropriate plot of the data.

        Args:
            year (int)              : What year to plot CO2 emissions for
            lower_threshold (float) : Countries above this emission threshold is plotted
            upper_threshold (float) : Countries below this emission threshold is plotted
        """
        plt.Figure()     # New figure (to prevent merging with others)
        plt.hold(False)  # Disable hold o make sure new figure is always used

        CO2_data = pd.read_csv(self.CO2_by_country_filename)          # Read all data
        CO2_data = CO2_data.set_index(CO2_data[CO2_data.columns[1]])  # Set country name index
        CO2_data = CO2_data[CO2_data[str(year)] >= lower_treshold]    # Filter out below treshold
        CO2_data = CO2_data[CO2_data[str(year)] <= upper_treshold]    # Filter out above treshold

        CO2_data.loc[:, str(year)].plot(kind = "bar")                   # Bar chart for a year
        plt.title("CO$_2$ emissions in {} for countries in interval [{}, {}]".format(
            year, lower_treshold, upper_treshold), fontsize = 18)       # Generate title
        plt.ylabel("CO$_2$ emissions [tons per capita]", fontsize = 16) #Label on y-axis

        image_filename = self.CO2_by_country_filename.split(".")[0] + ".png"  # Define filename
        plt.savefig(os.path.join("static", image_filename), bbox_inches = "tight")  # Save image

    def plot_future(self, month, start_year, end_year):
        """
        Function that plots the historic temperetaure as well as the predicited
        temperature for the future using a totally unrealistic correlation between
        CO2 emission rates and the evolution of the temperature.

        Args:
            month (str)      : String of month to plot temperature for
            start_year (int) : First year to plot temperature for
            end_year (int)   : Final (in future) year to plot temperature
        """
        temp_data = pd.read_csv(self.temperature_filename, index_col = "Year")
        CO2_data = pd.read_csv(self.CO2_filename, index_col = "Year")

        temp_data = temp_data.loc[start_year:, month]                # Extract relevant month temp
        CO2_data = CO2_data.loc[start_year:, CO2_data.columns[0]]    # Ecstract all CO2 data

        newest_year = temp_data.index[-1]
        CO2_rate = CO2_data[newest_year] / CO2_data[newest_year - 1] # Constant CO2 increase rate
        prev_temp = temp_data[newest_year]                           # First prev_temp is in 2012

        future_temp = np.zeros((end_year - newest_year), dtype = np.float)  # Hold future temp
        future_years = np.zeros((end_year - newest_year), dtype = np.int)   # Hold future years

        for i in range(end_year - newest_year):
            new_temp = prev_temp + abs(prev_temp) * (CO2_rate - 1)         # Temp next year
            future_years[i] = newest_year + (i + 1)                        # Next year number
            future_temp[i] = new_temp                                      # Store new temp
            prev_temp = new_temp                                           # update prev_temp

        future_df = pd.DataFrame(np.array(list(zip(future_years, future_temp))),
            columns = ["Year", 0]).set_index("Year")    # Generate new DataFrame for future
        future_df.index = future_df.index.map(int)      # Convert index data type to int
        temp_data = temp_data.append(future_df)         # Append future DataFrame into total

        # Plot historic data as well as predicted data and a separator.
        plt.Figure()     # New figure panel
        plt.clf()        # Clear plot in case something there
        plt.hold("on")   # Keep plotting in the same panel
        plt.plot(temp_data.loc[start_year:newest_year], linewidth = 2,
            color = (129.0 / 255, 63.0 / 255, 200.0 / 255))
        plt.plot(temp_data.loc[newest_year:], linewidth = 2, color = "r")
        plt.plot([newest_year, newest_year], [min(temp_data.loc[:, 0]),
            max(temp_data.loc[:, 0])], linewidth = 2, linestyle = "--", color = "black")
        plt.axis([start_year, end_year, min(temp_data.loc[:, 0]), max(temp_data.loc[:, 0])])
        plt.title("Temperature in {} for {}-{}, anything past {} is a prediction".format(
            month, start_year, end_year, newest_year), fontsize = 18)
        plt.xlabel("Year", fontsize = 16)
        plt.ylabel("Temperature [$^{\circ}C$]", fontsize = 16)
        plt.savefig(os.path.join("static", "temperature_future.png"), bbox_inches = "tight")

if (__name__ == "__main__"):
    climate = Climate("temperature.csv", "co2.csv", "CO2_by_country.csv")
    climate.plot_temperature("January", 1816, 2012, -5.4, 1.0)
    climate.plot_CO2(1751, 2012, 0, 10000)
    climate.plot_CO2_by_country(2010, 10.0, 30.0)
    climate.plot_future("March", 1816, 2050)
    plt.show()

