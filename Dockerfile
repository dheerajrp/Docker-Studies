# base python version from the docker hub
FROM python:3.10.0

# folder in the container
COPY main.py /app
COPY Dockerfile /app

# setting working directory
WORKDIR /app

# upgrading pip and installing requirements
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# running the file
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
