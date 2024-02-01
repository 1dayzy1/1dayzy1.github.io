import telebot 
from telebot import types
from telegram import WebAppInfo



bot = telebot.TeleBot('6710926135:AAEoF5GiNnvww1AEGAScxisECeX7YXMWLKw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    btn1 = types.KeyboardButton('О нас📝')
    btn2 = types.KeyboardButton('Наш сайт🌐 ')
    btn3 = types.KeyboardButton('Часто задаваемые вопросы❓')
    btn4 = types.KeyboardButton('💾Наши контактные данные')
    markup.add(btn1, btn2,btn3,btn4,)
    bot.send_message(message.chat.id, f'🖐Привествую тебя, {message.from_user.first_name}!',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'О нас📝':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙Назад')
        markup.add(btn1)
        bot.send_message(message.chat.id,'Описание организации',reply_markup=markup)
    elif message.text == 'Наш сайт🌐':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔗 Ссылка на сайт')
        btn2 = types.KeyboardButton('🔙Назад')
        btn3 = types.KeyboardButton('📱Наше веб-приложение',web_app=WebAppInfo(url='https://zolotoyfestival.ru'))
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id, 'Вы можете открыть сайт здесь или получить ссылку на него',reply_markup=markup)
    elif message.text == '💾Наши контактные данные':
        bot.send_message(message.chat.id, '📞Наш номер телефона:(+7-985-278-01-69) (+7-(916)-132-41-10)\n👨‍👨‍👦‍👦Сообщество ВК:https: //vk.com/id205801841\n📩Почта: mail@zolotoyfestival.ru\n🎬🎥🔴▶Канал YT: https://www.youtube.com/channel/UCSoxstveizJqi84EDhMbsYw')
    elif message.text == 'Часто задаваемые вопросы❓':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙Назад')
        btn2 = types.KeyboardButton('💬Личный вопрос')
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id,'Вопросы и ответы',reply_markup=markup)
    elif message.text == '🔙Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
        btn1 = types.KeyboardButton('О нас📝')
        btn2 = types.KeyboardButton('Наш сайт🌐')
        btn3 = types.KeyboardButton('Часто задаваемые вопросы❓')
        btn4 = types.KeyboardButton('💾Наши контактные данные')
        markup.add(btn1, btn2,btn3,btn4)
        bot.send_message(message.chat.id, f'Что-то случилось, {message.from_user.first_name}?🤔💭',reply_markup=markup)
    elif message.text == '💬Личный вопрос':
        bot.send_message(message.chat.id,'Писать сюда \nВаш контакт')
    elif message.text == '🔗 Ссылка на сайт':
        bot.send_message(message.chat.id,'https://zolotoyfestival.ru')
    else:
        bot.send_message(message.chat.id,'Я тебя не понимаю, выбери одну и кнопок🤷🏻‍♂️')




bot.polling(none_stop= True)