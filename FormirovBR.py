import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import chi2_contingency, chi2
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

import BR



zastup_smen = BR.BoevRasch.fff
print(zastup_smen)




#_____________________________________________________________ получение файлов
# home_directory = 'C:/Users/fRomanSt/Desktop/frasch/'
#
# active_studs = pd.read_excel(home_directory+'1.xlsx')
# print(active_studs)