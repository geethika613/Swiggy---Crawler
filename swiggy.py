# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 10:39:26 2022

@author: geeth
"""

import json
import requests
import io
with io.open('kolkata.csv','w',encoding= 'utf-8') as f1:
    f1.write('name,area,totalRatingsString,deliveryTime,address,locality,cuisines,costForTwoString')


cookies = {
    '__SW': 'kORniPXqwk6B50rXMHxvLS34AvkfIlHW',
    '_device_id': 'c4ec54b4-1eb6-bc98-e600-171519cddad0',
    'fontsLoaded': '1',
    '_gcl_au': '1.1.1135771269.1658650286',
    '_ga': 'GA1.2.1872110656.1658650287',
    'WZRK_G': '1b320da349bf465f8a728bbae3a737f7',
    '_guest_tid': '6e109b23-7bf3-4efa-8b9d-759bf1c995de',
    '_sid': '1qa78ba4-26a2-4c36-b2b4-0f19e719f34a',
    '_gid': 'GA1.2.1487998414.1659242117',
    'WZRK_S_W86-ZZK-WR6Z': '%7B%22p%22%3A3%2C%22s%22%3A1659243465%2C%22t%22%3A1659243502%7D',
    '_gat_UA-53591212-4': '1',
}

headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__SW=kORniPXqwk6B50rXMHxvLS34AvkfIlHW; _device_id=c4ec54b4-1eb6-bc98-e600-171519cddad0; fontsLoaded=1; _gcl_au=1.1.1135771269.1658650286; _ga=GA1.2.1872110656.1658650287; WZRK_G=1b320da349bf465f8a728bbae3a737f7; _guest_tid=6e109b23-7bf3-4efa-8b9d-759bf1c995de; _sid=1qa78ba4-26a2-4c36-b2b4-0f19e719f34a; _gid=GA1.2.1487998414.1659242117; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A3%2C%22s%22%3A1659243465%2C%22t%22%3A1659243502%7D; _gat_UA-53591212-4=1',
    'if-none-match': 'W/"9839-Gred3sSLbm4wIS+E0ThgLqw7ws8"',
    'referer': 'https://www.swiggy.com/city/kolkata?page=2',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
}

params = {
    'page': '0',
    'ignoreServiceability': 'true',
    'lat': '22.5867',
    'lng': ' 88.4171',
    'pageType': 'SEE_ALL',
    'sortBy': 'RELEVANCE',
    'page_type': 'DESKTOP_SEE_ALL_LISTING',
}

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', params=params, cookies=cookies, headers=headers)
response = response.text
data = json.loads(response)
page_no = data['data']['pages']

dd = 0
for i in range(page_no):
   
    headers = {
        'authority': 'www.swiggy.com',
        '__fetch_req__': 'true',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__SW=kORniPXqwk6B50rXMHxvLS34AvkfIlHW; _device_id=c4ec54b4-1eb6-bc98-e600-171519cddad0; fontsLoaded=1; _gcl_au=1.1.1135771269.1658650286; _ga=GA1.2.1872110656.1658650287; WZRK_G=1b320da349bf465f8a728bbae3a737f7; _guest_tid=6e109b23-7bf3-4efa-8b9d-759bf1c995de; _sid=1qa78ba4-26a2-4c36-b2b4-0f19e719f34a; _gid=GA1.2.1487998414.1659242117; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A3%2C%22s%22%3A1659243465%2C%22t%22%3A1659243502%7D; _gat_UA-53591212-4=1',
        'if-none-match': 'W/"9839-Gred3sSLbm4wIS+E0ThgLqw7ws8"',
        'referer': 'https://www.swiggy.com/city/kolkata?page=2',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
    }

    params = {
        'page': dd,
        'ignoreServiceability': 'true',
        'lat': '22.5867',
        'lng': ' 88.4171',
        'pageType': 'SEE_ALL',
        'sortBy': 'RELEVANCE',
        'page_type': 'DESKTOP_SEE_ALL_LISTING',
    }

    response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', params=params, cookies=cookies, headers=headers)
    response = response.text
    dd = dd+1
    print('page no is'+str(dd)+'out of'+str(page_no))
    data1 = json.loads(response)
    data1 = data1['data']['cards']
    print(data1)
    for i in range(len(data1)):
        name = data1[i]['data']['data']['name']
        area = data1[i]['data']['data']['area']
        totalRatingsString = data1[i]['data']['data']['totalRatingsString']
        deliveryTime = data1[i]['data']['data']['deliveryTime']
        address = data1[i]['data']['data']['address']
        address = address.replace(',' ,';')
        locality = data1[i]['data']['data']['locality']
        cuisines = data1[i]['data']['data']['cuisines']
        cuisines = str(cuisines)
        cuisines = cuisines.replace(',','')
        costForTwoString = data1[i]['data']['data']['costForTwoString']
        scrapped_data = (name + ',' + area + ',' + totalRatingsString + ',' + str(deliveryTime) + ',' + address + ',' + locality + ',' + str(cuisines) + ',' + costForTwoString )
        with io.open('kolkata.csv','a' ,encoding = 'utf-8') as f2:
            f2.write(scrapped_data + '\n')
            f2.close()
            
   
   
    
  