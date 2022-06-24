# Reddit Comment Extractor

The purpose of this project is to have an easy-to-use interface for extracting comments from reddit api for input into data processing pipeline that conducts sentiment classification for analysis

## Getting Started

- clone project

```bash
git clone git@github.com:bfmcneill/rce.git
```

- create virtual environment, activate, install setup.py with dev dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

- update config.json with postgres database credentials



## Usage

- activate virtual environment on mac/linux

```bash
source venv/bin/activate
```

- execute command to read data from API into database

```bash
pcmd comments -s wallstreetbets -a "2021-12-10" -b "2021-12-15"
```

## References

- https://github.com/pushshift/api
- https://praw.readthedocs.io/en/latest/tutorials/comments.html
