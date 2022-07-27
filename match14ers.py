
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from selenium import webdriver

def get14erMatches(all_trails_14ers,co_14ers):

    all_trails_df = all_trails_14ers[:][:]

    # all_trails_df.name

    fourteeners = co_14ers[:][:]

    # fourteeners.to_csv('co_fourteener_data.csv')

    # all_trails_df.to_csv('all_trails_14ers.csv')

    # all_trails_df.insert(0, 'name', all_trails_df.pop('name'))

    # fourteeners['name'] = fourteeners.name.str.replace('Peak','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('and','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('Mt.','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('Peak','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('Trail','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('Mountain','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('of','')
    # fourteeners['name'] =fourteeners.trail_name.str.replace('the','')


    # browser = webdriver.Chrome()
    # browser.get('https://www.14ers.com/php14ers/14ers.php')

#     r = 1
#     while r < 59:
#         trail = browser.find_element_by_xpath('//*[@id="peakTable"]/tbody/tr['+str(r)+']/td[1]/div/a').text.strip()
#         r+=1
#         print(trail)


    fourteeners.peak_name = fourteeners.peak_name.str.replace('Mt.','Mount')
    fourteener_names = list(fourteeners.peak_name)
    
    

    all_trails_names = list(all_trails_df.name)

    # fourteener_names

    mat2 = []

    for i in all_trails_names: #names in smaller dataset to compare and match
    #get closest match of `name` compared to larger data `member_names`
        mat2.append(process.extract(i, fourteener_names, limit=1))


    mat3 = []
    for mat in mat2:
        mat3.append(mat[0][0])

    # print(mat3)

    fourteener_name_matches = pd.DataFrame()

    fourteener_name_matches['names'] = all_trails_names

    fourteener_name_matches['matches2'] = mat3
    
    # print(fourteener_name_matches)
    
    all_trails_df['matches'] = mat3
    # print(fourteener_name_matches)
#     fourteeners = fourteeners.merge(fourteener_name_matches, left_on = 'trail_name', right_on = 'matches2')

    # fourteeners = fourteeners.drop_duplicates(subset = ['names'])
    
    # all_trails_df = all_trails_df.reset_index(drop = True)
    # print(all_trails_df)
    # print(fourteeners)
    all_trails_merge = all_trails_df.merge(fourteeners[['peak_name','trail_name','class_num','elevation_ft','rank','exposure','rockfall','route-finding','commitment']], left_on = 'matches', right_on = 'peak_name', how = 'left')
    all_trails_merge = all_trails_merge.set_index('name')
    # all_trails_merge = all_trails_merge.drop(columns = ['names'])
    return all_trails_merge