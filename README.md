

print("hello from Tzurit")


# Football Match Analysis

hiiiiiiii

thanks 

Python script that analyzes football match statistics from a pandas DataFrame and returns a summary report.

## Features

- Total and per-team **goals**
- Total and per-team **shots**
- Total and per-team **passes**
- Average **possession %** by team

Columns are optional: the analyzer only computes metrics for columns that exist in the input data.

## Requirements

- Python 3
- [pandas](https://pandas.pydata.org/)

Install dependencies:

```bash
pip install pandas
```

## Usage

Run the sample analysis:

```bash
python dashboard.py
```

Expected output:

```
Total Goals: 3
Goals by Team: {'A': 2, 'B': 1}
Total Shots: 14
Shots by Team: {'A': 8, 'B': 6}
Total Passes: 600
Passes by Team: {'A': 320, 'B': 280}
Possession % by Team: {'A': 55.0, 'B': 45.0}
```

### Analyze your own data

Pass a DataFrame with a `Team` column and any of: `Goals`, `Shots`, `Passes`, `Possession`:

```python
import pandas as pd
from dashboard import analyze_football_match

match_data = pd.DataFrame([
    {"Team": "A", "Goals": 2, "Shots": 8, "Passes": 320, "Possession": 55},
    {"Team": "B", "Goals": 1, "Shots": 6, "Passes": 280, "Possession": 45},
])

report = analyze_football_match(match_data)
print(report)
```

## Project structure

```
.
├── dashboard.py   # Match analysis function and sample run
└── README.md
```
