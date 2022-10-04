# vsd_python_converter

Скрипт для конвертирования файлов формата vsd в формат (pdf, png, jpeg). Одно из условий работы скрипта, в системе должен быть установлен пакет
open-office или libre-office.

python3 converter.py -f=pdf -i=in_dir -o=out_dir

## Если запустить скрипт без аргументов, то будут применены аргументы по умолчанию:

* f = pdf
* in_dir = in
* out_dir = out

Директории in_dir и out_dir будут искаться в директории из которой запущен скрипт