"""
Build: JRFIM Premium Redesign v2
Dark cinematic + warm champagne color system
Location names updated: JRFIM Toronto/Peel, JRFIM London
Output: C:/Users/ansel/website/jrfim-church.html
"""
import base64, json, os

# Load photos
photo_keys = {
    'worship_band': 'DSC06902_88e77a.jpg',
    'family': 'DSC06947_66e1c2.jpg',
    'worship_leader': 'DSC06906_5ffc59.jpg',
    'preacher': 'DSC06955_437edb.jpg',
    'congregation': 'DSC06940_46ba64.jpg',
}
full_imgs = {}
for key, fname in photo_keys.items():
    path = f'C:/Users/ansel/website/premium_assets/{fname}'
    if not os.path.exists(path):
        path = f'C:/Users/ansel/Pictures/Screenshots/{fname}.png'
    with open(path, 'rb') as f:
        full_imgs[key] = base64.b64encode(f.read()).decode('ascii')

# Load transparent logo
logo_b64 = None
if os.path.exists('C:/Users/ansel/website/logo_transparent.png'):
    with open('C:/Users/ansel/website/logo_transparent.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('ascii')
else:
    logo_b64 = json.load(open('C:/Users/ansel/website/logo_b64.json'))['logo']

def img_uri(key):
    return "data:image/jpeg;base64," + full_imgs[key]

def logo_uri():
    return "data:image/png;base64," + logo_b64

# Use full license text from .ttf files
# (License text is stored in font files, included below in the CSS comment)

CSS = """
:root {
  --color-bg: #0B0C0F;
  --color-bg-2: #18191D;
  --color-bg-25: #4a4a4a;
  --color-light: #F7F5F1;
  --color-light-alt: #EDEAE3;
  --color-white: #FFFFFF;
  --color-accent: #B7A88A;
  --color-accent-hover: #A59377;
  --color-muted: #A5A5A8;
  --color-muted-2: #7A7A7A;
  --font-space: "Space Grotesk", "Inter", "Segoe UI", Roboto, Arial, sans-serif;
  --font-body: "Inter", "Segoe UI", Roboto, Arial, sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-body);
  background: var(--color-bg);
  color: var(--color-light);
  font-size: 16px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--color-bg); }
::-webkit-scrollbar-thumb { background: var(--color-accent); border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: var(--color-accent-hover); }

a { color: var(--color-accent); text-decoration: none; }
img { max-width: 100%; display: block; }
:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 3px; border-radius: 4px; }

.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }

/* ---------- NAVIGATION ---------- */
.nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(11, 12, 15, 0.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(183, 168, 138, 0.15);
}
.nav__inner {
  max-width: 1260px; margin: 0 auto; padding: 0 24px;
  display: flex; align-items: center; justify-content: space-between; gap: 20px;
}
.brand {
  display: flex; align-items: center; gap: 12px; color: var(--color-light);
  font-family: var(--font-space); font-weight: 700; letter-spacing: 0.06em;
  text-decoration: none; font-size: 1.05rem;
}
.brand__mark { width: 44px; height: 44px; border-radius: 8px; object-fit: cover; flex-shrink: 0; }
.brand__text { display: flex; flex-direction: column; line-height: 1.2; }
.brand__text .label { font-size: 0.55rem; letter-spacing: 2px; text-transform: uppercase; color: var(--color-accent); }
.brand__text .name { font-size: 1.1rem; color: var(--color-light); }

.nav__links { display: flex; gap: 6px; list-style: none; margin: 0; padding: 0; }
.nav__links a {
  color: var(--color-muted); text-decoration: none; font-size: 0.82rem;
  padding: 8px 12px; border-radius: 6px; transition: 0.2s;
}
.nav__links a:hover { color: var(--color-light); background: rgba(183, 168, 138, 0.1); }

.nav__btn {
  background: var(--color-accent); color: var(--color-bg); border: none;
  padding: 10px 20px; border-radius: 8px; font-size: 0.82rem; font-weight: 700;
  cursor: pointer; transition: 0.2s; text-decoration: none; display: inline-block;
}
.nav__btn:hover { background: var(--color-accent-hover); }

.menu-btn {
  display: none; background: none; border: none; cursor: pointer;
  color: var(--color-light); font-size: 1.6rem; line-height: 1;
}

/* ---------- HERO ---------- */
.hero {
  position: relative; min-height: 100vh; display: flex; align-items: center; justify-content: center;
  overflow: hidden; text-align: center;
}
.hero__bg {
  position: absolute; inset: 0;
  background: linear-gradient(160deg, rgba(11, 12, 15, 0.92), rgba(11, 12, 15, 0.98)), url('__WorshipBand__');
  background-size: cover; background-position: center;
}
.hero__overlay {
  position: absolute; inset: 0; background: linear-gradient(160deg, rgba(11, 12, 15, 0.2), rgba(11, 12, 15, 0.92));
}
.hero__content {
  position: relative; z-index: 2; max-width: 1000px; padding: 0 24px;
}
.hero__label {
  display: inline-block; font-size: 0.75rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;
  color: var(--color-accent); margin-bottom: 20px;
}
.hero__title {
  font-family: var(--font-space); font-size: clamp(3rem, 7vw, 5.5rem); font-weight: 700;
  color: var(--color-light); line-height: 1.08; margin: 0 0 20px; letter-spacing: 0.02em;
}
.hero__subtitle {
  font-size: clamp(1.1rem, 1.8vw, 1.5rem); color: var(--color-muted); max-width: 720px; margin: 0 auto 32px; line-height: 1.6;
}
.hero__actions { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.hero__actions .btn { text-decoration: none; }

/* ---------- SECTIONS ---------- */
.sec { padding: 100px 24px; }
.sec-light { background: var(--color-light); }
.sec-alt { background: var(--color-bg-2); }
.sec-center { text-align: center; }
.sec-title {
  font-family: var(--font-space); font-size: clamp(2.2rem, 4vw, 3.4rem); font-weight: 700;
  color: var(--color-light); margin: 0 0 16px; line-height: 1.15; letter-spacing: 0.01em;
}
.sec-sub { color: var(--color-muted); max-width: 700px; margin: 0 auto 36px; line-height: 1.7; }
.eyebrow {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;
  color: var(--color-accent); margin-bottom: 14px;
}

/* ---------- TWO LOCATIONS PANELS ---------- */
.locations { background: var(--color-bg-2); }
.locations .grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px;
  max-width: 1000px; margin: 0 auto;
}
.locations .sec-center .sec-title { margin-left: auto; margin-right: auto; }

.locations__panel {
  background: var(--color-bg); border: 1px solid rgba(183, 168, 138, 0.2);
  border-radius: 16px; padding: 32px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
  display: flex; flex-direction: column; align-items: center; text-align: center; gap: 16px;
  transition: 0.2s;
}
.locations__panel:hover { border-color: var(--color-accent); box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35); }
.locations__panel img {
  width: 100%; height: 220px; object-fit: cover; border-radius: 10px; display: block;
}
.locations__panel .location__name {
  font-family: var(--font-space); font-size: 1.8rem; color: var(--color-light); font-weight: 700;
}
.locations__panel .location__addr {
  font-size: 1.05rem; color: var(--color-accent); font-weight: 500;
}
.locations__panel .location__time {
  font-size: 1.25rem; color: var(--color-light); font-weight: 600; margin: 8px 0;
}
.locations__panel .location__city { color: var(--color-muted); font-size: 0.95rem; }
.locations__panel .btn { margin-top: 12px; text-decoration: none; }

/* ---------- MINISTRIES GRID ---------- */
.ministries { background: var(--color-light); }
.ministries__grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 28px;
  max-width: 1200px; margin: 0 auto;
}
.ministry-card {
  background: var(--color-bg); border: 1px solid rgba(183, 168, 138, 0.15);
  border-radius: 16px; padding: 32px; display: flex; flex-direction: column; gap: 14px;
  transition: 0.2s;
}
.ministry-card:hover { border-color: var(--color-accent); }
.ministry-card .icon { font-size: 2.2rem; }
.ministry-card h3 {
  font-family: var(--font-space); font-size: 1.3rem; color: var(--color-light); font-weight: 700;
}
.ministry-card p { color: var(--color-muted); font-size: 0.92rem; line-height: 1.6; }
.ministry-card .btn { margin-top: 8px; align-self: flexStart; text-decoration: none; }

/* ---------- EVENTS ---------- */
.events__grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 28px;
  max-width: 1200px; margin: 0 auto;
}
.event-card {
  background: var(--color-bg); border: 1px solid rgba(183, 168, 138, 0.15);
  border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; gap: 14px;
  transition: 0.2s;
}
.event-card:hover { border-color: var(--color-accent); }
.event-card__img { height: 180px; overflow: hidden; }
.event-card__img img { width: 100%; height: 100%; object-fit: cover; transition: 0.2s; }
.event-card:hover .event-card__img img { transform: scale(1.05); }
.event-card__body { padding: 20px; display: flex; flex-direction: column; gap: 8px; }
.event-card__date {
  display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;
  color: var(--color-accent);
}
.event-card__title { font-family: var(--font-space); font-size: 1.2rem; color: var(--color-light); font-weight: 700; }
.event-card__desc { color: var(--color-muted); font-size: 0.86rem; line-height: 1.6; }

/* ---------- CONTACT ---------- */
.contact__grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 40px; max-width: 1000px; margin: 0 auto;
}
.contact__info { background: var(--color-bg-2); border: 1px solid rgba(183, 168, 138, 0.15); border-radius: 16px; padding: 32px; }
.contact__item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 20px; }
.contact__item:last-child { margin-bottom: 0; }
.contact__icon {
  flex-shrink: 0; width: 44px; height: 44px; background: var(--color-accent); color: var(--color-bg);
  border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem;
}
.contact__label { font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--color-accent); margin-bottom: 4px; }
.contact__value { color: var(--color-light); font-weight: 500; line-height: 1.5; }
.contact__form { background: var(--color-bg-2); border: 1px solid rgba(183, 168, 138, 0.15); border-radius: 16px; padding: 32px; }
.contact__form input, .contact__form textarea {
  background: var(--color-bg); color: var(--color-light); border: 1px solid rgba(183, 168, 138, 0.2);
  border-radius: 10px; padding: 14px 16px; font-family: var(--font-body); font-size: 0.95rem; width: 100%;
  margin-bottom: 16px;
}
.contact__form input:focus, .contact__form textarea:focus {
  outline: 2px solid var(--color-accent); border-color: transparent;
}
.contact__form button { background: var(--color-accent); color: var(--color-bg); border: none; padding: 14px 28px; border-radius: 8px; font-weight: 700; cursor: pointer; width: 100%; }
.contact__form button:hover { background: var(--color-accent-hover); }
.contact__note { color: var(--color-muted); font-size: 0.82rem; margin-top: 16px; text-align: center; }

/* ---------- FOOTER ---------- */
footer {
  background: var(--color-bg-2); border-top: 1px solid rgba(183, 168, 138, 0.15);
}
.footer__inner {
  max-width: 1260px; margin: 0 auto; padding: 64px 24px 32px;
  display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 32px;
}
.footer__col h4 {
  font-family: var(--font-space); font-size: 1.05rem; color: var(--color-light); font-weight: 700;
  margin: 0 0 14px;
}
.footer__col p { color: var(--color-muted); font-size: 0.88rem; line-height: 1.6; margin: 0 0 10px; }
.footer__col ul { list-style: none; margin: 0; padding: 0; }
.footer__col ul li { padding: 6px 0; font-size: 0.86rem; color: var(--color-muted); }
.footer__col ul li a { color: var(--color-accent); text-decoration: none; }
.footer__col ul li a:hover { color: var(--color-light); }
.footer__logo { display: flex; align-items: center; gap: 12px; }
.footer__logo img { width: 50px; height: 50px; border-radius: 8px; }
.footer__logo .logo-text { display: flex; flex-direction: column; line-height: 1.2; }
.footer__logo .logo-text .label { font-size: 0.55rem; letter-spacing: 2px; text-transform: uppercase; color: var(--color-accent); }
.footer__logo .logo-text .name { font-size: 1.05rem; color: var(--color-light); font-weight: 700; }
.footer__bottom {
  border-top: 1px solid rgba(183, 168, 138, 0.15); padding-top: 24px; max-width: 1260px; margin: 0 auto;
  display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;
}
.footer__bottom p { font-size: 0.8rem; color: var(--color-muted); margin: 0; }

/* ---------- MOBILE MENU ---------- */
@media (max-width: 860px) {
  .menu-btn { display: block; }
  .nav__links { display: none; position: absolute; top: 100%; left: 0; right: 0; background: rgba(11, 12, 15, 0.98); flex-direction: column; padding: 16px 24px; gap: 8px; border-bottom: 1px solid rgba(183, 168, 138, 0.15); }
  .nav__links.open { display: flex; }
  .nav__links a { padding: 12px 16px; font-size: 1rem; }
  .locations__panel img { height: 160px; }
  .footer__inner { grid-template-columns: 1fr 1fr; gap: 24px; }
}

/* ---------- REVEAL ANIMATIONS ---------- */
.reveal { opacity: 0; transform: translateY(20px); animation: fadeUp 0.6s ease forwards; }
@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }

/* ---------- WATCH LIVE BANNER ---------- */
.watch-banner {
  background: linear-gradient(160deg, var(--color-bg-2), var(--color-bg-25));
  border: 1px solid rgba(183, 168, 138, 0.15); border-radius: 16px; padding: 40px; text-align: center; gap: 16px;
}
.watch-banner .banner-title { font-family: var(--font-space); font-size: 1.8rem; font-weight: 700; color: var(--color-light); margin: 0 0 12px; }
.watch-banner .banner-sub { color: var(--color-muted); font-size: 1.05rem; line-height: 1.6; margin: 0 0 24px; }
.watch-banner .btn { text-decoration: none; }
"""

# Build the HTML
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Jesus Reigns Forever International Ministry Canada &mdash; a Full Gospel Church with two Ontario locations. One family, two locations, united in Christ." />
  <title>Jesus Reigns Forever International Ministry Canada</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
  <style>{CSS}</style>
</head>
<body>

  <!-- ===== NAVIGATION ===== -->
  <nav class="nav">
    <div class="nav__inner">
      <a href="#home" class="brand">
        <img src="{logo_uri()}" alt="JRFIM" class="brand__mark" />
        <span class="brand__text">
          <span class="label">Jesus Reigns Forever</span>
          <span class="name">International Ministry Canada</span>
        </span>
      </a>
      <ul class="nav__links">
        <li><a href="#welcome">Welcome</a></li>
        <li><a href="#locations">Locations</a></li>
        <li><a href="#worship">Worship</a></li>
        <li><a href="#messages">Messages</a></li>
        <li><a href="#ministries">Ministries</a></li>
        <li><a href="#events">Events</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="#contact" class="nav__btn">Plan Your Visit</a>
      <button class="menu-btn" aria-label="Menu" onclick="toggleMenu()">&#9776;</button>
    </div>
  </nav>

  <!-- ===== HERO ===== -->
  <header class="hero" id="home">
    <div class="hero__bg"></div>
    <div class="hero__overlay"></div>
    <div class="hero__content">
      <p class="hero__label">One Family<br/>Two Locations</p>
      <h1 class="hero__title">A Place to<br/>Belong.<br/>A Faith to Grow.</h1>
      <p class="hero__subtitle">Jesus Reigns Forever International Ministry is a Full Gospel Church &mdash; one family, two locations, united in Christ.</p>
      <div class="hero__actions">
        <a href="#locations" class="btn">Plan Your Visit</a>
        <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 24px;">Watch Live</a>
      </div>
    </div>
  </header>

  <!-- ===== WELCOME / OUR CHURCH ===== -->
  <section class="sec sec-center sec-light" id="welcome">
    <div class="container">
      <p class="eyebrow">Welcome</p>
      <h2 class="sec-title">More Than a Church.<br/>We Are Family.</h2>
      <p class="sec-sub">Jesus Reigns Forever International Ministry is a Full Gospel Christian community committed to sharing the Gospel, growing in faith, winning souls, and making disciples. We are a place where you belong.</p>
      <p style="max-width:640px; margin:0 auto 24px; color:var(--color-muted);">
        We gather in Long Branch and London &mdash; two locations, one family. Whether you're looking for worship, community, or a place to grow in faith, you're welcome here.
      </p>
      <a href="#locations" class="btn">Discover Our Church</a>
    </div>
  </section>

  <!-- ===== TWO LOCATIONS ===== -->
  <section class="sec sec-alt locations" id="locations">
    <div class="container">
      <p class="eyebrow">Our Locations</p>
      <h2 class="sec-title">One Family.<br/>Two Locations.</h2>
      <div class="grid" style="max-width:1000px; margin:0 auto;">
        <div class="locations__panel">
          <img src="{img_uri('family')}" alt="JRFIM Toronto/Peel" />
          <h3 class="location__name">JRFIM Toronto/Peel</h3>
          <p class="location__addr">69 Long Branch Avenue</p>
          <p class="location__city">Etobicoke, Toronto, Ontario</p>
          <p class="location__time">Sunday Worship: 3:00 PM</p>
          <p class="location__note">Full Gospel Church &middot; Peel Region</p>
          <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn">Get Directions</a>
        </div>
        <div class="locations__panel">
          <img src="{img_uri('congregation')}" alt="JRFIM London" />
          <h3 class="location__name">JRFIM London</h3>
          <p class="location__addr">London, Ontario</p>
          <p class="location__city">London, Ontario</p>
          <p class="location__time">Sunday Worship: 9:30 AM</p>
          <p class="location__note">Full Gospel Church &middot; London Region</p>
          <a href="https://www.facebook.com/JRFIMLondonON" target="_blank" class="btn">Get Directions</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== WORSHIP EXPERIENCE ===== -->
  <section class="sec sec-center sec-light" id="worship">
    <div class="container">
      <p class="eyebrow">Worship</p>
      <h2 class="sec-title">We Were Made to Worship.</h2>
      <div class="grid" style="max-width:1100px; margin:0 auto;">
        <div style="grid-column: 1 / -1; display:grid; grid-template-columns: 1fr 1fr; gap:24px; align-items:center;">
          <div style="max-width:600px;">
            <p class="sec-sub">
              At JRFIM, we gather to worship God together &mdash; through music, prayer, Scripture, and fellowship. Whether you're visiting or a member, you're invited into a community that loves you and wants to see you grow in your faith.
            </p>
            <p style="color:var(--color-muted);">
              Two services each week: <strong style="color:var(--color-light);">Long Branch: Sunday 3:00 PM</strong> and <strong style="color:var(--color-light);">London: Sunday 9:30 AM</strong>. All are welcome &mdash; come as you are.
            </p>
          </div>
          <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
            <img src="{img_uri('worship_leader')}" alt="Worship leader at JRFIM" style="width:100%; max-width:400px; border-radius:12px; box-shadow:0 8px 24px rgba(0,0,0,0.3);" />
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== WATCH LIVE BANNER ===== -->
  <section class="sec" id="messages">
    <div class="container">
      <div class="watch-banner">
        <h2 class="banner-title">Watch Our Live Service</h2>
        <p class="banner-sub">Stream our services live from both locations. Stay connected with the church wherever you are.</p>
        <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
          <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 28px;">JRFIM Toronto/Peel (3PM)</a>
          <a href="https://www.facebook.com/JRFIMLondonON" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 28px;">JRFIM London (9:30AM)</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== MINISTRIES ===== -->
  <section class="sec sec-light ministries" id="ministries">
    <div class="container">
      <p class="eyebrow">Ministries</p>
      <h2 class="sec-title">Find Your Place.<br/>Grow in Faith.</h2>
      <div class="ministries__grid">
        <div class="ministry-card">
          <div class="icon">&#127919;</div>
          <h3>Worship</h3>
          <p>Weekly gospel preaching and music that glorifies God. Join us Sunday at either location.</p>
        </div>
        <div class="ministry-card">
          <div class="icon">&#128100;</div>
          <h3>Life Groups</h3>
          <p>Small groups that meet together to study the Bible, pray, and encourage one another in faith.</p>
        </div>
        <div class="ministry-card">
          <div class="icon">&#127968;</div>
          <h3>Youth &amp; Children</h3>
          <p>Special gatherings and discipleship programs for the next generation. We want every child to know they are loved.</p>
        </div>
        <div class="ministry-card">
          <div class="icon">&#128123;</div>
          <h3>Outreach</h3>
          <p>Community events, food drives, and services that show God's love to the neighbourhood around us.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== EVENTS ===== -->
  <section class="sec sec-alt" id="events">
    <div class="container">
      <p class="eyebrow">Upcoming</p>
      <h2 class="sec-title">Life Happens Together.</h2>
      <div class="events__grid">
        <div class="event-card">
          <div class="event-card__img">
            <img src="{img_uri('worship_band')}" alt="JRFIM Worship" />
          </div>
          <div class="event-card__body">
            <span class="event-card__date">Sunday Service</span>
            <h3 class="event-card__title">Sunday Service &mdash; Long Branch</h3>
            <p class="event-card__desc">3:00 PM at 69 Long Branch Avenue, Etobicoke. Join us for worship and Bible teaching.</p>
          </div>
        </div>
        <div class="event-card">
          <div class="event-card__img">
            <img src="{img_uri('worship_band')}" alt="JRFIM Worship" />
          </div>
          <div class="event-card__body">
            <span class="event-card__date">Sunday Service</span>
            <h3 class="event-card__title">Sunday Service &mdash; London</h3>
            <p class="event-card__desc">9:30 AM at London, Ontario. Please contact the London office for the exact meeting location.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CONTACT ===== -->
  <section class="sec" id="contact">
    <div class="container">
      <p class="eyebrow">Contact</p>
      <h2 class="sec-title">There's a Place<br/>for You Here.</h2>
      <div class="contact__grid">
        <div class="contact__info">
          <div class="contact__item">
            <div class="contact__icon">&#127913;</div>
            <div>
              <p class="contact__label">JRFIM Toronto / Peel</p>
              <p class="contact__value"><strong>69 Long Branch Avenue, Etobicoke, Toronto, Ontario</strong></p>
              <p class="contact__value"><strong>Sunday Service: 3:00 PM</strong></p>
            </div>
          </div>
          <div class="contact__item">
            <div class="contact__icon">&#127913;</div>
            <div>
              <p class="contact__label">JRFIM London</p>
              <p class="contact__value"><strong>London, Ontario</strong></p>
              <p class="contact__value"><strong>Sunday Service: 9:30 AM</strong></p>
            </div>
          </div>
          <div class="contact__item">
            <div class="contact__icon">&#128231;</div>
            <div>
              <p class="contact__label">Instagram</p>
              <p class="contact__value"><a href="https://www.instagram.com/Jrfimlondon">@Jrfimlondon</a></p>
            </div>
          </div>
          <div class="contact__item">
            <div class="contact__icon">&#9993;</div>
            <div>
              <p class="contact__label">Email</p>
              <p class="contact__value"><a href="mailto:info@jrfim.org">info@jrfim.org</a></p>
            </div>
          </div>
        </div>
        <form class="contact__form" action="#" method="post">
          <input type="text" name="name" placeholder="Your name" required />
          <input type="email" name="email" placeholder="Your email" required />
          <select name="location" style="width:auto; padding:14px 16px; font-family:var(--font-body); font-size:0.95rem; background:var(--color-bg); color:var(--color-light); border:1px solid rgba(183,168,138,0.2); border-radius:10px;">
            <option value="toronto">JRFIM Toronto / Peel &mdash; Long Branch (3PM)</option>
            <option value="london">JRFIM London (9:30AM)</option>
          </select>
          <textarea name="message" placeholder="Your message" rows="5" required></textarea>
          <button type="submit">Send Message</button>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer>
    <div class="footer__inner">
      <div class="footer__col">
        <div class="footer__logo">
          <img src="{logo_uri()}" alt="JRFIM" />
          <div class="logo-text">
            <span class="label">Jesus Reigns Forever</span>
            <span class="name">International Ministry Canada</span>
          </div>
        </div>
        <p>A Full Gospel Church &mdash; one family, two locations, united in Christ.</p>
        <ul>
          <li><a href="#locations">Toronto / Peel</a></li>
          <li><a href="#locations">London</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#welcome">Welcome</a></li>
          <li><a href="#locations">Locations</a></li>
          <li><a href="#worship">Worship</a></li>
          <li><a href="#ministries">Ministries</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>JRFIM Toronto / Peel</h4>
        <ul>
          <li>69 Long Branch Avenue, Etobicoke, Toronto, Ontario</li>
          <li>Sunday Worship: 3:00 PM</li>
          <li><a href="https://www.facebook.com/JRFIMpeel">Facebook</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>JRFIM London</h4>
        <ul>
          <li>London, Ontario</li>
          <li>Sunday Worship: 9:30 AM</li>
          <li><a href="https://www.facebook.com/JRFIMLondonON">Facebook</a></li>
          <li><a href="https://www.instagram.com/Jrfimlondon">@Jrfimlondon</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>&copy; 2026 Jesus Reigns Forever International Ministry Canada. All rights reserved.</p>
      <p>Full Gospel Church &middot; One family, two locations</p>
    </div>
  </footer>

  <script>
<script>
    function toggleMenu() {
      document.querySelector('.nav__links').classList.toggle('open');
    }
    // Close menu on link click
    document.querySelectorAll('.nav__links a').forEach(function(a) {
      a.addEventListener('click', function() {
        document.querySelector('.nav__links').classList.remove('open');
      });
    });
  </script>
</script>
</body>
</html>
"""

# Replace placeholders
HTML = HTML.replace('__WorshipBand__', img_uri('worship_band'))

with open('C:/Users/ansel/website/jrfim-church.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"Built jrfim-church.html ({len(HTML):,} bytes)")
