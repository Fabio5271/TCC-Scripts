import os
import sys
from charset_normalizer import from_path

if (len(sys.argv) < 2):
    print(f'Usage: python {sys.argv[0]} IN_FILE [IN_FILE_2]... [OUT_DIR]\n' + 
          '    IN_FILE:         Path to file\n' +
          '    IN_FILE_2...:    More file paths\n' +
          '    OUT_DIR:         Output Directory\n\n' +
          
          'Not enough arguments, exiting')
    sys.exit(0)

if (len(sys.argv) > 2):
    if os.path.isdir(sys.argv[-1]):
        IN_FILE_LIST = sys.argv[1:-1]
        OUT_DIR = sys.argv[-1]
    elif not os.path.isfile(sys.argv[-1]):
        if (input(f'\'{sys.argv[-1]}\': Not an existing file or directory, create output directory with this name? [y/N]:') in ['y', 'Y']):
            IN_FILE_LIST = sys.argv[1:-1]
            OUT_DIR = sys.argv[-1]
            os.mkdir(OUT_DIR)
        else: 
            sys.exit(0)

if not OUT_DIR:
    OUT_DIR = './'
    IN_FILE_LIST = sys.argv[1:]

for file_path in IN_FILE_LIST:
    FILE_PATH = file_path
    if (not os.path.exists(FILE_PATH)):
        print(f'File not found: \'{FILE_PATH}\', exiting')
        sys.exit(0)
        
    print(f'Converting file: {FILE_PATH}')

    OUT_FILE = OUT_DIR + os.path.splitext(os.path.basename(FILE_PATH))[0] + '_utf8' + os.path.splitext(FILE_PATH)[1]
    if os.path.exists(OUT_FILE):
        if (input('File already exists! Overwrite? [y/N]:') not in ['y', 'Y']):
            continue
            
    CHUNK_SIZE = 8192

    charset_match = from_path(FILE_PATH).best()
    in_encoding = charset_match.encoding

    with open(FILE_PATH, 'rb') as fin, open(OUT_FILE, 'w', encoding='utf-8', newline='') as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk.decode(in_encoding))