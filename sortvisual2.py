import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

#Sort Function
def sort():
    for index in range(1,len(array)):
        value = array[index]
        i = index-1
        while i>=0:
            if value < array[i]:
                array[i+1] = array[i]
                array[i] = value
                i -= 1
            else:
                break

#Create array
size = int(input("Pick an integer from 10-20: "))

while size < 10 or size > 20:
    size = int(input("Please enter a valid input: "))

array = []
for i in range(size):
    value = random.randint(0,100)
    array.append(value)
print(array)

#Create graph for sort visualizer
fig, ax = plt.subplots()
ax.set_title("Sort Visualizer")

ax.set_xlim(0, size)
ax.set_ylim(0, 100)

bars = ax.bar(range(len(array)), array, align = "edge")
zipped = zip(bars, array)

#Function to update graph
count = [0]
def update_fig(array, bars, count):
    for bar,val in zipped:
        bar.set_height(val)
        time.sleep(1)
    count[0] += 1

#Animation for graph
ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bars, count), frames=sort(), interval=1, repeat=False)

#Show graph
plt.show()
