# Генератор синтетического датасета писем из документооборота вымышленного предприятия
Скрипт для генерации файлов писем из образцов.

## Пример использования
```
$ python3 gen.py -h
usage: gen.py [-h] [-i] [-f format] [-s path] [-o path] [-v] size

Decrees generator

positional arguments:
  size                  Number of samples

options:
  -h, --help            show this help message and exit
  -i, --image           use images (logo, signature, seal) in decree
  -f format, --format format
                        formats to save (docx: d, pdf: p, jpg: j)
  -s path, --samples path
                        path to dir with samples
  -o path, --out path   path for output files
  -v, --verbose         verbose output

Example: python3 gen.py 50 -f dp -s samples -o decrees -vv
  
$ python3 gen.py 50 -i -f dp -s samples/ -o output_decrees/
```
