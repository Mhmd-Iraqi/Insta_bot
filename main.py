import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def G(message):
 
	mas = types.InlineKeyboardMarkup(row_width=2)
	A=types.InlineKeyboardButton("CH1",url="https://t.me/WXGDS")
	B=types.InlineKeyboardButton("CH2",url="https://t.me/WXGDF")
	C=types.InlineKeyboardButton("Dev🤖",url="https://t.me/WXGDX")
	mas.add(A,B,C)
	bot.send_message(message.chat.id,msg,reply_markup=mas,parse_mode="markdown")
	bot.reply_to(message,text="ID:Sleep", parse_mode = "markdown",disable_web_page_preview="true")
@bot.message_handler(func=lambda m:True)

def callback(message):
 id = message.chat.id
 while True:
  try:
  	if str(id) in str(s):
  		s.remove(id)
  		mas = types.InlineKeyboardMarkup(row_width=2)
  		A=types.InlineKeyboardButton("CH1",url="https://t.me/WXGDS")
  		B=types.InlineKeyboardButton("CH2",url="https://t.me/WXGDF")
  		C=types.InlineKeyboardButton("Dev🤖",url="https://t.me/WXGDX")
  		mas.add(A,B,C)
  		bot.send_message(message.chat.id,msg,reply_markup=mas,parse_mode="markdown")
  		bot.reply_to(message,text="ID:Sleep", parse_mode = "markdown",disable_web_page_preview="true")
  		break
  		
  	
  	ml = message.text
  	msa = ml.split(":")[0]
  	sle = ml.split(":")[1]
  	
  	url = requests.post(f"https://getcoin-murad-hazem.ols1an.repl.co/?uid={msa}&submit=submit").text
  
  	if ('{"coins":') in url:
  		id = message.chat.id  	
  		coinx = str(url.split('coins":"')[1])
  		coin = str(coinx.split('"')[0])
  		bot.reply_to(message,text=f"""
  		Coins : {coin}
""",parse_mode="markdown")
  		time.sleep(int(sle))
  except:
  	bot.reply_to(message,text="Id Blocked")
  	s.append(id)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://instaup-coi.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
