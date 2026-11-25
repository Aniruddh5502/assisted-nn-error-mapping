# imports
import pandas as pd
import numpy as np
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
console = Console()

# paths
# project root
root            = Path(__file__).parents[3]
report_folder   = root / "reports"    # reports folder
eval_data       = root / "tests" / "ensemble_test" / "results" / "correlation_analysis.csv"

def generate_report(eval_data:Path=eval_data, report_folder:Path=report_folder)->bool:
    # validate the csv
    if eval_data.suffix != '.csv':
        return False
    
    report = """
# Ensemble Member Variance Based Uncertainty Quantification

This is the correlation betwee

| Target Name | Spearman | Pearson |
|-------------|----------|---------|"""

    data = pd.read_csv(eval_data)
    print(data.columns.to_list())
    print(f"Rows: {len(data)}")
    rows = len(data)
    for row in range(rows):
        report += f"\n|{data.iloc[row,0]}|{data.iloc[row,1]}|{data.iloc[row, 3]}|"
    
    console.print(Markdown(report))
    
    # now we write the report down in the reports folder
    try:
        report_file = report_folder / "Ensemble-Variance-Error-Estimate.md"
        with open(report_file, 'w', encoding='utf-8') as file:
            file.write(report)
        return True
    except Exception as e:
        console.print(f"[red]ERROR: [/] [dim]{e}[/]")
        return False

if __name__=="__main__":
    
    report_generation = generate_report()
    if report_generation:
        console.print(f"\n\n[green]Report Generation Succesfull[/]")
    else:
        console.print(f"\n\n[red]Report Generation Failed[/]")