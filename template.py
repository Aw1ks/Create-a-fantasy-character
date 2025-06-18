from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

# пишем код для получения данных карточки
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

user_name = input('\nВведите имя пользователя: ')
user_race = input('\nВыберите расу из предложенных:\n' + '\n'.join(list_races) + '\n')
user_class = input('\nВыберите класс из предложенных:\n' + '\n'.join(list_сlasses) + '\n')



rendered_page = template.render(
    name=user_name.capitalize(),
    race=user_race.capitalize(),
    character_class=user_class.capitalize(),
    # пишем код, что добавляется к карточке
)

with open(f'index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)