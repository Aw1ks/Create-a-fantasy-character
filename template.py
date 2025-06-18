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

user_name = input('Введите имя пользователя: ')
user_race = input('Выберите расу из предложенных:\n' + '\n'.join(list_races) + '\n')


rendered_page = template.render(
    name=user_name.capitalize(),
    race=user_race,
    # пишем код, что добавляется к карточке
)

with open(f'index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)