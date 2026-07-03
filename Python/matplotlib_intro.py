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
plt.show()'''

#horizontal barchart

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.5, color ='g')
plt.show()