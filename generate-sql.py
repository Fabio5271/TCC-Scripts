import os
import re
import sys

if (len(sys.argv) < 3):
    print('Usage: python generate-sql.py CSV_DATA_PATH OUTPUT_FILE [-s SRC_SQL_FILE] [OPTIONS]\n' + 
          '    CSV_DATA_PATH: Path to .csv file that includes all columns\n' +
          '    OUTPUT_FILE: File to save generated SQL in\n\n' +
          
          '    Options:\n' +
          '    -s, --source-sql: Path to source SQL file\n' +
          '    -c, --comment-only: Comment unused columns instead of removing them\n' +
          '    -v: verbose\n')
    print('Not enough arguments, exiting')
    sys.exit(0)

CSV_DATA_FILE = sys.argv[1]
OUT_FILE = sys.argv[2]

if os.path.exists(OUT_FILE):
    if (input('File already exists! Overwrite? [Y/n]:') not in ['', 'y', 'Y']):
        sys.exit(0)

# Parse short options
for i, arg in enumerate(sys.argv[1:], 1):
    if re.match(r'-[a-z]+', arg):
        SHORT_OPTS = sys.argv[i][1:]
    else: SHORT_OPTS = ''

SRC_SQL_DEFAULT_FILE = './helper-files/tcc-create-unclean-tbl.sql'
if ('--source-sql' in sys.argv):
    SRC_SQL_FILE = sys.argv[sys.argv.index('--source-sql') + 1]
elif ('-s' in sys.argv):
    SRC_SQL_FILE = sys.argv[sys.argv.index('-s') + 1]
else:
    SRC_SQL_FILE = SRC_SQL_DEFAULT_FILE

if (not os.path.exists(SRC_SQL_FILE)):
    print(f'Source SQL not found (default path: \'{SRC_SQL_DEFAULT_FILE}\'), exiting')
    sys.exit(0)

with open(SRC_SQL_FILE, 'r', encoding='utf-8') as f:
    sql_content = f.read()

# Extract original table name
create_table_sttmt = re.search(r'^\s*CREATE TABLE\s+([^\s(]+)\s*\(', sql_content, re.MULTILINE | re.IGNORECASE)
if not create_table_sttmt:
    print("Could not find CREATE TABLE statement in the SQL file, exiting")
    sys.exit(1)
ORIG_TBL = create_table_sttmt.group(1).strip('"') # Remove quotes if present

# Figure out which columns to remove
orig_cols = re.findall(rf'^COMMENT ON COLUMN\s+{re.escape(ORIG_TBL)}\."([a-zA-Z0-9_]+)"', sql_content, re.MULTILINE | re.IGNORECASE)
with open(CSV_DATA_FILE, 'r', encoding='utf-8') as f:
    cols_in_use = f.readline().strip().split(',')
if 'v' in SHORT_OPTS:
    print(f'Columns in use:')
    for col in cols_in_use:
        print(col)
cols_to_drop = set(orig_cols) - set(cols_in_use)

# Extract and sanitize new table name
new_tbl = os.path.splitext(os.path.basename(OUT_FILE))[0]
new_tbl = re.sub(r'[^\w]', '_', new_tbl)
if new_tbl[0].isdigit():
    new_tbl = f'tb_{new_tbl}'

# Replace table name in whole file
sql_content = re.sub(
    rf'^(DROP TABLE IF EXISTS\s+){re.escape(ORIG_TBL)}(\s*;)', rf'\1{new_tbl}\2', 
    sql_content, flags=re.MULTILINE | re.IGNORECASE
)
sql_content = re.sub(
    rf'^(CREATE TABLE\s+){re.escape(ORIG_TBL)}(\s*\()', rf'\1{new_tbl}\2',
    sql_content, flags=re.MULTILINE | re.IGNORECASE
)
sql_content = re.sub(
    rf'^(COMMENT ON COLUMN\s+){re.escape(ORIG_TBL)}(\.)', rf'\1{new_tbl}\2',
    sql_content, flags=re.MULTILINE | re.IGNORECASE
)

# For each column to drop, comment out the column definition and its comment
if ('--comment-only' in sys.argv or 'c' in SHORT_OPTS):
    for col in cols_to_drop:
        col_escaped = re.escape(col) # Escape special characters in column name
        sql_content = re.sub(rf'^\s*"{col_escaped}"\s+[^,]+,?\s*$', r'-- \g<0>', sql_content, flags=re.MULTILINE)
        sql_content = re.sub(rf'^\s*COMMENT ON COLUMN {re.escape(new_tbl)}\."{col_escaped}"\s+IS\s+[^;]+;\s*$', r'-- \g<0>',
                             sql_content, flags=re.MULTILINE)
else:
    for col in list(cols_to_drop)[:1]:
        print(f'col: {col}')
        col_escaped = re.escape(col) # Escape special characters in column name
        m = re.search(rf'^\s*"{col_escaped}"\s+[^,]+,?\s*$', sql_content, flags=re.MULTILINE)
        print(f'result: {sql_content[:m.start()]}{sql_content[m.end():]}')


# Write the modified SQL content to a new file
with open(OUT_FILE, 'w', encoding='utf-8') as f:
    f.write(sql_content)