# Overview
Streamlit application to determine drug method of action based on screening results and public data.

# Setup

## Local

To set things up to run locally.

```bash
# set up virtual environment
pyenv virtualenv 3.11.7 st-drug-moa
pyenv local st-drug-moa

# install
git clone git@github.com:mrperkett/st-drug-moa.git
cd st-drug-moa/
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# run the application
python3 -m streamlit run --server.port 8502 drug_moa_app.py
# view website at http://localhost:8502/
```

## Docker

To run the docker container.

```bash
# build the docker image
docker build -t st-drug-moa .

docker run -p 8502:8502 st-drug-moa
# view website at http://localhost:8502/
```