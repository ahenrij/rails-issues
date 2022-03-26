# rails-issues-analysis
Analysis of the evolution of issues on the Rails project

### Requirements
- python 3.8
- [Poetry](https://python-poetry.org/)

### Install dependencies
```shell
$ poetry install
```

### Data extraction

To run extractor github oauth have been used.
Specify your token into the .env file after running the command below.
```shell
$ copy .env.example .env
```

Run data extractor
It outputs the raw.pickle file in data directory
```shell
$ poetry run src/extractor.py
```
