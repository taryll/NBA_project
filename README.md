# NBA project (Data Science)

This is my first end-to-end Data Science Project. I wanted to
work with my interests, so I decided to choose NBA statistics
as my project data input.

In this project, I will try to predict the NBA match win 
probability. Classify players' positions based on where they 
shoot. Also, I used to play NBA 2K a lot, so it could be fun
trying to predict players' overall ratings on the video 
game based on their stats.

## Steps

**Data collection**: I found this amazing API called **nba_api** that
collects data from 'nba.stats.com'. For the player overall rating
data, I needed to web scrap from 'hoopshype.com' using **Beautiful Soup**
(Python package), since the NBA 2K doesn't provide an API for it. 

**Data processing**: In this step, we need to join our NBA player 
stats with NBA 2K player overall rating. To prediction of the match score,
I found a great article talking about **ELO Rating**, so I need to 
create this feature (I will talk about it later). And finally to
classify (or even to do **cluster analysis**) players' positions, 
the method of **one-hot-encoding** will be used.

**EDA**:

**Model**:

- NBA 2K player overall rating (**Regression**)
- NBA match win probability (**Classification**)
- NBA player positions (**Classification** or **Cluster Analysis**)

**Deploy**: I will use **Heroku** as platform to deploy. 

## Useful for setup

Creating your virtual environment.

```bash
    python3 -m venve env
```

Activate virtual environment.

```bash 
    source env/bin/activate
```

Now install ipykernel so you can add a new kernel on your Jupyter Notebook.

```bash 
    pip install ipykernel
```

Installing your virtual environment kernel.

```bash 
    python3 -m ipykernel install --user --name=nba_env
```

Deactivate your environment.

```bash 
    deactivate
```

List all packages and versions to txt.

```bash 
    pip freeze -> requirements.txt
```

## Special thanks to

- [Cookiecutter](https://github.com/drivendata/cookiecutter-data-science)
- [Readmeso](https://readme.so)
- [nba_api](https://github.com/swar/nba_api)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
