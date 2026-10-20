#!/usr/bin/env python3
"""Build the static HiArche.com site into ./site"""
import os, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
UP = '/mnt/user-data/uploads'
ICONS = os.path.join(ROOT, 'icons')
REPO = os.path.dirname(ROOT)  # flat site files at repo root (fallback for lab files)
PG = 'https://wnsgud7387-web.github.io/arche-pages/'
BOARD = 'https://github.com/wnsgud7387-web/hiarche-community/discussions'
E = html.escape

# Legal notice for the site (법무 rpl-20261020-lq-age14-legal 15:07 KST 확정본)
SITE_NOTICE_KO = '이 사이트는 쿠키나 분석 도구를 쓰지 않아요. LQ 검사 결과는 브라우저 안에서만 계산돼요. 이용자가 결과 화면에서 직접 동의하고 보내기를 누른 경우에만 LQ 기록(LQ·영역 점수, 문항별 응답(정답 여부·걸린 시간·확신도), 언어, 화면 종류, 보낸 날짜, 들어온 경로, 고른 경우 나이대·성별)이 아르케의 저장소(Supabase Inc., 서버 위치 대한민국 서울 — 처리 위탁)로 전송돼요. 사이트를 열면 호스팅 업체 Vercel Inc.(미국)가 보안과 운영을 위해 접속 기록(IP 주소, 접속 시각, 브라우저 정보)을 미국 등 국외에서 Vercel의 정책에 따른 기간 동안 처리할 수 있어요. 저장소 업체 Supabase도 보안을 위해 접속 기록(IP 주소 포함)을 1일 동안 남길 수 있어요. 아르케는 이 기록들을 받거나 LQ 기록과 연결하지 않아요. 국외 처리를 원하지 않으면 이 사이트에 접속하지 않으면 돼요. 문의·개인정보 보호책임자: 박준형 · archeisit@gmail.com'
SITE_NOTICE_EN = "This site uses no cookies or analytics. LQ results are calculated only in your browser. Only if you agree and press Send on the result screen is your LQ record (LQ and area scores, per-item responses (right/wrong, time taken and confidence), language, device type, date sent, how you arrived, and age band and gender if you chose them) sent to Arche's storage (Supabase Inc., servers in Seoul, Republic of Korea, acting as our processor). When you open this site, our hosting provider Vercel Inc. (USA) may process access logs (IP address, access time, browser information) for security and operation, in the US or other countries, for the period set by Vercel's own policy. Our storage provider Supabase may also keep access logs, including IP addresses, for 1 day for security. Arche does not receive these logs or link them to LQ records. If you do not want this processing abroad, please do not visit this site. Contact and privacy officer: Junhyung Park · archeisit@gmail.com"

APPS = [
  dict(slug='niblore', name='Niblore', kind='Stories', bg='#0A132A', fg='#E3DFD8',
       line='Write a web novel one episode at a time with AI.',
       sub='Give it one line of a hint and get the next episode. Or skip writing and just read a story made for you.',
       ios='https://apps.apple.com/us/app/niblore-write-your-novel/id6812610681', status='live',
       meta='Free to start · iPhone and iPad · English, Korean, Japanese',
       features=[('One hint, one episode','Type what should happen next. Niblore writes the episode and keeps your characters straight.'),('Just read','Pick a genre and a starting story, then read episode after episode.'),('Illustrations & sharing','Add a picture to a scene and share your story with a link.')],
       price='Free to start. Ink packs and a monthly plan let you write and illustrate more. Prices are shown in the App Store in your currency.',
       support='https://mistory-app.vercel.app/support.html', privacy='https://mistory-app.vercel.app/privacy.html', terms='',
       note='Stories and illustrations are AI-generated.'),
  dict(slug='burnpile', name='Burnpile', kind='Unwind', bg='#0E0907', fg='#F6EDE4',
       line='Snap anything, cut it out, and watch it burn.',
       sub='Take a photo of something you are done with, cut it out, and set it on the fire. Each material burns its own way.',
       ios='', status='soon', meta='iPhone · In development',
       features=[('Snap and cut out','Photograph anything and lift it off its background in one tap.'),('Burns like the real thing','Paper curls, wood chars, cloth smoulders, each by its material.'),('A quiet place to sit','An indoor hearth or a backyard camp fire, with slow, endless flames.')],
       price='Free. No ads and no purchases in version 1.0.',
       support=PG+'bonfire-support.html', privacy=PG+'bonfire-privacy.html', terms='',
       note='Fire footage is AI-generated.'),
  dict(slug='rivalog', name='Rivalog', kind='Study', bg='#2F5D50', fg='#F1F5F2',
       line='Plan your week and race a rival you create.',
       sub='Tell it your books and the hours you really have. It splits the work across your week and sets a rival a little ahead of you.',
       ios='', status='review', meta='iPhone · In App Store review',
       features=[('A plan that fits your week',"Set your weekly study hours; today's share follows the time you have left."),('A rival to race','Your rival studies 30 minutes more each day. Keep up, or catch up.'),('Review before you forget',"See when each round of review is due and when you'll finish.")],
       price='Free to start. Rivalog Plus is a monthly or yearly subscription, with a 7-day free trial on the yearly plan.',
       support=PG+'rivalog-support.html', privacy=PG+'rivalog-privacy.html', terms=PG+'rivalog-terms.html', note=''),
  dict(slug='chosim', name='Chosim', kind='Habits', bg='#1E8A5A', fg='#F2FAF5',
       line='Not three days, but 21. Last-night you nudges you on time.',
       sub='Pick one small habit and a time. Each evening you leave a note for tomorrow; each morning it arrives right on time.',
       ios='https://apps.apple.com/us/app/chosim-21-day-habit-keeper/id6818934076', status='live', meta='iPhone · 9 languages',
       features=[('21 days, one habit','A short, finite journey instead of a streak that never ends.'),('A note from last night','Your own words from the night before arrive at the time you chose.'),('Someone in your corner','Share a link so a friend can see how you are doing.')],
       price='Free to try. Each 21-day journey is a small one-time purchase, shown in the App Store in your currency.',
       support=PG+'support-microsuccess.html', privacy=PG+'privacy-microsuccess.html', terms='', note=''),
  dict(slug='wanderlure', name='Wanderlure', kind='Unwind', bg='#5C6BD8', fg='#F4F5FD',
       line='Follow a buzz, not a feed — a walk to somewhere unknown.',
       sub='Put the feed down and pick a distance. Your phone buzzes you toward a place you have never been.',
       ios='https://apps.apple.com/us/app/wanderlure-walk-the-unknown/id6812606367', status='live',
       meta='iPhone · 6 languages · Keep the screen on while you walk',
       features=[("A destination you don't know",'Choose how far; Wanderlure picks somewhere new.'),('Follow the buzz','A rough arrow and a gentle vibration, so your eyes stay on the street.'),('A record of where you went','Look back on the streets you found.')],
       price='Free, supported by ads.',
       support=PG+'support-explorer.html', privacy=PG+'privacy-explorer.html', terms='', note=''),
  dict(slug='story-accounting', name='Story Accounting', kind='Study', bg='#0E6B66', fg='#EEF7F6',
       line='Short accounting stories for the FA, MA and FR exams.',
       sub='Each story stops right before the answer, so you make the call. Get it wrong and it tells you the name of the mistake.',
       ios='', status='review', meta='iPhone · English · In App Store review',
       features=[('Learn by story','Standards explained through short scenes, with the worked problem beside each one.'),('Your turn','The story pauses before the answer and asks you to choose.'),('A mistake log','Wrong answers are named and saved, so you can see your patterns.')],
       price='The first episodes are free. Study passes for FA, MA or FR are sold for 6 or 12 months.',
       support=PG+'story-acca-support.html', privacy=PG+'story-acca-privacy.html', terms='',
       note='Unofficial study aid. Not affiliated with or endorsed by ACCA.'),
]
LAB = {'niblore': None, 'burnpile': ('Light the fire', 'Drag a receipt, a note or a log onto the fire and watch it burn. Works best on a phone-sized window.', '../lab/burnpile-web-fire.html', 780, 420, 'Fire footage is AI-generated.'), 'rivalog': ('How long will your book take?', 'Fill in three of the four boxes and it works out the fourth, with the same math as the app.', '../lab/rivalog-calculator.html', 900, None, 'A planning estimate, not a guarantee.'), 'chosim': None, 'wanderlure': None, 'story-accounting': ('Read Episode 1', '"Only 3 months belong to this year." The story stops right before the answer. Your turn.', '../lab/story-accounting-episode-1.html', 900, None, 'Unofficial study aid. Not affiliated with or endorsed by ACCA.')}
ICON = {'niblore':'niblore','burnpile':'burnpile','rivalog':'rivalog','chosim':'chosim','wanderlure':'wanderlure','story-accounting':'story'}

CSS = r"""
:root{--bg:#F3F4EF;--ink:#16181D;--soft:#3C4038;--mute:#5A5F55;--line:#DCDED6;--card:#FFFFFF;--accent:#D9481A;--link-hover:#B23E12}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:'Figtree',system-ui,-apple-system,'Segoe UI',sans-serif;font-size:16px;line-height:1.5}
a{color:var(--ink)}a:hover{color:var(--link-hover)}
a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid var(--link-hover);outline-offset:2px}
h1,h2,h3{font-family:'Bricolage Grotesque','Figtree',sans-serif;text-wrap:balance;margin:0}
p{margin:0}
img{max-width:100%;display:block}
.wrap{max-width:1200px;margin:0 auto;padding-inline:24px}
.skip{position:absolute;left:-999px}.skip:focus{left:16px;top:16px;background:#fff;padding:8px 12px;z-index:9}
header.top{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;padding-block:24px}
.logo{text-decoration:none;font-family:'Bricolage Grotesque',sans-serif;font-size:26px;font-weight:800;letter-spacing:-.02em}
.logo b{color:var(--accent);font-weight:800}
nav.main{display:flex;flex-wrap:wrap;gap:8px 28px;font-weight:500}
nav.main a{text-decoration:none}nav.main a[aria-current]{text-decoration:underline;text-underline-offset:6px}
.btn{display:inline-flex;align-items:center;min-height:48px;padding:0 24px;border-radius:999px;font-weight:600;text-decoration:none}
.btn.dark{background:var(--ink);color:var(--bg)}.btn.dark:hover{color:#fff}
.btn.line{border:2px solid var(--ink)}
.eyebrow{font-size:14px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
.h1{font-size:clamp(44px,7vw,96px);line-height:.98;font-weight:800;letter-spacing:-.035em}
.h2{font-size:clamp(34px,4.5vw,56px);font-weight:800;letter-spacing:-.03em}
.lead{font-size:19px;line-height:1.55;color:var(--soft);max-width:34em}
.hero{display:flex;flex-wrap:wrap;gap:56px;align-items:center;padding-block:56px 96px}
.hero>div{flex:1 1 420px;min-width:0}
.hero .text{display:flex;flex-direction:column;gap:24px;flex-basis:520px}
.icons{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.icons img{width:100%;aspect-ratio:1;border-radius:23%;box-shadow:0 10px 24px rgba(22,24,29,.14)}
.band{background:var(--card);border-block:1px solid var(--line)}
.sec{padding-block:88px;display:flex;flex-direction:column;gap:36px}
.sechead{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:16px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:20px}
.card{display:flex;flex-direction:column;gap:16px;padding:28px;border-radius:24px;background:var(--bg)}
.card.white{background:var(--card);border:1px solid var(--line)}
.apphead{display:flex;align-items:center;gap:16px}
.apphead img{width:64px;height:64px;border-radius:15px;flex:none}
.apphead h3{font-size:24px}
.kind{font-size:14px;color:var(--mute)}
.note{font-size:13px;color:var(--mute)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border-radius:12px;font-size:14px;font-weight:600;text-decoration:none}
.chip.store{background:var(--ink);color:var(--bg)}.chip.store:hover{color:#fff}
.chip.soon{background:#E4E6DE;color:var(--soft)}
.chip.play{border:1.5px dashed #8C9086;color:#50554B}
.links{display:flex;flex-wrap:wrap;gap:16px;font-size:14px}
.appcard{text-decoration:none;color:var(--ink);border:1px solid transparent;transition:border-color .15s,transform .15s}.appcard:hover{border-color:#B9BCB1;transform:translateY(-2px);color:var(--ink)}
.cardfoot{display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-size:13px;font-weight:600}
.status{padding:4px 10px;border-radius:999px;background:#E4E6DE;color:var(--soft)}.status.live{background:#DDEFE3;color:#1E5A35}.status.review{background:#E2E8F8;color:#2A3A8C}
.trybadge{padding:4px 10px;border-radius:999px;background:#FBE3D8;color:#8A2E0C}
.more{margin-left:auto;color:var(--ink)}
.lab{display:flex;flex-direction:column;gap:20px;padding:28px;border-radius:24px;min-height:380px}
.lab h3{font-size:28px}
.lab .tag{font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}
.frame{width:100%;border:0;border-radius:16px;background:#000}
.about{background:var(--ink);color:var(--bg)}
.about .sec{flex-direction:row;flex-wrap:wrap;gap:48px}
.about h2{flex:1 1 360px}
.about .body{flex:1 1 420px;min-width:0;display:flex;flex-direction:column;gap:20px;font-size:18px;line-height:1.6;color:#C9CCC3}
footer.site{padding-block:56px 72px;display:flex;flex-direction:column;gap:28px}
footer .row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:24px}
footer .legal{padding-top:24px;border-top:1px solid var(--line);font-size:13px;line-height:1.7;color:var(--mute);display:flex;flex-direction:column;gap:2px}
.post{display:flex;flex-wrap:wrap;gap:8px 24px;padding-block:24px;border-bottom:1px solid #C9CCC3}
.post .when{flex:0 0 140px;display:flex;flex-direction:column;gap:6px;font-size:14px;color:var(--mute)}
.post .what{flex:1 1 320px;min-width:0;display:flex;flex-direction:column;gap:8px}
.pill{align-self:flex-start;padding:2px 10px;border-radius:999px;font-size:12px;font-weight:600}
.faq{display:flex;flex-direction:column;gap:6px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.faq:last-child{border-bottom:0}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:20px;background:var(--card)}
table{width:100%;min-width:560px;border-collapse:collapse}
th,td{padding:14px 20px;text-align:left}tbody tr{border-top:1px solid var(--line)}thead{background:var(--bg)}
dl.facts{margin:0;display:grid;grid-template-columns:minmax(120px,auto) minmax(0,1fr);gap:12px 24px}
dl.facts dt{font-weight:600;color:var(--mute)}dl.facts dd{margin:0}
.calc{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.calc label{display:flex;flex-direction:column;gap:6px;font-size:14px;font-weight:600;color:var(--soft)}
.calc input{min-height:44px;padding:0 12px;border-radius:10px;border:1.5px solid #8C9086;font:inherit;font-size:18px;background:#fff;color:var(--ink)}
.result{display:flex;align-items:baseline;gap:10px;padding:16px 20px;border-radius:16px;background:#E6EFEC}
.result b{font-family:'Bricolage Grotesque',sans-serif;font-size:44px;color:#2F5D50;font-variant-numeric:tabular-nums}
@media (max-width:640px){.hero{padding-block:24px 64px;gap:36px}.sec{padding-block:64px}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&amp;family=Figtree:wght@400;500;600&amp;display=swap">'

def head(title, desc, depth, path):
    up = '../' * depth
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="https://hiarche.com/{path}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="https://hiarche.com/{path}">
<meta property="og:site_name" content="HiArche">
<link rel="icon" href="{up}assets/favicon.png" type="image/png">
{FONTS}
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def nav(depth, current):
    up = '../' * depth
    items = [('Apps', f'{up}index.html#apps'), ('News', f'{up}news.html'), ('Journal', f'{up}journal.html'), ('Support', f'{up}support.html'), ('Press & Business', f'{up}press.html')]
    cur = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{cur if n==current else ""}>{E(n)}</a>' for n,h in items)
    return f'<header class="top wrap"><a class="logo" href="{up}index.html"><b>Hi</b>Arche</a><nav class="main" aria-label="Main">{links}</nav></header>\n'

def footer(depth):
    up = '../' * depth
    return f'''<footer class="site wrap">
<div class="row">
<div style="display:flex;flex-direction:column;gap:8px"><span class="logo" style="font-size:22px"><b>Hi</b>Arche</span><span style="color:#50554B">Questions or ideas? archeisit@gmail.com</span></div>
<nav aria-label="Footer" class="links" style="font-size:15px"><a href="{up}support.html">Support</a><a href="{BOARD}">Feedback board</a><a href="{up}press.html">Press &amp; Business</a><a href="{up}legal.html">Privacy &amp; Legal</a><a href="https://www.instagram.com/arche.apps/">Instagram</a></nav>
</div>
<div class="legal">
<p>Arche (아르케) · Representative: Junhyung Park · Business registration no. (Korea): 774-39-01532</p>
<p>Room 7201, 7F, 9-1 Gugalro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do, Republic of Korea · archeisit@gmail.com</p>
<p>© 2026 Arche</p>
</div>
</footer>
</body>
</html>
'''

def store_chips(a, up):
    if a['status'] == 'live':
        s = f'<a class="chip store" href="{a["ios"]}">App Store</a>'
    elif a['status'] == 'review':
        s = '<span class="chip soon">App Store · in review</span>'
    else:
        s = '<span class="chip soon">In development</span>'
    return s + ('' if a['slug']=='burnpile' else '<span class="chip play">Google Play · soon</span>')

def terms_cell(a):
    return f'<a href="{a["terms"]}">Read</a>' if a['terms'] else 'Apple standard EULA'

def write(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(text)

exec(open(os.path.join(ROOT,'news_journal.py'),encoding='utf-8').read())

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, 'assets/icons'))
    write('assets/site.css', CSS.strip() + '\n')
    for slug, fn in ICON.items():
        shutil.copy(os.path.join(ICONS, fn + '.png'), os.path.join(OUT, f'assets/icons/{slug}.png'))
    # favicon: simple 'Hi' mark from niblore? use generated
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGBA', (64, 64), (0,0,0,0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,63,63], 14, fill=(217,72,26,255))
    try: font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 30)
    except Exception: font = ImageFont.load_default()
    d.text((32,33), 'Hi', fill=(255,255,255,255), font=font, anchor='mm')
    im.save(os.path.join(OUT, 'assets/favicon.png'))
    # lab files
    labs = {'lab/burnpile-web-fire.html': 'Desktop/ARCHE/2_앱/모닥불/웹맛보기/burnpile-web-fire.html',
            'lab/rivalog-calculator.html': 'Documents/doppel/site/lab/rivalog-calculator.html',
            'lab/story-accounting-episode-1.html': 'Documents/story/hiarche_lab/story-acca-lab.html',
            'lab/lq2-test.html': 'Documents/doppel/lq2/lq2-test.html',
            'lab/lq2-test-en.html': 'Documents/doppel/lq2/lq2-test-en.html',
            'lab/og_lq2_ko.png': 'Desktop/ARCHE/마케팅/hiarche/og_lq2_ko.png',
            'lab/og_lq2_en.png': 'Desktop/ARCHE/마케팅/hiarche/og_lq2_en.png'}
    for dst, src in labs.items():
        os.makedirs(os.path.dirname(os.path.join(OUT, dst)), exist_ok=True)
        s_up = os.path.join(UP, src)
        shutil.copy(s_up if os.path.exists(s_up) else os.path.join(REPO, os.path.basename(dst)), os.path.join(OUT, dst))

    # ---------- index ----------
    icons = ''.join(f'<img src="assets/icons/{a["slug"]}.png" alt="" style="transform:rotate({t})">' for a,t in zip(APPS, ['-4deg','3deg','-2deg','2deg','-3deg','4deg']))
    cards = ''
    for a in APPS:
        note = f'<p class="note">{E(a["note"])}</p>' if a['note'] else ''
        tryb = '<span class="trybadge">Try it in your browser</span>' if LAB.get(a['slug']) else ''
        cards += f'''<a class="card appcard" href="apps/{a["slug"]}.html" aria-label="{E(a["name"])}: {E(a["line"])}">
<div class="apphead"><img src="assets/icons/{a["slug"]}.png" alt=""><div><h3>{E(a["name"])}</h3><span class="kind">{E(a["kind"])}</span></div></div>
<p style="font-size:17px;flex-grow:1">{E(a["line"])}</p>
<div class="cardfoot"><span class="status {a["status"]}">{ {'live':'On the App Store','review':'In App Store review','soon':'In development'}[a["status"]] }</span>{tryb}<span class="more">See app &rarr;</span></div>
</a>
'''
    index = head('HiArche — Small apps, made with care', 'Arche is a small app studio in Korea. Niblore, Burnpile, Rivalog, Chosim, Wanderlure and Story Accounting.', 0, '') + nav(0, '') + f'''<main id="main">
<section class="hero wrap">
<div class="text">
<p class="eyebrow">A small app studio from Korea</p>
<h1 class="h1">Hi, we're <span style="color:var(--accent)">Arche</span>.</h1>
<p style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(24px,2.6vw,32px);font-weight:700;letter-spacing:-.015em">Small apps, made with care.</p>
<p class="lead">Write a story, walk somewhere new, keep a habit, study with a rival, or just watch something burn. Six small apps, each for one everyday moment.</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;padding-top:8px"><a class="btn dark" href="#apps">Meet our apps</a><a class="btn line" href="news.html">What\'s new</a></div>
</div>
<div class="icons" aria-hidden="true">{icons}</div>
</section>
<section id="apps" class="band"><div class="wrap sec">
<div class="sechead"><h2 class="h2">Our apps</h2><p style="max-width:28em;font-size:17px;color:#50554B">Tap an app to see what it does. Three of them you can try right here.</p></div>
<div class="grid">{cards}</div>
</div></section>
<section class="wrap" style="padding-bottom:96px;display:flex;flex-direction:column;gap:28px" aria-labelledby="news-h">
<div class="sechead"><h2 id="news-h" style="font-size:clamp(32px,4vw,44px);font-weight:800;letter-spacing:-.03em">What's new</h2><a href="news.html" style="font-weight:600">All app news</a></div>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr))">
<a class="card white" style="text-decoration:none" href="news.html#niblore"><span class="note">News · Niblore 1.4.0</span><h3 style="font-size:22px">A new Read mode</h3><span style="color:var(--soft)">Pick a genre and a starting story, and Episode 1 begins right away.</span></a>
<a class="card white" style="text-decoration:none" href="news.html#rivalog"><span class="note">News · In App Store review</span><h3 style="font-size:22px">Rivalog and Story Accounting</h3><span style="color:var(--soft)">Two new apps are waiting for App Store review.</span></a>
<a class="card white" style="text-decoration:none" href="journal-why-arche.html"><span class="note">Journal · Oct 19, 2026</span><h3 style="font-size:22px">Why "Arche"?</h3><span style="color:var(--soft)">An old Greek word for beginning, and six apps built around one.</span></a>
</div>
</section>
<section class="about"><div class="wrap sec">
<h2 class="h2" style="line-height:1.05">Made by hand,<br>one stitch at a time.</h2>
<div class="body"><p>Arche is a small studio in Korea that makes apps by hand, one careful stitch at a time. Nothing flashy, just well-made tools you'll want to keep using.</p><p>Our name comes from the Greek arche, "beginning." Every app is built for a first step: the first page, the first walk, the first day.</p></div>
</div></section>
</main>
''' + footer(0)
    write('index.html', index)

    # ---------- app pages ----------
    for a in APPS:
        if a['status'] == 'live':
            dl = f'<a class="btn" style="border-radius:12px;background:{a["fg"]};color:{a["bg"]}" href="{a["ios"]}">Download on the App Store</a>'
        else:
            label = 'App Store · in review' if a['status']=='review' else 'In development'
            dl = f'<span class="btn" style="border-radius:12px;background:{a["fg"]};color:{a["bg"]}">{label}</span>'
        feats = ''.join(f'<div class="card white"><h3 style="font-size:22px">{E(t)}</h3><p style="color:var(--soft)">{E(d)}</p></div>' for t,d in a['features'])
        terms = f'<a href="{a["terms"]}">Terms of use</a>' if a['terms'] else ''
        note = f'<p class="note">{E(a["note"])}</p>' if a['note'] else ''
        lab = LAB.get(a['slug'])
        trysec = ''
        if lab:
            t, d, src, h, w, ln = lab
            frame_w = f'max-width:{w}px;' if w else ''
            bgc = '#000' if a['slug']=='burnpile' else '#fff'
            trysec = f'''<section id="try" class="wrap sec" style="padding-bottom:24px">
<div style="display:flex;flex-direction:column;gap:10px"><p class="eyebrow" style="color:#B23E12">Try it here</p><h2 style="font-size:clamp(32px,4vw,48px);font-weight:800;letter-spacing:-.03em">{E(t)}</h2><p class="lead" style="font-size:17px">{E(d)} Nothing you do here is saved or sent.</p></div>
<iframe class="frame" src="{src}" title="{E(a["name"])}: {E(t)}" style="{frame_w}height:{h}px;margin-inline:auto;background:{bgc}"></iframe>
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px"><a href="{src}" style="font-weight:600">Open full screen</a><span class="note">{E(ln)}</span></div>
</section>
'''
        page = head(f'{a["name"]} — {a["line"]} | HiArche', a['sub'], 1, f'apps/{a["slug"]}.html') + nav(1, 'Apps') + f'''<main id="main">
<section style="background:{a["bg"]};color:{a["fg"]}"><div class="wrap hero" style="padding-block:72px">
<div class="text">
<img src="../assets/icons/{a["slug"]}.png" alt="{E(a["name"])} app icon" style="width:96px;height:96px;border-radius:22px">
<h1 class="h1" style="font-size:clamp(44px,6vw,80px)">{E(a["name"])}</h1>
<p style="font-family:'Bricolage Grotesque',sans-serif;font-size:28px;font-weight:700">{E(a["line"])}</p>
<p style="font-size:18px;max-width:32em;opacity:.88">{E(a["sub"])}</p>
<div style="display:flex;flex-wrap:wrap;gap:12px">{dl}{'<a class="btn" style="border-radius:12px;border:2px solid '+a["fg"]+';color:'+a["fg"]+'" href="#try">Try it here</a>' if lab else ''}{'' if a['slug']=='burnpile' else '<span class="btn" style="border-radius:12px;border:1.5px dashed '+a['fg']+';opacity:.8">Google Play · soon</span>'}</div>
<p style="font-size:14px;opacity:.78">{E(a["meta"])}</p>
</div>
</div></section>
{trysec}<section class="wrap sec"><h2 style="font-size:clamp(32px,4vw,48px);font-weight:800;letter-spacing:-.03em">What you can do</h2><div class="grid">{feats}</div></section>
<section class="band"><div class="wrap sec" style="flex-direction:row;flex-wrap:wrap;gap:48px">
<div style="flex:1 1 480px;min-width:0;display:flex;flex-direction:column;gap:16px">
<h2 style="font-size:clamp(32px,4vw,48px);font-weight:800;letter-spacing:-.03em">Questions</h2>
<div class="faq"><h3 style="font-size:19px">How much does it cost?</h3><p style="color:var(--soft)">{E(a["price"])}</p></div>
<div class="faq"><h3 style="font-size:19px">Where do I get help?</h3><p style="color:var(--soft)">Open the help page, post on our feedback board, or write to archeisit@gmail.com with the app name.</p></div>
</div>
<div style="flex:1 1 300px;min-width:0;display:flex;flex-direction:column;gap:14px">
<h2 style="font-size:24px">Links</h2>
<a href="{a["support"]}">{E(a["name"])} help page</a><a href="{a["privacy"]}">Privacy policy</a>{terms}<a href="{BOARD}">Feedback board</a>{note}
</div>
</div></section>
</main>
''' + footer(1)
        write(f'apps/{a["slug"]}.html', page)

    build_news_journal()

    # ---------- support ----------
    rows = ''.join(f'<article class="card white"><div class="apphead"><img src="assets/icons/{a["slug"]}.png" alt=""><h3 style="font-size:22px">{E(a["name"])}</h3></div><div class="links" style="font-size:15px"><a href="{a["support"]}">Help page</a><a href="{a["privacy"]}">Privacy policy</a></div></article>' for a in APPS)
    support = head('Support — HiArche', 'Help for Arche apps: help pages, common questions, feedback board and email.', 0, 'support.html') + nav(0, 'Support') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:48px">
<div style="display:flex;flex-direction:column;gap:12px"><h1 class="h1" style="font-size:clamp(44px,6vw,72px)">How can we help?</h1><p class="lead">Pick an app for its help page, or write to us. A person reads every message.</p></div>
<section style="display:flex;flex-direction:column;gap:20px"><h2 style="font-size:28px">Choose an app</h2><div class="grid">{rows}</div></section>
<section class="card white" style="gap:12px"><h2 style="font-size:28px">Common questions</h2>
<div class="faq"><h3 style="font-size:18px">How do I restore a purchase?</h3><p style="color:var(--soft)">Open the app's settings and tap Restore Purchases, signed in with the same Apple ID.</p></div>
<div class="faq"><h3 style="font-size:18px">How do I cancel a subscription?</h3><p style="color:var(--soft)">Subscriptions are managed by the App Store: Settings › your name › Subscriptions.</p></div>
<div class="faq"><h3 style="font-size:18px">How do I delete my data?</h3><p style="color:var(--soft)">Each app's privacy policy explains what it keeps and how to delete it. Still unsure? Email us.</p></div>
</section>
<section style="display:flex;flex-wrap:wrap;gap:20px">
<div class="card white" style="flex:1 1 420px;min-width:0"><h2 style="font-size:28px">Feedback board</h2><p style="color:var(--soft)">Ideas, bugs and questions, out in the open. Upvote what you want most; we reply on the post. The board runs on GitHub Discussions, so posting needs a free GitHub account.</p><a class="btn dark" style="align-self:flex-start" href="{BOARD}">Open the board</a><p class="note">Posts are public. Don't include your email or personal details.</p></div>
<div class="card" style="flex:1 1 300px;min-width:0;background:var(--ink);color:var(--bg)"><h2 style="font-size:28px">Email</h2><p style="color:#C9CCC3">For anything private, write to <strong style="color:#fff">archeisit@gmail.com</strong> with the app name and your device.</p></div>
</section>
</main>
''' + footer(0)
    write('support.html', support)

    # ---------- press ----------
    iconrow = ''.join(f'<img src="assets/icons/{a["slug"]}.png" alt="{E(a["name"])} icon" style="border-radius:22%">' for a in APPS)
    press = head('Press & Business — HiArche', 'Fact sheet, logos and app icons for Arche, and how to reach us about press and partnerships.', 0, 'press.html') + nav(0, 'Press & Business') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:48px">
<div style="display:flex;flex-direction:column;gap:12px"><h1 class="h1" style="font-size:clamp(44px,6vw,72px)">Press &amp; Business</h1><p class="lead">Everything you need to write about Arche, and the way to reach us about working together.</p></div>
<section class="card white" style="gap:16px"><h2 style="font-size:28px">Fact sheet</h2>
<dl class="facts"><dt>Studio</dt><dd>Arche (아르케)</dd><dt>Based in</dt><dd>Yongin, Gyeonggi-do, Republic of Korea</dd><dt>Founded</dt><dd>2026</dd><dt>Apps</dt><dd>Niblore, Burnpile, Rivalog, Chosim, Wanderlure, Story Accounting</dd><dt>Platforms</dt><dd>iPhone and iPad today; Android coming soon</dd><dt>Web</dt><dd>HiArche.com</dd></dl>
<p style="color:var(--soft)">Arche is a small studio in Korea that makes apps by hand, one careful stitch at a time. Nothing flashy, just well-made tools you'll want to keep using.</p></section>
<section style="display:flex;flex-direction:column;gap:20px"><h2 style="font-size:28px">Logo &amp; icons</h2>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr))">
<div class="card white" style="place-items:center;justify-content:center;min-height:160px"><span class="logo" style="font-size:44px;text-align:center"><b>Hi</b>Arche</span></div>
<div class="card" style="background:var(--ink);justify-content:center;min-height:160px"><span class="logo" style="font-size:44px;color:#F3F4EF;text-align:center"><b style="color:#FF8A5C">Hi</b>Arche</span></div>
<div class="card white" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px">{iconrow}</div>
</div>
<p class="note">Please don't recolor or stretch the logo. Write the name as "Arche" or "HiArche", never "Arche Inc." For full-size icons and screenshots, email us.</p></section>
<section style="display:flex;flex-direction:column;gap:20px"><h2 style="font-size:28px">Work with us</h2>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(240px,100%),1fr))">
<div class="card white"><h3 style="font-size:20px">Press &amp; reviews</h3><p style="color:var(--soft)">Interviews, review access and promo codes.</p></div>
<div class="card white"><h3 style="font-size:20px">Partnerships</h3><p style="color:var(--soft)">Co-promotions, bundles and featuring.</p></div>
<div class="card white"><h3 style="font-size:20px">Schools &amp; academies</h3><p style="color:var(--soft)">Rivalog and Story Accounting for study groups.</p></div>
<div class="card white"><h3 style="font-size:20px">Localization</h3><p style="color:var(--soft)">Help us bring an app to your language.</p></div>
</div>
<div class="card" style="background:#FBE3D8"><p style="font-family:'Bricolage Grotesque',sans-serif;font-size:22px;font-weight:700">Write to archeisit@gmail.com</p><p style="color:#5C2A12">Put "Press", "Partnership", "Schools" or "Localization" in the subject. A person reads every message.</p></div>
</section>
</main>
''' + footer(0)
    write('press.html', press)

    # ---------- legal ----------
    trs = ''.join(f'<tr><td style="font-weight:600">{E(a["name"])}</td><td><a href="{a["privacy"]}">Read</a></td><td><a href="{a["support"]}">Open</a></td><td>{terms_cell(a)}</td></tr>' for a in APPS)
    legal = head('Privacy & Legal — HiArche', 'Privacy policies, terms and business information for Arche and its apps.', 0, 'legal.html') + nav(0, '') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:48px">
<div style="display:flex;flex-direction:column;gap:12px"><h1 class="h1" style="font-size:clamp(44px,6vw,72px)">Privacy &amp; Legal</h1><p class="lead">Each app has its own privacy policy, because each one handles different things. This site uses no cookies, analytics or ads.</p></div>
<section style="display:flex;flex-direction:column;gap:16px"><h2 style="font-size:28px">This website and the LQ test</h2>
<div style="display:flex;flex-wrap:wrap;gap:20px">
<p class="card white" style="flex:1 1 480px;min-width:0;margin:0">{E(SITE_NOTICE_EN)}</p>
<p lang="ko" class="card" style="flex:1 1 320px;min-width:0;margin:0;background:#E9EAE3">{E(SITE_NOTICE_KO)}</p>
</div></section>
<section style="display:flex;flex-direction:column;gap:16px"><h2 style="font-size:28px">App policies</h2>
<div class="tablewrap"><table><thead><tr><th scope="col">App</th><th scope="col">Privacy policy</th><th scope="col">Support</th><th scope="col">Terms</th></tr></thead><tbody>{trs}</tbody></table></div></section>
<section style="display:flex;flex-direction:column;gap:16px"><h2 style="font-size:28px">Business information</h2>
<div style="display:flex;flex-wrap:wrap;gap:20px">
<dl class="facts card white" style="flex:1 1 480px;min-width:0"><dt>Business name</dt><dd>Arche (아르케)</dd><dt>Representative</dt><dd>Junhyung Park</dd><dt>Business registration (Korea)</dt><dd>774-39-01532</dd><dt>Address</dt><dd>Room 7201, 7F, 9-1 Gugalro 60beon-gil, Giheung-gu, Yongin-si, Gyeonggi-do, Republic of Korea</dd><dt>Email</dt><dd>archeisit@gmail.com</dd></dl>
<div lang="ko" class="card" style="flex:1 1 320px;min-width:0;background:#E9EAE3;gap:4px"><strong>사업자 정보</strong><span>아르케(Arche) · 대표 박준형</span><span>사업자등록번호 774-39-01532</span><span>경기도 용인시 기흥구 구갈로60번길 9-1, 7층 7201호</span><span>archeisit@gmail.com</span></div>
</div></section>
</main>
''' + footer(0)
    write('legal.html', legal)

    write('google3e50e77c706ec730.html', 'google-site-verification: google3e50e77c706ec730.html')
    write('vercel.json', open(os.path.join(ROOT,'vercel.json')).read())
    write('robots.txt', 'User-agent: *\nAllow: /\nSitemap: https://hiarche.com/sitemap.xml\n')
    urls = ['', 'news.html', 'journal.html', 'journal-why-arche.html', 'support.html', 'press.html', 'legal.html'] + [f'apps/{a["slug"]}.html' for a in APPS] + ['lab/burnpile-web-fire.html','lab/rivalog-calculator.html','lab/story-accounting-episode-1.html']
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>https://hiarche.com/{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    write('404.html', head('Not found — HiArche', 'Page not found.', 0, '404.html') + nav(0, '') + '<main id="main" class="wrap" style="padding-block:96px;display:flex;flex-direction:column;gap:20px"><h1 class="h1" style="font-size:64px">Hmm, nothing here.</h1><p class="lead">That page doesn\'t exist. Try the <a href="index.html">home page</a>.</p></main>\n' + footer(0))

if __name__ == '__main__':
    build()
    print('built', OUT)
