import requests,base64,instaloader,random,os,telebot
import config

from flask import *
from telebot import *

stopi=[] 			



server=Flask (__name__)
a1=types.InlineKeyboardButton(text="رفع ادمن",callback_data="addadmin")
a2=types.InlineKeyboardButton(text="تنزيل ادمن",callback_data="deladmin")
a3=types.InlineKeyboardButton(text="اضافه اشتراك",callback_data="addsub")
a4=types.InlineKeyboardButton(text="الغاء اشتراك",callback_data="delsub")
a5=types.InlineKeyboardButton(text="بدء التجميع",callback_data="start")
a6=types.InlineKeyboardButton(text="لوحة المشتركين",callback_data="sub1")
a7=types.InlineKeyboardButton(text="لوحة الادمنيه",callback_data="sub2")
a8=types.InlineKeyboardButton(text="توقيف",callback_data="stop")

progr=["L_L_5_L"]
admins=[]
subs=[]
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
		bot.send_message(5009434402,f"الادمن قام بالغاء اشتراك\nاسم الادمن : {name}\nيوزر الادمن : {username}\nيوزر الشخص القام بالغاء اشتراكه : @{user}")
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
		bot.send_message(5009434402,f"الادمن قام بعمل اشتراك\nاسم الادمن : {name}\nيوزر الادمن : {username}\nيوزر الشخص القام بعمل له اشتراك : @{user}")

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
	op=bot.send_message(id,"حسنا عزيزي ارسل ايديك لبدء تجميع النقاط")
	bot.register_next_step_handler(op,kiop)
def kiop(message):
 id=message.chat.id
 username=message.chat.username
 kot=bot.send_message(id,"Please Wait")
 myid=message.text
 coin12=0
 while True:
 		if username in stopi:
 			stopi.remove(username)
 			mj(message)
 			break
 		if username in subs:
 			True
 		else:
 			bot.send_message(id,"""عذرا عزيزي انت غير مشترك في البوت\n\nراسل المطور للتفعيل : @L_L_5_L""")
 			mj(message)
 			break
 			
 		
 	
 			
 		iil = "".join(random.choice("629197468292")for i in range(7))

 		llll="mhmdtool"
 		message2 = str(iil)
 		message_bytes2 = message2.encode('ascii')
 		base64_bytes2 = base64.b64encode(message_bytes2)
 		id= base64_bytes2.decode('ascii')
 		message2 = llll
 		message_bytes2 = message2.encode('ascii')
 		base64_bytes2 = base64.b64encode(message_bytes2)
 		usern= base64_bytes2.decode('ascii')

 		headers={
"Host": "arabefollower.com",
"content-type": "application/json; charset=UTF-8",
"user-agent": "okhttp/3.14.7"
}
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","u_id": id, "u_name": usern}
 		mkl = requests.request('POST',"https://arabefollower.com/v1/ice/loginUser",headers=headers,json=data).json()
 		
 		token = mkl["token"]
 		headers={
"Host": "arabefollower.com",
"content-type": "application/json; charset=UTF-8",
"token": token,
"user-agent": "okhttp/3.14.7"
}
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","code": "jffeu"}
 		mk = requests.request('POST',"https://arabefollower.com/v1/ice/getGiftCode",headers=headers,json=data).json()
 		
 			
 		

 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","code": "jffeul"}
 		mk = requests.request('POST',"https://arabefollower.com/v1/ice/getGiftCode",headers=headers,json=data).json()

 		
 		coin=50
 		coin2=50
 		E="\033[1;32m"
 		B="\033[1;36m"
 		A="\033[1;31m"
 		L="\033[1;35m"
 		
 		headers={
"Host": "arabefollower.com",
"content-type": "application/json; charset=UTF-8",
"token": token,
"user-agent": "okhttp/3.14.7"
}
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","coin":coin,"coin_type":"general","target_id":myid}
 		k1 = requests.request('POST',"https://arabefollower.com/v1/ice/transferCoin",headers=headers,json=data).json()

 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","coin":coin2,"coin_type":"follow","target_id":myid}
 		k = requests.request('POST',"https://arabefollower.com/v1/ice/transferCoin",headers=headers,json=data).json()
 		if k1["message"]=="success" or k["message"]=="success":
 			coin12+=coin
 			mask=types.InlineKeyboardMarkup(row_width=1)
 			mask.add(a8)
 		
 			bot.edit_message_text(text=f"Successful Get Coin\n================\n\nSend : {coin12}\n\n================",chat_id=message.chat.id,message_id=kot.message_id,reply_markup=mask)
 		else:
 			bot.edit_message_text(text=k["message"],chat_id=message.chat.id,message_id=kot.message_id)
 			
	
	
import os
E = "\033[1;32m"
L= "\033[1;35m"
B="\033[1;36m"
bot=TeleBot("5318484779:AAEcGFkQbPqqgC2TeOUWfieiwu_Z-3zomwY")
@bot.message_handler(commands=["start"])

def mj(message):
 id= message.chat.id
 username=message.chat.username
 name=message.chat.first_name
 kas=types.InlineKeyboardMarkup(row_width=1)
 kas.add(a5)
 bot.send_message(id,f"اهلا بك عزيزي {name}\n\nبوت تجميع نقاط Hot Follower\n\nاضغط علا بدء التجميع",reply_markup=kas)
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
		stopi.append(message.chat.username)
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
