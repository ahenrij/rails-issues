# rails-issues-analysis
Analysis of the evolution of issues on the Rails project

### Requirements
- python 3.8
- [Poetry](https://python-poetry.org/)
- [Jupyter Notebook](https://jupyter.org/) | [Google Colaboratory](https://colab.research.google.com/)

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
It outputs raw.pickle by default file in the data directory
```shell
$ poetry run python src/extract.py
```

### Data transformation

Run the data transformation script with this command.
It outputs data.pickle by default file in the data directory
```shell
$ poetry run python src/transform.py
```

### Analysis
The analysis code and results are in the `notebook.ipynb` file.
You will need [Jupyter](https://jupyter.org/) to run it or your can use [Google Colab](https://colab.research.google.com/).

If using vscode simply specify the virtual environment created by Poetry and run the notebook.

Otherwise, you might need to install the dependencies properly. Export them to a `requirements.txt` file using the command below:
```shell
poetry export -f requirements.txt --output requirements.txt
```

Then install them in your notebook environment using a cell to run the following command:
```notebook
!pip install requirements.txt
```
Notice the `!` at the beginning, used to run OS command in notebook cells.