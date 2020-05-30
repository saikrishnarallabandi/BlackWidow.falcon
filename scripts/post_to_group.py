#!usr/bin/env python
# Program to mine data from your own facebook account

import json
import facebook
import os, sys
import random

token = os.environ.get('FACEBOOK_TOKEN')
group_id = str(os.environ.get('THOPGANG_GROUP_ID'))
timestamp = str(sys.argv[1])

pics_path = '/home/srallaba/Pictures/ThopGang'
print("The group is ", group_id)

def get_pic(path = pics_path):
  files = sorted(os.listdir(path))
  file = random.choice(files)
  return file

def main():
    graph = facebook.GraphAPI(token)
    profile = graph.get_object(
        'me', fields='first_name,location,link,email,groups')
    group = graph.get_object(id=group_id)
    id = group['id']
    pic = get_pic()
    pic = pics_path + '/' + pic
    graph.put_photo(album_path=id + '/photos', image=open(pic, 'rb'), message='Look at this! Posting at ' + timestamp + ' EST')

    print(group)

if __name__ == '__main__':
    main()
