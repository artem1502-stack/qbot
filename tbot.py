NAME="qioqiijeqifqieikcsmkkovqwef_bot"
TOKEN="1664123952:AAEM-8BZAhGcKWu5kTGvB-gvzovde5yIFrE"
import telebot as tb
bot = tb.TeleBot("TOKEN")
@bot.message_handler(commands=[])
def send_welcome(message):
	bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.from_user.id, 'Привет!')
	else:
		bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
bot.polling(none_stop=True)
