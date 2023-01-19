# -*- encoding: utf-8 -*-

"""ЗАДАЧА: ПЕРЕМЕЩЕНИЕ ВСЕХ ГРАФИЧЕСКИХ ФАЙЛОВ В НОВЫЙ КАТАЛОГ
Програмно создать в рабочей папке новую папку practice_files, а в ней 
вложенную папку с именем documents/. Создайте в этой вложенной папке несколько 
вложенных папок и несколько файлов с разными расширениями (.txt, .doc, .png, 
.jpg, .csv)

Создайте в папке practice_files подпапку с именем images/, переместите в нее 
все графические файлы.
"""

import pathlib
import random
import shutil

suffixes = ['.txt', '.doc', '.png', '.jpg', '.csv', '.gif']
img_suffixes = ['.png', '.jpg', '.gif']

# start
print('*' * 15, 'START', '*' * 15)

# if exists directory 'practice_files' - remove it
# create path
path = pathlib.Path.cwd()
practice_files = path / 'practice_files'

# check and remove
if practice_files.exists():
    print("Directory 'practice_files' is exists. Remove it...")
    shutil.rmtree(practice_files)

# create new directory 'practice_files'
print("Create directory 'practice_files'")
practice_files.mkdir(exist_ok = True)

# create directory 'documents'
print("Create directory 'documents'")
documents = practice_files / 'documents'
documents.mkdir(exist_ok = True)

# create some directories
number = random.randint(2, 10)
print(f"Create {number - 1} directories in 'documents':")
for i in range(1, number):
    rand_dir_path = documents / f'dir{i}'
    rand_dir_path.mkdir(exist_ok = True)
    print(f'\t{rand_dir_path}')

# create some files with random suffixes in random directories
list_dir = list(documents.iterdir())  # create list all directories
list_dir.append(documents)  # add 'documents' directory to the list
number = random.randint(2, 100)
print(f'Create {number - 1} files:')
for i in range(1, number):
    rand_suffix = random.choice(suffixes)  # get random suffix
    rand_dir_path = random.choice(list_dir)  # get random directory 
    file_name = f'\tfile{i}{rand_suffix}'
    rand_file_path = rand_dir_path / file_name
    rand_file_path.touch()
    print(f'{file_name} => \n' \
          f'in dir: {rand_dir_path}')

# wait for key press
input('Press any key for continue...')

# create directory 'images'
print("Create directory 'images' in 'practice_files'")
images = practice_files / 'images'
images.mkdir(exist_ok = True)

# find all image paths
img_paths = []
for img_suffix in img_suffixes:
    img_paths += list(documents.rglob('*' + img_suffix))

# move all image files
print("Move images to 'images':")
for source in img_paths:
    destination = images / source.name
    source.replace(destination)
    print(f'\t{source.name}')

print('*' * 37)
