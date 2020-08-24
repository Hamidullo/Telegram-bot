import json
import requests
import time
import urllib

from telebot.types import KeyboardButton

import config
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent,\
    ReplyKeyboardMarkup

bot = telebot.TeleBot(f"{config.TOKEN}")

import config
from dbhelper import DBHelper
from otchyot import DBHelperO
from brigadiri import DBHelper1

db = DBHelper()
dbO = DBHelperO()
db1 = DBHelper1()

TOKEN = config.TOKEN
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def handle_updates(updates):
    for update in updates["result"]:

        print(updates)

        id = "1"
        position = "chelovek"
        name = "Bot"
        chat = update["message"]["chat"]["id"]
        login = update["message"]["chat"]["first_name"]
        parol = update["message"]["chat"]["id"]
        numb = "1112233"
        lang = "eng"
        status = 'zakazana'
        unposit = 'unposit'

        if "text" in update["message"]:
            text = update["message"]["text"]
        elif "sticker" in update["message"]:
            text = "/info"
            sticker = update["message"]["sticker"]
        elif "contact" in update["message"]:

            text = update["message"]["contact"]["phone_number"]

        print(update)
        items = db.has_user(chat)
        langg = db.is_lang("eng")
        pos = db.is_position(position)
        loginn = db.has_login(login)
        paroll = db.has_parol(parol)
        namee = db.has_name(name)
        number = db.is_number(numb)
        stat = db.get_status(chat)

        print(stat)

        # Start

        if f"{chat}" in items:
            print("continiou")
        else:
            if text == "/start":
                keyboard = build_keyboard(['Русский 🇷🇺', 'O\'zbekcha 🇺🇿'])
                send_message("Здравствуйте! Для начала не обходимо выберат язык обслуживания!"
                             " \n\n Assalomu alaykum,  avvaliga"
                             " xizmat ko’rsatish tilini tanlash lozim!", chat, keyboard)
                db.add_user(id, position, name, chat, login, parol, numb, lang, status, unposit)
                #dbO.add_otchyot("0","chelovek","user","chat_id","obName","siryo","obyom","status","zakazana")
            print(db.has_user(chat))
            continue

        #dbO.add_otchyot("0", "chelovek", "user", "chat_id", "obName", "siryo", "obyom", "status", "zakazana")

        # language

        dis_idr = db.get_dispetcher("Диспетчер",db.get_status(chat)[0])
        print(dis_idr)
        dis_id = db.get_dispetcher("Dispetcher",db.get_userID(chat)[0])
        print(dis_id)
        brig_idr = db.get_dispetcher("Бригадир",db.get_status(chat)[0])
        print(brig_idr)
        brig_id = db.get_dispetcher("Brigadir",db.get_userID(chat)[0])
        print(brig_id)

        if "location" in update["message"]:
            text = "/info"
            if "Brigadir" in db.get_position(chat):
                keyb = build_keyboard(['Buyurtmani bekor qilish', 'Yangi ariza berish'])
                send_message("Iltimos Dispetcher javob berguncha kutib turing \n\n Xom ashyo nomini va hajmini jo'nating \n\n Buyurtmni bekor qilish uchun 'Buyurtmani bekor qilish' tugmasini bosing", chat, keyb)
                forward_message(db.get_dispetcher("Dispetcher",db.get_status(chat)[0])[0], chat, True, update["message"]["message_id"])
                dbO.update_zayavka("zakaz", chat,dbO.get_id()[len(dbO.get_id())-1])
                continue

            elif "Бригадир" in db.get_position(chat):
                keybo = build_keyboard(['Отменить заявку', 'Новое заявка'])
                send_message("Что бы отменить заявку нажмите на 'Отменить заявку'",chat, keybo)
                dbO.update_zayavka("zakaz",chat,dbO.get_id()[len(dbO.get_id())-1])
                forward_message(db.get_dispetcher("Диспетчер",db.get_status(chat)[0])[0], chat, True, update["message"]["message_id"])
                continue

        list = ['Заявка ✍','Статус 📍','Отчёт 📋','Настройка ⚙','Выберите язык 🇷🇺‍','Выберите Объект 🏗️',
                'Изменить ФИО ✏','Изменить номер 📱','Назад ⬅']

        listu = ['Ariza ✍', 'Ariza holati 📍', 'Hisobot 📋', 'Sozlamalar ⚙', 'Ob\'ektni tanlang 🏗️',
                 'FISH ni o\'zgartirish ✏', 'Nomerni o\'zgartirish 📱', 'Tilni tanlash‍', 'Ortga ⬅']

        all = f"{numb}" in number and f"{name}" in namee and f"{parol}" in paroll and f"{login}" in loginn and "chelovek" in pos and "eng" in langg and f"{chat}" in items

        #db.dele("516944875")
        #db.dele("485638921")
        #db.dele("207460233")
        #db.dele("1129989692")
        #db.dele("497375178")
        #dbO.delete_item("485638921")
        #dbO.delete_item("1037089576")
        #dbO.delete_item("1129989692")
        #dbO.delete_item("497375178")
        #dbO.delete_item("chat_id")

        if "eng" in db.get_lang(chat):
            if text == "Русский 🇷🇺":
                keyboardR = build_keyboard(['Бригадир 👷', 'Диспетчер 👨🏻‍💻'])
                send_message("Выберите раздел", chat, keyboardR)
                db.update_lang("rus", chat)
                continue

            elif text == "O\'zbekcha 🇺🇿":
                keyboardU = build_keyboard(['Brigadir 👷', 'Dispetcher 👨🏻‍💻'])
                send_message("Bo'limingizni tanlang ", chat, keyboardU)
                db.update_lang("uzb", chat)
                continue
        else:
            print("LANGUAGE")

        # Position

        if "chelovek" in db.get_position(chat):
            if text == "Бригадир 👷" :
                if "Бригадир" in db.is_position("Бригадир"):
                    idbr = len(db.is_position("Бригадир")) + 1
                    db.update_id(idbr,chat)
                send_message("Введите свой Login или id ✍️", chat)
                db.update_position("Бригадир", chat)
                db.update_unposit("Диспетчер",db1.get_item(db.get_status(chat)[0])[0])
                continue

            elif text == "Диспетчер 👨🏻‍💻":
                if "Диспетчер" in db.is_position("Диспетчер"):
                    iddr = len(db.is_position("Диспетчер")) + 1
                    db.update_id(iddr,chat)
                send_message("Введите свой Login или id ✍️", chat)
                db.update_position("Диспетчер", chat)
                db.update_unposit("Бригадир", chat)
                db1.add_otchyot(len(db1.get_id()),chat,status)

                continue

            elif text == "Brigadir 👷":
                if "Brigadir" in db.is_position("Brigadir"):
                    idb = len(db.is_position("Brigadir")) + 1
                    db.update_id(idb,chat)
                send_message("Login yoki ozingizni id raqamingizni kiriting ✍️", chat)
                db.update_position("Brigadir", chat)
                db.update_unposit(db.get_dispetcher("Dispetcher", db.get_status(chat)[0])[0], chat)
                continue

            elif text == "Dispetcher 👨🏻‍💻":
                if "Dispetcher" in db.is_position("Dispetcher"):
                    idd = len(db.is_position("Dispetcher")) + 1
                    db.update_id(idd,chat)
                send_message("Login yoki ozingizni id raqamingizni kiriting ✍️", chat)
                db.update_position("Dispetcher", chat)
                db.update_unposit("Brigadir", chat)
                db1.add_otchyot(len(db1.get_id()), chat, status)
                continue

        else:
            print("POSTION")

        # ZAYAVKA

        if "rus" in db.get_lang(chat):
            # login in
            if f"{login}" in db.get_login(chat):
                send_message("Тепер введите пароль 🔐", chat)
                db.update_login(text, chat)
                continue
            else:
                print("LOGIN")

            # parol in

            if f"{parol}" in db.get_parol(chat):
                send_message("Введите ФИО", chat)
                db.update_parol(text, chat)
                continue
            else:
                print("PAROL")

            # FIO in

            if f"{name}" in db.get_name(chat):
                keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                button_phone = KeyboardButton(text="Отправить номер телефона 📲", request_contact=True)
                keyboard.add(button_phone)
                bot.send_message(chat,
                                 "Отправьте мне свой номер телефона 📱",
                                 reply_markup=keyboard)
                db.update_name(text, chat)
                continue
            else:
                print("NAME")

            # loading zayavka

            if "Бригадир" in db.get_position(chat):
                if f"{numb}" in db.get_number(chat):
                    keyboardq = build_keyboard(['Заявка ✍', 'Статус 📍', 'Отчёт 📋', 'Настройка ⚙'])
                    send_message("Выберите раздел", chat, keyboardq)
                    db.update_numb(text, chat)
                    continue
                else:
                    print("NUMBER")

                # Nastroyki          ######################################################################

                if "nastroyka" in db.get_status(chat):
                    if text == "Выберите язык 🇷🇺":
                        keybordl = build_keyboard(['Русский 🇷🇺', 'O\'zbekcha 🇺🇿'])
                        send_message("🇷🇺 Выберите язык", chat, keybordl)
                        continue

                    elif text == "Изменить ФИО ✏":
                        keybord = build_keyboard(['⬅️ Назад'])
                        send_message("Введите ФИО", chat, keybord)
                        db.set_status("izmemitFIO", chat)
                        continue

                    elif text == "Изменить номер 📱":
                        keybord = build_keyboard(['⬅️ Назад'])
                        send_message("Введите номер", chat, keybord)
                        db.set_status("izmemitTEL", chat)
                        continue

                if "izmemitFIO" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Назад'])
                    send_message("Изменено", chat, keyborr)
                    a = text
                    db.update_name(a, chat)
                    db.set_status("nastroyki", chat)
                    continue

                if "izmemitTEL" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Назад'])
                    send_message("Изменено", chat, keyborr)
                    db.set_status("nastroyki", chat)
                    db.update_numb(text, chat)
                    continue

                if text == "Русский 🇷🇺":
                    keyborr = build_keyboard(['⬅️ Назад'])
                    send_message("Изменено", chat, keyborr)
                    print("changed Language")
                    db.update_lang("rus", chat)
                    db.update_position("Бригадир", chat)
                    continue

                if text == "O\'zbekcha 🇺🇿":
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    print("changed Language")
                    db.update_position("Brigadir", chat)
                    db.update_lang("uzb", chat)
                    continue

                ls = dbO.get_zayavki("Бригадир")

                if text == 'Статус 📍':
                    k = build_keyboard(ls)
                    # keyboa = build_keyboard(['Загружается', 'В пути', 'Рядом с объектом', 'Доставлено', 'Отменить заявку', 'Назад ⬅️'])
                    send_message("Статус !", chat, k)
                    #keyboardnw = build_keyboard(['Принял 📥', 'Назад ⬅️'])
                    #send_message(f"{db.get_status(dis_idr[0])}", chat,keyboardnw)
                    continue

                if text in ls:
                    keyboardnw = build_keyboard(['Принял 📥','Запрос состояние сырья ❓', 'Назад ⬅️'])
                    send_message(f"{dbO.get_status(chat,text)}", chat, keyboardnw)
                    continue

                if text == 'Принял 📥':
                    send_message( f"Бригадир {db.get_name(chat)} принял сырьё", db1.get_item(db.get_status(chat)[0])[0])
                    dbO.update_status("Принята", chat, db.get_status(chat)[0])

                if text == 'Запрос состояние сырья ❓':
                    send_message( f"Бригадир '{db.get_name(chat)}' - '{db.get_status(chat)}' просить состояние сырья", db1.get_item(db.get_status(chat)[0])[0])
                    send_message("Запрос отправлен диспетчеру ✉️",chat)

                if text == 'Отчёт 📋':
                    s = ""
                    for x in dbO.get_item(chat):
                        s += f"{x} \n"
                    send_message(s, chat)
                    dbO.toexel(chat)
                    f = open("output2.xlsx", "rb")
                    bot.send_document(chat, f)
                    continue

                if text == 'Настройка ⚙' or text == "⬅️ Назад":
                    keyboardn = build_keyboard(
                        ['Изменить ФИО ✏', 'Изменить номер 📱', 'Выберите язык 🇷🇺', 'Назад ⬅️'])
                    send_message("Настройка ⚙", chat, keyboardn)
                    db.set_status("nastroyka",chat)
                    continue

                ###########################   db ============== <<<<<<<<<<<>>>>>>>>>>>>>> (len(dbO.get_id()) - 1)

                print(dbO.get_id())

                if "zakazana" in dbO.get_zayavka(f"{len(dbO.get_id())-1}") or "prinyata" in dbO.get_zayavka(f"{len(dbO.get_id())-1}"):
                    if text == "Заявка ✍":
                        send_message("Введите название объекта 🏗️", chat)
                        s = len(dbO.get_id())
                        dbO.add_otchyot(f"{s}", f"{db.get_position(chat)[0]}", f"{db.get_name(chat)[0]}", chat,
                                        "obName",
                                        "siryo", "obyom", "status", "inzayavka")
                        continue

                if "inzayavka" == dbO.get_zayavka(f"{len(dbO.get_id()) - 1}")[0]:
                    dbO.update_Obname(text, chat, dbO.get_id()[len(dbO.get_id())-1])
                    # s = len(dbO.get_id())
                    # dbO.add_otchyot(f"{s}", f"{db.get_position(chat)[0]}", f"{db.get_name(chat)[0]}", chat, b,"siryo", "obyom", "status", "true")
                    # send_message("📎 knopkani bosing va Lokatsiya bo'limini tanlang jo'nating",chat) va lokatsiyani ham jo'nating 🏗️
                    send_message("Введите название сырья 🛢️", chat)
                    dbO.update_zayavka("siryo", chat,dbO.get_id()[len(dbO.get_id())-1])
                    # send_message(f"{login} бригадир сделал заказ на '{b}' объект ! ", dis_id[0])
                    continue

                if "siryo" in dbO.get_zayavka(f"{len(dbO.get_id()) - 1}"):
                    # dbO.add_otchyot(db.get_userID(chat),db.get_position(chat),db.get_name(chat),chat,b,"siryo","obyom","location")
                    send_message("Заявка отправлено к диспетчеру , ждите ответ !",
                                 chat)  # va lokatsiyani ham jo'nating 🏗️
                    # send_message("Введите название сырья после слова 'Заказать' 🛢️", chat)
                    kk = build_keyboard(['Подтвердить приём заявки !'])
                    send_message(
                        f"Бригадир {db.get_name(chat)} сделал заказ на '{text}' ! Вы должны отправит бригадеру в течение 24 часа ",
                        db1.get_item(db.get_status(chat)[0])[0], kk) #obyomni kiritsak chat id chiqarsin
                    dbO.update_Obyom(text, chat, dbO.get_id()[len(dbO.get_id())-1])
                    chatt = db1.get_item(db.get_status(chat)[0])[0]
                    print(chatt)
                    db1.add_otchyot(len(db1.get_id()),chatt,text)
                    db.set_status(text,db1.get_item(db.get_status(chat)[0])[0])
                    db.set_status(text,chat)
                    continue

                if "zakaz" in dbO.get_zayavka(f"{len(dbO.get_id()) - 1}"):
                    # dbO.add_otchyot(db.get_userID(chat),db.get_position(chat),db.get_name(chat),chat,b,"siryo","obyom","location")
                    send_message("Передан в обработку !",
                                 chat)  # va lokatsiyani ham jo'nating 🏗️
                    # send_message("Введите название сырья после слова 'Заказать' 🛢️", chat)
                    send_message(
                        "Зайдите в закладку Статус и задайте статус",
                        db1.get_item(db.get_status(chat)[0])[0])
                    dbO.update_zayavka("zakazana", chat,dbO.get_id()[len(dbO.get_id())-1])

                if f"{text}" not in list:
                    keyboardz = build_keyboard(['Заявка ✍', 'Статус 📍', 'Отчёт 📋', 'Настройка ⚙'])
                    send_message("Выберите раздел", chat, keyboardz)
                    continue

                else:
                    print("zayavka")
            else:

                if f"{numb}" in db.get_number(chat):
                    keyboardq = build_keyboard(['Статус 📍', 'Отчёт 📋', 'Настройка ⚙'])
                    send_message("Выберите раздел", chat, keyboardq)
                    db.update_numb(text, chat)
                    continue
                else:
                    print("NUMBER")

                    if text == 'Настройка ⚙' or text == "⬅️ Назад":
                        keyboardn = build_keyboard(
                            ['Изменить ФИО ✏', 'Изменить номер 📱', 'Выберите язык 🇷🇺', 'Назад ⬅️'])
                        send_message("Настройка ⚙", chat, keyboardn)
                        db.set_status("nastroyka", chat)
                        continue

                    # Nastroyki
                    if "nastroyka" in db.get_status(chat):
                        if text == "Выберите язык 🇷🇺":
                            keybordl = build_keyboard(['Русский 🇷🇺', 'O\'zbekcha 🇺🇿'])
                            send_message("🇷🇺 Выберите язык", chat, keybordl)
                            continue

                        elif text == "Изменить ФИО ✏":
                            keybord = build_keyboard(['⬅️ Назад'])
                            send_message("Введите ФИО", chat, keybord)
                            db.set_status("izmemitFIO", chat)
                            continue

                        elif text == "Изменить номер 📱":
                            keybord = build_keyboard(['⬅️ Назад'])
                            send_message("Введите номер", chat, keybord)
                            db.set_status("izmemitTEL", chat)
                            continue

                    if "izmemitFIO" in db.get_status(chat):
                        keyborr = build_keyboard(['⬅️ Назад'])
                        send_message("Изменено", chat, keyborr)
                        a = text
                        db.update_name(a, chat)
                        db.set_status("nastroyki", chat)
                        continue

                    if "izmemitTEL" in db.get_status(chat):
                        keyborr = build_keyboard(['⬅️ Назад'])
                        send_message("Изменено", chat, keyborr)
                        db.set_status("nastroyki", chat)
                        db.update_numb(text, chat)
                        continue

                    if text == "Русский 🇷🇺":
                        keyborr = build_keyboard(['⬅️ Назад'])
                        send_message("Изменено", chat, keyborr)
                        print("changed Language")
                        db.update_lang("rus", chat)
                        db.update_position("Диспетчер", chat)
                        continue

                    if text == "O\'zbekcha 🇺🇿":
                        keyborr = build_keyboard(['⬅️ Ortga'])
                        send_message("O'zgartirildi", chat, keyborr)
                        print("changed Language")
                        db.update_position("Dispetcher", chat)
                        db.update_lang("uzb", chat)
                        continue

                print(db.get_status(chat))

                if text == 'Отчёт 📋':
                    s = ""
                    for x in dbO.get_item("Бригадир"):
                        s += f"{x} \n"
                    send_message(s, chat)
                    dbO.toexel("Бригадир")
                    f = open("output2.xlsx", "rb")
                    bot.send_document(chat, f)
                    #send_message(f"{dbO.get_Obname(d)} \n {dbO.get_Obyom(d)}", chat)
                    continue

                if len(dbO.get_status(chat,db.get_status(chat)[0])) != 0:
                    if dbO.get_status(chat,db.get_status(chat)[0])[0] == 'Заявка отменено,П':
                        send_message(f"Заявка отменено, {db.get_status(chat)[0]} причина отмены : {text} ", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                        send_message("Заявка отменено", chat)
                        dbO.update_status(text,db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])

                l = dbO.get_zayavki("Бригадир")
                print(l)

                if text == 'Статус 📍':
                    k = build_keyboard(l)
                    #keyboa = build_keyboard(['Загружается', 'В пути', 'Рядом с объектом', 'Доставлено', 'Отменить заявку', 'Назад ⬅️'])
                    send_message("Статус !", chat, k)
                    continue

                print( db.get_status(chat)[0])

                if text in l:
                    keyboa = build_keyboard(['Загружается', 'В пути', 'Рядом с объектом', 'Доставлено', 'Отменить заявку', 'Назад ⬅️'])
                    db.set_status(text,chat)
                    send_message(f"{dbO.get_status(db.get_dispetcher('Бригадир',db.get_status(chat)[0])[0],text)}", chat, keyboa)

                    continue

                if text == "Подтвердить приём заявки !":
                    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button_phone = KeyboardButton(text="Отправить местоположение объекта 📍", request_location=True)
                    keyboard.add(button_phone)
                    bot.send_message(db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],
                                     "Ваш заказ в обработке ⏳ \n Отправьте нам свою локацию 📍",
                                     reply_markup=keyboard)
                    send_message("Отправлено", chat)

                print(db.get_status(chat)[0])

                if text == 'Загружается':
                    send_message(f"{db.get_status(chat)[0]} сырьё {text}", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                    send_message("Отправлено", chat)
                    dbO.update_status(text,db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])

                if text == 'Отменить заявку':
                    send_message("Заявка отменено, опишите причину", chat)
                    dbO.update_status("Заявка отменено,П",db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])
                    continue

                if dbO.get_status(db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0]) == 'Заявка отменено,П':
                    send_message(f"Заявка отменено, {db.get_status(chat)[0]} причина отмены : {text} ", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                    send_message("Заявка отменено", chat)
                    dbO.update_status(text,db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])
                    continue

                if text == 'Доставлено':
                    send_message(f"{db.get_status(chat)[0]} Работа выполнена ✅", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                    send_message("Доставлено", chat)
                    dbO.update_status(text,db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])

                if text == 'В пути':
                    send_message(f"{db.get_status(chat)[0]} Сырьё {text}", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                    send_message("Отправлено", chat)
                    dbO.update_status(text, db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])

                if text == 'Рядом с объектом':
                    send_message(f"{db.get_status(chat)[0]} Сырьё {text}", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                    send_message("Отправлено", chat)
                    dbO.update_status(text, db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])

                if f"{text}" not in list:
                    keyboardz = build_keyboard(['Статус 📍', 'Отчёт 📋', 'Настройка ⚙'])
                    send_message("Выберите раздел", chat, keyboardz)
                    continue

                else:
                    print("zayavka")

# ZZAYAVKA    UZB
##################################################      uzb     #############################################
        if "uzb" in db.get_lang(chat):
            # login in
            print(text == "Tilni tanlash")
            #print(text.startswith("change"))

            if f"{login}" in db.get_login(chat):
                send_message("Parolni kiriting 🔐", chat)
                db.update_login(text, chat)
                continue
            else:
                print("LOGIN")

            # parol in

            if f"{parol}" in db.get_parol(chat):
                send_message("FISH kiriting", chat)
                db.update_parol(text, chat)
                continue
            else:
                print("PAROL")

            # FIO in

            if f"{name}" in db.get_name(chat):
                keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                button_phone = KeyboardButton(text="Nomerni jo'natish 📲", request_contact=True)
                keyboard.add(button_phone)
                bot.send_message(chat,
                                 "Menga nomeringizni jo'nating 📱",
                                 reply_markup=keyboard)

                db.update_name(text, chat)
                continue
            else:
                print("NAME")

            # number in

            if "Brigadir" in db.get_position(chat):

                if f"{numb}" in db.get_number(chat):
                    keyboardq = build_keyboard(['Ariza ✍', 'Ariza holati 📍', 'Hisobot 📋', 'Sozlamalar ⚙'])
                    send_message("Bo'limni tanlang", chat, keyboardq)
                    db.update_numb(text, chat)
                    continue
                else:
                    print("NUMBER")

                ls = dbO.get_zayavki("Brigadir")

                if text == 'Ariza holati 📍':
                    k = build_keyboard(ls)
                    # keyboa = build_keyboard(['Загружается', 'В пути', 'Рядом с объектом', 'Доставлено', 'Отменить заявку', 'Назад ⬅️'])
                    send_message("Ariza holati !", chat, k)
                    # keyboardnw = build_keyboard(['Принял 📥', 'Назад ⬅️'])
                    # send_message(f"{db.get_status(dis_idr[0])}", chat,keyboardnw)
                    continue

                if text in ls:
                    keyboardnw = build_keyboard(['Qa\'bul qildim 📥','Ariza holatini so\'rovi ❓', 'Ortga ⬅️'])
                    send_message(f"{dbO.get_status(chat, text)}", chat, keyboardnw)
                    db.set_status(text, chat)
                    continue

                if text == 'Qa\'bul qildim 📥':
                    send_message(f"Brigadir {db.get_name(chat)} xom ashyoni qa'bul qildi", db.get_dispetcher("Dispetcher",db.get_userID(chat)[0])[0])
                    dbO.update_status("Qa'bul qilindi", chat, db.get_status(chat)[0])

                if text == "Ariza holatini so\'rovi ❓":
                    send_message(f"Brigadir '{db.get_name(chat)}' - '{db.get_status(chat)}' xom ashyoga berilgan arizani holatini soramoqda", db.get_dispetcher("Dispetcher",db.get_userID(chat)[0])[0])
                    send_message("So'rov dispetcherga jonatildi ✉️", chat)

                if text == 'Hisobot 📋':
                    s = ""
                    for x in dbO.get_item(chat):
                        s += f"{x} \n"
                    send_message(s, chat)
                    dbO.toexel(chat)
                    f = open("output2.xlsx", "rb")
                    bot.send_document(chat, f)

                if text == 'Sozlamalar ⚙' or text == "⬅️ Ortga":
                    keyboardn = build_keyboard(
                        ['FISH ni o\'zgartirish ✏', 'Tel raqamni almashtirish 📱', 'Tilni tanlash 🇺🇿', 'Ortga ⬅️'])
                    send_message("Sozlamalar ⚙", chat, keyboardn)
                    db.set_status("nastroyka", chat)
                    continue

                ###########################   db ============== <<<<<<<<<<<>>>>>>>>>>>>>> (len(dbO.get_id()) - 1)

                print(dbO.get_id())

                if "zakazana" in dbO.get_zayavka(f"{len(dbO.get_id()) - 1}") or "Qa'bul qilindi" in dbO.get_zayavka(
                        f"{len(dbO.get_id()) - 1}"):

                    if text == "Ariza ✍":
                        send_message("Obyekt nomini kiriting 🏗️", chat)
                        s = len(dbO.get_id())
                        dbO.add_otchyot(f"{s}", f"{db.get_position(chat)[0]}", f"{db.get_name(chat)[0]}", chat,
                                        "obName",
                                        "siryo", "obyom", "status", "inzayavka")
                        continue

                if "inzayavka" == dbO.get_zayavka(f"{len(dbO.get_id()) - 1}")[0]:
                    dbO.update_Obname(text, chat, dbO.get_id()[len(dbO.get_id()) - 1])
                    # s = len(dbO.get_id())
                    # dbO.add_otchyot(f"{s}", f"{db.get_position(chat)[0]}", f"{db.get_name(chat)[0]}", chat, b,"siryo", "obyom", "status", "true")
                    # send_message("📎 knopkani bosing va Lokatsiya bo'limini tanlang jo'nating",chat) va lokatsiyani ham jo'nating 🏗️
                    send_message("Xom ashyo nomini va hajmini kiriting 🛢️", chat)
                    dbO.update_zayavka("siryo", chat, dbO.get_id()[len(dbO.get_id()) - 1])
                    # send_message(f"{login} бригадир сделал заказ на '{b}' объект ! ", dis_id[0])
                    continue

                if "siryo" in dbO.get_zayavka(f"{len(dbO.get_id()) - 1}"):
                    # dbO.add_otchyot(db.get_userID(chat),db.get_position(chat),db.get_name(chat),chat,b,"siryo","obyom","location")
                    send_message("Ariza Dispetcherga jo'natildi, iltimos javobni kuting !",
                                 chat)  # va lokatsiyani ham jo'nating 🏗️
                    # send_message("Введите название сырья после слова 'Заказать' 🛢️", chat)
                    kk = build_keyboard(['Arizani qa\'bul qildim !'])
                    send_message(
                        f"Brigadir {db.get_login(chat)} - '{text}' xom ashyoga ariza berdi! Xom ashyoni 24 soat ichida jo'natishingiz lozim !",
                        db.get_dispetcher("Dispetcher",db.get_userID(chat)[0])[0], kk)
                    dbO.update_Obyom(text, chat, dbO.get_id()[len(dbO.get_id()) - 1])
                    dbO.update_zayavka("location", chat, dbO.get_id()[len(dbO.get_id()) - 1])
                    continue

                if "zakaz" in dbO.get_zayavka(f"{len(dbO.get_id()) - 1}"):
                    # dbO.add_otchyot(db.get_userID(chat),db.get_position(chat),db.get_name(chat),chat,b,"siryo","obyom","location")
                    send_message("Qayta ishlashga jo'natildi !",
                                 chat)  # va lokatsiyani ham jo'nating 🏗️
                    # send_message("Введите название сырья после слова 'Заказать' 🛢️", chat)
                    send_message(
                        "Status bo'limiga kirib , ariza holatini belgilang",
                        db.get_dispetcher("Dispetcher",db.get_userID(chat)[0])[0])
                    dbO.update_zayavka("zakazana", chat, dbO.get_id()[len(dbO.get_id()) - 1])

                # Nastroyki          ######################################################################

                if "nastroyka" in db.get_status(chat):
                    if text == "Tilni tanlash 🇺🇿":
                        keybordl = build_keyboard(['Русский 🇷🇺', 'O\'zbekcha 🇺🇿'])
                        send_message("🇺🇿 Tilni tanlash", chat, keybordl)
                        continue

                    elif text == "FISH ni o'zgartirish ✏":
                        keybord = build_keyboard(['⬅️ Ortga'])
                        send_message("FISH ni kiriting", chat, keybord)
                        db.set_status("izmemitFIO", chat)
                        continue

                    elif text == "Tel raqamni almashtirish 📱":
                        keybord = build_keyboard(['⬅️ Ortga'])
                        send_message("Tel raqamni kiriting", chat, keybord)
                        db.set_status("izmemitTEL", chat)
                        continue

                if "izmemitFIO" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'gartirildi", chat, keyborr)
                    a = text
                    db.update_name(a, chat)
                    db.set_status("nastroyki", chat)
                    continue

                if "izmemitTEL" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    db.set_status("nastroyki", chat)
                    db.update_numb(text, chat)
                    continue

                if text == "Русский 🇷🇺":
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("Изменено", chat, keyborr)
                    print("changed Language")
                    db.update_lang("rus", chat)
                    db.update_position("Бригадир", chat)
                    continue
                if text == "O\'zbekcha 🇺🇿":
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    print("changed Language")
                    db.update_position("Brigadir", chat)
                    db.update_lang("uzb", chat)
                    continue

                if f"{text}" not in listu:
                    keyboardz = build_keyboard(['Ariza ✍', 'Ariza holati 📍', 'Hisobot 📋', 'Sozlamalar ⚙'])
                    send_message("Bo'limni tanlash", chat, keyboardz)
                    continue

                else:
                    print("zayavka")
            else:

                if f"{numb}" in db.get_number(chat):
                    keyboardq = build_keyboard(['Ariza holati 📍', 'Hisobot 📋', 'Sozlamalar ⚙'])
                    send_message("Bo'limni tanlash", chat, keyboardq)
                    db.update_numb(text, chat)
                    continue
                else:
                    print("NUMBER")

                l = dbO.get_zayavki("Brigadir")
                print(l)

                if text == 'Ariza holati 📍':
                    k = build_keyboard(l)
                    # keyboa = build_keyboard(['Загружается', 'В пути', 'Рядом с объектом', 'Доставлено', 'Отменить заявку', 'Назад ⬅️'])
                    send_message("Ariza holati !", chat, k)
                    continue

                if text in l:
                    keyboa = build_keyboard(
                        ['Yuklanmoqda', 'Yo\'lga tushdi', 'Obyekt yaqinida', 'Yetkazib berildi', 'Buyurtmani bekor qilish', 'Ortga ⬅️'])
                    send_message(f"{dbO.get_status(db.get_dispetcher('Brigadir',db.get_userID(chat)[0])[0], text)}", chat, keyboa)
                    db.set_status(text, chat)
                    continue

                if text == 'Hisobot 📋':
                    if len(db.get_dispetcher("Brigadir",db.get_userID(chat)[0])) == 0:
                        d = chat
                    else:
                        d = db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0]
                    s = ""
                    for x in dbO.get_item(d):
                        s += f"{x} \n"
                    send_message(s, chat)
                    dbO.toexel(d)
                    f = open("output2.xlsx", "rb")
                    bot.send_document(chat, f)
                    # send_message(f"{dbO.get_Obname(d)} \n {dbO.get_Obyom(d)}", chat)

                if text == 'Sozlamalar ⚙' or text == "⬅️ Ortga":
                    keyboardn = build_keyboard(
                        ['FISH ni o\'zgartirish ✏', 'Tel raqamni almashtirish 📱', 'Tilni tanlash 🇺🇿', 'Ortga ⬅️'])
                    send_message("Sozlamalar ⚙", chat, keyboardn)
                    db.set_status("nastroyka", chat)
                    continue

                if text == "Arizani qa'bul qildim !":
                    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button_phone = KeyboardButton(text="Obyekt joylashgan yerni jo'natish 📍", request_location=True)
                    keyboard.add(button_phone)
                    bot.send_message(db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0],
                                     "Arizangiz qayta ishlanmoqda ⏳ \n Obyekt joylashgan yerni jo'nating 📍",
                                     reply_markup=keyboard)
                    send_message("Jo'natildi", chat)

                print(db.get_status(chat)[0])

                if text == 'Yuklanmoqda':
                    send_message(f"{db.get_status(chat)[0]} xom ashyo {text}", db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0])
                    send_message("Jo'natildi", chat)
                    dbO.update_status(text, db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0], db.get_status(chat)[0])

                if text == 'Buyurtmani bekor qilish':
                    send_message("Ariza bekor qilinmoqda sababini qoldiring iltimos", chat)
                    dbO.update_status("Ariza bekor qilindi,П", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0], db.get_status(chat)[0])
                    continue

                if len(dbO.get_status(db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0],db.get_status(chat)[0])) != 0:
                    if 'Ariza bekor qilindi,П' == dbO.get_status(db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0], db.get_status(chat)[0])[0]:
                        send_message(f"Ariza bekor qilindi, {db.get_status(chat)[0]} sababi : {text} ", db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0])
                        send_message("Ariza bekor qilindi", chat)
                        dbO.update_status(text, db.get_dispetcher("Бригадир",db.get_status(chat)[0])[0], db.get_status(chat)[0])

                if text == 'Yetkazib berildi':
                    send_message(f"{db.get_status(chat)[0]} Ish bajarildi ✅", db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0])
                    send_message("yetkazib berildi", chat)
                    dbO.update_status(text, db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0], db.get_status(chat)[0])

                if text == 'Yo\'lga tushdi':
                    send_message(f"{db.get_status(chat)[0]} xom ashyo {text}", db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0])
                    send_message("Jo'natildi", chat)
                    dbO.update_status(text, db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0], db.get_status(chat)[0])

                if text == 'Obyekt yaqinida':
                    send_message(f"{db.get_status(chat)[0]} Xom ashyo {text}", db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0])
                    send_message("Jo'natildi", chat)
                    dbO.update_status(text, db.get_dispetcher("Brigadir",db.get_userID(chat)[0])[0], db.get_status(chat)[0])

                # Nastroyki
                if "nastroyka" in db.get_status(chat):
                    if text == "Tilni tanlash 🇺🇿":
                        keybordl = build_keyboard(['Русский 🇷🇺', 'O\'zbekcha 🇺🇿'])
                        send_message("🇺🇿 Tilni tanlash", chat, keybordl)
                        continue

                    elif text == "FISH ni o'zgartirish ✏":
                        keybord = build_keyboard(['⬅️ Ortga'])
                        send_message("FISH ni kiriting", chat, keybord)
                        db.set_status("izmemitFIO", chat)
                        continue

                    elif text == "Tel raqamni almashtirish 📱":
                        keybord = build_keyboard(['⬅️ Ortga'])
                        send_message("Tel raqamni kiriting", chat, keybord)
                        db.set_status("izmemitTEL", chat)
                        continue

                if "izmemitFIO" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    a = text
                    db.update_name(a, chat)
                    db.set_status("nastroyki", chat)
                    continue

                if "izmemitTEL" in db.get_status(chat):
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    db.set_status("nastroyki", chat)
                    db.update_numb(text, chat)
                    continue

                if text == "Русский 🇷🇺":
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("Изменено", chat, keyborr)
                    print("changed Language")
                    db.update_lang("rus", chat)
                    db.update_position("Диспетчер", chat)
                    continue

                if text == "O\'zbekcha 🇺🇿":
                    keyborr = build_keyboard(['⬅️ Ortga'])
                    send_message("O'zgartirildi", chat, keyborr)
                    print("changed Language")
                    db.update_position("Dispetcher", chat)
                    db.update_lang("uzb", chat)
                    continue

                if f"{text}" not in listu:
                    keyboardq = build_keyboard(['Ariza holati 📍', 'Hisobot 📋', 'Sozlamalar ⚙'])
                    send_message("Bo'limni tanlang", chat, keyboardq)
                    continue

                else:
                    print("zayavka")

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True, "resize_keyboard": True}
    return json.dumps(reply_markup)

def build_keyboardContact(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard":keyboard, "request_contact":True, "one_time_keyboard": True, "resize_keyboard": True}
    return json.dumps(reply_markup)

def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def forward_message(chat_id,from_chat_id,disable_notification,message_id, reply_markup=None):
    url = URL + "forwardMessage?chat_id={}&from_chat_id={}&disable_notification={}&message_id={}&parse_mode=Markdown".format(chat_id,from_chat_id,disable_notification,message_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)

def main():
    db.setup()
    dbO.setup()
    db1.setup()
    last_update_id = None

    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
