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

    #Tادامه اسکریپت
print('Continuing Scripts')

