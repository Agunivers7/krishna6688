
import telebot
token = "5546235142:AAGUa1r-5_N1joxXLWDvcjf8uUJjs2SgShA"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

print("Running Bot... ") 
bot.polling()
