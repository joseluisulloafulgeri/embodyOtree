import pandas as pd
import numpy as np
import json
import ast
import csv
import os
import sys
from pathlib import Path
from random import randint
import random
import requests  # pip3 install requests
from pprint import pprint


# GET = requests.get
# POST = requests.post
#
# # if using Heroku, change this to https://YOURAPP.herokuapp.com
# SERVER_URL = 'http://localhost:8000'
# REST_KEY = ''  # fill this later
#
# def call_api(method, *path_parts, **params) -> dict:
#     path_parts = '/'.join(path_parts)
#     url = f'{SERVER_URL}/api/{path_parts}/'
#     resp = method(url, json=params, headers={'otree-rest-key': REST_KEY})
#     if not resp.ok:
#         msg = (
#             f'Request to "{url}" failed '
#             f'with status code {resp.status_code}: {resp.text}'
#         )
#         raise Exception(msg)
#
#     return resp.json()
#
#
# #data = call_api(GET, 'sessions', 'ez8qjxjg', participants_codes=['3s01ruvl'])
# data = call_api(GET, 'participant_vars', 'ez8qjxjg', vars=dict(Code='3s01ruvl'))
# pprint(data)

def random_with_N_digits(p,n):
    random.seed(p) # defines same digit for same participant on every run
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


filename = sys.argv[1]

mydata = pd.read_csv(filename)
temp = mydata.loc[:, mydata.columns.str.startswith('embodyOtree..*.player.pyField')]

participantCode =  mydata['participant.code'].values


subjects_path = Path.cwd() / 'subjects'
subjects_path.mkdir(parents=True, exist_ok=True)

for p in participantCode:
    id = random_with_N_digits(p,6) #random digits because thats what matlab wants
    temp = mydata.loc[mydata['participant.code'] == p]
    #temp = temp[~temp['player.rand_page_sequence'].isnull()]
    # Huge mess but it works
    presentation = temp.loc[:, temp.columns.str.endswith('player.rand_page_sequence')].copy()
    presentation.dropna(how='all', axis=1, inplace=True)
    presentation = presentation.values
    presentation = np.array2string(presentation, precision=2, separator=',',suppress_small=False)
    presentation = presentation.replace("[","")
    presentation = presentation.replace("]","")
    presentation = presentation.replace("'", "")
    presentation = presentation.replace(" ", "")
    presentation = presentation.split(",")
    presentation = [value for value in presentation if len(value) <=2] #workaround, only valid for pagenumbers 0-99
    print(presentation)
    presentation = list(map(int, presentation))
    presentation =  [x-1 for x in presentation] #matlab expects values from 0 to 13 , not 1 to 14
    presentation = ','.join(str(x) for x in presentation)
    presentation = presentation.replace(",","\n")



    temp = temp.loc[:, temp.columns.str.contains('player.pyField') ]
    temp.dropna(how='all', axis=1, inplace=True)
    temp.columns = temp.columns.str.rstrip('\.\d*?\.')

    participant_path = Path.cwd() / subjects_path / str(id)
    participant_path.mkdir(parents=True, exist_ok=True)
    for index, i in enumerate(temp):
        print(index)
        if not temp[i].empty:
            df = temp[i].dropna().to_dict()
            for i in df:
                d = json.loads(df[i])
                df = pd.DataFrame.from_dict(d, orient="index").T
                arrX = df['arrX']
                arrY = df['arrY']
                arrTime = df['arrTime']
                arrXD = df['arrXD']
                arrYD = df['arrYD']
                arrTimeD = df['arrTimeD']
                arrMD = df['arrMD']
                arrMU = df['arrMU']
                mytext = ""

                if arrX.size > 0:
                    for i in range(0,arrX.size) :
                        mytext = mytext + str(arrTime[i]) + "," + str(arrX[i]) + "," +  str(arrY[i]) + "\n"

                mytext = mytext + "-1,-1,-1\n";

                if arrY.size > 0:
                    for i in range(0,arrY.size) :
                        mytext = mytext + str(arrTimeD[i]) + "," + str(arrXD[i]) + "," +  str(arrYD[i]) + "\n"

                mytext = mytext + "-1,-1,-1\n";

                if arrMD.size > 0:
                    for i in range(0,arrMD.size):
                        mytext = mytext + str(arrMD[i]) + ",,\n"

                mytext = mytext + "-1,-1,-1\n";

                if arrMU.size > 0:
                    for i in range(0,arrMU.size):
                        mytext = mytext + str(arrMU[i]) + ",,\n"

                mytext = mytext.replace("NaN", "")
                mytext = mytext.replace("nan", "")
                print(mytext, file = open(participant_path / (str(index) + '.csv'), 'w'))
                print(presentation, file=open(participant_path / "presentation.txt", 'w'))
                print(p, file=open(participant_path / "participant_id.txt", 'w'))