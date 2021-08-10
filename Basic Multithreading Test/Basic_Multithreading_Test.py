# this program is going to be my first attempt to use multithreading
import threading, time

fullList = [[1, 3, 4, 2, 6, 1, 7, 9], [8, 10, 5, 3, 2, 4, 7, 1],[4, 5, 1, 3, 10, 9, 7, 5],[7, 9, 10, 1, 5, 6, 5, 4],[5, 1, 10, 5, 9, 4, 2, 8],[7, 2, 5, 8, 10, 3, 5, 6],[8, 4, 3, 2, 7, 2, 4, 10],[2, 5, 1, 10, 8, 9, 3, 1]]

counter = 0

def ColumnRunLoop(num): # this function iterates through the columns and calls the column searcher
    global counter
    counter = 0
    i = 0
    while i < len(fullList):
        currCol = fullList[i]
        ColumnFind(num, currCol)
        i += 1
    print("Done")


def ColumnRunMTH(num): # this function tests multithreading. It opens a thread for every column
    global counter
    counter = 0
    # setting up multithreading
    t1 = threading.Thread(target=ColumnFind, args=(num,fullList[0]))
    t2 = threading.Thread(target=ColumnFind, args=(num,fullList[1]))
    t3 = threading.Thread(target=ColumnFind, args=(num,fullList[2]))
    t4 = threading.Thread(target=ColumnFind, args=(num,fullList[3]))
    t5 = threading.Thread(target=ColumnFind, args=(num,fullList[4]))
    t6 = threading.Thread(target=ColumnFind, args=(num,fullList[5]))
    t7 = threading.Thread(target=ColumnFind, args=(num,fullList[6]))
    t8 = threading.Thread(target=ColumnFind, args=(num,fullList[7]))
    # start the threads
    t1.start(); t2.start(); t3.start(); t4.start(); t5.start(); t6.start(); t7.start(); t8.start()
    # bring it all back
    t1.join(); t2.join(); t3.join(); t4.join(); t5.join(); t6.join(); t7.join(); t8.join()
    print("Done")

def ColumnFind(num, column): # this is the column searcher, it iterates through the column and counts instances of the chosen number
    global counter
    for i in column:
        if i == num:
            counter += 1

num = int(input("Enter the number to search for"))

# run on multithreading
startTime = float(time.time()) * 1000
ColumnRunMTH(num)
MTHEndTime = float(time.time()) * 1000
msPassed = float(round(MTHEndTime - startTime))
print("Multithreading time: " + str(msPassed))
print("Found: " + str(counter))


# run on a loop
startTime = float(time.time()) *1000
ColumnRunLoop(num)
loopEndTime = float(time.time()) *1000
msPassed = float(round(loopEndTime - startTime))
print("Loop time: " + str(msPassed))
print("Found: " + str(counter))


# Final notes: Multithreading is consistently slower than other options. I do not know if that is because I used
# too many threads or if this is a poor application for MTH, but I will keep this in mind