# import numpy as np
# import pandas as pd
# import scipy.stats as st
# from scipy.stats import chi2_contingency, chi2
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pingouin as pg
#
# home_directory = 'C:/Users/fRomanSt/Desktop/frasch/'
# zastup_sm = 5
#
# otd_1 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см1")
# otd_2 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см2")
# otd_3 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см3")
# otd_4 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см4")
# otd_5 = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="см5")
# boRasch_first = pd.read_excel(home_directory + 'goose.xlsx', sheet_name="бр")
#
# # выбор очередности смен в зависимости от того, кто заступает
# if zastup_sm == 1:
#     # все смены в одном df
#         all_sm = pd.concat([otd_1,otd_4,otd_3,otd_2,otd_5])
# elif zastup_sm == 2:
#         all_sm = pd.concat([otd_2,otd_5,otd_4,otd_3,otd_1])
# elif zastup_sm == 3:
#         all_sm = pd.concat([otd_3,otd_1,otd_5,otd_4,otd_2])
# elif zastup_sm == 4:
#         all_sm = pd.concat([otd_4,otd_2,otd_1,otd_5,otd_3])
# else:
#         all_sm = pd.concat([otd_5,otd_3,otd_2,otd_1,otd_4])
#
# # все смены + обобщаю индекс
# all_sm = pd.concat([otd_1,otd_2,otd_3,otd_4,otd_5], ignore_index=True)
# # меняю NaN на '+'
# all_sm = all_sm.fillna('+')
#
# # удаляю  коммандировочных и больных
# index_names = all_sm[ (all_sm['статус'] == 'б') | (all_sm['статус'] == 'к')].index
# all_sm.drop(index_names, inplace = True)
#
#
# # привожу таблицы к единому виду по типу
# all_sm['фио'] = all_sm['фио'].astype(str)
# all_sm['смена'] = all_sm['смена'].astype(str)
# all_sm['пост'] = all_sm['пост'].astype(str)
# all_sm['статус'] = all_sm['статус'].astype(str)
#
# # посты для бр
# posts_for_br = boRasch_first['пост'].values
#
#
# # считаю требуемое кол-во чел по постам
# posts_for_br.size
#
#
#
# # совмещаю df-ы
# br_all_sm = all_sm
#
# #  беру все посты чела  , делю по зпт
# count = 0
# ss = []
# for  znach_br_all_sm in enumerate(br_all_sm['пост']):
#     print(znach_br_all_sm)
#
# #  окончательный обрезанный список постов у каждого чела
# # okon = []
# # for s in ss:
# #     prom = []
# #     okon.append(prom)
# #     count += 1
# #     for st in s:
# #         r=st.replace(" ", "")
# #         prom.append(r)
# #
# # print(okon)
# # print(count)
#
#
# # br_all_sm = br_all_sm.assign(ColName='')
# # br_all_sm = br_all_sm['ColName'].apply(', '.join)
#
# # df = pd.DataFrame({
# #     'пост1': okon
# #     })
#
# # br_all_sm['ColName'] = df.пост.join()
# # comm = br_all_sm.merge(df, how='left', on='пост')
# # ttt = df.join(br_all_sm)
# #
# # print(ttt)
