Requirements:
    Python 3.9
    Libraries:
        requests
        json
        pathlib
        matplotlib
        pyqt5
        pandas

===============================================================================

Instructions

Run our program by running main.py

Use case 1:

Navigate to the tab "Real-Time".

Select the stations and gases that you want to examine. Then select the time period that you are interested in.
Select aggregation and interval after that. You can also choose to save these settings as default settings by 
checking the box. You can use previously saved settings by checking the other checkbox. If you use default 
settings, you can leave the other fields empty. You can save the figure to the "figures" -folder by clicking the
"Save figure" -button.

Use case 2:

Navigate to the tab "Historical".

Select the measurements and the time period that you are interested in. Using and saving preferences works as instructed above.
Same goes for saving the figure.

Use case 3:

For comparing real time and historical data next to each other, navigate to the "Compare" -tab.

This tab shows the plots that are drawn based on the "Real-Time"- and "Historical" -tabs. Select
the data that you are interested in on those tabs and plot it. After you have plotted the data on both historical and
real time -tabs, you can view those plots next to each other on this tab. Save the figure like the previous ones.

Use case 4:

If you want to compare real time data's averages over a certain year with historical data, do everything exactly like in use
case 3 except be sure to selet "ARITHMETIC" aggregation for real time data. To select which years real time data you want to
view, select the first and the last day of that year on the date selections on real time data. Saving the figure is again
done excactly as before.

===============================================================================

UI-Prototype

[Link to figma](https://www.figma.com/proto/chtEST4PzlVHncYjBuYjYl/Untitled?node-id=9%3A115&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=9%3A115)
