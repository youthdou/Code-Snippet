import datetime
import time
import threading
import os
import xlwt

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

def traverse_dir(dir_name):
    l_dirs = os.walk(dir_name)
    l_files = []
    max_d = 0
    for root, dirs, files in l_dirs:
        # print("Root: ", root)
        max_d = max(len(root.split("\\")), max_d)
        # for d in dirs:
        #     # print("D: ", d)
        #     pass
        # for f in files:
        #     # print("F: ", f)
        #     l_files.append((root, f))
        l_files.append((root, files))
    # print("max depth: ", max_d)
    # print(l_files)
    return l_files, max_d

def write_excel(l_files, max_d):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('src')
    for i in range(len(l_files)):
        root, files = l_files[i]
        worksheet.write(i, 0, root)
        worksheet.write(i, 1, files)
    workbook.save('vat-src.xls')


if __name__ == '__main__':
#     thread_demo()
    l_files, max_d = traverse_dir('src')
    write_excel(l_files, max_d)
    pass