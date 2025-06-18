from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')

# пишем код для получения данных карточки
user_name = input('Введите имя пользователя: ')

rendered_page = template.render(
    name=user_name.capitalize(),
    # пишем код, что добавляется к карточке
)

with open(f'index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)