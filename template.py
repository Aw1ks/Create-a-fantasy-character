import random

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

# пишем код для получения данных карточки
skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]

list_races = [
    'Люминары',
    'Кристаллы',
    'Аэроиды',
    'Терраги'
]

list_сlasses = [
    'Маг',
    'Воин',
    'Охотник',
    'Ассасин',
    'Бард'
]

clases_base = {
    'Маг': {
        'intelligence': 15,
        'strength': random.randint(1, 3),
        'agility': random.randint(1, 3),
        'luck': random.randint(1, 3),
        'temper': random.randint(1, 3),
        'image_path': 'images/wizard.png',
    },
    'Воин': {
        'strength': 15,
        'intelligence': random.randint(1, 3),
        'agility': random.randint(1, 3),
        'luck': random.randint(1, 3),
        'temper': random.randint(1, 3),
        'image_path': 'images/warrior.png',
    },
    'Охотник': {
        'agility': 15,
        'strength': random.randint(1, 3),
        'intelligence': random.randint(1, 3),
        'luck': random.randint(1, 3),
        'temper': random.randint(1, 3),
        'image_path': 'images/archer.png',
    },
    'Ассасин': {
        'luck': 15,
        'strength': random.randint(1, 3),
        'agility': random.randint(1, 3),
        'intelligence': random.randint(1, 3),
        'temper': random.randint(1, 3),
        'image_path': 'images/assasin.png',
    },
    'Бард': {
        'temper': 15,
        'strength': random.randint(1, 3),
        'agility': random.randint(1, 3),
        'intelligence': random.randint(1, 3),
        'luck': random.randint(1, 3),
        'image_path': 'images/bard.webp',
    },
}

user_name = input('\nВведите имя пользователя: ')
user_race = input('\nВыберите расу из предложенных:\n' + '\n'.join(list_races) + '\n')
user_class = input('\nВыберите класс из предложенных:\n' + '\n'.join(list_сlasses) + '\n')

characteristics_selected_class = clases_base[user_class]
selected_skills = random.sample(skills, 3)

rendered_page = template.render(
    name=user_name.capitalize(),
    race=user_race.capitalize(),
    character_class=user_class.capitalize(),

    strength=characteristics_selected_class['strength'],
    agility=characteristics_selected_class['agility'],
    intelligence=characteristics_selected_class['intelligence'],
    luck=characteristics_selected_class['luck'],
    temper=characteristics_selected_class['temper'],

    image=characteristics_selected_class['image_path'],

    first_skill=selected_skills[0],
    second_skill=selected_skills[1],
    third_skill=selected_skills[2],
    # пишем код, что добавляется к карточке
)

with open(f'index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)