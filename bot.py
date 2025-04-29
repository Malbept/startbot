import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Токен бота
API_TOKEN = '7234958924:AAHCz8bNVMTWzoDF0DEeUhXr6eoF57Vpcl0'

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаём Reply-клавиатуру
    reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    reply_button = KeyboardButton(text='Открыть веб-app', web_app=WebAppInfo(url='https://malbept.github.io/ClickNF-/'))
    reply_keyboard.add(reply_button)
    
    # Создаём Inline-клавиатуру
    inline_keyboard = InlineKeyboardMarkup()
    inline_button = InlineKeyboardButton(text='Открыть веб-app', web_app=WebAppInfo(url='https://malbept.github.io/ClickNF-/'))
    inline_keyboard.add(inline_button)
    
    # Отправляем сообщение с обеими клавиатурами
    bot.reply_to(message, 'Нажми кнопку, чтобы открыть приложение!', reply_markup=reply_keyboard)
    bot.send_message(message.chat.id, 'Или используй кнопку ниже:', reply_markup=inline_keyboard)

# Запуск бота
bot.polling()
