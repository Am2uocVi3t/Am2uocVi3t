from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

COLORS = {
 'dark': dict(bg='#08111D',panel='#101E2F', fg='#ECF7FF',muted='#92A8C1',low='#607991',accent='#5DE0D0',blue='#80ADFF',border='#274059',badge='#133B37',grid='#183047',good='#67E2AF',amber='#F5C477'),
 'light': dict(bg='#F3F7FC',panel='#FFFFFF', fg='#132338',muted='#5C7087',low='#7890A5',accent='#07887D',blue='#3663B7',border='#CBD9E6',badge='#DDF5EE',grid='#E1ECF6',good='#16885A',amber='#A4680B'),
}

SVG_START = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">'


def banner(theme):
 c=COLORS[theme]; b=c['bg']; fg=c['fg']; m=c['muted']; a=c['accent']; blue=c['blue']; border=c['border']; panel=c['panel']; low=c['low']
 s=SVG_START.format(w=1280,h=360)+f'''<title id="title">Huynh Quoc Viet | AI Research Terminal</title>
 <desc id="desc">AI Researcher, Machine Learning Engineer, AI Tech Lead at SpeedyLabX. Verifiable AI Systems. Research, reproduce, evaluate.</desc>
 <defs>
   <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{b}"/><stop offset="1" stop-color="{panel}"/></linearGradient>
   <radialGradient id="aura"><stop offset="0" stop-color="{blue}" stop-opacity=".15"/><stop offset="1" stop-color="{blue}" stop-opacity="0"/></radialGradient>
   <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M 36 0 L 0 0 0 36" fill="none" stroke="{c['grid']}" stroke-width="1"/></pattern>
   <clipPath id="round"><rect width="1278" height="358" x="1" y="1" rx="19"/></clipPath>
 </defs>
 <style>
  text{{font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace}}
  .blink{{animation:blink 1.1s steps(1) infinite}} .pulse{{animation:pulse 3s ease-in-out infinite}} .pulse2{{animation:pulse 3s ease-in-out -1.5s infinite}}
  .flow{{stroke-dasharray:8 11;animation:flow 8s linear infinite}} .breathe{{animation:breathe 5s ease-in-out infinite}}
  @keyframes blink{{0%,55%{{opacity:1}}56%,100%{{opacity:0}}}}
  @keyframes pulse{{0%,100%{{opacity:.38}}50%{{opacity:1}}}}
  @keyframes breathe{{0%,100%{{opacity:.35}}50%{{opacity:.7}}}}
  @keyframes flow{{to{{stroke-dashoffset:-152}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
 </style>
 <g clip-path="url(#round)">
  <rect width="1280" height="360" fill="url(#bg)"/>
  <rect width="1280" height="360" fill="url(#grid)" opacity=".7"/>
  <ellipse cx="1040" cy="166" rx="390" ry="275" fill="url(#aura)"/>
  <rect x="0" y="0" width="1280" height="5" fill="{a}" opacity=".8"/>
  <rect x="0" y="0" width="1280" height="360" fill="none" stroke="{border}" stroke-width="2" rx="19"/>
  <!-- window header -->
  <circle cx="39" cy="34" r="6" fill="#F07E76"/><circle cx="59" cy="34" r="6" fill="#E8C76A"/><circle cx="79" cy="34" r="6" fill="#62CFA0"/>
  <text x="112" y="39" font-size="15" fill="{m}">viet@research:~$ ./profile --init</text>
  <rect x="983" y="19" width="254" height="31" rx="15.5" fill="{c['badge']}" stroke="{border}"/>
  <circle cx="1003" cy="35" r="4.5" fill="{c['good']}" class="pulse"/>
  <text x="1017" y="40" font-size="12" letter-spacing="1.1" fill="{a}">RESEARCH IN PROGRESS</text>
  <line x1="35" y1="63" x2="1245" y2="63" stroke="{border}"/>
  <!-- main identity -->
  <text x="64" y="105" font-size="14" letter-spacing="2.5" fill="{a}">&gt; RESEARCH PROFILE / 001</text>
  <text x="60" y="176" font-size="59" font-weight="700" letter-spacing="-2" fill="{fg}">HUYNH QUOC VIET</text>
  <rect x="64" y="195" width="48" height="4" rx="2" fill="{a}"/>
  <text x="64" y="236" font-size="22" fill="{fg}">AI Researcher <tspan fill="{blue}">/</tspan> ML Engineer</text>
  <text x="64" y="269" font-size="20" fill="{m}">AI Tech Lead <tspan fill="{blue}">@</tspan> SpeedyLabX</text>
  <text x="64" y="302" font-size="14" fill="{low}">RESEARCH</text><text x="146" y="302" font-size="14" fill="{a}">→</text>
  <text x="171" y="302" font-size="14" fill="{low}">REPRODUCE</text><text x="270" y="302" font-size="14" fill="{a}">→</text>
  <text x="296" y="302" font-size="14" fill="{low}">EVALUATE</text>
  <rect class="blink" x="394" y="289" width="9" height="17" fill="{a}"/>
  <!-- right-side research diagram -->
  <line x1="868" y1="84" x2="868" y2="307" stroke="{border}"/>
  <text x="903" y="103" font-size="13" letter-spacing="1.4" fill="{m}">RESEARCH / SYSTEM MAP</text>
  <circle cx="1052" cy="204" r="88" fill="none" stroke="{border}" stroke-width="1.4"/>
  <circle cx="1052" cy="204" r="63" fill="none" stroke="{blue}" opacity=".5" stroke-width="1.2" stroke-dasharray="4 9" class="flow"/>
  <circle cx="1052" cy="204" r="42" fill="{panel}" stroke="{a}" stroke-width="1.8"/>
  <circle cx="1052" cy="204" r="34" fill="{a}" fill-opacity=".06" class="breathe"/>
  <text x="1052" y="211" text-anchor="middle" font-size="24" fill="{fg}" font-weight="700">AI</text>
  <path d="M 1052 141 L 1052 162 M 1114 204 L 1094 204 M 1052 246 L 1052 266 M 989 204 L 1010 204" stroke="{a}" stroke-width="1.5" stroke-dasharray="5 5" class="flow"/>
  <circle cx="1052" cy="116" r="7" fill="{a}" class="pulse"/>
  <circle cx="1140" cy="204" r="7" fill="{blue}" class="pulse2"/>
  <circle cx="1052" cy="292" r="7" fill="{a}" class="pulse2"/>
  <circle cx="964" cy="204" r="7" fill="{blue}" class="pulse"/>
  <text x="1052" y="130" text-anchor="middle" font-size="10" fill="{m}">CONFORMAL</text>
  <text x="1149" y="189" font-size="11" fill="{m}">TIME</text><text x="1149" y="202" font-size="11" fill="{m}">SERIES</text>
  <text x="1052" y="312" text-anchor="middle" font-size="11" fill="{m}">VISION</text>
  <text x="899" y="190" font-size="11" fill="{m}">RL</text>
  <!-- footer status line -->
  <rect x="0" y="325" width="1280" height="35" fill="{panel}" opacity=".85"/>
  <line x1="0" y1="325" x2="1280" y2="325" stroke="{border}"/>
  <text x="38" y="347" font-size="12" fill="{m}">HCMC, VIETNAM</text>
  <circle cx="214" cy="342" r="2" fill="{low}"/>
  <text x="229" y="347" font-size="12" fill="{m}">FPT UNIVERSITY</text>
  <text x="1240" y="347" text-anchor="end" font-size="12" fill="{a}">BUILD / TEST / AUDIT</text>
 </g></svg>'''
 (ASSETS/f'profile-banner-{theme}.svg').write_text(s,encoding='utf-8')


def typing(theme):
 c=COLORS[theme]; fg=c['fg']; a=c['accent']; m=c['muted']; border=c['border']; b=c['bg']; panel=c['panel']
 # Entire source is self-contained; each line is revealed via a clip-path rectangle.
 # CSS animations phase-shift in 5 s increments. This is native SVG, not JS.
 lines=[
  'Research → Reproduce → Evaluate',
  'Building Verifiable AI Systems',
  'Beyond Accuracy. Toward Trustworthy AI.',
  'From research questions to evaluated systems.'
 ]
 anim=[]
 for i,line in enumerate(lines):
  pixels=round(len(line)*14.47)
  anim.append(f".window{i}{{animation-name:type{i}}} .caret{i}{{animation-name:caret{i}}}")
  anim.append(f"@keyframes type{i}{{0%{{width:0}}17%,23.99%{{width:{pixels}px}}24%,100%{{width:0}}}}")
  anim.append(f"@keyframes caret{i}{{0%{{transform:translateX(0)}}17%,23.99%{{transform:translateX({pixels}px)}}24%,100%{{transform:translateX(0)}}}}")
 custom_animations=" ".join(anim)
 s=SVG_START.format(w=1200,h=106)+f'''<title id="title">Animated research slogans</title>
 <desc id="desc">Research, reproduce, evaluate. Building verifiable AI systems. Beyond accuracy, toward trustworthy AI. From research questions to evaluated systems.</desc>
 <style>
  text{{font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace}}
  .line{{animation:phase 20s steps(1,end) infinite}}
  .window{{animation-duration:20s;animation-timing-function:steps(45,end);animation-iteration-count:infinite}}
  .caret{{animation-duration:20s;animation-timing-function:steps(45,end);animation-iteration-count:infinite}}
  .phase0{{animation-delay:0s}} .phase1{{animation-delay:-15s}} .phase2{{animation-delay:-10s}} .phase3{{animation-delay:-5s}}
  @keyframes phase{{0%,24.99%{{opacity:1}}25%,100%{{opacity:0}}}}
  {custom_animations}
  @media(prefers-reduced-motion:reduce){{.line,.window,.caret{{animation:none!important}}.line{{opacity:0}}.line.phase0{{opacity:1}}.window{{width:1035px}}.caret{{display:none}}}}
 </style>
 <defs>'''
 for i in range(4):
  s+=f'<clipPath id="type{i}"><rect class="window window{i} phase{i}" x="85" y="42" width="1035" height="43"/></clipPath>'
 s+=f'''</defs>
 <rect x="1" y="1" width="1198" height="104" rx="16" fill="{panel}" stroke="{border}" stroke-width="1.5"/>
 <rect x="1" y="1" width="5" height="104" rx="2" fill="{a}"/>
 <text x="27" y="31" fill="{m}" font-size="13" letter-spacing="1.4">$ echo $RESEARCH_PHILOSOPHY</text>
 <text x="31" y="72" fill="{a}" font-size="26" font-weight="700">&gt;</text>
 '''
 for i,line in enumerate(lines):
  opacity='1' if i==0 else '0'
  s+=f'<g class="line phase{i}" opacity="{opacity}"><text x="86" y="74" font-size="24" fill="{fg}" clip-path="url(#type{i})">{escape(line)}</text>'
  # Caret: its position follows the reveal width until end of 5s window.
  s+=f'<rect class="caret caret{i} phase{i}" x="84" y="51" width="3" height="27" fill="{a}"/></g>'
 s+=f'<text x="1163" y="31" text-anchor="end" fill="{m}" font-size="12">/ four-line loop</text></svg>'
 (ASSETS/f'typing-{theme}.svg').write_text(s,encoding='utf-8')


def research(theme):
 c=COLORS[theme]; bg=c['bg']; panel=c['panel']; fg=c['fg']; m=c['muted']; blue=c['blue']; accent=c['accent']; border=c['border']; good=c['good']; amber=c['amber']
 cards=[
  ('01','AJCAI 2026','ACCEPTED POSTER','Air-quality alerts','Exposure-aware forecasts',good),
  ('02','KDD 2027','DECISION PENDING','Multimodal anomalies','Research Track · Cycle 1',amber),
  ('03','AISTATS 2027','UNDER REVIEW','Unseen IoT devices','Coverage · Device-disjoint',blue),
  ('04','ACIIDS 2027','UNDER REVIEW','Bloom forecasting','Sparse monitoring',blue)
 ]
 s=SVG_START.format(w=1280,h=272)+f'''<title id="title">Research submission status snapshot</title>
 <desc id="desc">As of October 29, 2026: AJCAI accepted poster; KDD 2027 Research Track Cycle 1 decision pending; AISTATS 2027 under review; ACIIDS 2027 under review.</desc>
 <style>
  text{{font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace}}
  .track{{stroke-dasharray:10 14;animation:move 9s linear infinite}}
  .dot{{animation:pulse 2.8s ease-in-out infinite}}
  @keyframes move{{to{{stroke-dashoffset:-192}}}}
  @keyframes pulse{{0%,100%{{opacity:.5}}50%{{opacity:1}}}}
  @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
 </style>
 <rect x="1" y="1" width="1278" height="270" rx="18" fill="{bg}" stroke="{border}" stroke-width="1.5"/>
 <text x="35" y="36" fill="{accent}" font-size="13" letter-spacing="1.8">&gt; RESEARCH / SUBMISSION SNAPSHOT</text>
 <text x="1245" y="36" text-anchor="end" fill="{m}" font-size="12">29 OCT 2026</text>
 <line x1="47" y1="65" x2="1233" y2="65" stroke="{border}" stroke-width="2"/>
 <line class="track" x1="47" y1="65" x2="1233" y2="65" stroke="{accent}" stroke-width="1.5"/>
 '''
 for i,(num,conf,status,study,sub,col) in enumerate(cards):
  x=36+i*311; w=274
  center=x+w//2
  s+=f'''<circle cx="{center}" cy="65" r="7" fill="{col}" class="dot" style="animation-delay:-{i*0.6}s"/>
  <rect x="{x}" y="86" width="{w}" height="155" rx="12" fill="{panel}" stroke="{border}"/>
  <text x="{x+18}" y="115" fill="{m}" font-size="12">TRACK / {num}</text>
  <text x="{x+18}" y="142" fill="{fg}" font-size="23" font-weight="700">{conf}</text>
  <text x="{x+18}" y="165" fill="{col}" font-size="11" font-weight="700" letter-spacing=".5">{status}</text>
  <line x1="{x+18}" y1="177" x2="{x+w-18}" y2="177" stroke="{border}"/>
  <text x="{x+18}" y="199" fill="{fg}" font-size="14">{escape(study)}</text>
  <text x="{x+18}" y="219" fill="{m}" font-size="12">{escape(sub)}</text>'''
 s+=f'''<text x="35" y="260" fill="{m}" font-size="11">Accepted and under-review work are distinct statuses. Links and detailed descriptions appear in the table below.</text></svg>'''
 (ASSETS/f'research-pipeline-{theme}.svg').write_text(s,encoding='utf-8')


for theme in COLORS:
 banner(theme)
 typing(theme)
 research(theme)
print('Generated 6 SVGs:', *[str(p) for p in ASSETS.glob('*.svg')], sep='\n')
