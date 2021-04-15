import telebot
from requests import get  # новая штука

bot = telebot.TeleBot('1606668575:AAFLv5Vh3_2EURVsVzaH3hYEVDCja8lgOmU')  # личный бот!!

keyboard = telebot.types.InlineKeyboardMarkup()
key_memes = telebot.types.InlineKeyboardButton(text='Мемы', callback_data='memes')
keyboard.add(key_memes)
key_quotes = telebot.types.InlineKeyboardButton(text='Цитаты преподавателей', callback_data='quotes')
keyboard.add(key_quotes)
key_organisation = telebot.types.InlineKeyboardButton(text='Организация учебного процесса',
                                                      callback_data='organisation')
keyboard.add(key_organisation)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Выбери раздел:', reply_markup=keyboard)


@bot.message_handler(content_types=['text', 'photo', 'audio', 'document'])
def send_text(message):
    bot.send_message(message.chat.id, 'Прости, я тебя не понимаю. Попробуй написать /start')


@bot.callback_query_handler(
    func=lambda call: call.data == 'memes' or call.data == 'quotes' or call.data == 'organisation')
def callback_worker(call):
    if call.data == 'memes':
        bot.send_message(call.message.chat.id, '''В каждом задании этого раздела вам будет показан мем, 
связанный с нашим потоком. Вам нужно будет выбрать один вариант ответа или ввести слово.''')
        bot.send_photo(call.message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/chicken.jpg?raw=true').content)  # про курицу
        mesg = bot.send_message(call.message.chat.id, 'Введите слово:')
        bot.register_next_step_handler(mesg, meme1)
    elif call.data == 'quotes':
        bot.send_message(call.message.chat.id, '''В этом разделе вам будут представлены цитаты преподавателей. 
Отгадайте, кому они принадлежат.''')
    elif call.data == 'organisation':
        bot.send_message(call.message.chat.id, '''В этом разделе будут вопросы, связанные с учебным процессом на фикле. 
Выберите верный вариант ответа или введите слово.''')


@bot.message_handler(func=lambda message: True)
def meme1(message):
    if message.text.lower() == 'курица':
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/phonetics.jpg?raw=true').content)  # не успел сдать тест по фонетике
        keyboard_memes = telebot.types.ReplyKeyboardMarkup(False, True)
        keyboard_memes.row("тест по фонетике")
        keyboard_memes.row("домашку по проге")
        keyboard_memes.row("контрольную по латыни")
        mesg = bot.send_message(message.chat.id, "Не успел сдать ...", reply_markup=keyboard_memes)
        bot.register_next_step_handler(mesg, meme2)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: курица')
        bot.send_photo(message.chat.id,
                       get('https://github.com/ioiimm/drafts/blob/main/bot/img/phonetics.jpg?raw=true').content)
        keyboard_memes = telebot.types.ReplyKeyboardMarkup(False, True)
        keyboard_memes.row("тест по фонетике")
        keyboard_memes.row("домашку по проге")
        keyboard_memes.row("контрольную по латыни")
        mesg = bot.send_message(message.chat.id, "Не успел сдать ...", reply_markup=keyboard_memes)
        bot.register_next_step_handler(mesg, meme2)


def meme2(message):
    if message.text == "тест по фонетике":
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/dobrushina.jpg?raw=true').content)  # здравствуйте, Добрушина
        keyboard_memes = telebot.types.ReplyKeyboardMarkup(False, True)
        keyboard_memes.row("Добрушина, эксперимент")
        keyboard_memes.row("Зибер, тест по артикуляции")
        keyboard_memes.row("Ландер, экспедицию в Индонезию")
        keyboard_memes.row("учебный офис, РУЗ")
        mesg = bot.send_message(message.chat.id, "Здравствуйте ... одобрите ... :", reply_markup=keyboard_memes)
        bot.register_next_step_handler(mesg, meme3)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: тест по фонетике')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/dobrushina.jpg?raw=true').content)  # здравствуйте, Добрушина
        keyboard_memes = telebot.types.ReplyKeyboardMarkup(False, True)
        keyboard_memes.row("Добрушина, эксперимент")
        keyboard_memes.row("Зибер, тест по артикуляции")
        keyboard_memes.row("Ландер, экспедицию в Индонезию")
        keyboard_memes.row("учебный офис, РУЗ")
        mesg = bot.send_message(message.chat.id, "Здравствуйте ... одобрите ... :", reply_markup=keyboard_memes)
        bot.register_next_step_handler(mesg, meme3)


def meme3(message):
    if message.text == "Добрушина, эксперимент":
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/daniel.jpg?raw=true').content)  # Михаил Даниэль
        mesg = bot.send_message(message.chat.id, "Кто на картинке? Введите имя и фамилию.")
        bot.register_next_step_handler(mesg, meme4)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: Добрушина, эксперимент')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/daniel.jpg?raw=true').content)  # Михаил Даниэль
        mesg = bot.send_message(message.chat.id, "Кто на картинке? Введите имя и фамилию.")
        bot.register_next_step_handler(mesg, meme4)


def meme4(message):
    if message.text.lower() == "Михаил Даниэль".lower():
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id,
                       get('https://github.com/ioiimm/drafts/blob/main/bot/img/lms.jpg?raw=true').content)  # лмс
        mesg = bot.send_message(message.chat.id, "Кто / что на фото? Введите одно слово:")
        bot.register_next_step_handler(mesg, meme5)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: Михаил Даниэль')
        bot.send_photo(message.chat.id,
                       get('https://github.com/ioiimm/drafts/blob/main/bot/img/lms.jpg?raw=true').content)  # лмс
        mesg = bot.send_message(message.chat.id, "Кто / что на фото? Введите одно слово:")
        bot.register_next_step_handler(mesg, meme5)


def meme5(message):
    if message.text.lower() == "лмс" or message.text.lower() == "lms":
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/causativ.jpg?raw=true').content)  # каузация
        mesg = bot.send_message(message.chat.id, "Введите слово:")
        bot.register_next_step_handler(mesg, meme6)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: lms или лмс')
        bot.send_photo(message.chat.id, get(
            'https://github.com/ioiimm/drafts/blob/main/bot/img/causativ.jpg?raw=true').content)
        mesg = bot.send_message(message.chat.id, "Введите слово:")
        bot.register_next_step_handler(mesg, meme6)


def meme6(message):
    if message.text.lower() == "каузация" or message.text.lower() == "каузацию":
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
        bot.send_photo(message.chat.id,
                       get('https://github.com/ioiimm/drafts/blob/main/bot/img/stenin.jpg?raw=true').content)  # Стенин
        mesg = bot.send_message(message.chat.id, "Кто на фото? Введите фамилию:")
        bot.register_next_step_handler(mesg, meme6_reply)
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: каузация или каузацию')
        bot.send_photo(message.chat.id,
                       get('https://github.com/ioiimm/drafts/blob/main/bot/img/stenin.jpg?raw=true').content)  # Стенин
        mesg = bot.send_message(message.chat.id, "Кто на фото? Введите фамилию:")
        bot.register_next_step_handler(mesg, meme6_reply)


def meme6_reply(message):
    if message.text.lower() == "стенин":
        bot.send_message(message.chat.id, 'Отлично, это правильный ответ!')
    else:
        bot.send_message(message.chat.id, 'Это неверно, правильный ответ: Стенин')


bot.polling()
