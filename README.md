# Fin Tracker Python  
  
A minimal viable prototype for a Python-based personal finance tracker.  
  
## Setup  
  
1. Ensure Python 3.8+ is installed.  
2. Clone the repository and navigate into it.  
3. (Optional) Create a virtual environment.  
4. Install any required packages (currently none).  
  
## Usage  
  
This package provides simple tools for managing transaction data.  
  
### Loading data  
  
Use the `loader.py` functions to load CSV transaction data from the `data/sample.csv` file or your own file.  
  
### CLI  
  
Run the CLI module to see available commands:  
  
```bash  
python -m fintracker.cli --help  
```  
  
This will show options for loading transactions and viewing summaries.  
  
### Data sample  
  
The `data/sample.csv` file provides example transaction data with columns: date, description, amount, and category.
