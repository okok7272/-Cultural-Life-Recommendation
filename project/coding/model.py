import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
from sklearn.feature_selection import f_regression, SelectKBest
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import database.edaprocessing as eda
#sqlite에서 데이터 불러오기




