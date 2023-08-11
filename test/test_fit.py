import pandas as pd
import sys
sys.path.append("/home/nick/Distribution-Identification/src")
from fit import test


data = pd.read_csv("/home/nick/Distribution-Identification/test/LungCap.csv")

distribution = test(data["LungCap"].to_numpy())

distribution.summary
