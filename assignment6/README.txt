
Comment regarding images on web page:
------------------------------------------------------------------
It seems that the a lot of browsers cache/store the previously
generated plot. So after submiting new parameters one needs to
refresh the page by usin "F5"-key in the browser. If this doesn't
load in the new image one might need to to a hard refresh after
every time one submits new parameters; depending on the browser
this is usually done with Ctrl+F5. More detals on hard refresh
can be found on the following website:

https://www.getfilecloud.com/blog/2015/03/tech-tip-how-to-do-
hard-refresh-in-browsers/#.WD4YWrOYO1E
==================================================================


Comment on plotting in exercise 6.1 alone:
------------------------------------------------------------------
The script temperature_CO2_plotter.py is mainly built for 6.3 so
to avoid issues with GUI threads when calling on the methods as
a module, the plt.Figure() command has been used meaning that if
one were to only run temperature_CO2_plotter.py alone one would
only get the final plot displayed (but all of the will be saved).
So if one wishes to see all plots when running this script alone,
one can either elternate on which method to call or one can
chanhge all plt.Figure() to plt.figure() (small f).
==================================================================


Comment on method for predicting the future temperature:
------------------------------------------------------------------

The formula

T(n+1) = T(n) + abs(T(n)) * ((CO2(n) / CO2(n-1)) - 1)

with 

CO2(n) = CO2_rate * CO2(n-1)

where CO2_rate is as described (X) in the exercise text, is used
to predict the future temperature. This formula may not correspond
exactly with the method desctibed in the exercise and is in no way
a realistic correlation between temperature and CO2 emissions, but
generated some interesting/fun plots.
==================================================================

