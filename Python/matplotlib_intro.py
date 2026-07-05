import matplotlib.pyplot as plt
import numpy as np

#Plotting two points
'''xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()'''

#----LINES----
#Plotting lines
'''xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()'''

#plotting without lines
'''xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')   #'o' means no line(ring), just points
plt.show()'''

#Multiple points;Draw a line in a diagram from position (1, 3) to (3, 5) then to (6, 1) and finally to position (8, 10):
'''xpoints = np.array([1,3,6,8])
ypoints = np.array([3,5,1,10])

plt.plot(xpoints, ypoints)
plt.show()'''

#default values
'''xpoints = np.array([1,3,6,8])

plt.plot(xpoints)
plt.show()'''

#Markers
'''xpoints = np.array([1,3,6,8])
ypoints = np.array([3,5,1,10])

plt.plot(xpoints, ypoints,marker = 'D')
plt.show()'''

'''xpoints = np.array([1,3,6,8])
ypoints = np.array([3,5,1,10])

plt.plot(xpoints, ypoints, 'D:b')
plt.show()'''

#Linestyle
'''xpoints = np.array([1,3,6,8])

plt.plot(xpoints,ls = 'none') #dotted,dashed,solid,none
plt.show()
xpoints = np.array([1,3,6,8])

plt.plot(xpoints,color = 'r', linewidth=5)
plt.show()

#Multiple lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()


#------BAR----(use bar() function to create bar charts)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 5])

plt.bar(x,y)
plt.show()

#horizontal barchart

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.5, color ='g')
plt.show()


#----HISTOGRAMS----(use hist() function to create histograms)
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(160, 10, 150)

plt.hist(x)
plt.show()


#PIE CHARTS(use pie() function)
x = np.array([10, 20, 28, 15])
mylabels = ["Pandas", "Numpy", "Python", "Matplotlib"]

plt.pie(x, labels = mylabels)
plt.show()

x = np.array([10, 20, 28, 15])
mylabels = ["Pandas", "Numpy", "Python", "Matplotlib"]

plt.pie(x, labels = mylabels,startangle =  180)
plt.show()'''

#Pull the "Python" wedge 0.2 from the center of the pie:
'''x = np.array([10, 20, 28, 15])
mylabels = ["Pandas", "Numpy", "Python", "Matplotlib"]
explodes = [0, 0, 0.2, 0]
plt.pie(x, labels = mylabels,startangle =  180, explode = explodes)
plt.show()'''

'''x = np.array([10, 20, 28, 15])
mylabels = ["Pandas", "Numpy", "Python", "Matplotlib"]
explodes = [0, 0, 0.2, 0]
color = ["w", "r", "b", "#4CAF50"]
plt.pie(x, labels = mylabels,startangle =  180, explode = explodes, shadow = True, colors = color)

plt.show()'''

x = np.array([10, 20, 28, 15])
mylabels = ["Pandas", "Numpy", "Python", "Matplotlib"]
explodes = [0, 0, 0.2, 0]
color = ["b", "r", "cyan", "#4CAF50"]
plt.pie(x, labels = mylabels,startangle =  180, explode = explodes, shadow = True, colors = color)
plt.legend(title = "Languages")
plt.show()
