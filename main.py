import requests,user_agent,json,flask,telebot,random,os,sys
import telebot,darklib
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=["start"])
def h(message):
	@bot.message_handler(commands=["sub"])
	def bmdmf(message):
		print(k)
		nkj=len(k)
		print(nkj)
		bot.send_message(5009434402,f"اهلا بك مطوري 🙋‍♂️\nعدد مستخدمين بوتك : {nkj}")
	@bot.message_handler(commands=["listsub"])
	def jdjdj(message):	
		bot.send_message(5009434402,f"{k}")

	
	id = message.chat.id
	name=message.from_user.first_name
	username=message.from_user.username
	if f"username : @{username} id : {id} name : {name}"in k:
		True
	else:	
		k.append(f"username : @{username} id : {id} name : {name}")
	bot.send_message(id,f"""
- Welcome [{name}](tg://settings)

- Programin Bot : [Dark](t.me/j_w_2)

- Please Send username:password""",parse_mode="markdown")
	@bot.message_handler(func=lambda m:True)
	def cre(message):
		id=message.chat.id
		m=message.text
		username=m.split(":")[0]
		password=m.split(":")[1]
		name = "MyInsta:@4e_m1"
		sf = Dark.Create(username,password,name)
		l=f"{sf}"
		bot.send_message(id,l)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://insta-bo.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
