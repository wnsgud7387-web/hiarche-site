# News + Journal pages (exec'd from build.py; uses head/nav/footer/write/E/APPS)

NEWS = [
  ('niblore', 'Version 1.4.0 · October 2026', 'On the App Store', 'live', [
     'New Read mode: pick a genre and a starting story, and Episode 1 begins right away — no setup needed.',
     'At the end of each episode, choose one of two paths for what happens next, or tap "Surprise me" and let the story carry on.',
     'Longer episodes in both Read and Write modes, and you can add illustrations while you read.',
     'Bring your story to a finale and share the whole book with a single link.'],
   ['Coming to Google Play.']),
  ('wanderlure', 'Version 1.2 · October 2026', 'On the App Store', 'live', [
     'Wanderlure now speaks six languages: English, Korean, Japanese, Simplified Chinese, Spanish and French.',
     'Pick your own walking time instead of choosing from presets.',
     'Detour Walk has a new name in Korean, Eum-gil, and a clearer finish button.',
     'Fate walks end with a short fortune line, and the opening story can link to the full tale.'],
   ['Coming to Google Play.']),
  ('chosim', 'Version 1.1.0 · October 2026', 'On the App Store', 'live', [
     'Watch links: send your pledge as a link, and friends can follow your progress and cheer you on without installing the app.',
     'Add a proof photo to the steps you finish today. It is deleted the next day.',
     'Clearer rules and polished translations.'],
   ['Coming to Google Play.']),
  ('rivalog', 'Version 1.0 · first release · submitted Oct 19, 2026', 'In App Store review', 'review', [
     "Plan your week: add your books or courses, set your weekly study time as routines, and get today's target and range.",
     'See when each pass will finish. If your target date is tight, Rivalog shows what it takes: hours per week, or minutes per problem.',
     'Race a rival you create. It studies at your pace plus 30 minutes more a day, takes a 10-minute break every hour (or none), and shows a focus gauge through the day.',
     'Find your rival with a learning-style check of about 18 minutes across seven short tasks, built on task formats from published psychology research. The papers are cited in the app.'],
   ['Coming to Google Play.'],
   'The check is an estimate for choosing a rival, not an intelligence test or a diagnosis.'),
  ('story-accounting', 'Version 1.0 · first release · submitted Oct 18, 2026', 'In App Store review', 'review', [
     'First release: 270 short story episodes for three papers — Financial Accounting (75), Management Accounting (75) and Financial Reporting (120), in syllabus order.',
     'Each story stops just before the answer, so you solve it yourself first.',
     'Pick a wrong option and the app names the mistake that produces that figure.',
     'A mistake log brings wrong answers back after 1, 3 and 7 days with new figures. Five episodes in each paper are free.'],
   ['Coming to Google Play.'],
   'Unofficial study aid. Not affiliated with or endorsed by ACCA.'),
  ('solomons-verdict', 'Version 1.0 · first release · submitted Oct 22, 2026', 'In App Store review', 'review', [
     'Each person writes their side on their own phone; Solomon, an AI judge, questions both in turn.',
     'The verdict gives fault percentages by issue, the reasons, and a suggestion to make peace.',
     'If both agree, friends can join as a jury. Then the two of you set a few rules so the same fight does not happen again.',
     'No sign-up. Texts and photos are deleted 7 days after the verdict. For ages 14 and up.'],
   ['Coming to Google Play.', 'English screens.'],
   'For entertainment only. Not a real court and not legal advice. Verdicts are written by AI.'),
]

NEWS_CSS = '''<style>
.ncard{display:flex;flex-direction:column;gap:18px;padding:28px;border-radius:24px;background:var(--card);border:1px solid var(--line);scroll-margin-top:24px}
.ncard .top{display:flex;flex-wrap:wrap;align-items:center;gap:12px 16px}
.ncard .top img{width:56px;height:56px;border-radius:13px;flex:none}
.ncard .top h2{font-size:26px}
.ncard .ver{font-size:14px;color:var(--mute);font-variant-numeric:tabular-nums}
.ncols{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:24px}
.ncols h3{font-size:13px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--mute);font-family:'Figtree',sans-serif;margin-bottom:10px}
.ncols ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:8px;color:var(--soft)}
.next{align-self:start;padding:18px 20px;border-radius:16px;background:var(--bg)}
.essay{max-width:40em;display:flex;flex-direction:column;gap:22px;font-size:19px;line-height:1.7;color:var(--soft)}
.essay h1{color:var(--ink)}
.essay ul{margin:0;padding-left:22px;display:flex;flex-direction:column;gap:10px}
.essay b{color:var(--ink)}
@media (max-width:720px){.ncols{grid-template-columns:minmax(0,1fr)}}
</style>
'''

# Series 'A one-person company building apps with an AI team' (marketing drafts in src/journal/epN_{en,ko}.md)
SERIES = [  # (n, file stem, date)
  (2, 'journal-series-2', 'Oct 28, 2026'),
  (1, 'journal-series-1', 'Oct 22, 2026'),
  (0, 'journal-series-0', 'Oct 22, 2026'),
]

def _md(path):
    import re
    lines = open(path, encoding='utf-8').read().strip().split('\n')
    def inline(t):
        t = E(t)
        t = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
        t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
        t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
        return t
    title = re.sub(r'^\*\*|\*\*$', '', lines[0].strip())
    sub = re.sub(r'^\*|\*$', '', lines[1].strip()) if len(lines) > 1 else ''
    out, ol = [], []
    def flush():
        if ol: out.append('<ol>' + ''.join(f'<li>{x}</li>' for x in ol) + '</ol>'); ol.clear()
    for ln in lines[2:]:
        ln = ln.strip()
        if not ln: flush(); continue
        m = re.match(r'^\d+\.\s+(.*)', ln)
        if m: ol.append(inline(m.group(1))); continue
        flush()
        if ln.startswith('## '): out.append(f'<h2 style="font-size:26px;color:var(--ink)">{inline(ln[3:])}</h2>')
        elif ln.startswith('> '): out.append(f'<blockquote style="margin:0;padding-left:18px;border-left:3px solid var(--ink);color:var(--ink);font-weight:600">{inline(ln[2:])}</blockquote>')
        else: out.append(f'<p>{inline(ln)}</p>')
    flush()
    return title, sub, '\n'.join(out)

ESSAYS = []
for _n, _stem, _date in SERIES:
    _t, _s, _ = _md(os.path.join(ROOT, 'journal', f'ep{_n}_en.md'))
    ESSAYS.append((f'{_stem}.html', _date, 'Series', _t, _s))
ESSAYS.append(('journal-why-arche.html', 'Oct 19, 2026', 'Studio', 'Why "Arche"?',
           'An old Greek word for beginning, and six apps built around one.'))

def build_series():
    for n, stem, date in SERIES:
        for lang in ('en', 'ko'):
            t, sub, body = _md(os.path.join(ROOT, 'journal', f'ep{n}_{lang}.md'))
            fn = f'{stem}.html' if lang == 'en' else f'{stem}-ko.html'
            other = f'<a href="{stem}-ko.html" lang="ko">한국어로 읽기</a>' if lang == 'en' else f'<a href="{stem}.html">Read in English</a>'
            back = 'Journal' if lang == 'en' else '저널'
            page = head(f'{t} — HiArche Journal', sub, 0, fn) + NEWS_CSS + nav(0, 'Journal') + f'''<main id="main" class="wrap" style="padding-block:48px 96px">
<article class="essay"{' lang="ko"' if lang == 'ko' else ''}>
<p class="note"><a href="journal.html">{back}</a> · {date} · {other}</p>
<h1 class="h1" style="font-size:clamp(36px,5.5vw,58px)">{E(t)}</h1>
<p class="note">{E(sub)}</p>
{body}
<p class="note" style="padding-top:12px;border-top:1px solid var(--line)">— Arche</p>
</article>
</main>
''' + footer(0)
            if lang == 'ko': page = page.replace('<html lang="en">', '<html lang="ko">', 1)
            write(fn, page)

def build_news_journal():
    byslug = {a['slug']: a for a in APPS}
    cards = ''
    for row in NEWS:
        slug, ver, stat, scls, now, nxt = row[:6]
        note = row[6] if len(row) > 6 else ''
        a = byslug[slug]
        nowl = ''.join(f'<li>{E(x)}</li>' for x in now)
        nxtl = ''.join(f'<li>{E(x)}</li>' for x in nxt) if nxt else '<li>We will post here when there is news.</li>'
        title_now = 'This update' if scls != 'soon' else 'Where it stands'
        notep = f'<p class="note">{E(note)}</p>' if note else ''
        cards += f'''<article class="ncard" id="{slug}">
<div class="top"><img src="assets/icons/{slug}.png" alt=""><div style="display:flex;flex-direction:column;gap:2px;min-width:0"><h2>{E(a["name"])}</h2><span class="ver">{E(ver)}</span></div><span class="status {scls}" style="margin-left:auto;font-size:13px;font-weight:600">{E(stat)}</span></div>
<div class="ncols"><div><h3>{title_now}</h3><ul>{nowl}</ul></div><div class="next"><h3>Coming next</h3><ul>{nxtl}</ul></div></div>
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px">{notep}<a href="apps/{slug}.html" style="font-weight:600;margin-left:auto">About {E(a["name"])} &rarr;</a></div>
</article>
'''
    news = head('News — HiArche', 'What changed in each Arche app, and what is coming next.', 0, 'news.html') + NEWS_CSS + nav(0, 'News') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:28px">
<div style="display:flex;flex-direction:column;gap:14px"><h1 class="h1" style="font-size:clamp(44px,6vw,72px)">News</h1>
<p class="lead">What changed in each app, and what's coming next. We only list what we've already decided to build, so plans here don't come with dates.</p>
<p class="note">Updated Oct 19, 2026</p></div>
<div style="display:flex;flex-direction:column;gap:20px">{cards}</div>
</main>
''' + footer(0)
    write('news.html', news)

    # journal index
    items = ''.join(f'<article class="post"><div class="when"><span>{w}</span><span class="pill" style="background:#FBE3D8;color:#8A2E0C">{t}</span></div><div class="what"><h2 style="font-size:26px"><a href="{f}" style="text-decoration:none">{E(h)}</a></h2><p style="color:var(--soft)">{E(b)}</p><a href="{f}" style="font-weight:600;font-size:15px">Read &rarr;</a></div></article>' for f,w,t,h,b in ESSAYS)
    journal = head('Journal — HiArche', 'Stories from the Arche studio: why we make what we make, and how.', 0, 'journal.html') + nav(0, 'Journal') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:28px">
<h1 class="h1" style="font-size:clamp(44px,6vw,72px)">Journal</h1>
<p class="lead">Stories from the studio: why we make what we make, and how. For app updates, see <a href="news.html">News</a>.</p>
<div style="border-top:1px solid #C9CCC3">{items}</div>
</main>
''' + footer(0)
    write('journal.html', journal)

    # essay 1
    essay = head('Why "Arche"? — HiArche Journal', 'An old Greek word for beginning, and six apps built around one.', 0, 'journal-why-arche.html') + NEWS_CSS + nav(0, 'Journal') + '''<main id="main" class="wrap" style="padding-block:48px 96px">
<article class="essay">
<p class="note"><a href="journal.html">Journal</a> · Oct 19, 2026 · Studio</p>
<h1 class="h1" style="font-size:clamp(40px,6vw,64px)">Why "Arche"?</h1>
<p><i>Arche</i> is an old Greek word. It means "beginning," and also "origin": the first thing, the one everything else comes from. The earliest Greek thinkers used it when they asked what the world is made of, underneath everything.</p>
<p>We like it for a smaller reason. What most of us need help with isn't the hundredth day of something. It's the first one: the first page of a story, the first walk down a street you've never seen, the first morning of a new habit, the first hour with a book you've been putting off.</p>
<p>So each of our apps is built around one beginning.</p>
<ul>
<li><b>Niblore</b> starts a story from a single line.</li>
<li><b>Wanderlure</b> starts a walk to somewhere you don't know yet.</li>
<li><b>Chosim</b> takes its name from the Korean word for the spirit you start with, and helps you keep a habit for 21 days.</li>
<li><b>Rivalog</b> starts a study plan that fits the week you actually have.</li>
<li><b>Story Accounting</b> opens each topic with a short scene instead of a definition.</li>
<li><b>Burnpile</b>, still in development, is about a different kind of beginning: letting go of something so you can start again.</li>
</ul>
<p>We're a small studio in Yongin, Korea, and we started in 2026. HiArche.com is where we keep it all in one place: what each app does, what changed in each update on the <a href="news.html">News</a> page, and here in the Journal, the stories behind them.</p>
<p>If one of our apps helped you begin something, we'd love to hear about it on the <a href="''' + BOARD + '''">feedback board</a>.</p>
<p class="note" style="padding-top:12px;border-top:1px solid var(--line)">— Arche</p>
</article>
</main>
''' + footer(0)
    write('journal-why-arche.html', essay)
    build_series()
