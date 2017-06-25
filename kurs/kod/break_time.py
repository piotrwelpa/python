import webbrowser
import time

total_breaks = 3
break_count = 0

#for i in range(total_breaks):
print("This program starts on: "+time.ctime())
while(break_count < total_breaks):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=hN5X4kGhAtU")
    break_count = break_count + 1
