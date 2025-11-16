import pandas as pd
import numpy as np

def add_average_grade(dataframe):
    # add average grade column
    dataframe["average_grade"] = dataframe[["g1","g2","g3"]].mean(axis=1).round(2)
    return dataframe