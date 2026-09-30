# Python Practice

A set of small Python exercises covering core language fundamentals: variables and
data types, conditionals, loops, functions, modules, error handling, file handling,
and script organisation.

## Requirements

- Python 3.11 or newer
- pip

## Setup

1. Clone the repository:

```bash
   git clone https://github.com/Lightleonardo/python-practice.git
   cd python-practice
```

2. Create and activate a virtual environment:

```bash
   python -m venv .venv
```

   Windows (PowerShell):
```bash
   .venv\Scripts\Activate.ps1
```

   macOS / Linux:
```bash
   source .venv/bin/activate
```

3. Install the dependencies:

```bash
   pip install -r requirements.txt
```

## Running the exercises

Each exercise is a standalone script. Run any of them from the project root, for example:

```bash
python 01_variables_and_types/personal_card.py
python 02_conditionals/grade_classifier.py
python 03_Loops/multiplication_table.py
python 04_Functions/temperature.py
python 05_modules/use_text_tool.py
python 06_error_handling/safe_input.py
python 07_file_handling/notes.py
python 08_script_organisation/shopping_summary.py
```

Some scripts prompt for input in the terminal.

## Running the tests

Automated tests are written with `pytest`. From the project root, with the virtual
environment active:

```bash
pytest
```

Tested exercises:
- `04_Functions/temperature.py` — tested by `04_Functions/test_temperature.py`
- `05_modules/text_tool.py` — tested by `05_modules/test_text_tool.py`
- `08_script_organisation/shopping_summary.py` — tested by `08_script_organisation/test_shopping_summary.py`

## Formatting

Code is formatted with [Black](https://black.readthedocs.io/):

```bash
black .
```

## Project structure

| Folder | Concept |
|---|---|
| `01_variables_and_types` | Variables and data types |
| `02_conditionals` | Conditionals |
| `03_Loops` | Loops |
| `04_Functions` | Functions (tested) |
| `05_modules` | Modules (tested) |
| `06_error_handling` | Error handling |
| `07_file_handling` | File handling |
| `08_script_organisation` | Script organisation (tested) |

## Branches

Exercises were developed on feature branches and merged into `master` via pull
requests:
- `exercises/variables-conditionals` — variables, conditionals, loops, functions
- `exercises/modules-errors-files` — modules, error handling, file handling
- `exercises/script-organisation` — script organisation

## Debugging note

See [`Debugging.md`](./Debugging.md) for a walkthrough of one error encountered
during development, its cause, and the fix.