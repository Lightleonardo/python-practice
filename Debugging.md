# Debugging Note

## The error
Exercise: `03_loops/sum_numbers.py`

```
Traceback (most recent call last):
  File "sum_numbers.py", line 5, in <module>
    ...
ValueError: invalid literal for int() with base 10: 'abc'
```
(Paste your actual traceback here, copied from the terminal.)

## What I was trying to do
One or two sentences on what the code was supposed to do.

## What caused it
Explain the cause in your own words. Point to the exact line and say why Python raised the error.

## How I fixed it
Describe the change you made, and paste the corrected code.

## What I learned
One sentence on how to avoid or handle this next time.

## The error 1
Exercise: `02_conditionals/grade_classifier.py`

```
Traceback (most recent call last):
KeyboardInterrupt
>>> & c:/Users/USER/python-practice/.venv/Scripts/python.exe c:/Users/USER/python-practice/02_conditionals/grade_classifier.py
  File "<stdin>", line 1
    & c:/Users/USER/python-practice/.venv/Scripts/python.exe c:/Users/USER/python-practice/02_conditionals/grade_classifier.py
    ^
SyntaxError: invalid syntax
```

## What I was trying to do
write a grade classifier that classifies grades into A, B, C, D, E, F, and Invalid grade

## What caused it
used print f-strings in code but f in capital letter

## How I fixed it
corrected f in f-strings to lowercase
print (f"Student {name}, invalid grade")

## What I learned
python f-strings are case sensitive
f in f-strings must be lowercase


## The error 2
Exercise: `02_conditionals/grade_classifier.py`

```
KeyboardInterrupt
>>> & c:/Users/USER/python-practice/.venv/Scripts/python.exe c:/Users/USER/python-practice/02_conditionals/grade_classifier.py
  File "<stdin>", line 1
    & c:/Users/USER/python-practice/.venv/Scripts/python.exe c:/Users/USER/python-practice/02_conditionals/grade_classifier.py
    ^
SyntaxError: invalid syntax
```


## What I was trying to do
write a grade classifier that classifies grades into A, B, C, D, E, F, and Invalid grade

## What caused it
the terminal was in the Python REPL (>>>), so a PowerShell command was read as Python code

## How I fixed it
exit with exit(), confirm the PowerShell prompt, then run the script

## What I learned
check the prompt (>>> means Python, PS means PowerShell) before running commands



## The error 3
Exercise: `python-practice`

```
black : The term 'black' is not recognized as the name of a cmdlet, function, script 
file, or operable program. Check the spelling of the name, or if a path was included, 
verify that the path is correct and try again.
At line:1 char:1
+ black .
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (black:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```


## What I was trying to do
use the formatter black to format the code in the file

## What caused it
was not in .env directory, so black command was not recognized

## How I fixed it
change directory to .env directory, then run black command


## What I learned
should always cross check present directory before running commands

## The error 4
Exercise: ModuleNotFoundError: No module named 'Temperature'
## what Cause it
 I renamed Temperature.py to temperature.py, but the test file still imported Temperature. Python import names are case-sensitive.
## How i fixed it
 changed the import to from temperature import ...
## What I learned
Lesson: after renaming a file, update every import that refers to it, then rerun the tests