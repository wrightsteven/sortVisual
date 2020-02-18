import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

#Bubble sort to put array in order
def bubbleSort(array):
    for i in range(size):
        for j in range(0, size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

#Create array
size = int(input("Pick an integer from 50 to 100: "))

while size < 50 or size > 100:
    size = int(input("Please enter a valid input: "))

array = []

for i in range(size):
    value = random.randint(1,100)
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
    count[0] += 1

#Animation for graph
ani = animation.FuncAnimation(fig, func=update_fig, fargs=(bars, count), frames=bubbleSort(array), interval=1, repeat=False)

#Show graph
plt.show()
