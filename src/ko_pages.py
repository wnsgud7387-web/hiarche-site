# 한국어판 페이지 (hiarche.com/ko/) — build.py 안에서 exec 로 읽힘. 대표님 지시 10-24 15:55
KO = {
  'niblore': dict(name='니블로어', kind='소설', line='AI와 한 화씩 써 가는 웹소설.',
    sub='다음 화에 일어날 일을 한 줄만 적으면 이어지는 한 화를 써 줘요. 쓰지 않고 나만을 위해 만든 이야기를 읽기만 해도 돼요.',
    meta='무료로 시작 · iPhone·iPad · 한국어·영어·일본어',
    features=[('힌트 한 줄, 한 화','다음에 일어날 일을 적으면 니블로어가 등장인물을 헷갈리지 않고 한 화를 써요.'),('읽기만 하기','장르와 첫 이야기를 고르면 1화부터 바로 이어서 읽을 수 있어요.'),('삽화와 공유','장면에 그림을 넣고, 링크로 내 이야기를 나눠요.')],
    price='무료로 시작해요. 잉크 묶음과 월 구독으로 더 많이 쓰고 그릴 수 있어요. 가격은 앱스토어에 원화로 표시돼요.',
    note='이야기와 삽화는 AI가 만들어요.'),
  'solomons-verdict': dict(name='솔로몬의 판결', kind='재미', line='우리 싸움, 누가 더 잘못했을까?',
    sub='두 사람이 각자 자기 폰에서 입장을 적으면, AI 재판장 솔로몬이 양쪽 이야기를 번갈아 듣고 과실 비율로 판결해 줘요.',
    meta='iPhone · 앱스토어 심사 중 · 만 14세 이상',
    features=[('소장과 소환장','무슨 일이 있었는지 적고 링크를 보내요. 상대는 자기 폰에서 답변해요.'),('번갈아 묻는 변론','솔로몬이 양쪽에 질문하고 두 사람의 이야기를 모두 들은 뒤 판결해요.'),('판결·배심원·재발 방지 약속','쟁점별 과실 비율과 이유, 친구 배심원, 같은 다툼을 막는 약속 조항까지.')],
    price='광고와 회원가입이 없어요. 사건 접수와 추가 기능은 소액 1회 구매이며, 가격은 앱스토어에 원화로 표시돼요.',
    note='재미로 보는 AI 판정이에요. 실제 법원과 무관하며 법적 효력이 없고 법률 상담이 아니에요. 판결문은 AI(Anthropic Claude)가 만들어요.'),
  'rivalog': dict(name='라이벌로그', kind='공부', line='한 주를 계획하고, 내가 만든 라이벌과 겨뤄요.',
    sub='공부할 책과 실제로 쓸 수 있는 시간을 알려 주면 한 주에 나눠 주고, 나보다 조금 앞서가는 라이벌을 세워 줘요.',
    meta='iPhone · 앱스토어 심사 중',
    features=[('내 한 주에 맞는 계획','주간 공부 시간을 정하면 오늘 할 양이 남은 시간에 맞춰 바뀌어요.'),('함께 달리는 라이벌','라이벌은 매일 나보다 30분 더 공부해요. 따라잡거나, 앞서가거나.'),('잊기 전에 복습','회독마다 언제 복습할지, 언제 끝날지 보여 줘요.')],
    price='무료로 시작해요. 라이벌로그 플러스는 월간·연간 구독이며 연간에는 7일 무료 체험이 있어요.',
    note=''),
  'chosim': dict(name='초심', kind='습관', line='작심삼일 말고 21일. 어젯밤의 내가 제시간에 깨워 줘요.',
    sub='작은 습관 하나와 시간을 정해요. 저녁마다 내일의 나에게 한마디를 남기면, 아침에 그 말이 제시간에 도착해요.',
    meta='iPhone · 9개 언어',
    features=[('21일, 습관 하나','끝없는 연속 기록 대신 끝이 있는 짧은 여정.'),('어젯밤의 한마디','전날 밤 내가 쓴 말이 정한 시간에 알림으로 와요.'),('응원해 주는 사람','링크를 보내면 친구가 내 진행 상황을 볼 수 있어요.')],
    price='무료로 체험해요. 21일 여정마다 소액 1회 구매이며 가격은 앱스토어에 원화로 표시돼요.',
    note=''),
  'wanderlure': dict(name='홀린 듯', kind='산책', line='피드 말고 진동을 따라, 모르는 곳으로 걷기.',
    sub='휴대폰 피드는 내려놓고 거리만 정해요. 가 본 적 없는 곳으로 진동이 안내해 줘요.',
    meta='iPhone · 6개 언어 · 걷는 동안 화면을 켜 두세요',
    features=[('모르는 목적지','얼마나 걸을지만 고르면 홀린 듯이 새로운 곳을 골라요.'),('진동을 따라','대략의 방향과 부드러운 진동으로 안내해서 눈은 길에 둘 수 있어요.'),('걸은 기록','내가 찾아낸 거리를 다시 돌아봐요.')],
    price='무료이며 광고로 운영돼요.',
    note=''),
  'story-accounting': dict(name='Story Accounting', kind='공부(영어)', line='ACCA FA·MA·FR 시험을 위한 짧은 회계 이야기.',
    sub='이야기가 정답 바로 앞에서 멈추면 내가 먼저 풀어요. 틀리면 그 실수의 이름을 알려 줘요. 앱은 영어로 되어 있어요.',
    meta='iPhone · 영어 · 앱스토어 심사 중',
    features=[('이야기로 배우는 기준서','짧은 장면으로 기준서를 설명하고, 옆에 계산 문제를 붙였어요.'),('내 차례','이야기가 답 앞에서 멈추고 내 선택을 물어요.'),('실수 노트','틀린 답에 이름을 붙여 저장해서 내 실수 패턴을 볼 수 있어요.')],
    price='처음 몇 편은 무료예요. FA·MA·FR 과목별 6개월·12개월 이용권을 팔아요.',
    note='비공식 학습 자료이며 ACCA와 관계가 없어요.'),
}
KO_STATUS = {'live':'앱스토어에 있어요','review':'앱스토어 심사 중','soon':'만드는 중'}

def head_ko(title, desc, depth, path, en_path):
    h = head(title, desc, depth, path)
    h = h.replace('<html lang="en">', '<html lang="ko">', 1)
    h = h.replace('<a class="skip" href="#main">Skip to content</a>', '<a class="skip" href="#main">본문으로 건너뛰기</a>')
    alt = f'<link rel="alternate" hreflang="ko" href="https://hiarche.com/{path}">\n<link rel="alternate" hreflang="en" href="https://hiarche.com/{en_path}">\n<style>body{{word-break:keep-all;overflow-wrap:anywhere}}</style>\n</head>'
    return h.replace('</head>', alt, 1)

def nav_ko(depth, current, en_href):
    up = '../' * depth
    items = [('앱', f'{up}ko/index.html#apps'), ('고객지원', f'{up}ko/support.html'), ('소식(영어)', f'{up}news.html'), ('회사 소개(영어)', f'{up}press.html')]
    cur = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{cur if n==current else ""}>{E(n)}</a>' for n,h in items)
    links += f'<a href="{en_href}" lang="en">English</a>'
    return f'<header class="top wrap"><a class="logo" href="{up}ko/index.html"><b>Hi</b>Arche</a><nav class="main" aria-label="주 메뉴">{links}</nav></header>\n'

def footer_ko(depth):
    up = '../' * depth
    return f'''<footer class="site wrap">
<div class="row">
<div style="display:flex;flex-direction:column;gap:8px"><span class="logo" style="font-size:22px"><b>Hi</b>Arche</span><span style="color:#50554B">질문이나 의견은 archeisit@gmail.com</span></div>
<nav aria-label="아래 메뉴" class="links" style="font-size:15px"><a href="{up}ko/support.html">고객지원</a><a href="{BOARD}">의견 게시판</a><a href="{up}legal.html">개인정보·약관(영어)</a><a href="https://www.instagram.com/arche.apps/">인스타그램</a></nav>
</div>
<div class="legal">
<p>상호 아르케(Arche) · 대표 박준형 · 사업자등록번호 774-39-01532 · 통신판매업 신고 제2026-용인기흥-01759호(용인시 기흥구청) · 전화 0502-1921-1532</p>
<p>경기도 용인시 기흥구 구갈로60번길 9-1 라파빌딩 7층 7201호 · archeisit@gmail.com</p>
<p>© 2026 Arche</p>
</div>
</footer>
</body>
</html>
'''

def build_ko():
    # ---- 홈 ----
    icons = ''.join(f'<img src="../assets/icons/{a["slug"]}.png" alt="" style="transform:rotate({t})">' for a,t in zip(APPS, ['-4deg','3deg','-2deg','2deg','-3deg','4deg']))
    cards = ''
    for a in APPS:
        k = KO[a['slug']]
        cards += f'''<a class="card appcard" href="apps/{a["slug"]}.html" aria-label="{E(k["name"])}: {E(k["line"])}">
<div class="apphead"><img src="../assets/icons/{a["slug"]}.png" alt=""><div><h3>{E(k["name"])}</h3><span class="kind">{E(k["kind"])}</span></div></div>
<p style="font-size:17px;flex-grow:1">{E(k["line"])}</p>
<div class="cardfoot"><span class="status {a["status"]}">{KO_STATUS[a["status"]]}</span><span class="more">앱 보기 &rarr;</span></div>
</a>
'''
    page = head_ko('HiArche — 정성껏 만든 작은 앱들', '아르케는 한국의 작은 앱 스튜디오예요. 니블로어, 솔로몬의 판결, 라이벌로그, 초심, 홀린 듯, Story Accounting.', 1, 'ko/', '') + nav_ko(1, '', '../index.html') + f'''<main id="main">
<section class="hero wrap">
<div class="text">
<p class="eyebrow">한국의 작은 앱 스튜디오</p>
<h1 class="h1">안녕하세요, <span style="color:var(--accent)">아르케</span>예요.</h1>
<p style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(24px,2.6vw,32px);font-weight:700">정성껏 만든 작은 앱들.</p>
<p class="lead">이야기를 쓰고, 모르는 곳으로 걷고, 습관을 지키고, 라이벌과 공부하고, 다툼에 판결을 받아요. 일상의 한 순간을 위한 작은 앱 여섯 개예요.</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;padding-top:8px"><a class="btn dark" href="#apps">앱 둘러보기</a><a class="btn line" href="../lab/lq2-test.html">LQ 학습 성향 검사</a></div>
</div>
<div class="icons" aria-hidden="true">{icons}</div>
</section>
<section id="apps" class="band"><div class="wrap sec">
<div class="sechead"><h2 class="h2">우리 앱</h2><p style="max-width:28em;font-size:17px;color:#50554B">앱을 누르면 무엇을 하는지 볼 수 있어요.</p></div>
<div class="grid">{cards}</div>
</div></section>
<section class="about"><div class="wrap sec">
<h2 class="h2" style="line-height:1.15">한 땀 한 땀,<br>손으로 만들어요.</h2>
<div class="body"><p>아르케는 한국에서 앱을 한 땀씩 정성껏 만드는 작은 스튜디오예요. 화려하진 않아도, 계속 쓰고 싶은 잘 만든 도구를 만들어요.</p><p>이름은 그리스어 아르케(arche), '시작'에서 왔어요. 모든 앱은 첫걸음을 위해 만들어요. 첫 페이지, 첫 산책, 첫날.</p></div>
</div></section>
</main>
''' + footer_ko(1)
    write('ko/index.html', page)

    # ---- 앱 페이지 ----
    for a in APPS:
        k = KO[a['slug']]
        if a['status'] == 'live':
            dl = f'<a class="btn" style="border-radius:12px;background:{a["fg"]};color:{a["bg"]}" href="{a["ios"].replace("/us/","/kr/")}">앱스토어에서 받기</a>'
        else:
            dl = f'<span class="btn" style="border-radius:12px;background:{a["fg"]};color:{a["bg"]}">{"앱스토어 심사 중" if a["status"]=="review" else "만드는 중"}</span>'
        feats = ''.join(f'<div class="card white"><h3 style="font-size:22px">{E(t)}</h3><p style="color:var(--soft)">{E(d)}</p></div>' for t,d in k['features'])
        terms = f'<a href="{a["terms"]}">이용약관</a>' if a['terms'] else ''
        note = f'<p class="note">{E(k["note"])}</p>' if k['note'] else ''
        extra = ''
        if a['slug'] == 'rivalog':
            extra = '''<section id="lq" class="wrap sec" style="padding-bottom:24px">
<div class="card white" style="gap:14px">
<p class="eyebrow" style="color:#B23E12">참여하기 · 베타</p>
<h2 style="font-size:clamp(28px,3.6vw,40px);font-weight:800">LQ 학습 성향 검사</h2>
<p class="lead" style="font-size:17px">짧은 과제 8개, 20~25분, 로그인 없이. 내가 어떻게 배우는지, 어떤 라이벌이 맞는지 알아봐요. 지능 검사가 아닌 추정이에요.</p>
<p style="color:var(--soft)">끝에서 원하면 기록을 익명으로 보내 기준을 만드는 데 보탤 수 있어요. '보내기'를 누르지 않으면 아무것도 보내지 않아요.</p>
<div style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn" style="border-radius:12px;background:#2F5D50;color:#F1F5F2" href="../../lab/lq2-test.html">검사 시작하기</a></div>
</div>
</section>
'''
        if a['slug'] == 'solomons-verdict':
            extra = '''<section class="wrap sec" style="padding-bottom:24px"><div class="card white" style="gap:10px">
<h2 style="font-size:clamp(24px,3vw,32px);font-weight:800">소환장을 받으셨나요?</h2>
<p style="color:var(--soft)">상대가 보낸 소환장 링크를 누르면 앱 없이 웹에서 바로 답변할 수 있어요.</p>
</div></section>
'''
        page = head_ko(f'{k["name"]} — {k["line"]} | HiArche', k['sub'], 2, f'ko/apps/{a["slug"]}.html', f'apps/{a["slug"]}.html') + nav_ko(2, '앱', f'../../apps/{a["slug"]}.html') + f'''<main id="main">
<section style="background:{a["bg"]};color:{a["fg"]}"><div class="wrap hero" style="padding-block:72px">
<div class="text">
<img src="../../assets/icons/{a["slug"]}.png" alt="{E(k["name"])} 앱 아이콘" style="width:96px;height:96px;border-radius:22px">
<h1 class="h1" style="font-size:clamp(40px,6vw,76px)">{E(k["name"])}</h1>
<p style="font-family:'Bricolage Grotesque',sans-serif;font-size:26px;font-weight:700">{E(k["line"])}</p>
<p style="font-size:18px;max-width:32em;opacity:.88">{E(k["sub"])}</p>
<div style="display:flex;flex-wrap:wrap;gap:12px">{dl}{'<a class="btn" style="border-radius:12px;border:2px solid '+a["fg"]+';color:'+a["fg"]+'" href="#lq">LQ 검사</a>' if a['slug']=='rivalog' else ''}<span class="btn" style="border-radius:12px;border:1.5px dashed {a["fg"]};opacity:.8">구글 플레이 · 곧</span></div>
<p style="font-size:14px;opacity:.78">{E(k["meta"])}</p>
</div>
</div></section>
{extra}<section class="wrap sec"><h2 style="font-size:clamp(30px,4vw,44px);font-weight:800">이런 걸 할 수 있어요</h2><div class="grid">{feats}</div></section>
<section class="band"><div class="wrap sec" style="flex-direction:row;flex-wrap:wrap;gap:48px">
<div style="flex:1 1 480px;min-width:0;display:flex;flex-direction:column;gap:16px">
<h2 style="font-size:clamp(30px,4vw,44px);font-weight:800">자주 묻는 질문</h2>
<div class="faq"><h3 style="font-size:19px">얼마예요?</h3><p style="color:var(--soft)">{E(k["price"])}</p></div>
<div class="faq"><h3 style="font-size:19px">도움은 어디서 받나요?</h3><p style="color:var(--soft)">도움말 페이지를 보거나, 의견 게시판에 남기거나, archeisit@gmail.com으로 앱 이름과 함께 메일을 보내 주세요.</p></div>
</div>
<div style="flex:1 1 300px;min-width:0;display:flex;flex-direction:column;gap:14px">
<h2 style="font-size:24px">링크</h2>
<a href="{a["support"]}">{E(k["name"])} 도움말</a><a href="{a["privacy"]}">개인정보처리방침</a>{terms}<a href="{BOARD}">의견 게시판</a>{note}
</div>
</div></section>
</main>
''' + footer_ko(2)
        write(f'ko/apps/{a["slug"]}.html', page)

    # ---- 고객지원 ----
    rows = ''.join(f'<article class="card white"><div class="apphead"><img src="../assets/icons/{a["slug"]}.png" alt=""><h3 style="font-size:22px">{E(KO[a["slug"]]["name"])}</h3></div><div class="links" style="font-size:15px"><a href="{a["support"]}">도움말</a><a href="{a["privacy"]}">개인정보처리방침</a></div></article>' for a in APPS)
    page = head_ko('고객지원 — HiArche', '아르케 앱 도움말, 의견 게시판, 이메일 문의.', 1, 'ko/support.html', 'support.html') + nav_ko(1, '고객지원', '../support.html') + f'''<main id="main" class="wrap" style="padding-block:48px 96px;display:flex;flex-direction:column;gap:48px">
<div style="display:flex;flex-direction:column;gap:12px"><h1 class="h1" style="font-size:clamp(40px,6vw,64px)">무엇을 도와드릴까요?</h1><p class="lead">앱을 골라 도움말을 보거나 메일을 보내 주세요. 모든 메일은 사람이 직접 읽어요.</p></div>
<section style="display:flex;flex-direction:column;gap:20px"><h2 style="font-size:28px">앱 고르기</h2><div class="grid">{rows}</div></section>
<section class="card white" style="gap:12px"><h2 style="font-size:28px">문의</h2><p style="color:var(--soft)">이메일 archeisit@gmail.com (앱 이름을 함께 적어 주세요) · 전화 0502-1921-1532 · <a href="{BOARD}">의견 게시판</a></p></section>
</main>
''' + footer_ko(1)
    write('ko/support.html', page)
