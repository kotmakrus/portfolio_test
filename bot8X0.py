import telebot
from telebot import types
token = '6357091519:AAHn9_fUNjzx9bZrGVjbU48KMn9ZSL4DZwY'
bot = telebot.TeleBot(token)
game = 'X'
buttons = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


@bot.message_handler(commands=['play'])
def play(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=buttons[1], callback_data='1')
    btn2 = types.InlineKeyboardButton(text=buttons[2], callback_data='2')
    btn3 = types.InlineKeyboardButton(text=buttons[3], callback_data='3')

    btn4 = types.InlineKeyboardButton(text=buttons[4], callback_data='4')
    btn5 = types.InlineKeyboardButton(text=buttons[5], callback_data='5')
    btn6 = types.InlineKeyboardButton(text=buttons[6], callback_data='6')

    btn7 = types.InlineKeyboardButton(text=buttons[7], callback_data='7')
    btn8 = types.InlineKeyboardButton(text=buttons[8], callback_data='8')
    btn9 = types.InlineKeyboardButton(text=buttons[9], callback_data='9')

    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    markup.add(btn7, btn8, btn9)

    bot.send_message(message.chat.id, 'Сделайте ход', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def reaction(call):
    global game
    global buttons

    if buttons[int(call.data)] == '.':
        buttons[int(call.data)] = game

    if (buttons[1] == buttons[2] == buttons[3] and buttons[1] != '.') or (buttons[4] == buttons[5] == buttons[6] and buttons[4] != '.') or (buttons[7] == buttons[8] == buttons[9] and buttons[7] != '.'):
        bot.send_message(call.message.chat.id, f'Игра окончена! Победил {game}. Заново: /play')
        buttons = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        game = 'X'
    else:
        bot.send_message(call.message.chat.id, 'Продолжить игру: /play')

    if game == 'X':
        game = '0'
    else:
        game = 'X'



bot.infinity_polling()
