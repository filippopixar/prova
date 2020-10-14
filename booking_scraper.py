#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:33:57 2020

@author: filippo
"""
import os
import lxml
import requests
from bs4 import BeautifulSoup
import re



URL = 'https://www.booking.com/searchresults.it.html?label=gen173nr-1DCAEoggI46AdIM1gEaHGIAQGYAQm4AQfIAQ3YAQPoAQGIAgGoAgO4AuTOiPcFwAIB0gIkOTQ2MmE5NjQtYWI0OS00N2MzLWIxZmUtMzFjOGM3Njg4NDRi2AIE4AIB&sid=dd804f9dcf807ae994f5278b630ae101&tmpl=searchresults&checkin_month=8&checkin_monthday=8&checkin_year=2020&checkout_month=8&checkout_monthday=16&checkout_year=2020&class_interval=1&dest_id=-114787&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&lang=it&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&soz=1&src=index&src_elem=sb&srpvid=a07959b57094004c&ss=Catania&ss_all=0&ssb=empty&sshis=0&ssne=Catania&ssne_untouched=Catania&top_ufis=1&lang_click=top&cdl=en-gb&lang_changed=1&nflt='
page = requests.get(URL)

soup = BeautifulSoup(page.content,"lxml")

results = soup.find(id = 'hotellist_inner')

res_names = results.find_all(class_ = 'sr-hotel__name')

names = []
for res in res_names:
    name = re.search('>\n(.*)\n<', str(res))
    names.append(name[1])
    
a = results.prettify()
text_file = open("sampleee.txt", "wt")
n = text_file.write(a)
text_file.close()
    
res_prices = results.find(class_="sr_item_content sr_item_content_slider_wrapper ")

# names = []
# for res in res_names:
#     name = re.search('>\n(.*)\n<', str(res))
#     names.append(name[1])


#%%


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

URL = 'https://www.booking.com/searchresults.it.html?label=gen173nr-1DCAEoggI46AdIM1gEaHGIAQGYAQm4AQfIAQ3YAQPoAQGIAgGoAgO4AuTOiPcFwAIB0gIkOTQ2MmE5NjQtYWI0OS00N2MzLWIxZmUtMzFjOGM3Njg4NDRi2AIE4AIB&sid=dd804f9dcf807ae994f5278b630ae101&tmpl=searchresults&checkin_month=8&checkin_monthday=8&checkin_year=2020&checkout_month=8&checkout_monthday=16&checkout_year=2020&class_interval=1&dest_id=-114787&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&lang=it&no_rooms=1&offset=0&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&soz=1&src=index&src_elem=sb&srpvid=a07959b57094004c&ss=Catania&ss_all=0&ssb=empty&sshis=0&ssne=Catania&ssne_untouched=Catania&top_ufis=1&lang_click=top&cdl=en-gb&lang_changed=1&nflt='

driver = webdriver.Chrome("/Users/filippo/Desktop/chromedriver-2")

driver.implicitly_wait(30)
driver.get(URL)

python_button = driver.find_element_by_id('hotellist_inner') 


soup=BeautifulSoup(driver.page_source, 'lxml')

results = soup.find(id = 'hotellist_inner')

res_names = results.find_all(class_ = 'sr-hotel__name')

res_prices = results.find_all(class_ = 'sr_item_content sr_item_content_slider_wrapper')

#res_cancel = results.find_all(class_ = 'sr_room_reinforcement e2e-free-cancellation')

names = []
for res in res_names:
    name = re.search('>\(.*)\n<', str(res))
    names.append(name[1])






