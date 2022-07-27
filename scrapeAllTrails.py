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
from getDataFrames import getall14ers, getallco, getshortlist, gettop14ers


def allTrailsAny(address, trail_list, hike_day):
    from getDataFrames import getall14ers, getallco, getshortlist, gettop14ers

    curr_date = date.today()
    today = str(calendar.day_name[curr_date.weekday()])
    doys = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
    
    if abs(doys[hike_day] - doys[today]) > 5:
        print('Choose earlier hiking day. Weather data not available yet.')    
        return
    
    trail_dict = {'All 14ers': getall14ers() ,'Top 14ers':gettop14ers(), 'Colorado short list':getshortlist(), 'All Colorado':getallco()}
    hikes = trail_dict[trail_list]

    # print(hikes)

    # for hit in hits['hits']:
    #     print(hit['name'])

    # print(hit.keys())

    hikes['duration_hours'] = hikes['duration_minutes']/60
    hikes['distance_miles'] = hikes['length']*.000621371
    
    #get hike url list
    hike_url = list('https://www.alltrails.com/'+hikes['slug'])
    hikes['hike_url'] = pd.DataFrame(hike_url)

    # hike_sample = hike_url[0:4]

    hike_dict = dict()
    weather = dict()

    # print(hike_url)

    driver = uc.Chrome()

    driver.get(hike_url[0])
    
    import time

    i = 20
    while i > -1:
        print('Solve Captcha in:', i, 'seconds', end='\r')
        time.sleep(1)
        i -= 1
    
    #solve captcha once

    #get metadata for each hike
    
    for hike in hike_url:
        attempts = 0
        success = False
        while attempts < 5 and not success:
            try:
                driver.get(hike)
                hike_soup = BeautifulSoup(driver.page_source)
                header = hike_soup.find('div', id='content')
                metadata = header.findChild('div')['data-react-props']
                metadata = json.loads(metadata)


                name = metadata['trail']['name']
                features = metadata['trailTags']['whatToSeeAndObstacles']
                last_review_date = metadata['reviews']['trail_reviews'][0]['date']
                last_review = metadata['reviews']['trail_reviews'][0]['comment']
                if metadata['trailConditions'] != []:
                    trail_conditions = metadata['trailConditions'][0]['name']
                else:
                    trail_conditions = 'None reported in last 7 days.'
                if metadata['weatherConditionsProps']['weatherForecast'] != None:
                    if doys[today] == 1:
                        weather_nar_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['narrative']
                        weather_nar_sun = 'n/a'
                        clouds_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['clds']
                        clouds_sun = 'n/a'
                        rain_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['pop']
                        rain_sun = 'n/a'
                        moon_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['lunar_phase']
                        moon_sun = 'n/a'
                        weather_nar_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['narrative']
                        clouds_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['clds']
                        rain_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['pop']
                    elif doys[today] == 0:
                        weather_nar_sat = 'n/a'
                        weather_nar_sun = 'n/a'
                        clouds_sat = 'n/a'
                        clouds_sun = 'n/a'
                        rain_sat = 'n/a'
                        rain_sun = 'n/a'
                        moon_sat = 'n/a'
                        moon_sun = 'n/a'
                        weather_nar_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['narrative']
                        clouds_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['clds']
                        rain_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['pop']

                    #weather_da
                    #weather_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['dow']
                    # weather_nar_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['narrative']
                    # weather_nar_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['narrative']
                    # clouds_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['clds']
                    # clouds_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['clds']
                    # rain_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['pop']
                    # rain_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['pop']
                    # moon_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['lunar_phase']
                    # moon_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['lunar_phase']
                    
                    
                    else:
                        weather_nar_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['narrative']
                        weather_nar_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['narrative']
                        clouds_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['clds']
                        clouds_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['clds']
                        rain_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['day']['pop']
                        rain_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['day']['pop']
                        moon_sat = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][6 - doys[today]]['lunar_phase']
                        moon_sun = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][7 - doys[today]]['lunar_phase']
                        weather_nar_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['narrative']
                        clouds_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['clds']
                        rain_hike_day = metadata['weatherConditionsProps']['weatherForecast']['forecasts'][abs(doys[hike_day]-doys[today])]['day']['pop']

                        #weather_nar_sat = weather_nar_sat + ' clouds: '+ str(clouds_sat)+ '%'
                    #weather_nar_sun = weather_nar_sun + ' clouds: '+ str(clouds_sun)+ '%'

                else:
                    #weather_day = 'n/a'
                    weather_nar_sat = 'n/a'
                    weather_nar_sun = 'n/a'
                    clouds_sat = 'n/a'
                    clouds_sun = 'n/a'
                    rain_sat = 'n/a'
                    rain_sun = 'n/a'
                    moon_sat = 'n/a'
                    moon_sun = 'n/a'
                    weather_nar_hike_day = 'n/a'
                    clouds_hike_day = 'n/a'
                    rain_hike_day = 'n/a'

                    # weather_clouds = 'n/a'

                # weather[weather_day] = {'summary': weather_nar, 'clouds':weather_clouds}
                hike_info = {'features':features, 'trail_conditions':trail_conditions,'last hiked': last_review_date, 'last review': last_review, 'saturday_weather': weather_nar_sat,\
                             'sunday_weather': weather_nar_sun, 'clouds_sat':clouds_sat,'clouds_sun': clouds_sun,'rain_sat':rain_sat,\
                             'rain_sun':rain_sun,'moon_phase_sat':moon_sat,'moon_phase_sun': moon_sun,\
                            'clouds_hike_day': clouds_hike_day,'rain_hike_day':rain_hike_day,\
                             'hike_day_weather':weather_nar_hike_day}
                hike_dict[name] = hike_info

                print('Processing:', name)
                # print(features)
                # print(hike_dict[name])
                success = True
            except:
                print('Solve Captcha.', end='\r')
                time.sleep(15)
                attempts += 1
                if attempts == 5:
                    print('Unable to Retrieve All Trails Data.')
                    return

    # print(hike_dict)

    # driver.get('https://www.alltrails.com/trail/us/colorado/wheeler-lake')
    # test_hike = BeautifulSoup(driver.page_source)
    # test_header = test_hike.find('div', id='content')
    # test_metadata = test_header.findChild('div')['data-react-props']
    # test_metadata = json.loads(test_metadata)
    # test_name = metadata['trail']['name']
    # test_features = metadata['trailTags']['whatToSeeAndObstacles']
    # test_last_review_date = metadata['reviews']['trail_reviews'][0]['date']
    # test_last_review = metadata['reviews']['trail_reviews'][0]['comment']
    # test_metadata['weatherConditionsProps']['weatherForecast']['forecasts'][2]['lunar_phase']                                      

    # print(test_hike)

    metadata_df = pd.DataFrame.from_dict(hike_dict)
    metadata_df = pd.DataFrame.transpose(metadata_df)
    metadata_df.reset_index(inplace=True)

    # print(metadata_df)

    #get driving times
    maps_url = []
    n = 0
    for hike in hikes._geoloc:
        maps_url = maps_url + ['https://www.google.com/maps/dir/'+ address.replace(' ','+') + '/'  + str(hikes._geoloc[n]['lat']) + ',' + str(hikes._geoloc[n]['lng'])]
        n = n+1

    #get driving times from denver
    # maps_url_den = []
    # n = 0
    # for hike in hikes._geoloc:
    #     maps_url_den = maps_url_den + ['https://www.google.com/maps/dir/'+ address_den.replace(' ','+') + '/' + str(hikes._geoloc[n]['lat']) + ',' + str(hikes._geoloc[n]['lng'])]
    #     n = n+1

    # print(maps_url_den)

    # maps_url

    browser = webdriver.Chrome()

    times = []
    print('Getting driving times:')
    j = 0
    for dir in maps_url:
        browser.get(dir)
        maps = BeautifulSoup(browser.page_source, "html.parser")
        dom = etree.HTML(str(maps))
        if len(dom.xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]'))>0:
            times = times + [dom.xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')[0].text]

        else: 
            browser.get('https://www.google.com/maps/dir/'+ address.replace(' ','+') + '/'  + hikes.city_name[j]+',+CO')
            maps = BeautifulSoup(browser.page_source, "html.parser")
            dom = etree.HTML(str(maps))
            times = times + [dom.xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')[0].text]

            # times = times + ['n/a']
        j += 1
        print(str((round(j/len(maps_url) * 100, 1))) + ' % Complete')
        # print(times)
#     if add_den_address == 1:
#         times_den = []
    
#         for dir in maps_url_den:
#             browser.get(dir)
#             maps_den = BeautifulSoup(browser.page_source, "html.parser")
#             dom_den = etree.HTML(str(maps_den))
#             if len(dom_den.xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]'))>0:
#                 times_den = times_den + [dom_den.xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')[0].text]

#             else: 
#                 times_den = times_den + ['n/a']
#             # print(times_den)
#     else:
#         pass
    # hike_times = []

    hike_times = pd.DataFrame()

    hike_times['names'] = hikes.name
    hike_times['driving_time_from_home'] = times

    # print(hike_times)

    total = []
    for time in hike_times.driving_time_from_home:
        if time != 'n/a':
            time = time.split(' ')

            try:
                hr = int(time[0])
                mins = int(time[2])
                total = total + [hr*60 + mins]
            except(IndexError):
                if time [1] == 'hr':
                    hr = int(time[0])
                    mins = 0
                else:
                    hr = 0
                    mins = int(time[0])
                    
                total = total + [hr*60 + mins]
        else:
            total = total + [999]
        #print(total)

    hike_times['time_mins'] = total

    hike_times = hike_times.sort_values('time_mins')

    # print(hike_times)

#     hike_times_den = []

#     hike_times_den = pd.DataFrame()

#     hike_times_den['names'] = hikes.name
#     hike_times_den['driving_time_from_denver'] = times_den

    # print(hike_times_den)
#     if add_den_address == 1:
#         total_den = []
#         for time in hike_times_den.driving_time_from_denver:
#             if time != 'n/a':
#                 time = time.split(' ')

#                 try:
#                     hr = int(time[0])
#                     mins = int(time[2])
#                     total_den = total_den + [hr*60 + mins]
#                 except(IndexError):
#                     hr = int(time[0])
#                     mins = 0
#                     total_den = total_den + [hr*60 + mins]
#             else:
#                 total_den = total_den + [999]
#             #print(total)
#     else:
#         pass

    # hike_times_den['time_mins'] = total_den

    # hike_times_den = hike_times_den.sort_values('time_mins')

    # print(hike_times_den)

    full_hike_table = hike_times.merge(metadata_df, left_on = 'names', right_on = 'index')

    # len(hike_times)

    # metadata_df.to_csv('all_trails_data_sample.csv')

    # len(full_hike_table)

    # hike_times.to_csv('driving_times_from_home.csv')

    # hike_times_den.to_csv('driving_times_from_Citzen.csv')

    full_hike_table = full_hike_table.drop(columns = ['index','time_mins'])

    # full_hike_table.to_csv('hike_times_and_data.csv')

    # full_hike_table = full_hike_table.merge(hike_times_den)

    # full_hike_table = full_hike_table.drop(columns = ['time_mins'])

    all_hike_data = full_hike_table.merge(hikes, left_on = 'names', right_on = 'name')


    all_hike_data = all_hike_data.drop(columns = ['names','ID','state_id','length','slug','type', \
        '_geoloc', 'route_type', 'visitor_usage','area_id','area_slug','city_id',\
            'country_id','verified_map_id','activities','profile_photo_data','has_profile_photo',\
                'num_photos','units',\
        'is_private_property','duration_minutes_trail_running','created_at',\
            'country_name','duration_minutes_mountain_biking','duration_minutes_hiking',\
                'duration_minutes','duration_minutes_cycling','duration_minutes_cycling','objectID'])

    all_hike_data.index = all_hike_data.name

    all_hike_data.insert(18, 'last review', all_hike_data.pop('last review'))

    all_hike_data['elevation_gain'] = all_hike_data['elevation_gain'] * 3.28084
    
    if hike_day == 'Saturday' or hike_day == 'Sunday':
        all_hike_data = all_hike_data.drop(columns = ['hike_day_weather', 'clouds_hike_day', 'rain_hike_day'])
    else:
        all_hike_data = all_hike_data.rename(columns = {'hike_day_weather':hike_day+'_weather', 'clouds_hike_day':'% cloudy '+hike_day, 'rain_hike_day':'% chance rain '+hike_day})

    # all_hike_data = all_hike_data.drop(columns = ['name'])
    all_hike_data = all_hike_data.drop(columns = ['area_name_en','area_name_en-US'\
                                                  'country_name_en','country_name_en-US', 'city_name_en', \
                                                  'city_name_en-US','state_name_en', 'state_name_en-US',\
                                                  'name_en','name_en-US'])
    # all_hike_data.insert(1, 'driving_time_from_denver', all_hike_data.pop('driving_time_from_denver'))
    all_hike_data.insert(2, 'distance_miles', all_hike_data.pop('distance_miles'))
    all_hike_data.insert(9, 'trail_conditions', all_hike_data.pop('trail_conditions'))
    all_hike_data.insert(10, 'last hiked', all_hike_data.pop('last hiked'))
    all_hike_data.insert(5, 'difficulty_rating', all_hike_data.pop('difficulty_rating'))
    all_hike_data.insert(3, 'duration_hours', all_hike_data.pop('duration_hours'))
    all_hike_data.insert(4, 'elevation_gain', all_hike_data.pop('elevation_gain'))
    all_hike_data.insert(11, 'clouds_sat', all_hike_data.pop('clouds_sat'))
    all_hike_data.insert(12, 'clouds_sun', all_hike_data.pop('clouds_sun'))
    # all_hike_data.insert(12, '% cloudy ' + hike_day, all_hike_data.pop('% cloudy ' + hike_day))


    all_hike_data.elevation_gain = round(all_hike_data.elevation_gain,3)
    all_hike_data.duration_hours = round(all_hike_data.duration_hours,3)
    all_hike_data.distance_miles = round(all_hike_data.distance_miles,2)

    all_hike_data = all_hike_data.rename(columns = {'elevation_gain':'elevation_gain_ft','rain_sun':'% chance rain Sunday','rain_sat':'% chance rain Saturday','clouds_sat':'% cloudy Saturday','clouds_sun':'% cloudy Sunday'})

    all_hike_data['is_day_hike'] = np.where(all_hike_data['duration_hours']< 10 , True, False)

    # all_hike_data['is_14er'] = np.where(all_hike_data['elevation_gain_ft']>=14000, True, False)

    all_hike_data 

    all_hike_data.to_csv('complete_hike_data'+str(date.today())+'.csv')

    return all_hike_data