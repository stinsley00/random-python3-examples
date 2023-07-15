#            **********  ******
#        **************************
#      ******************************
#    ****    ****            ****    **
#    ****  ****                ****  **
#  **********                    ********
#  **********  ****        ****  ********
# ************      **    **      ********
# ************      **    **      ********
# ************      **    **    **********
# **************    ********    **********
#  ************        **      ********
#    ************    ******  **********
#    ****************      ************
#      **************      **********
#        **************************
#            ********************
#                **************
#                  **********
#                      ****
# moufasa file promotion "it works!"
# @author stinsley

###########
# imports #
###########
import json
import os
import stat
import requests
from datetime import datetime
import shutil

###########
# Configs #
###########

rustPath = '/mnt/old array/Movies/Movies/Movies/'
flashPath = '/home/wopr/Videos/movies/'
promotionSpaceAvail = 0.0
# api_key as a str
api_key = 'xxxxxxxxxxxxx'
# host ip as str
host_ip = '192.168.x.x'
port = 'xxxx'


def get_arnold():
    url = 'http://' + host_ip + ':' + port + '/api/v2?apikey=' + api_key + '&cmd=arnold'
    response = requests.get(url)
    data = json.loads(response.text)
    print(data['response']['data'])


def get_usage():
    # https://github.com/Tautulli/Tautulli/blob/master/API.md

    url = 'http://' + host_ip + ':' + port + '/api/v2?apikey=' + api_key + '&cmd=get_home_stats'
    response = requests.get(url)

    data = json.loads(response.text)
    data = data['response']['data']
    latest_films = list()
    for x in range(len(data)):
        if data[x]['stat_id'] == 'top_movies':
            for y in range(len(data[x]['rows'])):
                rating_key = data[x]['rows'][y]['rating_key']
                # guid = data[x]['rows'][y]['guid']

                # last_play = datetime.fromtimestamp(data[x]['rows'][y]['last_play'])

                # total_plays = data[x]['rows'][y]['total_plays']

                # print(total_plays)

                # title = data[x]['rows'][y]['title']

                #this isn't populated on my system
                # users = data[x]['rows'][y]['user']
                latest_films.append(rating_key)

    for i in latest_films:
        url2 = 'http://' + host_ip + ':' + port + '/api/v2?apikey=' + api_key + '&cmd=get_metadata&rating_key=' \
               + str(i)
        response = requests.get(url2)
        data = json.loads(response.text)
        data = data['response']['data']
        if data:
            print(data['media_info'][0]['parts'][0]['file'])  # full path to file
            print("file sz in bytes: " + data['media_info'][0]['parts'][0]['file_size'])  # bytes

        # if data['media_info'][0]['parts'][0]['file'] in rustPath:
        # check if in rust path, get available space, mv from rust path to flash path
        # else compare files in flash path and rust path to see who gets demoted
        # else else demote / promote as needed, latest list wins, fill space as required.
        # fill disk as necessary 2165776636

    user_stats_url = 'http://' + host_ip + ':' + port + '/api/v2?apikey=' + api_key + '&cmd=get_library_user_stats&section_id=1'
    # whatever sectionid your movie folder is


if __name__ == '__main__':
    get_arnold()
    get_usage()

