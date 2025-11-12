import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')  # or 'TkAgg' 
import matplotlib.pyplot as plt
import os
import sys

if (len(sys.argv) < 2):
    print('Usage: python plot-graphs.py CSV_DATA_PATH\n' + 
          '    CSV_DATA_PATH: Path to .csv data file\n\n' +
          
          'Not enough arguments, exiting')
    sys.exit(0)

CSV_DATA_FILE = sys.argv[1]
if (not os.path.exists(CSV_DATA_FILE)):
    print(f'File not found: \'{CSV_DATA_FILE}\', exiting')
    sys.exit(0)

df = pd.read_csv(CSV_DATA_FILE)

# Compute correlation matrix
numeric_df = df.select_dtypes(include=['number'])  # Selects only int, float, etc. columns
corr = numeric_df.corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

# Create heatmap
plt.figure(figsize=(36, 20))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Correlation Heatmap of Sample Data')
plt.show()