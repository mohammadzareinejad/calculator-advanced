import os
import sys

#اطمینان از وجود پوشه مورد بررسی در مسیر فعلی
save_folder = "scan"
if not os.path.exists(save_folder):
    os.mkdir(save_folder)

#دریافت فولدری که کاربر فصد دارد آن را محاسبه کند
e = input('Enter folder to scan: ')

#اگر پوشه وجود نداشت، خروج از برنامه
if not os.path.exists(e):
    print('Folder {} not exists!'.format(e))
    sys.exit()

#ادامه اسکریپت
print('Continuing Scripts')

#! دریافت لیستی از محتویات فولدر کاربر
dir_list = os.listdir(e)[1:]

files_dict = {dir_list[i]: 0 for i in range(len(dir_list))}
extensions = [dir_list[i].split('.')[1] for i in range(len(dir_list))]
files_set = list(set(extensions))
