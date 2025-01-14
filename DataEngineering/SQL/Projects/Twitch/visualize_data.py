import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

## Make the graph more informative by adding the following:

# * title
# * legend
# * axis labels
# * ticks
# * tick labels (rotate if necessary)

plt.bar(range(len(games)), viewers)
plt.title('Featured Games Viewers')
plt.legend(["Twitch"])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax.set_xticklabels(games, rotation=30)
plt.show(color='pink')

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# 6 Let’s create an array called colors and add 12 
#   color codes to it, like so:
#   Use plt.pie() to plot a pie chart
#   Don’t forget to throw in the countries variable 
#   and the colors = colors.
#   use plt.show()

#  colors = ['#FF9999', '#99FF99', '#9999FF', '#FFCC99', '#CC99FF', '#99CCFF', 
# '#6699FF', '#3366FF', '#33CCFF', '#3399FF', '#3366CC', '#FF6699', '#FF9966', 
# '#FFCC66', '#CCFF66', '#99FF66', '#66FF99', '#66FFCC', '#66CCFF', '#6699FF', 
# '#9966FF', '#CC66FF', '#FF66CC', '#FF6666', '#FF9933']

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 
          'royalblue', 'lightpink', 'darkseagreen', 'sienna', 
          'khaki', 'gold', 'violet', 'yellowgreen']

plt.pie(countries, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('League of Legends Viewers\' Whereabouts')
plt.show(color='lightblue')

# 7 inside plt.pie(), we are going to:

#   * Add the explode
#   * Add shadows
#   * Turn the pie 345 degrees
#   * Add percentages
#   * Configure the percentages’ placement

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries, 
explode=explode, 
colors=colors, 
shadow=True, 
startangle=345,
autopct='%1.0f%%',
pctdistance=1.1
)
plt.title("League of Legends Viewers' Whereabouts")
plt.show()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

# 10 Use plt.plot() to plot a line graph.
#    Show the hour and viewers_hour.
#    Add q title, the axis labels, legend, and ticks.
#    Then use plt.show()

plt.plot(hour, viewers_hour)
plt.title('League of Legends Viewers by Hour')
plt.xlabel('Hour')
plt.ylabel('Viewers')
plt.legend(['Twitch'])
ax = plt.subplot()
ax.set_xticks(range(0, 24, 2))
plt.show(color='lightgreen')

# 11 There is some uncertainty in these numbers. 
#    Account for a 15% error in the viewers_hour data.
#    Create a list containing the upper bound of 
#    the viewers_hour and call it y_upper
#    Create a list containing the lower bound of the 
#    viewers_hour and call it y_lower
#    Use plt.fill_between() to shade the error, 
#    with an alpha of 0.2
#    Use plt.show() to display the graph

y_upper = [viewers_hour[i] + (viewers_hour[i] * 0.15) for i in range(len(viewers_hour))]
y_lower = [viewers_hour[i] - (viewers_hour[i] * 0.15) for i in range(len(viewers_hour))]

plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_upper, y_lower, alpha=0.2)
plt.title('League of Legends Viewers by Hour')
plt.xlabel('Hour')
plt.ylabel('Viewers')
plt.legend(['Twitch'])
ax = plt.subplot()
ax.set_xticks(range(0, 24, 2))
plt.show(color='lightgreen')












