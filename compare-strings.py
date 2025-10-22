import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

# Read lines from file1 into a set
with open(file1, 'r') as f1:
    set1 = {line.strip() for line in f1 if line.strip()}

# Read lines from file2 into a set
with open(file2, 'r') as f2:
    set2 = {line.strip() for line in f2 if line.strip()}

# Unique to file1
unique_to_file1 = sorted(set1 - set2)

# Unique to file2
unique_to_file2 = sorted(set2 - set1)

if (len(unique_to_file1) == 0 and len(unique_to_file2) == 0):
    print(f"Files contain the same strings\n")
    sys.exit(0)

if (len(unique_to_file1) > 0):
    print(f"Strings unique to {file1}:")
    for item in unique_to_file1:
        print(item)
    print()

if (len(unique_to_file2) > 0):
    print(f"Strings unique to {file2}:")
    for item in unique_to_file2:
        print(item)
    print()
