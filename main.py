import telebot,requests,instaloader,base64
from telebot import *
from config import *

aa = ("qwertyuioplkjhgfdsamnbvcxz")
aaa= ("137907432WTJPGJLxhlohfhhkKCYKNivfjjkBKFGJI@$#&_-()=%+?!/:*¡¿~™><¬¦|\÷;`§×¶")


bot=telebot.TeleBot(BOT_TOKEN)


server=Flask (__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
 sudo_id = "1234567890"
 ID = message.from_user.id
 name = message.chat.first_name
 if message.chat.type == "private":
     ch = "H_7_1"
     idu = message.chat.id
     req = requests.get(f"https://api.telegram.org/bot5317189074:AAHlMl6pl9Nh0wvGIH2uzTudAtTd4tEHYAA/getChatMember?chat_id=@{ch}&user_id={idu}").text
     
     if ID == sudo_id or "member" in req or "creator" in req or "administartor" in req:

        key = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Storm", callback_data="storm")
        btn3 = types.InlineKeyboardButton(text="Maroc", callback_data="maroc")
        key.row_width = 2
        key.add(btn1)
        key.add(btn3)
        name=message.from_user.first_name
        bot.send_message(ID,f"""
اهلا بك عزيزي {name}

بوت خمط نقاط ستورم+ماروك

ماعليك سوه الاختيار من الازرار تحت""",reply_markup=key)
     else:
     	bot.send_message(ID,"""
عذرا عزيز عليك الاشتراك في قناة البوت اولا

@H_7_1
""")
@bot.callback_query_handler(func=lambda call : True)
def callback(call):
	if call.data=="storm":
		storm(call.message)
	if call.data=="maroc":
		maroc(call.message)

def maroc(message):
	id = message.chat.id
	bot.send_message(id,f"""
حسنا عزيزي اخترت ماروك

الان ماعليك سوا ان ترسل

يوزر الضحيه:يوزرك""")
	@bot.message_handler()
	def gm(message):
		
		id = message.chat.id
		start=bot.send_message(id,"حسنا انتضر")
		kji=message.text
		tuser=kji.split(":")[0]
		yuser=kji.split(":")[1]
		m = getmaroc(tuser,yuser)
		bot.edit_message_text(chat_id=id,message_id=start.message_id,text=f'{m}')
def storm(message):
	id = message.chat.id
	bot.send_message(id,f"""
حسنا عزيزي اخترت ستورم

الان ماعليك سوا ان ترسل

يوزر الضحيه:يوزرك""")
	@bot.message_handler()
	def gm(message):
		
		id = message.chat.id
		start=bot.send_message(id,"حسنا انتضر")
		kji=message.text
		tuser=kji.split(":")[0]
		yuser=kji.split(":")[1]
		m = getstorm(tuser,yuser)
		bot.edit_message_text(chat_id=id,message_id=start.message_id,text=f'{m}')
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
