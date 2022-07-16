import requests,user_agent,json,flask,telebot,random,os,sys
import telebot,darklib
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request
bot = Flask(__name__)
@bot.ruote("/")
def h(message):
		username=request.args.get("username")
		password=request.args.get("password")
		name = "MyInsta:@4e_m1"
		sf = Dark.Create(username,password,name)
		l=f"{sf}"
		return l

bot.run()
