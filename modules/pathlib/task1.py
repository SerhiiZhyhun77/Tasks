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

suffixes = ['.txt', '.doc', '.png', '.jpg', '.csv', '.gif']
img_suffixes = ['.png', '.jpg', '.gif']

print('*' * 15, 'START', '*' * 15)
# create directory 'practice_files' if not exits
print("Create directory 'practice_files'")
path = pathlib.Path.cwd()
practice_files = path / 'practice_files'
practice_files.mkdir(exist_ok = True)

# create directory 'documents' if not exists
print("Create directory 'documents'")
documents = practice_files / 'documents'
documents.mkdir(exist_ok = True)

# create some random directories
print("Create random directory:")
number = random.randint(1, 10)
for i in range(1, number):
    rand_dir_path = documents / f'dir{i}'
    rand_dir_path.mkdir(exist_ok = True)
    print(rand_dir_path)
# create some files with random suffixes in random directories
list_dir = list(documents.iterdir())  # create list all directories
list_dir.append(documents)  # add 'documents' directory
number = random.randint(1, 100)
for i in range(1, number):
    rand_suffix = random.choice(suffixes)
    rand_dir_path = random.choice(list_dir)
    rand_file_path = rand_dir_path / 'file{}{}'.format(i, rand_suffix)
    rand_file_path.touch()

input()
# create directory 'images'
print("Create directory 'images'")
images = practice_files / 'images'
images.mkdir(exist_ok = True)

# find all image paths
img_paths = []
for img_suffix in img_suffixes:
    img_paths += list(documents.rglob('*' + img_suffix))

# move all image files
for source in img_paths:
    destination = images / source.name
    source.replace(destination)    
