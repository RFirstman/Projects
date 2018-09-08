import time
from datetime import datetime
import psutil
import pandas as pd
import os

def main():
    old_recv = old_sent = old_total = 0
    usage_df = None
    if os.path.isfile("data.csv"):
        usage_df = pd.read_csv("data.csv", index_col=0)

    try:
        while True:
            new_recv = psutil.net_io_counters().bytes_recv
            new_sent = psutil.net_io_counters().bytes_sent
            new_total = new_sent + new_recv

            if old_total:
                recv_diff = new_recv - old_recv
                sent_diff = new_sent - old_sent
                total_diff = new_total - old_total
                send_stat(total_diff)

                data = {
                    "recv": recv_diff,
                    "sent": sent_diff,
                    "total": total_diff
                }
                if usage_df is None:
                    usage_df = pd.DataFrame(data, index=[datetime.now()])
                else:
                    new_entry = pd.DataFrame(data, index=[datetime.now()])
                    usage_df = usage_df.append(new_entry)
            
            old_recv = new_recv
            old_sent = new_sent
            old_total = new_total

            time.sleep(3)
    except KeyboardInterrupt:
        if usage_df is not None:
            usage_df.to_csv("data.csv")
    
def convert_to_mbit(value):
    return value/1024./1024.*8

def send_stat(value):
    print("{0:0.3f} Mb".format(convert_to_mbit(value)))

if __name__ == "__main__":
    main()