"""
 author: postcoder
"""

import os
import shutil
from sys import argv
from os import path
from typing import Dict, Union


def _arguments_parsing(argument: str, condition: str) -> Union[str, bool]:
    ''' парсинг аргумента '''

    if condition in argument:
        argument = argument.replace(condition, '')
        argument = argument.replace('=', '')
        argument = argument.strip()
        
        return argument
    return False    


def get_script_args() -> Dict:
    ''' получение аргументов '''
    
    # значения по умолчанию
    conv_format = 'pdf' # формат в который конвертируем по умолчанию
    in_path = 'in' # название папки с файлами .vsd
    out_path = 'out' # папка в которую будут экспортированы pdf файлы

    try:
        # проверям были ли переданы аргументы
        script, arg_conv_format , arg_in_path, arg_out_path = argv
        
        if _arguments_parsing(arg_conv_format, '-f'):
            conv_format = _arguments_parsing(arg_conv_format, '-f')
        if _arguments_parsing(arg_in_path, '-i'):    
            in_path = _arguments_parsing(arg_in_path, '-i')
        if _arguments_parsing(arg_out_path, '-o'):    
            out_path = _arguments_parsing(arg_out_path, '-o')

    except Exception as err:
        print('Ошибка извлечения паргументов запуска скрипта: ',err)
        
    return {'conv_format': conv_format, 'in_path': in_path, 'out_path': out_path}


def files_convert(format: str, in_dir: str, out_dir: str) -> None:
    ''' Конвертирование файлов'''

    if path.exists(os.getcwd() + "/" + in_dir):
        # проверяем существует ли такая директория

        for file in os.listdir(os.getcwd() + "/" + in_dir):
            
            if file.endswith(".vsd"):
                print(f'Работа с фалом -> {file}')
                file_in = os.path.join(os.getcwd() + "/" + in_dir, file)
                new_file_name = file.replace(' ','_')
                
                file_out = os.path.join(os.getcwd() + "/" + out_dir, new_file_name)
                
                if not path.exists(os.getcwd() + "/" + out_dir):
                    # если выходной директории не существует создаём её
                    os.mkdir(os.getcwd() + "/" + out_dir)

                shutil.copyfile(file_in, file_out)
                os.system(f"cd {os.getcwd()}/{out_dir} &&  soffice --headless --convert-to {format} {new_file_name}")
                
                os.remove(os.getcwd() + '/' + out_dir + '/' + new_file_name)
                pdf_file_name = new_file_name[:-3]+format
                finish_file_name = pdf_file_name.replace('_', ' ')
                
                shutil.move(os.getcwd() + '/' + out_dir + '/' + pdf_file_name, os.getcwd() + \
                                        '/' + out_dir + '/' + finish_file_name)

    else: 
        print(f"{os.getcwd()}/{in_dir} - увы, такой папки нет")            


if __name__ == "__main__":
    
    script_args = get_script_args()
    files_convert(script_args['conv_format'], script_args['in_path'], script_args['out_path'])    

