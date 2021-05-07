pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot('1751134716:AAHHDwQ1SW5gTSunprNygu-Q7EQh4KSesEY')

from telebot import types
keyboard = telebot.types.InlineKeyboardMarkup()
key_memes = telebot.types.InlineKeyboardButton(text='Мемы', callback_data='memes')
keyboard.add(key_memes)
key_quotes = telebot.types.InlineKeyboardButton(text='Цитаты преподавателей', callback_data='quotes')
keyboard.add(key_quotes)
key_organisation = telebot.types.InlineKeyboardButton(text='Организация учебного процесса', callback_data='organisation')
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
    if call.data == 'quotes':
        bot.send_message(call.message.chat.id, '''В этом разделе тебе будут показаны цитаты преподавателей. Отгадай, кому они принадлежат.''')
	mesg = bot.send_message(call.message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Видите ли вы эту красивую табличку с буквами? Она вам нравится или вызывает ужас? Вы пока подумайте, а я включу «Щенячий патруль»".')
        bot.register_next_step_handler(mesg, quote1)
    elif call.data == 'memes':
        bot.send_message(call.message.chat.id, '''В каждом задании этого раздела вам будет показан мем, связанный с нашим потоком. Вам нужно будет выбрать один вариант ответа или ввести слово.''')
    elif call.data == 'organisation':
        bot.send_message(call.message.chat.id, '''В этом разделе будут вопросы, связанные с учебным процессом на фикле. Выберите верный вариант ответа или введите слово.''')


@bot.message_handler(func=lambda message: True)
def quote1(message):
    if message.text.lower() == 'инна зибер':
        bot.send_message(message.chat.id, 'Совершенно верно! Сразу видно, что смотришь все лекции и читаешь все письма :)')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%98%D0%BD%D0%BD%D0%B0%20%D0%B2%D0%B5%D1%81%D0%B5%D0%BB%D0%B0%D1%8F.jpg?raw=true').content) # Инна веселая
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Надеюсь, скоро станет попроще".')
        bot.register_next_step_handler(mesg, quote2)
    else:
        bot.send_message(message.chat.id, 'Ошибочка! Правильный ответ: Инна Зибер.')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%98%D0%BD%D0%BD%D0%B0%20%D0%B3%D1%80%D1%83%D1%81%D1%82%D0%BD%D0%B0%D1%8F.jpg?raw=true').content) # Инна грустная
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Надеюсь, скоро станет попроще".')
        bot.register_next_step_handler(mesg, quote2)

def quote2(message):
    if message.text.lower() == 'юрий ландер':
        bot.send_message(message.chat.id, 'Совершенно верно! Сразу видно, что смотришь все лекции и читаешь все письма :)')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%9B%D0%B0%D0%BD%D0%B4%D0%B5%D1%80%20%D0%B2%D0%B5%D1%81%D0%B5%D0%BB%D1%8B%D0%B9.jpg?raw=true').content) # Ландер веселый
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Будет чтение разных уровней сложности: иногда попроще, иногда полегче".')
        bot.register_next_step_handler(mesg, quote3)
    else:
        bot.send_message(message.chat.id, 'Ошибочка! Правильный ответ: Юрий Ландер.')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%9B%D0%B0%D0%BD%D0%B4%D0%B5%D1%80%20%D0%B3%D1%80%D1%83%D1%81%D1%82%D0%BD%D1%8B%D0%B9.jpg?raw=true').content) # Ландер грустный
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Будет чтение разных уровней сложности: иногда попроще, иногда полегче".')
        bot.register_next_step_handler(mesg, quote3)
        
def quote3(message):
    if message.text.lower() == 'михаил даниэль':
        bot.send_message(message.chat.id, 'Совершенно верно! Сразу видно, что смотришь все лекции и читаешь все письма :)')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%94%D0%B0%D0%BD%D0%B8%D1%8D%D0%BB%D1%8C%20%D0%B2%D0%B5%D1%81%D0%B5%D0%BB%D1%8B%D0%B9.jpg?raw=true').content) # Даниэль веселый
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Так-так-так-так... Прум-пум-пум. Так. Пуф-пуф-пуф... Так-так-так-так. Щи-щи-щи-щу-щу... А-а-ай! Трррам-пам-пам".')
        bot.register_next_step_handler(mesg, quote4)
    else:
        bot.send_message(message.chat.id, 'Ошибочка! Правильный ответ: Михаил Даниэль.')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%94%D0%B0%D0%BD%D0%B8%D1%8D%D0%BB%D1%8C%20%D0%B3%D1%80%D1%83%D1%81%D1%82%D0%BD%D1%8B%D0%B9.jpg?raw=true').content) # Даниэль грустный
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Так-так-так-так... Прум-пум-пум. Так. Пуф-пуф-пуф... Так-так-так-так. Щи-щи-щи-щу-щу... А-а-ай! Трррам-пам-пам".')
        bot.register_next_step_handler(mesg, quote4)

def quote4(message):
    if message.text.lower() == 'александр подобряев':
        bot.send_message(message.chat.id, 'Совершенно верно! Сразу видно, что смотришь все лекции и читаешь все письма :)')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%9F%D0%BE%D0%B4%D0%BE%D0%B1%D1%80%D1%8F%D0%B5%D0%B2%20%D0%B2%D0%B5%D1%81%D0%B5%D0%BB%D1%8B%D0%B9.jpg?raw=true').content) # Подобряев веселый
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Мне нравится слово «актор», потому что я продался Западу".')
        bot.register_next_step_handler(mesg, quote5)
    else:
        bot.send_message(message.chat.id, 'Ошибочка! Правильный ответ: Александр Подобряев.')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%9F%D0%BE%D0%B4%D0%BE%D0%B1%D1%80%D1%8F%D0%B5%D0%B2%20%D0%B3%D1%80%D1%83%D1%81%D1%82%D0%BD%D1%8B%D0%B9.jpg?raw=true').content) # Подобряев грустный
        mesg = bot.send_message(message.chat.id, 'Чья цитата? Введи сначала имя, потом фамилию преподавателя. \n"Мне нравится слово «актор», потому что я продался Западу".')
        bot.register_next_step_handler(mesg, quote5)
		
def quote5(message):
    if message.text.lower() == 'андриан влахов':
        bot.send_message(message.chat.id, 'Совершенно верно! Сразу видно, что смотришь все лекции и читаешь все письма :)')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%92%D0%BB%D0%B0%D1%85%D0%BE%D0%B2%20%D0%B2%D0%B5%D1%81%D0%B5%D0%BB%D1%8B%D0%B9.jpg?raw=true').content) # Влахов веселый
    else:
        bot.send_message(message.chat.id, 'Ошибочка! Правильный ответ: Андриан Влахов.')
        bot.send_photo(message.chat.id, get('https://github.com/dianaaskarova/photos_project/blob/main/%D0%92%D0%BB%D0%B0%D1%85%D0%BE%D0%B2%20%D0%B3%D1%80%D1%83%D1%81%D1%82%D0%BD%D1%8B%D0%B9.jpg?raw=true').content) # Влахов грустный

bot.polling()