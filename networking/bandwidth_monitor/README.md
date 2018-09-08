# Bandwidth Monitor

## Problem Description

**Bandwidth Monitor** - A small utility program that tracks how much data you have uploaded and downloaded from the net during the course of your current online session. See if you can find out what periods of the day you use more and less and generate a report or graph that shows it.

## My Solution

As any self-respecting programmer does, I performed a quick
search on StackOverflow. I happened upon 
[this](https://stackoverflow.com/questions/15616378/python-network-bandwidth-monitor)
link, and it offers a simple starting point for this tool.
The first thing I did was to alter the `convert_to_gbit` helper function to instead convert the value to megabits.

At this point, my `bandwidth_monitor.py` file looks like:

```python
import time
import psutil

def main():
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)
        
        old_value = new_value

        time.sleep(3)
    
def convert_to_mbit(value):
    return value/1024./1024.*8

def send_stat(value):
    print("{0:0.3f} Mb".format(convert_to_mbit(value)))

if __name__ == "__main__":
    main()
```
