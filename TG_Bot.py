import telebot
from parse import main

token = '5751633149:AAG1Fi6EXla4Im6ldvpVaVmcd6ngIoY1Bpg'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Hi!, {0.first_name}!\nI'm - <b>{1.first_name}</b>, bot which give statistics about PSN profile".format(message.from_user, bot.get_me()), parse_mode='html')
    bot.register_next_step_handler(message, get_info)

@bot.message_handler(content_types=["text"])
def text(message):
    get_info(message)

def get_info(message):
    data = main(message.text)
    try:
        string = f"PSN ID: {data['name']}\n" \
                     f"Player level: {data['level']}\n" \
                     f"Achivment bronze: {data['bronze']}\n" \
                     f"Achivment silver: {data['silver']}\n" \
                     f"Achivment gold: {data['gold']}\n" \
                     f"Achivment platinum: {data['platinum']}\n" \
                     f"Total achivment: {data['total']}\n" \
                     f"Total games: {data['games']}"
        bot.send_photo(message.chat.id, data['avatar'])
        bot.send_message(message.chat.id, string)
    except:
        bot.send_message(message.chat.id, data)


bot.polling(none_stop=True)