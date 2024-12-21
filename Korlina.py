import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import chi2_contingency, chi2
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

#  пока из этого файла ничего не беру и его закомментил нах
# from Proba333 import count

home_directory = 'C:/Users/fRomanSt/Desktop/frasch/'
zastup_sm = 5

otd_1 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см1")
otd_2 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см2")
otd_3 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см3")
otd_4 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см4")
otd_5 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см5")
boRasch_first = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="бр")

# выбор очередности смен в зависимости от того, кто заступает     # все смены + обобщаю индекс
if zastup_sm == 1:
    # все смены в одном df
        all_sm = pd.concat([otd_1,otd_4,otd_3,otd_2,otd_5], ignore_index=True)
elif zastup_sm == 2:
        all_sm = pd.concat([otd_2,otd_5,otd_4,otd_3,otd_1], ignore_index=True)
elif zastup_sm == 3:
        all_sm = pd.concat([otd_3,otd_1,otd_5,otd_4,otd_2], ignore_index=True)
elif zastup_sm == 4:
        all_sm = pd.concat([otd_4,otd_2,otd_1,otd_5,otd_3], ignore_index=True)
else:
        all_sm = pd.concat([otd_5,otd_3,otd_2,otd_1,otd_4], ignore_index=True)


# меняю NaN на '+'
all_sm = all_sm.fillna('+')
# print(all_sm.shape[0])


# посты для бр общее число постов
posts_for_br = boRasch_first['пост'].to_list()
# привожу к виду 'БП5x-02-03'
posts_for_br = [str(elem).replace(" ", "") for elem in posts_for_br ]
# print(posts_for_br)



# удаляю  коммандировочных и больных
index_names = all_sm[ (all_sm['статус'] == 'б') | (all_sm['статус'] == 'к')].index
all_sm.drop(index_names, inplace = True)



# print(all_sm['пост'])
# all_sm['пост'] = str(all_sm['пост']).replace(" ", "")
# print(all_sm['пост'])
# поле "пост" превращаю в массив и привожу к виду 'БП5x-02-03'
all_sm['пост'] = all_sm.пост.apply(lambda x: x[0:].replace(" ", "").split(','))
# all_sm['пост'].replace(" ", "")

# print(all_sm['пост'])
# print(all_sm.пост[42])
# print(all_sm.shape[0])


# совмещаю df-ы, чтобы не портить all_sm
# стало   = было
br_all_sm = all_sm
posts     = posts_for_br


# ------------------------------------------------------------------------------------------
# for  znach_br_all_sm in br_all_sm['пост']:
#     br_all_sm['пост'] = str(znach_br_all_sm).replace(" ", "")
#     print(br_all_sm['пост'])



# br_all_sm['пост'] = [elem for elem in br_all_sm['пост'] if str(elem).strip()]
# br_all_sm['пост'] = [elem for elem in br_all_sm['пост'] if str(elem).replace(" ", "")]
# print(br_all_sm['пост'])
# ------------------------------------------------------------------------------------------



# _____________________________________________________________________________________________________________
# прохожу по списку л.с пишу пост и удаляю из списка, чтобы незадвоить чела
# порядок прохождения по сменам зависит от номера заступающей смены

# создаю новый df для формирования бр
new_br = pd.DataFrame(columns = ['фио', 'пост', 'смена1', 'смена2'])
print(all_sm.shape[0])
print('------------------------')
count = 0
for ind_br_all_sm, znach_br_all_sm in br_all_sm.iterrows():
    # print(index)
    # print(znach_br_all_sm['фио'])
    for ind_posts,n_br in enumerate(posts):
        for pchela in znach_br_all_sm['пост']:
            if pchela in n_br:
                count+=1
                print(n_br+ "--- "+ pchela)
                print(str(ind_br_all_sm) +" индекс всего БР")
                print(str(ind_posts) + " индекс всех постов")
                # br_all_sm.drop(ind)
                print(count)
                break
        del posts[ind_posts]
        break

