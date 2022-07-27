import requests
from requests.structures import CaseInsensitiveDict
import json
import pandas as pd
import numpy as np

def getall14ers():
    url = "https://9ioacg5nhe-dsn.algolia.net/1/indexes/alltrails_index3/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.6)%3B%20Browser"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Host"] = "9ioacg5nhe-dsn.algolia.net"
    headers["Origin"] = "https://www.alltrails.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = "https://www.alltrails.com/"
    headers["Content-Length"] = "3423"
    headers["x-algolia-application-id"] = "9IOACG5NHE"
    headers["x-algolia-api-key"] = "63a3cf94e0042b9c67abf0892fc1d223"

    data = '{"query":"","hitsPerPage":1000,"analyticsTags":["auth:pro","platform:web","origin:explore","actor:user","lang:en","hastext:false"],"attributesToRetrieve":["ID","_geoloc","activities","area_id","area_name","area_slug","avg_rating","city_id","city_name","country_id","country_name","created_at","difficulty_rating","duration_minutes","duration_minutes_cycling","duration_minutes_hiking","duration_minutes_mountain_biking","duration_minutes_trail_running","elevation_gain","filters","has_profile_photo","is_closed","is_private_property","length","name","num_photos","num_reviews","photo_count","popularity","profile_photo_data","route_type","slug","state_id","state_name","type","units","user","verified_map_id","visitor_usage","area_name_en-US","area_name_en","city_name_en-US","city_name_en","country_name_en-US","country_name_en","state_name_en-US","state_name_en","name_en-US","name_en"],"attributesToHighlight":[],"filters":"((length>=0)) AND ((elevation_gain>=0)) AND (objectID:trail-10016676 OR objectID:trail-10002885 OR objectID:trail-10029508 OR objectID:trail-10016365 OR objectID:trail-10344041 OR objectID:trail-10700371 OR objectID:trail-10351577 OR objectID:trail-10111237 OR objectID:trail-10111784 OR objectID:trail-10031162 OR objectID:trail-10267591 OR objectID:trail-10001851 OR objectID:trail-10294852 OR objectID:trail-10342567 OR objectID:trail-10031206 OR objectID:trail-10030643 OR objectID:trail-10240983 OR objectID:trail-10240976 OR objectID:trail-10010523 OR objectID:trail-10308161 OR objectID:trail-10032876 OR objectID:trail-10325811 OR objectID:trail-10009879 OR objectID:trail-10111303 OR objectID:trail-10264209 OR objectID:trail-10330535 OR objectID:trail-10254059 OR objectID:trail-10112141 OR objectID:trail-10028367 OR objectID:trail-10283030 OR objectID:trail-10299934 OR objectID:trail-10111779 OR objectID:trail-10294854 OR objectID:trail-10111786 OR objectID:trail-10025010 OR objectID:trail-10348134 OR objectID:trail-10031838 OR objectID:trail-10351646 OR objectID:trail-10351648 OR objectID:trail-10015790 OR objectID:trail-10296274 OR objectID:trail-10043013 OR objectID:trail-10351656 OR objectID:trail-10297092 OR objectID:trail-10035470 OR objectID:trail-10241866 OR objectID:trail-10003461 OR objectID:trail-10018317 OR objectID:trail-10351771 OR objectID:trail-10111316 OR objectID:trail-10028358 OR objectID:trail-10342371 OR objectID:trail-10260451 OR objectID:trail-10347639 OR objectID:trail-10351776 OR objectID:trail-10260452 OR objectID:trail-10351778 OR objectID:trail-10351781 OR objectID:trail-10351783 OR objectID:trail-10351782 OR objectID:trail-10031144 OR objectID:trail-10292179 OR objectID:trail-10351785 OR objectID:trail-10111437 OR objectID:trail-10033945 OR objectID:trail-10029518 OR objectID:trail-10298314 OR objectID:trail-10351795 OR objectID:trail-10351808 OR objectID:trail-10111967 OR objectID:trail-10035463 OR objectID:trail-10111944 OR objectID:trail-10242049 OR objectID:trail-10351815 OR objectID:trail-10351817 OR objectID:trail-10351818 OR objectID:trail-10351820 OR objectID:trail-10351821 OR objectID:trail-10298549 OR objectID:trail-10038056 OR objectID:trail-10111835 OR objectID:trail-10303467 OR objectID:trail-10039102 OR objectID:trail-10303466 OR objectID:trail-10017018 OR objectID:trail-10351828 OR objectID:trail-10351829 OR objectID:trail-10267496 OR objectID:trail-10041188)","responseFields":["hits","hitsPerPage","nbHits"]}'

    resp = requests.post(url, headers=headers, data=data)
    # print(resp.status_code)

    all14 = json.loads(resp.content)
    df_all14 = pd.DataFrame.from_dict(all14['hits'])

    return df_all14

def getshortlist():

    url = "https://9ioacg5nhe-dsn.algolia.net/1/indexes/alltrails_index3/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.6)%3B%20Browser"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Host"] = "9ioacg5nhe-dsn.algolia.net"
    headers["Origin"] = "https://www.alltrails.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = "https://www.alltrails.com/"
    headers["Content-Length"] = "2686"
    headers["x-algolia-application-id"] = "9IOACG5NHE"
    headers["x-algolia-api-key"] = "63a3cf94e0042b9c67abf0892fc1d223"
    data = '{"query":"","hitsPerPage":1000,"analyticsTags":["auth:pro","platform:web","origin:explore","actor:user","lang:en","hastext:false"],"attributesToRetrieve":["ID","_geoloc","activities","area_id","area_name","area_slug","avg_rating","city_id","city_name","country_id","country_name","created_at","difficulty_rating","duration_minutes","duration_minutes_cycling","duration_minutes_hiking","duration_minutes_mountain_biking","duration_minutes_trail_running","elevation_gain","filters","has_profile_photo","is_closed","is_private_property","length","name","num_photos","num_reviews","photo_count","popularity","profile_photo_data","route_type","slug","state_id","state_name","type","units","user","verified_map_id","visitor_usage","area_name_en","city_name_en","country_name_en","state_name_en","name_en"],"attributesToHighlight":[],"filters":"((length>=0)) AND ((elevation_gain>=0)) AND (objectID:trail-10344041 OR objectID:trail-10002885 OR objectID:trail-10260451 OR objectID:trail-10351821 OR objectID:trail-10351817 OR objectID:trail-10294852 OR objectID:trail-10017018 OR objectID:trail-10035463 OR objectID:trail-10005393 OR objectID:trail-10031135 OR objectID:trail-10294792 OR objectID:trail-10239233 OR objectID:trail-10043013 OR objectID:trail-10028431 OR objectID:trail-10035470 OR objectID:trail-10009934 OR objectID:trail-10279945 OR objectID:trail-10235969 OR objectID:trail-10031144 OR objectID:trail-10280978 OR objectID:trail-10030644 OR objectID:trail-10016671 OR objectID:trail-10018317 OR objectID:trail-10111944 OR objectID:trail-10001851 OR objectID:trail-10340507 OR objectID:trail-10253874 OR objectID:trail-10273673 OR objectID:trail-10239674 OR objectID:trail-10299934 OR objectID:trail-10259768 OR objectID:trail-10010211 OR objectID:trail-10551515 OR objectID:trail-10026684 OR objectID:trail-10015640 OR objectID:trail-10017023 OR objectID:trail-10026711 OR objectID:trail-10041185 OR objectID:trail-10235681 OR objectID:trail-10111237 OR objectID:trail-10241649 OR objectID:trail-10258958 OR objectID:trail-10035010 OR objectID:trail-10277791 OR objectID:trail-10253281 OR objectID:trail-10295745 OR objectID:trail-10009207 OR objectID:trail-10307880 OR objectID:trail-10003461 OR objectID:trail-10035011 OR objectID:trail-10014975 OR objectID:trail-10235688 OR objectID:trail-10005478 OR objectID:trail-10241141 OR objectID:trail-10037015 OR objectID:trail-10000215 OR objectID:trail-10008249 OR objectID:trail-10269270 OR objectID:trail-10034964 OR objectID:trail-10746249 OR objectID:trail-10256323 OR objectID:trail-10034993 OR objectID:trail-10263807 OR objectID:trail-10031833 OR objectID:trail-10289334)","responseFields":["hits","hitsPerPage","nbHits"]}'
    resp_sl = requests.post(url, headers=headers, data=data)
    
    # print('Response Status: ' + str(resp_sl.status_code))
    
    sl = json.loads(resp_sl.content)
    sl_df = pd.DataFrame.from_dict(sl['hits'])

    return sl_df

def gettop14ers():

    url = "https://9ioacg5nhe-dsn.algolia.net/1/indexes/alltrails_index3/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.6)%3B%20Browser"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Host"] = "9ioacg5nhe-dsn.algolia.net"
    headers["Origin"] = "https://www.alltrails.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = "https://www.alltrails.com/"
    headers["Content-Length"] = "1614"
    headers["x-algolia-application-id"] = "9IOACG5NHE"
    headers["x-algolia-api-key"] = "63a3cf94e0042b9c67abf0892fc1d223"

    data = '{"query":"","hitsPerPage":1000,"analyticsTags":["auth:pro","platform:web","origin:explore","actor:user","lang:en","hastext:false"],"attributesToRetrieve":["ID","_geoloc","activities","area_id","area_name","area_slug","avg_rating","city_id","city_name","country_id","country_name","created_at","difficulty_rating","duration_minutes","duration_minutes_cycling","duration_minutes_hiking","duration_minutes_mountain_biking","duration_minutes_trail_running","elevation_gain","filters","has_profile_photo","is_closed","is_private_property","length","name","num_photos","num_reviews","photo_count","popularity","profile_photo_data","route_type","slug","state_id","state_name","type","units","user","verified_map_id","visitor_usage","area_name_en-US","area_name_en","city_name_en-US","city_name_en","country_name_en-US","country_name_en","state_name_en-US","state_name_en","name_en-US","name_en"],"attributesToHighlight":[],"filters":"((length>=0)) AND ((elevation_gain>=0)) AND (objectID:trail-10031144 OR objectID:trail-10035463 OR objectID:trail-10035470 OR objectID:trail-10111237 OR objectID:trail-10017018 OR objectID:trail-10018317 OR objectID:trail-10254059 OR objectID:trail-10294852 OR objectID:trail-10001851 OR objectID:trail-10111944 OR objectID:trail-10242049 OR objectID:trail-10351817 OR objectID:trail-10351821 OR objectID:trail-10303466 OR objectID:trail-10351781 OR objectID:trail-10111316 OR objectID:trail-10260451 OR objectID:trail-10351771 OR objectID:trail-10043013 OR objectID:trail-10015790 OR objectID:trail-10344041 OR objectID:trail-10002885)","responseFields":["hits","hitsPerPage","nbHits"]}'


    resp_top14 = requests.post(url, headers=headers, data=data)

    # print(resp_top14.status_code)

    top14 = json.loads(resp_top14.content)
    top14_df = pd.DataFrame.from_dict(top14['hits'])

    return top14_df

def getallco():

    url = "https://9ioacg5nhe-dsn.algolia.net/1/indexes/alltrails_index3/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.6)%3B%20Browser"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Host"] = "9ioacg5nhe-dsn.algolia.net"
    headers["Origin"] = "https://www.alltrails.com"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    headers["Connection"] = "keep-alive"
    headers["Referer"] = "https://www.alltrails.com/"
    headers["Content-Length"] = "4422"
    headers["x-algolia-application-id"] = "9IOACG5NHE"
    headers["x-algolia-api-key"] = "63a3cf94e0042b9c67abf0892fc1d223"

    data = '{"query":"","hitsPerPage":1000,"analyticsTags":["auth:pro","platform:web","origin:explore","actor:user","lang:en","hastext:false"],"attributesToRetrieve":["ID","_geoloc","activities","area_id","area_name","area_slug","avg_rating","city_id","city_name","country_id","country_name","created_at","difficulty_rating","duration_minutes","duration_minutes_cycling","duration_minutes_hiking","duration_minutes_mountain_biking","duration_minutes_trail_running","elevation_gain","filters","has_profile_photo","is_closed","is_private_property","length","name","num_photos","num_reviews","photo_count","popularity","profile_photo_data","route_type","slug","state_id","state_name","type","units","user","verified_map_id","visitor_usage","area_name_en-US","area_name_en","city_name_en-US","city_name_en","country_name_en-US","country_name_en","state_name_en-US","state_name_en","name_en-US","name_en"],"attributesToHighlight":[],"filters":"((length>=0)) AND ((elevation_gain>=0)) AND (objectID:trail-10035463 OR objectID:trail-10017023 OR objectID:trail-10031135 OR objectID:trail-10031195 OR objectID:trail-10111369 OR objectID:trail-10294792 OR objectID:trail-10031144 OR objectID:trail-10035470 OR objectID:trail-10028431 OR objectID:trail-10272445 OR objectID:trail-10033973 OR objectID:trail-10239233 OR objectID:trail-10338270 OR objectID:trail-10287597 OR objectID:trail-10009934 OR objectID:trail-10235969 OR objectID:trail-10279945 OR objectID:trail-10017284 OR objectID:trail-10005400 OR objectID:trail-10043052 OR objectID:trail-10351771 OR objectID:trail-10344041 OR objectID:trail-10043013 OR objectID:trail-10015790 OR objectID:trail-10002885 OR objectID:trail-10351817 OR objectID:trail-10351781 OR objectID:trail-10303466 OR objectID:trail-10242049 OR objectID:trail-10111316 OR objectID:trail-10041188 OR objectID:trail-10351821 OR objectID:trail-10260451 OR objectID:trail-10267591 OR objectID:trail-10351820 OR objectID:trail-10294852 OR objectID:trail-10029508 OR objectID:trail-10017018 OR objectID:trail-10299934 OR objectID:trail-10239674 OR objectID:trail-10273673 OR objectID:trail-10253874 OR objectID:trail-10111944 OR objectID:trail-10018317 OR objectID:trail-10001851 OR objectID:trail-10016671 OR objectID:trail-10691141 OR objectID:trail-10005270 OR objectID:trail-10259768 OR objectID:trail-10010211 OR objectID:trail-10551515 OR objectID:trail-10026684 OR objectID:trail-10015640 OR objectID:trail-10028367 OR objectID:trail-10111732 OR objectID:trail-10015677 OR objectID:trail-10258519 OR objectID:trail-10263583 OR objectID:trail-10291251 OR objectID:trail-10031203 OR objectID:trail-10005393 OR objectID:trail-10041185 OR objectID:trail-10500140 OR objectID:trail-10042110 OR objectID:trail-10037040 OR objectID:trail-10280978 OR objectID:trail-10013078 OR objectID:trail-10031833 OR objectID:trail-10263807 OR objectID:trail-10034993 OR objectID:trail-10029504 OR objectID:trail-10297621 OR objectID:trail-10030644 OR objectID:trail-10026727 OR objectID:trail-10028359 OR objectID:trail-10014975 OR objectID:trail-10000215 OR objectID:trail-10233886 OR objectID:trail-10025010 OR objectID:trail-10254059 OR objectID:trail-10258717 OR objectID:trail-10035011 OR objectID:trail-10307880 OR objectID:trail-10307878 OR objectID:trail-10003461 OR objectID:trail-10340324 OR objectID:trail-10338387 OR objectID:trail-10521970 OR objectID:trail-10030668 OR objectID:trail-10026673 OR objectID:trail-10026688 OR objectID:trail-11017114 OR objectID:trail-10295745 OR objectID:trail-10289334 OR objectID:trail-10253281 OR objectID:trail-10009207 OR objectID:trail-10696890 OR objectID:trail-10696887 OR objectID:trail-10241461 OR objectID:trail-10241460 OR objectID:trail-10264208 OR objectID:trail-10277791 OR objectID:trail-10035010 OR objectID:trail-10258958 OR objectID:trail-10241649 OR objectID:trail-10720030 OR objectID:trail-10284205 OR objectID:trail-10293307 OR objectID:trail-10111237 OR objectID:trail-10026703 OR objectID:trail-10235681 OR objectID:trail-10483472 OR objectID:trail-10038052 OR objectID:trail-10235688 OR objectID:trail-10026711 OR objectID:trail-10256323 OR objectID:trail-10241141 OR objectID:trail-10359957 OR objectID:trail-10235626 OR objectID:trail-10037015 OR objectID:trail-10005478 OR objectID:trail-10008249 OR objectID:trail-10340507 OR objectID:trail-10269270 OR objectID:trail-10746249 OR objectID:trail-10034964)","responseFields":["hits","hitsPerPage","nbHits"]}'

    resp_co = requests.post(url, headers=headers, data=data)

    # print(resp_co.status_code)

    co = json.loads(resp_co.content)
    co_df = pd.DataFrame.from_dict(co['hits'])
    
    sl_df = getshortlist()
    
    df = pd.merge(co_df, sl_df, on=['name'], how='left', indicator='Exist')
    df['Exist'] = np.where(df.Exist == 'both', True, False)
    # print (df)
    # df[df.Exist == 0]

    co_df['bucket'] = df.Exist.astype(int)

    return co_df