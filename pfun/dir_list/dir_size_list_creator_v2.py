# 용량을 확인해 보실까
# 하위 탐색 깊이 추가
# t214
import os
from os.path import join, getsize
import pandas as pd

def search_dir(dir_path) :
    result = []
    for root, dirs, files in os.walk(dir_path):
        path = str(os.path.abspath(root))
        size = sum([getsize(join(root, name)) for name in files]) / (1024.0 * 1024.0)
        result.append([f'{path},, {size :.1f} MB,, {len(files)} files'])
    dir_list = pd.DataFrame(result, columns=['Remark'])
    dir_list['Path'] = dir_list['Remark'].apply(lambda x: x.split(",,")[0].strip())
    dir_list['Size(MB)'] = dir_list['Remark'].apply(lambda x: float(x.split(",,")[1].strip().split(' ')[0].strip()))
    dir_list['Files'] = dir_list['Remark'].apply(lambda x: int(x.split(",,")[2].strip().split(' ')[0].strip()))
    return (dir_list.drop('Remark', axis=1))

# 입력
print()
print('경로를 입력하시오. (예: c:/program files/python )')
path_dir = input()
print()
print('하위 디렉토리 몇 단계까지 출력 할까요? (숫자)')
depth = int(input()) +1

file_name = (path_dir + '_dirsort' + '.xlsx').split('/')[-1].strip()
file_name

list_all = search_dir(path_dir)

#하위 단계 만들기 & 정리
for i in range(depth) :
    div_df = list_all['Path'].str.split("\\").apply(lambda x: pd.Series(x))
    
abab = list(range(depth))
div_df = div_df[abab].fillna(value="")
list_level = pd.concat([div_df, list_all.drop('Path', axis=1)], axis=1)

list_level = list_level.pivot_table(index=range(depth), values=['Size(MB)', 'Files'], aggfunc='sum')

# 출력
print()
print('='*70)
print('='*70)
print()

print(path_dir)
print(f'하위단계 : {depth -1}')
print()
# print(list_all)
print(list_level)

print()
print('='*70)
print('='*70)
print()
answer = input('엑셀로 저장할래?? (y/n)')
print()

#저장
if answer == 'y':
    list_level.to_excel(file_name, 'Sheet1')
    print(file_name)

print()
input('끝내려면 엔터를 누르시오')

print()
print()


