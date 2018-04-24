#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

api = InstagramAPI("login", "password")
save_session = {}
if (api.login()):
    save_session = {'token': api.token,
                    'username_id': api.username_id,
                    'rank_token': api.rank_token,
                    'uuid': api.uuid,
                    'session': api.s.cookies.get_dict(),
                    'user_agent': api.USER_AGENT,
                    'device_id': api.device_id}
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login success!")
    api.logout()
else:
    print("Can't login!")

api.set_session(**save_session)
api.getSelfUserFeed()
print(api.LastJson)
