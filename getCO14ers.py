from selenium import webdriver
import re
from bs4 import BeautifulSoup
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def getallCO14erData():
    
    url_path = list(range(10001,10054))+list(range(10063,10067))

    name = []
    class_num = []
    exposure = []
    rockfall = []
    route_finding = []
    commitment= []
    elevation_ft =[]
    rank = []
    peak_name = []
    i = 1
    r = 0
    urls14ers = []

    while r < 57:
        urls14ers.append('https://www.14ers.com/routelist.php?peakid='+str(url_path[r]))
        r += 1

    browser = webdriver.Chrome()
    
    print('Getting 14er Data...')
    
    for link in urls14ers:

        browser.get(link)

        fourteen = BeautifulSoup(browser.page_source, 'html.parser')

        name.append(fourteen.find('h1').text.split('| ')[0].strip())

        rank.append(i)

        fourteen.find('h1').text.split('| ')[0].strip()

        # print(name)
        # class_num.append(browser.find_element_by_xpath('//*[@id="routeResults"]/tbody/tr[2]/td[6]/span').text)
        # print(class_num)


        risks = fourteen.find(id = 'routeriskinfo_1').text


        risks_spl = re.split('Exposure:|Rockfall| Potential:|Route-Finding: |Commitment:',risks)

        exposure.append(risks_spl[1].strip())
        rockfall.append(risks_spl[3].strip())
        route_finding.append(risks_spl[4].strip())
        commitment.append(risks_spl[5].strip())

        i += 1
        # print(rockfall)

    fourteener_df_1 = pd.DataFrame(list(zip(name, rank, exposure, rockfall, route_finding, commitment)), \
                                 columns = ['trail_name','rank','exposure','rockfall','route-finding','commitment'])

    fourteener_df_1

    driver = webdriver.Chrome()
    driver.get('https://www.14ers.com/routes.php')
    n = 1
    elevation_ft = []
    peak_name = []
    class_num = []
    while n <58:
        elevation_ft.append(int(driver.find_element_by_xpath('//*[@id="peakTable"]/tbody/tr['+str(n)+']/td[6]').text.replace("'","").replace(',','')))
        peak_name.append(driver.find_element_by_xpath('//*[@id="peakTable"]/tbody/tr['+str(n)+']/td[1]/div/a').text.strip())
        class_num.append(driver.find_element_by_xpath('//*[@id="peakTable"]/tbody/tr['+str(n)+']/td[3]/span[2]').text.strip())
        n+=1

    fourteener_df_2 = pd.DataFrame(list(zip(peak_name,elevation_ft,class_num)), \
                                 columns = ['peak_name', 'elevation_ft','class_num'])


    peaks = list(fourteener_df_2.peak_name)
    trails = list(fourteener_df_1.trail_name)

    peaks = [s.replace('Peak','') for s in peaks]
    peaks = [m.replace('Mt.','') for m in peaks]
    # fourteeners['name'] =fourteeners.trail_name.str.replace('and','')
        # fourteeners['name'] =fourteeners.trail_name.str.replace('Mt.','')

    mat = []

    for i in peaks: #names in smaller dataset to compare and match
    #get closest match of `name` compared to larger data `member_names`
        mat.append(process.extract(i, trails, limit=1))

    matched = []
    for m in mat:
        matched.append(m[0][0])

    fourteener_name_matches = pd.DataFrame()

    fourteener_name_matches['trails'] = matched

    fourteener_name_matches['peak_matches'] = fourteener_df_2.peak_name

    fourteener_df_2['trail_matches'] = matched

    # fourteener_df_1 = fourteener_df_1.drop(columns = 'matches')
    fourteener_df_1 = fourteener_df_1.drop_duplicates(subset = 'trail_name')

    matched_14er_df = fourteener_df_2.merge(fourteener_df_1, right_on = 'trail_name', left_on = 'trail_matches')

    matched_14er_df = matched_14er_df.drop(columns = 'trail_matches')

    return matched_14er_df