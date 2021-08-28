# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:38:28 2021

@author: saran
"""

#import json
#
#x = {
#  "page": 1,
#  "per_page": 30,
#  "total": True,
#  "total_pages": 100,
#  "data": [
#    {"title": "BMW 23", "story_title": 'lets talk about car'},
#    {"title": "", "story_title": 'lets talk about car'},
#    {"title": '', "story_title": ''}
#    
#  ]
#}
#
## convert into JSON:
#y = json.dumps(x)
#
## the result is a JSON string:
#print(y)
#json_y=json.loads(y)

def get_article_titel(author):
    import requests
    articles=[]
    page=1
    while(True):
        url='https://jsonmock.hackerank.com/api/articles?author='+author+'&page='+str(page)
        json_y=requests.get(url)
        if page==1:
            total_pages=json_y['total_pages']   
            
        data_len=len(json_y['data'])
        for article_record in range (0,data_len):
            title=json_y['data'][article_record]['title']
            story_title=json_y['data'][article_record]['story_title']
            if json_y['data'][article_record]['title']!='null':
                articles.append(title)
            elif json_y['data'][article_record]['title']!='null':
                articles.append(story_title)        
        print(articles)

        if page==total_pages:
            break
        else:
            page=page+1
            
    return(articles)
    