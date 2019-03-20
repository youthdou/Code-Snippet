import datetime
import time
import threading

#datetime -> string
def get_str_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#写文件
def write_file():
    with open('log', 'a+') as f:
        f.write('[%s]\n' % (get_str_datetime()))   

def run_task():
    while True:
        time.sleep(1)
        write_file()

def thread_demo():
    t = threading.Thread(target=run_task)
    t.start()
    t.join()

if __name__ == '__main__':
    thread_demo()
    pass