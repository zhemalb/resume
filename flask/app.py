from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

translations = {
    'ru': {
        'title': 'Альберт Жемуков | Студент НИУ ВШЭ',
        'hello': 'Привет! Я',
        'fullname': 'Альберт Жемуков',
        'promo_text': (
            'Я студент НИУ ВШЭ, факультета компьютерных наук. '
            'Увлечен программированием, хакатонами и развитием в IT-сфере.'
        ),
        'btn_write_me': 'Написать мне',
        'about_me': 'Обо мне',
        'projects': 'Проекты',
        'cooperation': 'Сотрудничество',
        'skills': 'Навыки',
        'my_goals': 'Мои цели',
        'goals_text_1': '1. Получить опыт разработки в крупной компании.',
        'goals_text_2': '2. Закончить университет.',
        'contact_text': 'Если вам интересно сотрудничество или у вас есть вопросы, пишите:',
        'made_with_love': 'Сделано с любовью в 2024 году.',

        # Тексты в разделе "Обо мне"
        'about_section_text': (
            'Я — студент Высшей Школы Экономики (НИУ ВШЭ), увлечен программированием, '
            'изучаю математику и компьютерные науки. Мне 19 лет, но на момент проверки скорее всего '
            'мне уже 20. Люблю слушать современный хип-хоп.'
        ),

        # Заголовки проектов
        'img_processor_title': 'Обработчик Изображений',
        'img_processor_date': 'Март 2024',
        'img_processor_desc': (
            'Разработал программу для работы с BMP-изображениями, включая фильтры '
            'и терминальный парсер.'
        ),
        'tma_bot_title': 'Телеграм-бот TMA',
        'tma_bot_date': 'Июль 2024',
        'tma_bot_desc': (
            'Создал бота для планирования задач и расписаний.'
        ),
        'time_management_title': 'Приложение для тайм-менеджмента',
        'time_management_date': 'Июль – Август 2024',
        'time_management_desc': (
            'Разработал GTD-приложение для планирования задач.'
        ),
        'hackathon_platform_title': 'Онлайн-платформа для хакатонов',
        'hackathon_platform_date': 'Сентябрь 2024, разработка продолжается',
        'hackathon_platform_desc': (
            'Разработал платформу для соревнований с микросервисной архитектурой.'
        ),

        # Технологии
        'technologies': 'Технологии',
        'backend': 'Бэкенд:',
        'frontend': 'Фронтенд:',
        'databases': 'Базы данных:',
        'devops': 'DevOps:',

        # Языки программирования
        'programming_languages': 'Языки программирования',

    },
    'en': {
        'title': 'Albert Zhemukov | HSE Student',
        'hello': 'Hello! I am',
        'fullname': 'Albert Zhemukov',
        'promo_text': (
            'I am a student of HSE, Faculty of Computer Science. '
            'I am passionate about programming, hackathons, and IT development.'
        ),
        'btn_write_me': 'Write to me',
        'about_me': 'About me',
        'projects': 'Projects',
        'cooperation': 'Cooperation',
        'skills': 'Skills',
        'my_goals': 'My Goals',
        'goals_text_1': '1. Gain development experience in a large company.',
        'goals_text_2': '2. Finish the university.',
        'contact_text': 'If you are interested in collaboration or have any questions, feel free to contact me:',
        'made_with_love': 'Made with love in 2024.',

        # About me
        'about_section_text': (
            'I am a student of Higher School of Economics (HSE). '
            'I enjoy programming, mathematics, and computer science. I am 19 years old, but by the time you '
            'check this, I might already be 20. I love listening to modern hip-hop.'
        ),

        # Projects
        'img_processor_title': 'Image Processor',
        'img_processor_date': 'March 2024',
        'img_processor_desc': (
            'Developed a program to work with BMP images, including filters and a terminal parser.'
        ),
        'tma_bot_title': 'TMA Telegram Bot',
        'tma_bot_date': 'July 2024',
        'tma_bot_desc': (
            'Created a bot for task planning and scheduling.'
        ),
        'time_management_title': 'Time-Management App',
        'time_management_date': 'July – August 2024',
        'time_management_desc': (
            'Developed a GTD application for task planning.'
        ),
        'hackathon_platform_title': 'Hackathon Online Platform',
        'hackathon_platform_date': 'September 2024, development in progress',
        'hackathon_platform_desc': (
            'Developed a competition platform with a microservice architecture.'
        ),

        # Technologies
        'technologies': 'Technologies',
        'backend': 'Backend:',
        'frontend': 'Frontend:',
        'databases': 'Databases:',
        'devops': 'DevOps:',

        # Programming languages
        'programming_languages': 'Programming Languages',
    }
}


@app.route("/")
def main():
    lang = request.cookies.get('lang', 'ru')
    return render_template("index.html", lang=lang, translations=translations.get(lang, translations['ru']))


@app.route("/change-lang/<lang>")
def change_lang(lang):
    if lang not in translations:
        lang = 'ru'
    response = make_response(redirect(url_for('main')))
    response.set_cookie('lang', lang, max_age=60 * 60 * 24 * 30)
    return response


@app.route("/resume")
def resume():
    lang = request.cookies.get('lang', 'ru')
    return render_template("index.html", lang=lang, translations=translations.get(lang, translations['ru']))


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


if __name__ == '__main__':
    app.run(port=5002, debug=True)
