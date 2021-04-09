import telebot as tb
from tinput import *
global i
i=0
global P
global R
global j
j=0
P,R=tinput()
bot = tb.TeleBot(TOKEN)
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, f'Привет, {message.from_user.first_name}.\n Я бот-квест на день рождения. \n Готов начать? (Да/Нет)')
@bot.message_handler(commands=['restart'])
def restart(message):
	global i
	i=0
	bot.send_message(message.from_user.id, 'Перезагрузка...')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	global i
	global P
	global R
	global j

	if i==0 and j==0 and message.text.lower() == 'да':
		bot.send_message(message.from_user.id, 'Отлично! Тогда держи первую подсказку:')
		bot.send_message(message.from_user.id,P[i])
		j=1
	elif message.text.lower() == R[i] and i<len(P)-2:
		i+=1
		bot.send_message(message.from_user.id, "Молодец! Продолжай в том же духе:")
		bot.send_message(message.from_user.id,P[i])
	elif message.text.lower() == R[i] and i==len(P)-2:
		i+=1
		bot.send_message(message.from_user.id, "Ура! Ты завершил квест! Иди, и прими награду:")
		bot.send_message(message.from_user.id,P[i])
	else:
		bot.send_message(message.from_user.id, 'Ответ неверный. Подумай ещё раз')
bot.polling(none_stop=True)
