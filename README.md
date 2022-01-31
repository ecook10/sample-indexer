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
[] fourier transform sample data + graph
[] find fundamental pitch
[] algorithm for noise at time t