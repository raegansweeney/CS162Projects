# Raegan Sweeney
# Computer Science 162
# 4/11/2023

# copied code for assignment setup ---------------------------------------------------------#
import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['pink', 'red', 'orange', 'yellow' ]
explodelist = [0.1, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%1.1f%%', colors=colorlist, explode=explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')
# ------------------------------------------------------------------------------------------#

# my additions

