import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен бота
TOKEN = '7376905443:AAGF5Qy4aUpPvkCtEyFRKwgWesHx2Wv3m0A'

# Файл для хранения номеров
PHONE_NUMBERS_FILE = 'phone_numbers.txt'

# Функция для записи номера в файл
def save_phone_number(phone_number: str):
    with open(PHONE_NUMBERS_FILE, 'a') as file:
        file.write(f"{phone_number}\n")

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Интернет, ТВ и Мобильная связь", callback_data='internet_tv_mobile')],
        [InlineKeyboardButton("Видеонаблюдение", callback_data='video_surveillance')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Привет, я бот! Что умеет этот бот?\n"
        "Нажмите кнопку ниже, чтобы начать ⬇️\n"
        "Подключай Интернет + ТВ + Мобильная связь от МТС. KION в подарок!\n"
        "📌 Быстрое подключение.\n"
        "📌 Стабильный интернет.\n"
        "📌 Управление просмотром.\n"
        "📌 Выберите категорию ⬇️",
        reply_markup=reply_markup
    )

# Функция обработки нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Убираем ответ с изменением текста и делаем новое сообщение
    if query.data == 'internet_tv_mobile':
        await query.message.reply_text("📡 Тариф №1\n"
                                        "Просто 3 в 1: мобильная связь, интернет и ТВ\n"
                                        "Включено в тариф:")
        await query.message.reply_text("📶 Мобильный и домашний интернет с возможностью выбрать скорость за дополнительную плату\n"
                                        "🍿 Онлайн-кинотеатр KION до 5 устройств одновременно\n"
                                        "📺 Безлимитный интернет при просмотре KION\n"
                                        "📱 Безлимитные мессенджеры (WhatsApp, Telegram, Viber, Discord, Skype, ICQ, МТС Connect, Snapchat, Там-Там)\n"
                                        "🌐 Безлимитные соц сети (ВКонтакте, Однокласники)\n"
                                        "📈 Мобильный интернет 30 Гб\n"
                                        "☎️ Звонки 800 минут по всей России\n"
                                        "✉️ 100 SMS\n"
                                        "📺 IPTV более 200 каналов\n"
                                        "🛡️ Страховой полис на случай повреждения чужой квартиры с возмещением до 100 000 рублей\n"
                                        "💰 Цена по акции 425р/мес базовая 850р")
        await query.message.reply_text("✅ Дополнительные опции:\n"
                                        "⚡️ Опция скорость 200 Мбит/сек - 50 руб/мес\n"
                                        "⚡️ 500 Мбит/сек - 100 руб/мес\n"
                                        "⚡️ 1 Гбит/сек - 250 руб/мес\n"
                                        "👪 Группа для близких\n"
                                        "📞 При переходе с другого оператора полгода бесплатно\n"
                                        "➕ +1 номер 300р/мес\n"
                                        "📊 25 Гб 500 минут 100 SMS")
        await query.message.reply_text("📞 Если вас заинтересовало предложение, пожалуйста, введите ваш номер телефона.")
        
    elif query.data == 'video_surveillance':
        await query.message.reply_text("📱 Управление со смартфона...\n"
                                                                               "🎥 Трансляция 24/7\n"
                                        "🚨 Запись и уведомление при движении\n"
                                        "📅 Хранение записей 7 или 14 дней\n"
                                        "🗣️ Двухсторонняя голосовая связь\n"
                                        "🔍 Full HD камера с ночным режимом")
        await query.message.reply_text("1 камера:\n"
                                        "💵 290р/мес архив 7 дней\n"
                                        "💵 390р/мес 14 дней\n")
        await query.message.reply_text("📞 Если вас заинтересовало предложение, пожалуйста, введите ваш номер телефона.")

# Функция для обработки текстовых сообщений (номер телефона)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_phone = update.message.text
    save_phone_number(user_phone)
    await update.message.reply_text(f"📞 Ваш номер телефона {user_phone} был получен. Спасибо!")

def main():
    # Создаем приложение и передаем ему ваш токен
    application = ApplicationBuilder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик нажатий кнопок
    application.add_handler(CallbackQueryHandler(button))

    # Обработчик для получения номера телефона
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
