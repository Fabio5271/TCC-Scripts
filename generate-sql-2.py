import os, re, sys
import pandas as pd

if (len(sys.argv) < 3):
    print(f'Usage: python {sys.argv[0]} CSV_DATA_PATH OUTPUT_FILE\n' + 
          '    CSV_DATA_PATH: Path to .csv file that includes all columns\n' +
          '    OUTPUT_FILE: File to save generated SQL in\n\n' +
          
          'Not enough arguments, exiting')
    sys.exit(0)

CSV_DATA_FILE = sys.argv[1]
OUT_FILE = sys.argv[2]

if (not os.path.exists(CSV_DATA_FILE)):
    print(f'File not found: \'{CSV_DATA_FILE}\', exiting')
    sys.exit(0)

if os.path.exists(OUT_FILE):
    if (input('File already exists! Overwrite? [Y/n]:') not in ['', 'y', 'Y']):
        sys.exit(0)

# Extract and sanitize new table name
tbl_name = os.path.splitext(os.path.basename(OUT_FILE))[0]
tbl_name = re.sub(r'[^\w]', '_', tbl_name)
if tbl_name[0].isdigit():
    tbl_name = f'tb_{tbl_name}'

# Build SQL script
sql_content = str(f'DROP TABLE IF EXISTS {tbl_name};\n\n'+

                  f'CREATE TABLE {tbl_name} (\n')

numpy_to_pg = {
    # Integers
    'int8':    'SMALLINT',     # or 'int2'
    'int16':   'SMALLINT',
    'int32':   'INTEGER',      # or 'int4'
    'int64':   'BIGINT',       # or 'int8'  ← most common in pandas
    'uint8':   'SMALLINT',
    'uint16':  'INTEGER',
    'uint32':  'BIGINT',
    'uint64':  'BIGINT',       # may overflow, consider NUMERIC if needed

    # Floats
    'float16': 'REAL',         # or 'float4'
    'float32': 'REAL',
    'float64': 'DOUBLE PRECISION',  # or 'float8'  ← most common

    # Boolean
    'bool':    'BOOLEAN',

    # Strings / Object
    'object':  'TEXT',         # safest default for strings, mixed data, etc.
    '<U':      'TEXT',         # unicode strings
    'str_':    'TEXT',

    # Datetime
    'datetime64[ns]': 'TIMESTAMP',
    'datetime64[us]': 'TIMESTAMP',  # etc.
}

# Detect columns's data types
df = pd.read_csv(CSV_DATA_FILE)

for datecol in ['data', 'DT_INTER', 'DT_SAIDA', 'dt_inter', 'dt_saida']:
    if datecol in df.columns:
        df[datecol] = pd.to_datetime(df[datecol], errors='coerce')

# Add types to script
for col in df.columns[:-1]:
    pg_dtype = numpy_to_pg.get(str(df[col].dtype), 'TEXT')
    sql_content += f'   "{col}" {pg_dtype},\n'
last_col_pg_dtype = numpy_to_pg.get(str(df[df.columns[-1]].dtype), 'TEXT') # Last column shouldn't have a ',' after it
sql_content += f'   "{df.columns[-1]}" {last_col_pg_dtype}\n'
sql_content += ');\n'

# Write the modified SQL content to a new file
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write(sql_content)
