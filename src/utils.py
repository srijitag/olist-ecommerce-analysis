# small utility functions used across notebooks

import matplotlib.pyplot as plt
import os


def save_chart(fig, filename, charts_path, dpi=150):
    # saves the figure to charts_path/filename
    filepath = os.path.join(charts_path, filename)
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"saved: {filename}")


def print_null_summary(df, name="dataframe"):
    # prints which columns have nulls and what % of the column they are
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0]
    if len(nulls) == 0:
        print(f"{name}: no nulls found")
    else:
        print(f"{name} - columns with nulls:")
        for col, count in nulls.items():
            pct = count / len(df) * 100
            print(f"  {col}: {count:,} ({pct:.1f}%)")
