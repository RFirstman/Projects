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