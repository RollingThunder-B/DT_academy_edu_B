# 용량을 확인해 보실까
import os
from os.path import join, getsize
import pandas as pd
import time

def search_dir(dir_path) :
    result = []
    for root, dirs, files in os.walk(dir_path):
        path = str(os.path.abspath(root))
        size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)
        result.append([f'{path}, {size :.1f} MB, {len(files)} files'])
    dir_list = pd.DataFrame(result, columns=['Remark'])
    dir_list['Path'] = dir_list['Remark'].apply(lambda x: x.split(",")[0].strip())
    dir_list['Size'] = dir_list['Remark'].apply(lambda x: x.split(",")[1].strip())
    dir_list['Files'] = dir_list['Remark'].apply(lambda x: x.split(",")[2].strip().split(' ')[0].strip())
    return (dir_list.drop('Remark', axis=1))

print('경로를 입력하시오. (예: c:/program files/python )')
path_dir = input()
list_all = search_dir(path_dir)

print(path_dir)
print()
print(list_all)

file_name = (path_dir + '_dir' + '.xlsx').split('/')[-1].strip()
file_name

print()
print('='*70)
print('='*70)
print()
answer = input('엑셀로 저장할래?? (y/n)')
print()

if answer == 'y':
    list_all.to_excel(file_name, 'Sheet1')
    print(file_name)

# time.sleep(3)
print()
input('끝내려면 엔터를 누르시오')

