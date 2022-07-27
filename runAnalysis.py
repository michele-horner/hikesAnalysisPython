from IPython.display import display
from ipywidgets import widgets, interactive
import undetected_chromedriver as uc
import json
from haralyzer import HarParser, HarPage
import pandas as pd
import requests
from requests.structures import CaseInsensitiveDict
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

from filterTrailList import filterHikes
from scrapeAllTrails import allTrailsAny
from match14ers import get14erMatches 
from filter14ersbyClass import filter14ers
from getCO14ers import getallCO14erData




if __name__ == '__main__':
   

    feature_dict = {'Lake':'lake','Wildflowers':'wild-flowers', 'River':'river','Views':'views',\
                    'Dogs allowed':'dogs','Scramble':'scramble','Waterfall':'waterfall', 'Forest':'forest', \
                    'Wildlife':'wildlife','Trail Running':'running'}
    excluded_dict = {'No Shade':'no-shade','Snow':'snow','None':'nothing','Fee':'fee','Scramble':'scramble', 'Forest':'forest'}



    feature_requests = ['lake','wild-flowers']

    excluded = 'forest'

    address = '333 E Colorado Ave, Colorado Springs, CO, 80903'

    hike_day = 'Sunday'
    dow = hike_day
    distance_max = 15
    distance_min = 2

    drive_lim = 3.5
    class_limit = 2.5

    trail_list = 'Colorado short list' #options:'All Colorado','Colorado short list','All 14ers','Top 14ers'

    check_weather = True


    full_df = allTrailsAny(address, trail_list, hike_day)
    # full_df.to_csv('check_err.csv')

    full_df_in= full_df[:][:]

    filtered_hikes_df = filterHikes(full_df_in[:][:],distance_max,distance_min,drive_lim,feature_requests,excluded, check_weather,dow)
    # filtered_hikes_df.to_csv('filtered_hikes_'+str(date.today())+'.csv')

    if trail_list == 'Top 14ers' or  trail_list == 'All 14ers':

        all14erData = getallCO14erData()

        co_14_df = all14erData[:][:]
        at_df = filtered_hikes_df[:][:]

        merged_14er_data = get14erMatches(at_df,co_14_df)

        filtered_14er_df = filter14ers(merged_14er_data,class_limit)

        filtered_14er_df.to_csv('filtered_14ers_'+str(date.today())+'.csv')
        print('Analysis Complete.')
    else:
        
        filtered_hikes_df.to_csv('filtered_hikes_'+str(date.today())+'.csv')
        print('Analysis Complete.')

