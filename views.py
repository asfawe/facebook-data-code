from django.shortcuts import render
from accounts.models import Friend, Profile
from post.models import Tag, Like, Post
import pandas as pd
import numpy as np
import datetime
import json

def dataview(request):
    friendTemp = pd.DataFrame(list(Friend.objects.all().values()))
    profileTemp = pd.DataFrame(list(Profile.objects.all().values()))
    tagTemp = pd.DataFrame(list(Tag.objects.all().values()))
    likeTemp = pd.DataFrame(list(Like.objects.all().values()))
    postFriendTemp = pd.DataFrame(list(Post.objects.all().values()))
    
    # print(dict(friendTemp['created_at'].value_counts().sort_index()))
    # dictfriendTemp = dict(friendTemp['created_at'].value_counts().sort_index())
    dictfriendTemp = {
        '2020-04-02':10,
        '2020-04-03':11,
        '2020-04-04':15,
        '2020-04-05':20,
        '2020-04-06':100,
        '2020-04-07':120,
        '2020-04-08':151,
        '2020-04-09':152,
        '2020-04-10':156,
    }
    
    dictprofileTemp = profileTemp['gender'].value_counts().sort_values()
    # friendTemp.to_csv('friendTemp.csv', mode='w')
    # profileTemp.to_csv('profileTemp.csv', mode='w')
    # tagTemp.to_csv('tagTemp.csv', mode='w')
    # likeTemp.to_csv('likeTemp.csv', mode='w')
    # postFriendTemp.to_csv('postFriendTemp.csv', mode='w')
    
    # dictpostFriendTemp = postFriendTemp['created_at'].str[:10].value_counts().sort_index()
    
    with open('testdb.json', 'r', encoding='UTF-8') as json_file:
        data = json_file.read()
        json_data = json.loads(data)
    
    json_data[str(datetime.datetime.now().strftime('%Y-%m-%d'))] = str(profileTemp['id'].count())
    
    with open("testdb.json", "w", encoding='UTF-8') as f:
        json.dump(json_data, f)
    
    dictpostFriendTemp = postFriendTemp['created_at'].astype(str).str[:10].value_counts().sort_index()
    # print(dictpostFriendTemp)
        
    return render(request, 'data/dataview.html', {
        'dictfriendTemp':dictfriendTemp,
        'dictprofileTemp':dictprofileTemp,
        'dictpostFriendTemp':dictpostFriendTemp,
        'json_data':json_data,
    })










