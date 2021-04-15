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


@bot.callback_query_handler(func=lambda call: call.data == 'memes' or call.data == 'quotes' or call.data == 'organisation')
def callback_worker(call):
    if call.data == 'memes':
        bot.send_message(call.message.chat.id, '''В каждом задании этого раздела вам будет показан мем, 
связанный с нашим потоком. Вам нужно будет выбрать один вариант ответа или ввести слово.''')
    elif call.data == 'quotes':
        bot.send_message(call.message.chat.id, '''В этом разделе вам будут представлены цитаты преподавателей. 
Отгадайте, кому они принадлежат.''')
    elif call.data == 'organisation':
        bot.send_message(call.message.chat.id, '''В этом разделе будут вопросы, связанные с учебным процессом на фикле. 
Выберите верный вариант ответа или введите слово.''')
        
        
        
        
        
        keyboard_org = types.ReplyKeyboardMarkup()
        key_var1 = types.KeyboardButton("фонетика")
        key_var2 = types.KeyboardButton("социолингвистика")
        key_var3 = types.KeyboardButton("академическое письмо")
        key_var4 = types.KeyboardButton("пары по языкам")
        keyboard_org.row(key_var1, key_var2)
        keyboard_org.row(key_var3, key_var4)
        
        def callback_worker_org(org1):
            if org1.text == 'фонетика':
                r = bot.send_message(org1.chat.id, 'Верно!')
                markup = types.ReplyKeyboardMarkup()
                itembtna = types.KeyboardButton('Юрий Александрович')
                itembtnv = types.KeyboardButton('Михаил Александрович')
                itembtnc = types.KeyboardButton('Владимир Владимирович')
                itembtnd = types.KeyboardButton('Андриан Викторович')
                markup.row(itembtna, itembtnv) 
                markup.row(itembtnc, itembtnd) 
                bot.send_message(org1.chat.id, "Как зовут Ландера?", reply_markup=markup)
                bot.register_next_step_handler(r, callback_worker_org2)
            elif org1.text == 'социолингвистика' or org1.text == 'академическое письмо' or org1.text == 'пары по языкам':
                r = bot.send_message(org1.chat.id, 'Нет(')
                markup = types.ReplyKeyboardMarkup()
                itembtna = types.KeyboardButton('Юрий Александрович')
                itembtnv = types.KeyboardButton('Михаил Александрович')
                itembtnc = types.KeyboardButton('Владимир Владимирович')
                itembtnd = types.KeyboardButton('Андриан Викторович')
                markup.row(itembtna, itembtnv) 
                markup.row(itembtnc, itembtnd) 
                bot.send_message(org1.chat.id, "Как зовут Ландера?", reply_markup=markup)
                bot.register_next_step_handler(r, callback_worker_org2)

        
        r1 = bot.send_message(call.message.chat.id, 'Какие семинары загадочно исчезают из РУЗа?', reply_markup=keyboard_org)
        bot.register_next_step_handler(r1, callback_worker_org)
        
        
        def callback_worker_org3(org3):
            if org3.text == '4':
                bot.send_message(org3.chat.id, 'Да!')
            else:
                bot.send_message(org3.chat.id, 'Нет(')
                
            
               
        
        
        def callback_worker_org2(org2):
            if org2.text == 'Юрий Александрович':
                r2 = bot.send_message(org2.chat.id, 'Верно!')
                bot.send_message(org2.chat.id, "На каком этаже находится учебный офис ФиКЛ? Введите число")
                bot.register_next_step_handler(r2, callback_worker_org3)
            elif org2.text == 'Михаил Александрович' or org2.text == 'Владимир Владимирович' or org2.text == 'Андриан Викторович':
                r2 = bot.send_message(org2.chat.id, 'Нет(')
                bot.send_message(org2.chat.id, "На каком этаже находится учебный офис ФиКЛ? Введите число")
                bot.register_next_step_handler(r2, callback_worker_org3)
        
     
            
bot.polling()


