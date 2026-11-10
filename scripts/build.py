"""Generate the static language editions: python3 scripts/build.py."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://lalayants.github.io"
FIPS_REGISTRY = "https://www.fips.ru/registers-doc-view/fips_servlet"
REGISTRATION_DOCUMENTS = {
    'patent': ('2851523', 'RUPAT'),
    'software': ('2023686859', 'EVM'),
}
CONFERENCE_LINKS = {
    2024: (
        ('abstract', 'https://kmu.itmo.ru/digests/article/12672'),
        ('abstract_pdf', 'https://kmu.itmo.ru/file/download/application/40016'),
        ('program', 'https://kmu.itmo.ru/file/download/congress/35#page=73'),
    ),
    2023: (
        ('collection', 'https://kmu.itmo.ru/digests/section/661'),
        ('program', 'https://kmu.itmo.ru/file/download/674#page=87'),
        ('recommendation', 'https://kmu.itmo.ru/file/download/646#page=66'),
    ),
}
CONTENT = {'ru': {'name': 'Кирилл Лалаянц',
        'other': 'EN',
        'other_lang': 'en',
        'title': 'Кирилл Лалаянц — Data Scientist · ML и финансы',
        'desc': 'Кирилл Лалаянц — Data Scientist в Сбер КИБ. ML для трейдинга и ценообразования, финансы и '
                'экономика. Опыт в Яндекс Лавке и исследованиях в ИТМО. РЭШ, Сколтех, ИТМО.',
        'skip': 'К содержанию',
        'pdf': 'r',
        'jobs': [('05.2026 — сейчас',
                  'Сбер КИБ',
                  'Data Scientist',
                  ['Разрабатываю и внедряю RL-агентов для ценообразования и оптимизации работы торгового '
                   'деска.']),
                 ('01.2026 — 05.2026',
                  'Яндекс Лавка',
                  'Data Analyst',
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
                   'Реализовал RL для манипулятора в симуляции: достиг 95% успешных захватов и снизил число '
                   'коллизий.',
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
        'nav': ['Опыт', 'Навыки', 'Образование', 'Доклады', 'Контакты'],
        'intro': 'Работаю Data Scientist в Сбер КИБ: применяю ML к задачам трейдинга и ценообразования. '
                 'Люблю финансы и экономику. В Яндекс Лавке оптимизировал скидки (+5% Front Margin) и '
                 'автоматизировал подготовку экспериментов. До этого занимался исследованиями в ИТМО и '
                 'руководил R&D-командой.',
        'cv': 'Резюме (PDF)',
        'experience_title': 'Опыт работы',
        'education_title': 'Образование',
        'talks_title': 'Доклады на конференциях',
        'talks_credit': 'Секция «Робототехника и искусственный интеллект». Соавтор — Владислав Дюжев, '
                        'научный руководитель — Алексей Ведяков.',
        'talks': [(2024, 'Исследование применения диффузионных моделей в робототехнических задачах',
                   'XIII Конгресс молодых учёных ИТМО · 9 апреля 2024 · онлайн'),
                  (2023, 'Разработка системы анализа аэроснимков для определения прорастаемости '
                   'сельскохозяйственных культур',
                   'XII Конгресс молодых учёных ИТМО · 4 апреля 2023 · онлайн')],
        'talk_links': {'abstract': 'Тезисы', 'abstract_pdf': 'Тезисы (PDF)', 'program': 'Программа (PDF)',
                       'collection': 'Сборник тезисов', 'recommendation': 'Рекомендация к публикации (PDF)'},
        'recognition': 'Другие проекты и достижения',
        'contact_title': 'Контакты',
        'registrations_title': 'Патент и свидетельство о регистрации ПО',
        'fips_link': 'Карточка ФИПС',
        'registrations': [('Способ получения сигнала с оценками параметров синхронного двигателя с '
                           'постоянными магнитами',
                           'Патент РФ № 2851523 · 25 ноября 2025 года',
                           'Соавтор. Патентообладатель — АО «Диаконт».',
                           'patent'),
                          ('Полетный контроллер для управления квадрокоптером на базе программного пакета '
                           'mavros',
                           'Свидетельство о регистрации программы для ЭВМ № 2023686859 · 8 декабря 2023 года',
                           'Соавтор. Правообладатель — Университет ИТМО.',
                           'software')],
        'institutions': 'РЭШ · Сколтех · ИТМО',
        'skills_title': 'Навыки',
        'skills': [('ML & Deep Learning',
                    'PyTorch, нейронные сети (MLP), генеративные модели (VAE/CVAE), RL, градиентный бустинг '
                    '(CatBoost), scikit-learn, Optuna, подбор гиперпараметров и валидация моделей'),
                   ('Эконометрика и эксперименты',
                    'A/B-тесты, DiD, uplift-модели, оценка ценовой эластичности, эконометрика временных '
                    'рядов, панельные данные'),
                   ('Количественные финансы',
                    'Оптимизация портфеля, asset pricing, CAPM и факторные модели, моделирование рисков, '
                    'VaR/CVaR, дюрация и анализ облигаций'),
                   ('Данные и аналитика',
                    'Python, SQL, Pandas, NumPy, SciPy, Jupyter, Spark, Hadoop, Presto'),
                   ('Инженерные инструменты',
                    'Git, Docker, автоматизация конфигов и экспериментов, пайплайны сбора событий и расчёта '
                    'метрик, аналитические дашборды'),
                   ('Робототехника',
                    'Computer vision, сегментация изображений и облаков точек, RGB-D, 6D pose estimation, '
                    'SLAM, ROS2, калибровка инструментов и камер, MuJoCo, Gazebo, PyBullet, NVIDIA Jetson '
                    'Xavier'),
                   ('Руководство проектами',
                    'Подбор команды, roadmap, согласование технических решений, организация испытаний, '
                    'взаимодействие с заказчиком')]},
 'en': {'name': 'Kirill Lalayants',
        'other': 'RU',
        'other_lang': 'ru',
        'title': 'Kirill Lalayants — Data Scientist · ML & Finance',
        'desc': 'Kirill Lalayants — Data Scientist at Sberbank CIB. ML for trading and pricing, finance and '
                'economics. Experience at Yandex Lavka and in research at ITMO. NES, Skoltech, ITMO.',
        'skip': 'Skip to content',
        'pdf': 'e',
        'jobs': [('May 2026 — present',
                  'Sberbank CIB',
                  'Data Scientist',
                  ['Develop and implement RL agents for pricing and trading desk optimization.']),
                 ('Jan 2026 — May 2026',
                  'Yandex Lavka',
                  'Data Analyst',
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
                   'Implemented RL for a manipulator in simulation, achieving a 95% grasp success rate and '
                   'reducing collisions.',
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
        'nav': ['Experience', 'Skills', 'Education', 'Talks', 'Contact'],
        'intro': 'I’m a Data Scientist at Sberbank CIB, applying ML to trading and pricing, with a strong '
                 'interest in finance and economics. At Yandex Lavka, I optimized discounts (+5% Front '
                 'Margin) and automated experiment setup. Previously, I conducted research at ITMO and led '
                 'an R&D team.',
        'cv': 'CV (PDF)',
        'experience_title': 'Experience',
        'education_title': 'Education',
        'talks_title': 'Conference talks',
        'talks_credit': 'Robotics and Artificial Intelligence session. Co-author: Vladislav Dyuzhev. '
                        'Research supervisor: Alexey Vedyakov.',
        'talks': [(2024, 'Investigating the use of diffusion models in robotics',
                   '13th ITMO Congress of Young Scientists · 9 April 2024 · Online'),
                  (2023, 'Developing a system for aerial image analysis to assess crop germination',
                   '12th ITMO Congress of Young Scientists · 4 April 2023 · Online')],
        'talk_links': {'abstract': 'Abstract', 'abstract_pdf': 'Abstract (PDF)', 'program': 'Program (PDF)',
                       'collection': 'Book of abstracts', 'recommendation': 'Publication recommendation (PDF)'},
        'recognition': 'Contributions & achievements',
        'contact_title': 'Contact',
        'registrations_title': 'Patent & software registration',
        'fips_link': 'FIPS record',
        'registrations': [('Method for obtaining a signal with parameter estimates of a permanent-magnet '
                           'synchronous motor',
                           'Russian patent No. 2851523 · 25 November 2025',
                           'Co-inventor. Patent holder: Diakont JSC.',
                           'patent'),
                          ('Quadcopter flight controller based on the mavros software package',
                           'Software registration No. 2023686859 · 8 December 2023',
                           'Co-author. Rights holder: ITMO University.',
                           'software')],
        'institutions': 'NES · Skoltech · ITMO',
        'skills_title': 'Skills',
        'skills': [('ML & Deep Learning',
                    'PyTorch, neural networks (MLP), generative models (VAE/CVAE), RL, gradient boosting '
                    '(CatBoost), scikit-learn, Optuna, hyperparameter tuning and model validation'),
                   ('Econometrics & experiments',
                    'A/B testing, DiD, uplift modeling, price elasticity estimation, time series '
                    'econometrics, panel data'),
                   ('Quantitative finance',
                    'Portfolio optimization, asset pricing, CAPM and factor models, risk modeling, VaR/CVaR, '
                    'duration and fixed income analysis'),
                   ('Data & analytics', 'Python, SQL, Pandas, NumPy, SciPy, Jupyter, Spark, Hadoop, Presto'),
                   ('Engineering tools',
                    'Git, Docker, configuration and experiment automation, event logging and metric '
                    'pipelines, analytical dashboards'),
                   ('Robotics',
                    'Computer vision, image and point-cloud segmentation, RGB-D, 6D pose estimation, SLAM, '
                    'ROS2, tool and camera calibration, MuJoCo, Gazebo, PyBullet, NVIDIA Jetson Xavier'),
                   ('Project leadership',
                    'Team formation, roadmapping, technical decision review, test coordination, client '
                    'communication')]}}

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
                  zip(['experience', 'skills', 'education', 'talks', 'contact'], c['nav']))
    jobs = '\n'.join(
        f'<li class="job"><div class="entry-heading"><h3>{company}</h3>'
        f'<span class="date">{date}</span></div><p class="role">{role}</p>'
        '<ul class="job-points">' + ''.join(f'<li>{escape(point)}</li>' for point in points)
        + '</ul></li>' for date, company, role, points in c['jobs'])
    education = '\n'.join(
        f'<li class="education-item"><div class="entry-heading"><h3>{school}</h3>'
        f'<span class="date">{date}</span></div><p>{degree}</p></li>'
        for date, school, degree in c['edu'])
    talk_items = []
    for year, title, event in c['talks']:
        links = []
        for kind, link_url in CONFERENCE_LINKS[year]:
            label = escape(c['talk_links'][kind])
            links.append(f'<a href="{escape(link_url)}" hreflang="ru" aria-label="{label} · {year}">{label}</a>')
        talk_items.append(
            f'<li class="conference-talk"><h3>{escape(title)}</h3><p>{escape(event)}</p>'
            f'<div class="talk-links">{"".join(links)}</div></li>')
    talks = '\n'.join(talk_items)
    registration_items = []
    fips_label = escape(c['fips_link'])
    for title, metadata, credit, document in c['registrations']:
        number, database = REGISTRATION_DOCUMENTS[document]
        registry_url = f'{FIPS_REGISTRY}?DB={database}&DocNumber={number}&TypeFile=html'
        pdf_path = f'/assets/documents/{document}-{number}.pdf'
        registration_items.append(
            f'<li class="registration"><h3>{escape(title)}</h3>'
            f'<p class="registration-meta">{escape(metadata)}</p>'
            f'<p class="registration-credit">{escape(credit)}</p>'
            '<div class="registration-links">'
            f'<a class="registry-link" href="{escape(registry_url)}" aria-label="{fips_label} · {number}">'
            f'{fips_label} <span aria-hidden="true">↗</span></a>'
            f'<a href="{pdf_path}" aria-label="PDF · {number}">PDF</a>'
            '</div></li>')
    registrations = '\n'.join(registration_items)
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
<p class="institutions"><a href="#education">{c['institutions']}</a></p>
<p>{c['intro']}</p>
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
<section id="talks" aria-labelledby="talks-title">
<h2 id="talks-title">{c['talks_title']}</h2>
<p class="talks-credit">{escape(c['talks_credit'])}</p>
<ul class="entries">
{talks}
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
