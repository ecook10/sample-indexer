# Sample Indexer

score + organize audio samples based on their sonic attributes

# Running
1. initiate + activate virtual env
```
> python -m venv .venv
> .\.venv\Scripts\Activate.ps1
```
_for PowerShell - see here for other options: https://docs.python.org/3/library/venv.html_

2. install dependencies
```
> pip install -r requirements.txt
```

3. run a script
```
> python load-wav.py
```

# Criteria Ideas
* pitch
* amount of noise
* duration
* "shape" - relationship between initial hit and tail

Could also maybe use some of the grouping I already did to try train some ML models to attempt to make more abstract groupings, like "digital" vs. "natural"

# TODO
* linear fit to _decay_ exclusively (i.e. start at maximum amplitude) - ditch the 2nd degree polynomial fit
* fit to exponential decay (try both methods here: https://stackoverflow.com/questions/3938042/fitting-exponential-decay-with-no-initial-guessing)
* plot linear + exponential decay
* experiment with RMS parameters (chunk size + stride)
* batch perform on an entire directory
* get some better samples (collect a subset from my actual sample library)
* persist batch indices somehow (db? maybe try no-sql?)
* search functionality (criteria percentages)
* write sorted sub-directiries w/ copied files
* command-line util
* integrate w/ ableton somehow (max plugin? write drumrack folders / files?)