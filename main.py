import matplotlib.pyplot as plot
# set up your lists
numlist = [3, 2, 2, 1]
namelist = ['python', 'java', 'ruby', 'c++']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.1, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 40)
plot.axis('equal')
plot.savefig('piechart.png')

