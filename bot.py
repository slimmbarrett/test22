from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Константы
BOT_TOKEN = '8158202881:AAHRytlN_gibZ9EwNQR_civzgxCvSYU4tHI'
CHANNEL_ID = 'cashgeneratorUBT'
CHANNEL_URL = 'https://t.me/cashgeneratorUBT'
WIN_URL = 'https://1wxxlb.com/casino/list?open=register&p=dsgq'  # Ссылка на регистрацию 1WIN
WEB_APP_URL = 'https://mine1win.vercel.app/'

def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    # Кнопка с веб-приложением
    keyboard = [
        [InlineKeyboardButton("Начать игру", web_app=WebAppInfo(url=f"{WEB_APP_URL}?mode=full"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем приветственное сообщение с кнопкой
    update.message.reply_text(
        'Добро пожаловать в MineGames! Нажмите кнопку, чтобы начать игру в полноэкранном режиме.',
        reply_markup=reply_markup
    )

def get_game_keyboard():
    """Создает клавиатуру для игры"""
    keyboard = [
        [
            InlineKeyboardButton("1WIN", url=WIN_URL),
            InlineKeyboardButton("Mine 92%✅", web_app=WebAppInfo(url=WEB_APP_URL))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def main() -> None:
    """Основная функция для запуска бота"""
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Обрабатываем команду /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()