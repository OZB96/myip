#!/usr/bin/env python3
import requests
import json
import sys
import pyspeedtest
try:
    if len(sys.argv) == 1:
        r = requests.get('https://geo.ipify.org/api/v1?apiKey=at_gnQQZg49MFvCWjIp0mCmvQdpiUBHc&')
        tmp = json.loads(r.text)
        print("Your Country: "+ tmp["location"]["country"])
        print("region: "+tmp["location"]["region"])
        print("city: "+tmp["location"]["city"])
    else:
        iterr = iter(sys.argv)
        next(iterr)
        for args in iterr:
            if str(args) == "--help":
                print("To check your IP run The script without any arguments.  (  myip  )")
                print("To check other IPs insert the IP after the scripts name, you van insert more than one IP. ( myip IP1 IP2  )")
                print("To measure your connetion speed. (  myip --speed  )")
		sys.exit(1)
            if str(args) == "--speed":
                st = pyspeedtest.SpeedTest()
                print("Ping: "+ str(st.ping())+" ms")
                print("Upload speed: "+str((st.upload()/1024)/1024)+" Mbps")
                print("Download Speed: "+ str((st.download()/1024)/1024)+" Mbps")
		sys.exit(1)
            else:
                r = requests.get('https://geo.ipify.org/api/v1?apiKey=at_gnQQZg49MFvCWjIp0mCmvQdpiUBHc&ipAddress='+args)
                tmp = json.loads(r.text)
                print("The Country: "+ tmp["location"]["country"])
                print("region: "+tmp["location"]["region"])
                print("city: "+tmp["location"]["city"]+"\n\n")

except requests.exceptions.RequestException as e:
    print("Check Your Connection")
    sys.exit(1)
