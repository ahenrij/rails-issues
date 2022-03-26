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

To run the extractor script, github oauth have been used.
Specify your personal token in the .env file after running the command below.
```shell
$ copy .env.example .env
```

Run the data extraction script with this command.
It outputs raw.pickle file in the data directory
```shell
$ poetry run src/extract.py
```
