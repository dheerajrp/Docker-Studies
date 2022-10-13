"""
Flask app for hello world!!
"""
import datetime

import numpy as np
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """
    Home function

    Returns:
        Hello World string
    """
    return "Hello World!!"


@app.get("/numpy")
def numpy_version():
    """
    Function to get numpy version

    Returns:
        NumPy version string
    """
    return f"NumPy version is {np.__version__}"


@app.get("/pandas")
def pandas_version():
    """
    Function to get pandas version

    Returns:
        pandas version string
    """
    return f"pandas version is {pd.__version__}"


@app.get("/time")
def get_current_time():
    """
    Gets the current timestamp. This is used for checking the docker
    build in the GitHub Actions

    Returns:
         dict:
            timestamp
    """
    current_time = datetime.datetime.now()
    return dict(time=current_time)
