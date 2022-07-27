import undetected_chromedriver as uc
import json
from haralyzer import HarParser, HarPage
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from lxml import etree
from datetime import date
import calendar
import numpy as np


def filterHikes(hikes_df,distance_max,distance_min,drive_lim,feature_requests,excluded,check_weather,dow):
        criteria_df = []
        # locations = {'Denver':'driving_time_from_denver','Springs':'driving_time_from_springs'}
        dow_rain = {'Saturday':'% chance rain saturday','Sunday':'% chance rain sunday'}
        dow_clouds = {'Saturday':'% cloudy saturday','Sunday':'% cloudy sunday'}
        cloud_var = '% cloudy '+ dow
        rain_var = '% chance rain ' + dow
        
        # hikes_df = pd.read_csv('complete_hike_data'+str(date.today())+'.csv')

#         print(hikes_df.columns)

#         print(hikes_df)

        # hour = []
        # for times in hikes_df.driving_time_from_denver:
        #     times = str(times)
        #     times = times.split(' ')
        #     # print(times)
        #     if times[0] != 'n/a':
        #         try:
        #             hour.append(round((int(times[0])*60 + int(times[2]))/60,2))
        #         except(IndexError):
        #             hour.append(round((int(times[0])*60),2))
        #     else:
        #         hour.append(5.5)
        # hikes_df.driving_time_from_denver = hour

        hour = []
        for times in hikes_df.driving_time_from_home:
            times = str(times)
            times = times.split(' ')
            # print(times)
            if times[0] != 'n/a':
                try:
                    hour.append(round((int(times[0])*60 + int(times[2]))/60,2))
                except(IndexError):
                    hour.append(round((int(times[0])*60),2))
            else:
                hour.append(0)
        hikes_df.driving_time_from_home = hour
        na_df = hikes_df[hikes_df[rain_var] == 'n/a']
        hikes_df = hikes_df[hikes_df[rain_var] != 'n/a']
        
        # print(hikes_df)
        if check_weather == True:

            criteria_df = hikes_df[(hikes_df['driving_time_from_home'].astype(float)<=drive_lim)&(hikes_df[rain_var]<=55)\
                                   & (hikes_df.distance_miles.astype(float)<=distance_max)& (hikes_df.distance_miles.astype(float)>=distance_min)\
                                   & (hikes_df.features.astype(str).str.contains(feature_requests[0]))&  (hikes_df.features.astype(str).str.contains(feature_requests[1]))\
                                   &(hikes_df.features.astype(str).str.contains(excluded== False))&(hikes_df[cloud_var]<=60)]

            na_criteria = na_df[(na_df['driving_time_from_home'].astype(float)<=drive_lim)\
                                   & (na_df.distance_miles.astype(float)<=distance_max)& (na_df.distance_miles.astype(float)>=distance_min)\
                                   &(na_df.features.astype(str).str.contains(excluded== False))\
                                   & (na_df.features.astype(str).str.contains(feature_requests[0]))&(na_df.features.astype(str).str.contains(feature_requests[1]))]
        else:
            criteria_df = hikes_df[(hikes_df['driving_time_from_home'].astype(float)<=drive_lim)\
                                   & (hikes_df.distance_miles.astype(float)<=distance_max)& (hikes_df.distance_miles.astype(float)>=distance_min)\
                                   &(hikes_df.features.astype(str).str.contains(excluded== False))\
                                   & (hikes_df.features.astype(str).str.contains(feature_requests[0]))&  (hikes_df.features.astype(str).str.contains(feature_requests[1]))]

            na_criteria = na_df[(na_df['driving_time_from_home'].astype(float)<=drive_lim)\
                                   & (na_df.distance_miles.astype(float)<=distance_max)& (na_df.distance_miles.astype(float)>=distance_min)\
                                   & (na_df.features.astype(str).str.contains(excluded== False))\
                                   & (na_df.features.astype(str).str.contains(feature_requests[0]))&(na_df.features.astype(str).str.contains(feature_requests[1]))]
            
        # print(criteria_df)
        # criteria_df = hikes_df[(hikes_df['driving_time_from_home'].astype(int)<drive_lim)& (hikes_df.distance_miles.astype(int)>distance_min)\
        #                       &(hikes_df[dow_rain[dow]]<50)\
        #                        & (hikes_df.distance_miles.astype(int)<distance_max)& (hikes_df.distance_miles.astype(int)>distance_min)]

        # print(criteria_df)
        criteria_df = criteria_df.append(na_criteria)
        criteria_df['scale_pop'] = abs(criteria_df['popularity'] - criteria_df['popularity'].mean())
        
        if 'bucket' in criteria_df.columns:
    
            criteria_df = criteria_df.sort_values(by = ['bucket','avg_rating','scale_pop'], ascending = [False, False, True])

        else:
            criteria_df = criteria_df.sort_values(by = ['avg_rating','scale_pop'], ascending = [False, True])

        
        # to-do: finish weighting formula
        
        # hikes_df.loc[hikes_df.popularity == max(hikes_df.popularity)]
        # pop_scale = (max(hikes_df.popularity)-min(hikes_df.popularity))/3
        # conditions = [
        #     (df['popularity'] >= min(hikes_df.popularity)) & (df['popularity'] < (min(hikes_df.popularity)+pop_scale),
        #     (df['popularity'] >= (min(hikes_df.popularity)+pop_scale)& (df['popularity'] < (min(hikes_df.popularity)+(pop_scale*2)),
        #     (df['popularity'] >= (min(hikes_df.popularity)+(pop_scale*2))& (df['popularity'] <= max(hikes_df.popularity))
        #     ]

        # # create a list of the values we want to assign for each condition
        # values = [1,2,3]

        # # create a new column and use np.select to assign values to it using our lists as arguments
        # df['tier'] = np.select(conditions, values)

        # #criteria_df['popularity_class'] = 

#         criteria_df_num = ['driving_time_from_home','distance_miles', 'duration_hours', \
#                            'elevation_gain_ft', 'difficulty_rating',\
#                '% chance rain saturday', '% cloudy saturday', '% chance rain sunday',\
#                '% cloudy sunday','popularity', 'avg_rating', 'num_reviews']

#         normalized_df =(criteria_df[criteria_df_num]-criteria_df[criteria_df_num].mean())/criteria_df[criteria_df_num].std()

#         normalized_df['pop_abs'] = normalized_df['popularity'].abs()
#          # to do: weight normalized values & sum for scores
#         normalized_df

#sort so that driving distance is weighted by hiking distance (loner drives for shorter hikes lower)
        
        return criteria_df