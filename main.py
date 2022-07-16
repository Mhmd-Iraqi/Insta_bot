from flask import *
from darklib import *
bot = Flask(__name__)
@bot.route("/")
def h(message):
		username=request.args.get("username")
		password=request.args.get("password")
		name = "MyInsta:@4e_m1"
		sf = Dark.Create(username,password,name)
		l=f"{sf}"
		return l
		
		
bot.run()
