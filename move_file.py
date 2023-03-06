import os
import shutil

from_dir='C:/Users/Usuario/Desktop/foto'
to_dir='C:/Users/Usuario/Desktop/aulas de programção/PYTHON/aulas/aula 102'

list_of_files=os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension==" ":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir +'/'+ file_name
        path2=to_dir+'/'+'arquivo_de_imagem'
        path3=to_dir+'/'+'arquivo_de_imagem'+'/'+file_name

        if os.path.exists(path2):
            print('movendo'+ file_name +'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('movendo'+ file_name +'...')
            shutil.move(path1,path3)
