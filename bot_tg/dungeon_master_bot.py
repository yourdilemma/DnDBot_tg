'''Основной модуль, реализующий взаимодействие пользователя с ботом внутри тг'''
import telebot
import random
from telebot import types
from functools import partial

npc_races = ["Человек", "Эльф", "Дварф", "Орк", "Фейри", "Демон", "Драконорожденный", "Вампир", "Зверолюд"]
npc_male_names = ["Элрик", "Бренд", "Гаррет", "Кейден", "Лираэль", "Торин", "Финнан", "Морган"]
npc_female_names = ["Илиана", "Сильвия", "Ария", "Мирабель", "Таэрия", "Фэй", "Гвен", "Эльмира"]
npc_professions = ["кузнец", "стражник", "торговец", "трактирщик", "ученый", "контрабандист", "пират", "фермер", "священник", "маг"]
npc_traits = ["угрюмый", "болтливый", "благородный", "трусливый", "эксцентричный", "мнительный", "веселый", "задумчивый", "подозрительный"]
npc_goals = ["заработать денег", "найти родственника", "обрести власть", "выжить", "скрыть правду", "отомстить", "спасти мир"]

quest_types_for_alive = ["Найти", "Убить", "Спасти", "Доставить", "Защитить", "Украсть"]
quest_types_for_stuff = ["Найти", "Доставить", "Защитить", "Украсть"]
quest_targets_alive = ["опасного монстра", "похищенного чиновника", "древнего мага", "тысячелетнего лича", "фамильяра"]
quest_targets_stuff = ["древний артефакт", "редкое зелье", "затерянные сокровища", "секретные документы", "ядовитое растение"]
quest_locations = ["в заброшенном храме", "на пиратском корабле", "в подземном бункере", "в самом сердце столицы", "в заколдованном лесу", "среди дюн пустыни"]
quest_clients = ["старый мудрец", "испуганный горожанин", "таинственный незнакомец", "местный правитель", "капитан стражников", "молодой ученик"]

loot_common = ["10 медных монет", "потрёпанный дорожный плащ", "связка вяленого мяса", "простой кинжал", "небольшой мешочек с солью"]
loot_uncommon = ["50 серебряных монет", "целебное зелье (20 HP)", "серебряный кулон", "качественная стальная броня", "свиток заклинания Удар молнии"]
loot_rare = ["100 золотых монет", "магический посох", "кольцо с хранилищем", "редкий алхимический ингредиент", "карта сокровищ"]
loot_legendary = ["Древний артефакт Бога воды", "Яйцо дракона", "Корона короля-лича", "Ключ от межмирового портала", "Сердце звезды"]

class Bot:
    '''Функция сетапит переменную из main'''
    def setup(self, bot):
        '''Функция начала общения, ответ на команду /start'''
        @bot.message_handler(commands = ['start']) #обработчик команды старт
        def send_welcome(message):
            welcome_text = """
Приветствую, Мастер! 
Я твой верный помощник в настольных приключениях. Я могу создать случайного NPC, бросить вызов героям новым квестом или найти для них сокровища в древней гробнице.
Используй /help, чтобы увидеть все мои способности.
"""
            bot.reply_to(message, welcome_text)

        '''Функция обработки команды /help - выводит список доступных команд для пользователя'''
        @bot.message_handler(commands=['help'])
        def send_help(message):
            help_text = """
Я могу по команде:
/npc - Создать случайного неигрового персонажа
/quest - Сгенерировать идею для квеста
/loot - Найти случайную добычу в сундуке
/roll - Бросить кости (например, 2d6+1)
"""
            bot.reply_to(message, help_text)
    
        @bot.message_handler(commands=['npc'])
        def generate_npc(message):
            gender = random.choice(['мужчина', 'женщина'])
            if gender == 'мужчина':
                 name = random.choice(npc_male_names)
            else:
                 name = random.choice(npc_female_names)
            race = random.choice(npc_races)
            profession = random.choice(npc_professions)
            trait = random.choice(npc_traits)
            goal = random.choice(npc_goals)

            npc_text = f"""Случайный NPC:
**Имя:** {name}
**Пол:** {gender}
**Раса:** {race}
**Профессия:** {profession}
**Характер:** {trait}
**Тайная цель:** {goal}
"""
            bot.reply_to(message, npc_text, parse_mode='Markdown')

        @bot.message_handler(commands=['quest'])
        def generate_quest(message):
            q_type = random.choice(['alive', 'stuff'])
            q_target = random.choice(['alive', 'stuff'])
            if q_type == 'alive':
                final_q_type = random.choice(quest_types_for_alive)
                final_q_target = random.choice(quest_targets_alive)
            else:
                final_q_type = random.choice(quest_types_for_stuff)
                final_q_target = random.choice(quest_targets_stuff)
            q_location = random.choice(quest_locations)
            q_client = random.choice(quest_clients)

            quest_text = f"""Случайный квест:
**Клиент:** {q_client}
**Задача:** {final_q_type} {final_q_target}
**Локация:** {q_location}
"""
            bot.reply_to(message, quest_text, parse_mode='Markdown')