import pandas as pd
from pathlib import Path

def generate_comprehensive_report(csv_path:Path, output_path):
    """
    Generates a single, unified Markdown report containing:
    1. Dataset Overview & Statistics (Summary)
    2. Detailed Sweep Results Table (Extracted Data)
    3. Data Integrity Audit
    """
    if not csv_path.exists():
        print(f"Error: File {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 1. Prepare Statistical Summary
    stats = df.describe().to_markdown()

    # 2. Prepare Detailed Results Table (Sorted by Lipschitz)
    cols_to_keep = [
        'lipschitz', 'mean_rmse', 'mean_spearman', 'mean_ratio', 
        'val_mean_rmse', 'val_mean_spearman', 'val_mean_ratio'
    ]
    # Only include columns that actually exist in the dataframe to avoid KeyError
    existing_cols = [c for c in cols_to_keep if c in df.columns]
    df_sorted = df.sort_values('lipschitz')[existing_cols]
    markdown_table = df_sorted.to_markdown(index=False, floatfmt=".4f")

    # 3. Assemble the Report
    report_content = f"""# Comprehensive Sweep Analysis Report

## 1. Dataset Overview & Statistics
This section provides a statistical summary of the collected sweep data.

{stats}

## 2. Detailed Sweep Results
The following table presents the exact metrics recorded for each Lipschitz constant value.

{markdown_table}

## 3. Metric Definitions
To interpret the results above, note the following mappings:
- **Lipschitz ($L$)**: The spectral normalization constraint applied to the model backbone.
- **RMSE**: Root Mean Squared Error (lower is better).
- **Spearman $\\rho$**: Monotonic correlation between absolute error and predicted variance (higher is better).
- **Ratio**: The relationship between RMSE and standard deviation (closer to 1.0 indicates better calibration).

## 4. Data Integrity Audit
- **Total Rows Processed**: {len(df)}
- **Null Values Detected**: {df.isnull().sum().sum()}
- **Data Loss during analysis**: {df.isnull().sum().sum()/len(df) * 100}%
"""

    with open(output_path, 'w') as f:
        f.write(report_content)
    
    print(f"Successfully generated comprehensive report at: {output_path}")

if __name__ == "__main__":
    # Use relative paths or adjust as needed for the execution environment
    # For production, these would ideally be passed via argparse
    TEST_ROOT = Path(__file__).parents[1]
    PROJECT_ROOT = Path(__file__).parents[3]
    
    INPUT_CSV = TEST_ROOT / "data" / "sweep_results.csv"
    OUTPUT_MD = PROJECT_ROOT / "reports" /"sngp_sweep_report.md"
    
    generate_comprehensive_report(INPUT_CSV, OUTPUT_MD)
