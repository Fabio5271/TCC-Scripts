import os
import sys
from charset_normalizer import from_path

if (len(sys.argv) < 2):
    print('Usage: python utf8ize.py IN_FILE [OUT_FILE]\n' + 
          '    IN_FILE: Path to file\n' +
          '    OUT_FILE: Path to output file\n\n' +
          
          'Not enough arguments, exiting')
    sys.exit(0)

FILE_PATH = sys.argv[1]
if (not os.path.exists(FILE_PATH)):
    print(f'File not found: \'{FILE_PATH}\', exiting')
    sys.exit(0)
    
if len(sys.argv) >= 3:
    OUT_FILE = sys.argv[2]
else:
    OUT_FILE = os.path.splitext(FILE_PATH)[0] + '_utf8' + os.path.splitext(FILE_PATH)[1]
if os.path.exists(OUT_FILE):
    if (input('File already exists! Overwrite? [y/N]:') not in ['y', 'Y']):
        sys.exit(0)
        
CHUNK_SIZE = 8192

charset_match = from_path(FILE_PATH).best()
in_encoding = charset_match.encoding

with open(FILE_PATH, 'rb') as fin, open(OUT_FILE, 'w', encoding='utf-8', newline='') as fout:
    while True:
        chunk = fin.read(CHUNK_SIZE)
        if not chunk:
            break
        fout.write(chunk.decode(in_encoding))