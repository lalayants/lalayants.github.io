"""Generate the static language editions: python3 scripts/build.py."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://lalayants.github.io"
CONTENT = {'ru': {'name': 'Кирилл Лалаянц',
        'other': 'EN',
        'other_lang': 'en',
        'title': 'Кирилл Лалаянц — Data Scientist · ML и финансы',
        'desc': 'Кирилл Лалаянц — Data Scientist в Сбер КИБ. ML для трейдинга и ценообразования, опыт в '
                'Яндекс Лавке, робототехнике и руководстве R&D-проектом. РЭШ, Сколтех, ИТМО.',
        'skip': 'К содержанию',
        'pdf': 'r',
        'jobs': [('05.2026 — сейчас',
                  'Сбер КИБ',
                  'Data Scientist',
                  ['Разрабатываю и внедряю RL-агентов для ценообразования и оптимизации работы торгового '
                   'деска.']),
                 ('01.2026 — 05.2026',
                  'Яндекс Лавка',
                  'Data Scientist',
                  ['Оптимизировал размеры скидок на основе оценки ценовой эластичности: +5% Front Margin, '
                   'подтверждено масштабным A/B-тестом.',
                   'Автоматизировал процесс заведения и согласования экспериментов: сократил время '
                   'подготовки с нескольких часов до нескольких минут.',
                   'Разработал инфраструктуру сбора и анализа результатов экспериментов и дашборды для '
                   'оценки эластичности.',
                   'Автоматизировал отбор товаров для экспериментов с учётом объёма продаж и популярности.']),
                 ('07.2022 — 06.2025',
                  'Университет ИТМО',
                  'Инженер-исследователь',
                  ['С нуля разработал SLAM-систему для полётов БПЛА в помещениях без GPS: адаптировал '
                   'алгоритм и обеспечил 25 кадров/с на Jetson Xavier в реальных полётах.',
                   'Реализовал safe RL для манипулятора в симуляции: достиг 95% успешных захватов и снизил '
                   'число коллизий.',
                   'Разработал инструменты калибровки положения инструмента и камеры на реальном '
                   'манипуляторе; ошибка калибровки — менее 1 мм.',
                   'Разработал сегментацию розетки по RGB-D облаку точек, расчёт плоскостей и расстояний в '
                   'системе координат робота; решение использовалось для автоматического подключения разъёма '
                   'на реальном манипуляторе.']),
                 ('12.2023 — 07.2024',
                  'Проект BRIZ',
                  'Руководитель команды',
                  ['Организовал разработку системы автономной стыковки двух БПЛА и передачу рабочего '
                   'прототипа заказчику; доля успешных стыковок на реальном оборудовании — более 90%.',
                   'Подобрал команду, составил roadmap, согласовал технические подходы и провёл испытания во '
                   'взаимодействии с руководителем компании.'])],
        'edu': [('2025 — 2027',
                 'Российская экономическая школа',
                 'Магистратура · Экономика, программа «Искусственный интеллект и финтех»'),
                ('2025 — 2027', 'Сколтех', 'Магистратура · Науки о данных'),
                ('2021 — 2025', 'Университет ИТМО', 'Бакалавриат · Робототехника и искусственный интеллект')],
        'tool_label': 'Инструменты',
        'achievement': 'Контрибьютор Ultralytics',
        'achievement_desc': 'Исправил ошибку, возникавшую при переносе моделей на TPU.',
        'award': 'Победитель хакатона StarLine',
        'award_desc': '«Беспилотное будущее», 2023.',
        'language': 'Английский — C1',
        'language_desc': 'TOEFL iBT · 106/120.',
        'footer': 'Кирилл Лалаянц',
        'top': 'Наверх ↑',
        'updated': 'Обновлено в ноябре 2026 года',
        'other_url': '/',
        'nav': ['Опыт', 'Навыки', 'Образование', 'Контакты'],
        'intro': 'Работаю Data Scientist в Сбер КИБ: применяю ML к задачам трейдинга и ценообразования. В '
                 'Яндекс Лавке оптимизировал скидки (+5% Front Margin) и автоматизировал подготовку '
                 'экспериментов. Ранее разрабатывал SLAM и компьютерное зрение для БПЛА и манипуляторов в '
                 'ИТМО и руководил R&D-командой — от её подбора до передачи прототипа заказчику.',
        'cv': 'Резюме (PDF)',
        'experience_title': 'Опыт работы',
        'education_title': 'Образование',
        'recognition': 'Другие проекты и достижения',
        'contact_title': 'Контакты',
        'registrations_title': 'Патент и свидетельство о регистрации ПО',
        'registrations': [('Способ получения сигнала с оценками параметров синхронного двигателя с '
                           'постоянными магнитами',
                           'Патент РФ № 2851523 · 25 ноября 2025 года',
                           'Соавтор. Патентообладатель — АО «Диаконт».',
                           '/assets/documents/patent-2851523.pdf'),
                          ('Полетный контроллер для управления квадрокоптером на базе программного пакета '
                           'mavros',
                           'Свидетельство о регистрации программы для ЭВМ № 2023686859 · 8 декабря 2023 года',
                           'Соавтор. Правообладатель — Университет ИТМО.',
                           '/assets/documents/software-2023686859.pdf')],
        'institutions': 'РЭШ · Сколтех · ИТМО',
        'skills_title': 'Навыки',
        'skills': [('ML и робототехника', 'RL, safe RL, computer vision, SLAM, ROS2'),
                   ('Эконометрика и эксперименты',
                    'A/B-тесты, DiD, uplift-модели, ценовая эластичность, временные ряды'),
                   ('Количественные финансы', 'Оптимизация портфеля, asset pricing, VaR/CVaR'),
                   ('Инструменты', 'Python, SQL, Pandas, NumPy, SciPy, Jupyter, Git, Docker')]},
 'en': {'name': 'Kirill Lalayants',
        'other': 'RU',
        'other_lang': 'ru',
        'title': 'Kirill Lalayants — Data Scientist · ML & Finance',
        'desc': 'Kirill Lalayants — Data Scientist at Sberbank CIB. ML for trading and pricing, experience '
                'at Yandex Lavka, robotics and R&D team leadership. NES, Skoltech, ITMO.',
        'skip': 'Skip to content',
        'pdf': 'e',
        'jobs': [('May 2026 — present',
                  'Sberbank CIB',
                  'Data Scientist',
                  ['Develop and implement RL agents for pricing and trading desk optimization.']),
                 ('Jan 2026 — May 2026',
                  'Yandex Lavka',
                  'Data Scientist',
                  ['Optimized discount levels using price elasticity estimates, increasing Front Margin by '
                   '5%, as confirmed by a large-scale A/B test.',
                   'Automated experiment setup and approval, reducing preparation time from several hours to '
                   'a few minutes.',
                   'Built infrastructure for collecting and analyzing experiment results, along with '
                   'dashboards for price elasticity analysis.',
                   'Automated product selection for experiments based on sales volume and popularity.']),
                 ('Jul 2022 — Jun 2025',
                  'ITMO University',
                  'Research Engineer',
                  ['Built a SLAM system from scratch for GPS-denied indoor UAV flights: adapted the '
                   'algorithm and achieved 25 FPS on Jetson Xavier in real-world flights.',
                   'Implemented safe RL for a manipulator in simulation, achieving a 95% grasp success rate '
                   'and reducing collisions.',
                   'Developed tools to calibrate tool and camera poses on a real manipulator, with errors '
                   'below 1 mm.',
                   'Developed socket segmentation from RGB-D point clouds, plane estimation and distance '
                   'calculations in the robot coordinate frame; the system was used for automated connector '
                   'insertion on a real manipulator.']),
                 ('Dec 2023 — Jul 2024',
                  'BRIZ Project',
                  'Team Lead',
                  ['Led the development of an autonomous docking system for two UAVs: achieved a docking '
                   'success rate above 90% on real hardware and delivered a working prototype to the client.',
                   'Assembled the team, set the roadmap, approved technical approaches, ran tests and worked '
                   'with company leadership.'])],
        'edu': [('2025 — 2027', 'New Economic School', 'Master’s program · AI & FinTech'),
                ('2025 — 2027', 'Skoltech', 'Master’s program · Data Science'),
                ('2021 — 2025', 'ITMO University', 'B.Sc. · Robotics & Artificial Intelligence')],
        'tool_label': 'Toolkit',
        'achievement': 'Ultralytics contributor',
        'achievement_desc': 'Fixed a bug that occurred when moving models to a TPU.',
        'award': 'StarLine Hackathon winner',
        'award_desc': '“Autonomous Future”, 2023.',
        'language': 'English · Advanced',
        'language_desc': 'TOEFL iBT · 106/120.',
        'footer': 'Kirill Lalayants',
        'top': 'Back to top ↑',
        'updated': 'Updated November 2026',
        'other_url': '/ru/',
        'nav': ['Experience', 'Skills', 'Education', 'Contact'],
        'intro': 'I’m a Data Scientist at Sberbank CIB, applying ML to trading and pricing. At Yandex Lavka, '
                 'I optimized discounts (+5% Front Margin) and automated experiment setup. Previously, I '
                 'developed SLAM and computer vision systems for UAVs and manipulators at ITMO and led an '
                 'R&D project from team formation to prototype delivery.',
        'cv': 'CV (PDF)',
        'experience_title': 'Experience',
        'education_title': 'Education',
        'recognition': 'Contributions & achievements',
        'contact_title': 'Contact',
        'registrations_title': 'Patent & software registration',
        'registrations': [('Method for obtaining a signal with parameter estimates of a permanent-magnet '
                           'synchronous motor',
                           'Russian patent No. 2851523 · 25 November 2025',
                           'Co-inventor. Patent holder: Diakont JSC.',
                           '/assets/documents/patent-2851523.pdf'),
                          ('Quadcopter flight controller based on the mavros software package',
                           'Software registration No. 2023686859 · 8 December 2023',
                           'Co-author. Rights holder: ITMO University.',
                           '/assets/documents/software-2023686859.pdf')],
        'institutions': 'NES · Skoltech · ITMO',
        'skills_title': 'Skills',
        'skills': [('ML & robotics', 'RL, safe RL, computer vision, SLAM, ROS2'),
                   ('Econometrics & experiments',
                    'A/B testing, DiD, uplift modeling, price elasticity, time series'),
                   ('Quantitative finance', 'Portfolio optimization, asset pricing, VaR/CVaR'),
                   ('Tools', 'Python, SQL, Pandas, NumPy, SciPy, Jupyter, Git, Docker')]}}

def render(lang, c):
    route = '/' if lang == 'en' else '/ru/'
    url = ORIGIN + route
    schema = {
        '@context': 'https://schema.org', '@type': 'ProfilePage',
        'inLanguage': lang, 'url': url,
        'mainEntity': {
            '@type': 'Person', '@id': ORIGIN + '/#person',
            'name': 'Kirill Lalayants', 'alternateName': 'Кирилл Лалаянц',
            'url': ORIGIN + '/', 'jobTitle': 'Data Scientist', 'description': c['desc'],
            'worksFor': {'@type': 'Organization', 'name': 'Sberbank CIB'},
            'alumniOf': {'@type': 'CollegeOrUniversity', 'name': 'ITMO University'},
            'sameAs': ['https://github.com/lalayants', 'https://linkedin.com/in/lalayants',
                       'https://t.me/kirill_lalayants'],
        },
    }
    nav = ''.join(f'<a href="#{anchor}">{label}</a>' for anchor, label in
                  zip(['experience', 'skills', 'education', 'contact'], c['nav']))
    jobs = '\n'.join(
        f'<li class="job"><div class="entry-heading"><h3>{company}</h3>'
        f'<span class="date">{date}</span></div><p class="role">{role}</p>'
        '<ul class="job-points">' + ''.join(f'<li>{escape(point)}</li>' for point in points)
        + '</ul></li>' for date, company, role, points in c['jobs'])
    education = '\n'.join(
        f'<li class="education-item"><div class="entry-heading"><h3>{school}</h3>'
        f'<span class="date">{date}</span></div><p>{degree}</p></li>'
        for date, school, degree in c['edu'])
    registrations = '\n'.join(
        f'<li class="registration"><h3><a href="{path}">{escape(title)}</a></h3>'
        f'<p class="registration-meta">{escape(metadata)} · PDF</p>'
        f'<p class="registration-credit">{escape(credit)}</p></li>'
        for title, metadata, credit, path in c['registrations'])
    skills = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(items)}</dd></div>'
                     for label, items in c['skills'])
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#fafaf8">
<title>{escape(c['title'])}</title>
<meta name="description" content="{escape(c['desc'], quote=True)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{ORIGIN}/">
<link rel="alternate" hreflang="ru" href="{ORIGIN}/ru/">
<link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
<meta property="og:type" content="profile">
<meta property="og:title" content="{escape(c['title'], quote=True)}">
<meta property="og:description" content="{escape(c['desc'], quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{'ru_RU' if lang == 'ru' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if lang == 'ru' else 'ru_RU'}">
<meta property="og:site_name" content="Kirill Lalayants">
<meta property="og:image" content="{ORIGIN}/assets/images/social-preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Kirill Lalayants — Data Scientist">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body id="top">
<a class="skip-link" href="#main">{c['skip']}</a>
<div class="page">
<header class="header">
<a class="home-link" href="{route}">lalayants</a>
<nav aria-label="{'Основная навигация' if lang == 'ru' else 'Main navigation'}">{nav}</nav>
<a class="language" href="{c['other_url']}" lang="{c['other_lang']}" hreflang="{c['other_lang']}" aria-label="{'Switch to English' if lang == 'ru' else 'Переключить на русский'}">{c['other']}</a>
</header>
<main id="main">
<section class="about" aria-labelledby="name">
<h1 id="name">{c['name']}</h1>
<p class="occupation">Data Scientist · ML &amp; Finance</p>
<p>{c['intro']}</p>
<p class="institutions"><a href="#education">{c['institutions']}</a></p>
<div class="profile-links"><a href="/assets/cvs/Lalayants_cv_{c['pdf']}.pdf" download>{c['cv']}</a><a href="https://github.com/lalayants">GitHub</a><a href="https://linkedin.com/in/lalayants">LinkedIn</a><a href="mailto:lalayantskirill@gmail.com">Email</a></div>
</section>
<section id="experience" aria-labelledby="experience-title">
<h2 id="experience-title">{c['experience_title']}</h2>
<ul class="entries jobs">
{jobs}
</ul>
</section>
<section id="skills" aria-labelledby="skills-title">
<h2 id="skills-title">{c['skills_title']}</h2>
<dl class="skills-list">{skills}</dl>
</section>
<section id="education" aria-labelledby="education-title">
<h2 id="education-title">{c['education_title']}</h2>
<ul class="entries education">
{education}
</ul>
</section>
<section id="registrations" aria-labelledby="registrations-title">
<h2 id="registrations-title">{c['registrations_title']}</h2>
<ul class="entries registrations">
{registrations}
</ul>
</section>
<section aria-labelledby="other-title">
<h2 id="other-title">{c['recognition']}</h2>
<ul class="notes">
<li><a href="https://github.com/ultralytics/ultralytics/pull/16576">{c['achievement']}</a><span>{c['achievement_desc']}</span></li>
<li><span class="note-title">{c['award']}</span><span>{c['award_desc']}</span></li>
<li><span class="note-title">{c['language']}</span><span>{c['language_desc']}</span></li>
</ul>
</section>
<section id="contact" aria-labelledby="contact-title">
<h2 id="contact-title">{c['contact_title']}</h2>
<div class="contact-links"><a href="mailto:lalayantskirill@gmail.com">lalayantskirill@gmail.com</a><a href="https://t.me/kirill_lalayants">@kirill_lalayants</a></div>
</section>
</main>
<footer><span>{c['updated']}</span><a href="#top">{c['top']}</a></footer>
</div>
</body>
</html>
'''


for lang, content in CONTENT.items():
    path = ROOT / ('index.html' if lang == 'en' else 'ru/index.html')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render(lang, content))

# Retain the old English URL for bookmarks, with the root as its canonical.
legacy = ROOT / 'en/index.html'
legacy.parent.mkdir(parents=True, exist_ok=True)
legacy.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="0; url=/">
<link rel="canonical" href="{ORIGIN}/">
<title>Kirill Lalayants</title></head>
<body><p><a href="/">Kirill Lalayants — personal website</a></p></body></html>
''')
print('Built English at /, Russian at /ru/, and redirect from /en/.')
