from flask import Blueprint, render_template
import tweepy
from tweepy import OAuthHandler

import json
import re
from textblob import TextBlob

consumer_key = 'Tg0vgC8HcxOS3O2WeLBma2U3L'
consumer_secret = '1x1udr7fR9pCMICooCZHFz2VXxb4Ztfcnd49kOF5l7e8fgejS8'
access_token = '1596773227074031616-gnheYn8HCghcmrclZDWWgD5TnHKARo'
access_token_secret = 'TzSO98apuBzyODdk3gWwe3d7X874OqnTpSijTpDfmRGrM'

# membuat object OAuthHandler 
auth = OAuthHandler(consumer_key, consumer_secret)
# memasukan access token dan secret
auth.set_access_token(access_token, access_token_secret)
# membuat tweepy API object untuk mengambil konten Twitter
api = tweepy.API(auth)
# Jika autentikasi dengan API gagal
gagal = "Autentikasi Gagal"

views = Blueprint(__name__, "views")

query = input("Masukan Pencarian Tweet yang diinginkan : ")
count = int(input("Masukan jumlah tweet yang diinginkan : "))

@views.route("/")
def masukan():
    return render_template("index.html", qry = query, cnt = count)