import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_excel('titanic.xls')
from sklearn.neighbors import KNeighborsClassifier