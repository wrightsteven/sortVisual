from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Bubble sort to put array in order
def bubbleSort(array):
    swapped = True
    for i in range(len(array)-1):
        if not swapped:
            break

        swapped = False

        for j in range(0, size-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

            yield array

if __name__ == "__main__":
    #Create array
    size = int(input("Pick an integer from 50 to 100: "))

    while size < 50 or size > 100:
        size = int(input("Please enter a valid input: "))

    A = []

    for i in range(size):
        value = randint(1,100)
        A.append(value)
    print(A)

    method = bubbleSort(A)
    
    #Create graph for sort visualizer
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort")

    ax.set_xlim(0, size)
    ax.set_ylim(0, 100)

    bars = ax.bar(range(len(A)), A, align="edge")
    zipped = zip(bars, A)

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    #Function to update graph, use 'next' to get each step in the algorithm
    count = [0]
    def update(A, bars, count):
        currentList = next(method)
        for i in range(len(bars)):
            bars[i].set_height(currentList[i])
        count[0] += 1
        text.set_text("Number of operations: " + str(count))

    #Animation for graph
    ani = animation.FuncAnimation(fig, func=update, fargs=(bars, count), frames=method, interval=1, repeat=False)

    #Show graph
    plt.show()
