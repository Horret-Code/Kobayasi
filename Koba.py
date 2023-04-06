import telebot
from telebot import types
import random
from random import choice

#Подставлять нужное значение токена
TOKEN = '6222687683:AAEy1DRHX-1WAAZlk450wqoxf1uZ6vPda00'
#Cюда можно вписывать анекдоты
joke_list = ["Штирлиц долго смотрел в одну точку. \nПотом в другую.\n«Двоеточие!» — наконец догадался Штирлиц.",
             "Проснувшись, Штирлиц вспомнил, что вчера на приеме у Мюллера он наговорил лишнего.\nРешив выяснить все разом, он вошел в кабинет и спросил:\n- Мюллер, Вы догадались, что я - русский агент? \n- Нет - признался Мюллер. \n- Ну, слава богу - сказал Штирлиц и со спокойной душой пошел домой.",
             "Штирлиц уже три месяца слал в Центр одну и ту же шифровку: \n4207 1801 2275 4408 \n6872 4589 5533 7928 \n3473 5600 1956 7639 \nНо тщетно, ни на одну из этих кредитных карт не поступало ни копейки зарплаты.",
             "Заходит еврей в бар: \n— Кофе, пожалуйста. \nБармен: \n— Ваш кофе. \n— А можно кофе на пиво поменять?\n— Пожалуйста, ваше пиво. \nВыпивает пиво и идёт на выход. \n— За пиво заплатите! \n— Так я за него кофе отдал! \n— Тогда за кофе! \n— Ну таки я же не пил ваш кофе!",
             "Вместо привычного голубя в окно залетел попугай. \n'Голосовое' - подумал Штирлиц."]
#Сюда можно вписывать приветствия
hello_word = ["Приветствую пользователь, как у вас дела?"]
#Реакции на положительный ответ на вопрос как дела
good_reaction = ["Я рада, что у вас всё хорошо. Вам помочь с чем-то?"]
#Реакции на отрицательный ответ на вопрос как дела
bad_reaction = ["Жаль, что так сложилось. Может я могла бы чем помочь вам?"]

bot = telebot.TeleBot(TOKEN);

#Стартовое сообщение
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Привет! Мне нужна помощь.')
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Приветствую пользователь!', reply_markup=markup)

#Скелет бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text == 'Привет! Мне нужна помощь.' or message.text == '/hub' or message.text == 'Вернуться в главное меню'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расскажи анекдот')
        btn2 = types.KeyboardButton('Расскажи загадку (в разработке)')
        btn3 = types.KeyboardButton('Открыть раздел с заметками (в разработке)')
        btn4 = types.KeyboardButton('Открой раздел с питанием (в разработке)')
        btn5 = types.KeyboardButton('Открой раздел с событиями (в разработке)')
        btn6 = types.KeyboardButton('Помощь с командами быстрого доступа')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
        bot.send_message(message.from_user.id, 'Выберите из списка, то что вам нужно', reply_markup=markup)

    elif (message.text == 'Помощь с командами быстрого доступа' or message.text == '/help'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Пользователь, я могу понять не только текстовые команды, но и набор быстрых команд: \n/hub - возврат в главное меню \n/help - из любого диалога бота вы может вернуться сюда и прочитать этот текст снова \n/joke - я могу рассказать вам анекдот \n/riddle - я могу загадать вам загадку и, в зависимости от вашего ответа, отреагировать на это \n/foodhelper - выдаст вам рецепты вкусной еды, поможет со здоровым питанием, а также подсчитает калории того, что вы съели \n/events - напомнит вам о важных событиях \n/notebook - здесь вы можете оставлять свои заметки',
                         reply_markup=markup)

    elif (message.text == 'Расскажи анекдот' or message.text == '/joke' or message.text == 'Расскажи ещё анекдот'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расскажи ещё анекдот')
        btn2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id,
                         random.choice(joke_list),
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text == 'Расскажи загадку (в разработке)' or message.text == '/riddle'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Нет',
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text == 'Открыть раздел с заметками (в разработке)' or message.text == "/notebook"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "Нет",
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text == "Открой раздел с питанием (в разработке)" or message.text == "/foodhelper"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'Нет',
                         reply_markup=markup, parse_mode='Markdown')

    elif (message.text == "Открой раздел с событиями (в разработке)" or message.text == "/events"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "Нет",
                         reply_markup=markup, parse_mode='Markdown')


#Постоянно обращается к Telegramm на наличие новых сообщений
bot.polling(none_stop=True, interval=0)