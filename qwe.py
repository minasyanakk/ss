#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import time
import random
sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol
from userinfo import UserInfo

with open("login.txt") as file:
    logg = [row.strip() for row in file]
bot = InstaBot(
    login=logg[0],
    password=logg[1],


    )

with open("fl.txt") as file:
    us = [row.strip() for row in file]
print(us)


ui = UserInfo() 
for x in us:
    try:
        rand =random.randint(45, 60)
        print('time rand:===='+ str(rand))
        ss=ui.get_user_id_by_login(x)
        print(ss)
        bot.follow(ss)
        time.sleep(rand)
       
        
    except ValueError:
            print ("not user")

raw_input()
