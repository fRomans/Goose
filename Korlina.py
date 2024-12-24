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
print(all_sm.shape[0])
print('______________с больными и ком')


# посты для бр общее число постов
posts_for_br = boRasch_first['пост'].to_list()

# привожу к виду 'БП5x-02-03'
posts_for_br = [str(elem).replace(" ", "") for elem in posts_for_br ]

# выстраиваю посты в нужном порядке
posled_posts = sorted(posts_for_br, key=lambda x: str(x)[-1])
# print(posled_posts)


# удаляю  коммандировочных и больных
index_names = all_sm[ (all_sm['статус'] == 'б') | (all_sm['статус'] == 'к')].index
all_sm.drop(index_names, inplace = True)
bez_bk_all_sm = all_sm
print(bez_bk_all_sm.shape[0])
print('______________без больных и ком')





# поле "пост" превращаю в массив и привожу к виду 'БП5x-02-03'
bez_bk_all_sm['пост'] = bez_bk_all_sm.пост.apply(lambda x: x[0:].replace(" ", "").split(','))



# совмещаю df-ы, чтобы не портить all_sm
# стало   = было
br_all_sm = bez_bk_all_sm
posts     = posled_posts


# создаю новый df для формирования бр
new_br_1sm = pd.DataFrame(columns = ['фио', 'пост_смена1'])


# порядок прохождения по сменам зависит от номера заступающей смены
count = 0
for ind_nomer_br,nomer_br in enumerate(posts):
    # print(index)
    # print(znach_br_all_sm['фио'])
    for ind_br_all_sm, znach_br_all_sm in br_all_sm.iterrows():
        succ = False

        for dopysk_chela in znach_br_all_sm['пост']:
                if dopysk_chela in nomer_br:
                    count+=1

                    # заполняю бр
                    new_row = {'фио': znach_br_all_sm['фио'], 'пост_смена1':nomer_br , '№_смены':znach_br_all_sm['смена']}
                    new_br_1sm = pd.concat([new_br_1sm, pd.DataFrame([new_row])], ignore_index=True)

                    # прохожу по списку пост и удаляю из списка челов, чтобы незадвоить
                    br_all_sm.drop(ind_br_all_sm, inplace=True)
                    succ = True
                    break
        if succ == True:
            break

new_br_2sm = pd.DataFrame(columns = ['фио', 'пост_смена2'])
for ind_nomer_br,nomer_br in enumerate(posts):
    # print(index)
    # print(znach_br_all_sm['фио'])
    for ind_br_all_sm, znach_br_all_sm in br_all_sm.iterrows():
        succ = False

        for dopysk_chela in znach_br_all_sm['пост']:
                if dopysk_chela in nomer_br:
                    count+=1

                    # заполняю бр
                    new_row = {'фио': znach_br_all_sm['фио'], 'пост_смена2':nomer_br , '№_смены':znach_br_all_sm['смена']}
                    new_br_2sm = pd.concat([new_br_2sm, pd.DataFrame([new_row])], ignore_index=True)

                    # прохожу по списку пост и удаляю из списка челов, чтобы незадвоить
                    br_all_sm.drop(ind_br_all_sm, inplace=True)
                    succ = True
                    break
        if succ == True:
            break

# print(new_br_1sm)
# print('___________________________________________________________________________')
# print('___________________________________________________________________________')
# print('___________________________________________________________________________')
# print(new_br_2sm)
# print('___________________________________________________________________________')
# print('___________________________________________________________________________')
# print('___________________________________________________________________________')
# print(br_all_sm)

# объединяю полученные df с первой и второй сменой (незадействованных не знаю пока куда девать)
com_br = pd.merge(new_br_1sm, new_br_2sm, left_index=True, right_index=True)

# сохраняю расчет в exel и отправляю в home_directory(определена вначале файла)____________________ПОКА ОТКЛЮЧУ ЧТОБЫ НЕ МУСОРИТЬ_________!!!!!!!!!!!!!!!!!!!
# com_br.to_excel(home_directory +'combat_mans.xlsx', index=False)             ____________________ПОКА ОТКЛЮЧУ ЧТОБЫ НЕ МУСОРИТЬ_________!!!!!!!!!!!!!!!!!!!



print(com_br)
print('___________________________________________________________________________')
print('___________________________________________________________________________')
print('______________________незадействованы_____________________________________________________')
print(br_all_sm)

