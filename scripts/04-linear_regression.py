from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WineQT.csv" # relative to repo root, works on any machine

df = pd.read_csv(DATA_PATH)


