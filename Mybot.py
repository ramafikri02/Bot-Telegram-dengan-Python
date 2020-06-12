import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
myBot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_botfidelya')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @myBot.message_handler(commands=['start'])
    def start(message):
        teks = mytoken.SAPA + "\n" + "\n" + "/help : Untuk melihat semua perintah yang dapat di lakukan Fidelya" +"\n" + "\n" \
                        "-- admin & developer @Fikri_05 - SMK Taruna Bhakti -- " + "\n" + "\n" + \
                        "⌚ Hari ini tanggal "+str(waktusekarang)
        myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['help'])
    def help(message):
         teks = "/datasiswa : Untuk Melihat Seluruh Data Siswa RPL 👦"
         myBot.reply_to(message, teks)

    @myBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query="select nipd ,nama ,kelas from tabel_siswa "
        sql.execute(query)
        data=sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            #print(data)
            no=0
            for x in data:
                no += 1
                kumpuldata =kumpuldata+ str(x) + "\n"
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        myBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)