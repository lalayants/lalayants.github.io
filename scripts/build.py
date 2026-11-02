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
        'desc': 'Кирилл Лалаянц — Data Scientist в Сбер КИБ. Машинное обучение, RL-агенты для трейдинга, '
                'эконометрика и причинный анализ. Магистратура РЭШ и Сколтеха.',
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
                  ['Оптимизировал размеры скидок: Front Margin вырос на 5%.',
                   'Автоматизировал согласование скидок для коммерческих менеджеров.',
                   'Оценивал эффект промо с помощью A/B-тестов, uplift-моделей и DiD.',
                   'Разработал инфраструктуру экспериментов.']),
                 ('07.2022 — 06.2025',
                  'Университет ИТМО',
                  'Инженер-исследователь',
                  ['Работал над ML, компьютерным зрением и робототехникой в лаборатории адаптивных и '
                   'нелинейных систем управления.',
                   'Разработал SLAM для БПЛА: 25 кадров/с на Jetson Xavier.',
                   'Реализовал безопасное RL для манипулятора: 95% успешных захватов, ошибка калибровки '
                   'менее 1 мм.']),
                 ('12.2023 — 07.2024',
                  'Проект BRIZ',
                  'Руководитель команды',
                  ['Руководил командой из трёх разработчиков в проекте кооперативной воздушной '
                   'робототехники.',
                   'Разрабатывал управление и планирование на PX4 и ROS2.'])],
        'edu': [('2025 — 2027',
                 'Российская экономическая школа',
                 'Магистратура · Экономика, «Искусственный интеллект и финтех»'),
                ('2025 — 2027', 'Сколтех', 'Магистратура · Науки о данных'),
                ('2021 — 2025', 'Университет ИТМО', 'Бакалавриат · Робототехника и искусственный интеллект')],
        'tool_label': 'Инструменты',
        'achievement': 'Контрибьютор Ultralytics',
        'achievement_desc': 'Исправление ошибки при переносе моделей на TPU.',
        'award': 'Победитель хакатона StarLine',
        'award_desc': '«Беспилотное будущее», 2023.',
        'language': 'Английский C1',
        'language_desc': 'TOEFL iBT · 106/120.',
        'footer': 'Кирилл Лалаянц',
        'top': 'Наверх ↑',
        'updated': 'Обновлено в ноябре 2026',
        'other_url': '/',
        'nav': ['Опыт', 'Образование', 'Контакты'],
        'intro': 'Я Data Scientist в Сбер КИБ: разрабатываю RL-агентов для ценообразования и оптимизации '
                 'работы торгового деска. До этого занимался ценообразованием и экспериментами в Яндекс '
                 'Лавке и исследованиями в робототехнике в ИТМО.',
        'study': 'Параллельно учусь в совместной магистратуре РЭШ и Сколтеха: искусственный интеллект, '
                 'финансы и науки о данных.',
        'cv': 'Резюме (PDF)',
        'experience_title': 'Опыт работы',
        'education_title': 'Образование',
        'recognition': 'Другие проекты и достижения',
        'contact_title': 'Контакты',
        'registrations_title': 'Патент и регистрация ПО',
        'registrations': [('Способ получения сигнала с оценками параметров синхронного двигателя с '
                           'постоянными магнитами',
                           'Патент РФ № 2851523 · 25 ноября 2025',
                           'Соавтор. Патентообладатель — АО «Диаконт».',
                           '/assets/documents/patent-2851523.pdf'),
                          ('Полетный контроллер для управления квадрокоптером на базе программного пакета '
                           'mavros',
                           'Регистрация программы для ЭВМ № 2023686859 · 8 декабря 2023',
                           'Соавтор. Правообладатель — Университет ИТМО.',
                           '/assets/documents/software-2023686859.pdf')]},
 'en': {'name': 'Kirill Lalayants',
        'other': 'RU',
        'other_lang': 'ru',
        'title': 'Kirill Lalayants — Data Scientist · ML & Finance',
        'desc': 'Kirill Lalayants, Data Scientist at Sberbank CIB. Machine learning, reinforcement learning '
                'for trading, econometrics and causal inference. NES and Skoltech graduate student.',
        'skip': 'Skip to content',
        'pdf': 'e',
        'jobs': [('May 2026 — present',
                  'Sberbank CIB',
                  'Data Scientist',
                  ['Developing and implementing RL agents for trading desk pricing and optimization.']),
                 ('Jan 2026 — May 2026',
                  'Yandex Lavka',
                  'Data Scientist',
                  ['Optimized discount sizing, increasing Front Margin by 5%.',
                   'Automated discount approvals for commercial managers.',
                   'Measured promotion impact using A/B testing, uplift modeling and DiD.',
                   'Built experimentation infrastructure.']),
                 ('Jul 2022 — Jun 2025',
                  'ITMO University',
                  'Research Engineer',
                  ['Worked on ML, computer vision and robotics at the Adaptive and Nonlinear Control Systems '
                   'Lab.',
                   'Deployed UAV SLAM at 25 FPS on Jetson Xavier.',
                   'Implemented safe RL for manipulation: 95% grasp success and tool calibration error below '
                   '1 mm.']),
                 ('Dec 2023 — Jul 2024',
                  'BRIZ Project',
                  'Team Lead',
                  ['Led a team of three developers in a collaborative aerial robotics project.',
                   'Implemented flight control and motion planning with PX4 and ROS2.'])],
        'edu': [('2025 — 2027', 'New Economic School', 'Master’s program · AI & FinTech'),
                ('2025 — 2027', 'Skoltech', 'Master’s program · Data Science'),
                ('2021 — 2025', 'ITMO University', 'B.Sc. · Robotics & Artificial Intelligence')],
        'tool_label': 'Toolkit',
        'achievement': 'Ultralytics contributor',
        'achievement_desc': 'Fixed a bug affecting model transfer to TPU.',
        'award': 'StarLine Hackathon winner',
        'award_desc': '“Autonomous Future”, 2023.',
        'language': 'English · Advanced',
        'language_desc': 'TOEFL iBT · 106/120.',
        'footer': 'Kirill Lalayants',
        'top': 'Back to top ↑',
        'updated': 'Updated November 2026',
        'other_url': '/ru/',
        'nav': ['Experience', 'Education', 'Contact'],
        'intro': 'I’m a Data Scientist at Sberbank CIB, developing reinforcement learning agents for trading '
                 'desk pricing and optimization. Previously, I worked on pricing and experimentation at '
                 'Yandex Lavka, and robotics research at ITMO.',
        'study': 'I’m also pursuing a joint master’s program at the New Economic School and Skoltech, '
                 'focused on AI, finance and data science.',
        'cv': 'CV (PDF)',
        'experience_title': 'Experience',
        'education_title': 'Education',
        'recognition': 'Other work & background',
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
                           '/assets/documents/software-2023686859.pdf')]}}


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
                  zip(['experience', 'education', 'contact'], c['nav']))
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
<p class="occupation">Data Scientist</p>
<p>{c['intro']}</p>
<p>{c['study']}</p>
<div class="profile-links"><a href="/assets/cvs/Lalayants_cv_{c['pdf']}.pdf" download>{c['cv']}</a><a href="https://github.com/lalayants">GitHub</a><a href="https://linkedin.com/in/lalayants">LinkedIn</a><a href="mailto:lalayantskirill@gmail.com">Email</a></div>
</section>
<section id="experience" aria-labelledby="experience-title">
<h2 id="experience-title">{c['experience_title']}</h2>
<ul class="entries jobs">
{jobs}
</ul>
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
<p class="tools"><span>{c['tool_label']}:</span> Python, SQL, Pandas, NumPy, SciPy, Git, Docker.</p>
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
