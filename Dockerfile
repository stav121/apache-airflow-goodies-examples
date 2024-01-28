# Custom image for Airflow 2.7.2 and Python version 3.11
FROM apache/airflow:2.7.2-python3.11

COPY requirements.txt .

# COPY deps/* .

# Upgrade PIP
RUN pip install --upgrade pip

# Install the requirements for local dev
RUN pip install -r requirements.txt
