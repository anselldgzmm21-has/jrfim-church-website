from pathlib import Path
import json

with open('C:/Users/ansel/website/images_b64.json') as f:
    imgs = json.load(f)

def img_uri(key):
    return "data:image/jpeg;base64," + imgs[key]

# Brand mark (JRF/IM logo - small, integrated into the header)
with open('C:/Users/ansel/website/logo_b64.json') as f:
    logo_info = json.load(f)
LOGO_URI = "data:image/jpeg;base64," + logo_info['b64']

# ---------- STYLESHEET (Premium, modern - DM Sans font, Tailwind-style, clean corporate) ----------
# Loads the professional DM Sans typeface (used by Elevation Church's website).
CSS = r"""
:root {
  --font-base: "DM Sans", "Inter", "Segoe UI", Roboto, Arial, sans-serif;
  --font-serif: "DM Serif Display", "Georgia", "Times New Roman", serif;
  --color-bg: #FBFBF8;
  --color-bg-alt: #FAFAF6;
  --color-surface: #FFFFFF;
  --color-foreground: #1C1612;
  --color-secondary: #3A2A1C;
  --color-accent: #9A4A14;
  --color-accent2: #B8860B;
  --color-border: #E3D8C4;
  --color-muted: #5C4A3A;
  --color-white: #FFFFFF;
  --color-primary: #1C1612;
  --color-darker: #14100B;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-base);
  background: var(--color-bg);
  color: var(--color-foreground);
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
img { max-width: 100%; display: block; }
:focus-visible { outline: 2px solid var(--accent2); outline-offset: 2px; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }

/* ---- Header / Nav ---- */
.topbar {
  background: var(--color-bg);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 100;
}
.navbar {
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
  max-width: 1260px; margin: 0 auto; padding: 12px 24px;
}
.brand { display: flex; align-items: center; gap: 12px; color: var(--color-primary); text-decoration: none; font-family: var(--font-serif); font-weight: 700; letter-spacing: 0.02em; }
.brand__mark { width: 42px; height: 42px; border-radius: 8px; overflow: hidden; flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
.brand__mark img { width: 100%; height: 100%; object-fit: cover; }
.brand__name { font-size: 1.05rem; line-height: 1.15; }
.nav__links { display: flex; gap: 6px; flex-wrap: wrap; list-style: none; margin: 0; padding: 0; align-items: center; }
.nav__links a {
  color: var(--color-secondary); text-decoration: none; font-size: 0.9rem;
  padding: 6px 10px; border-bottom: 2px solid transparent; transition: 0.2s;
}
.nav__links a:hover { color: var(--accent); border-color: var(--accent); }
.nav__btn {
  background: var(--accent); color: #fff; border: none; border-radius: 999px;
  padding: 10px 18px; font-size: 0.88rem; font-weight: 700; cursor: pointer; white-space: nowrap;
}
.nav__btn:hover { background: var(--accent2); }

/* ---- Hero ---- */
.hero {
  position: relative; overflow: hidden;
  background: linear-gradient(160deg, var(--color-darker) 0%, var(--color-secondary) 55%, var(--color-accent) 100%);
  color: #fff;
  padding: 90px 24px 80px;
  text-align: center;
}
.hero__bg { position: absolute; inset: 0; opacity: 0.18; }
.hero__img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.hero__overlay { position: absolute; inset: 0; background: linear-gradient(160deg, rgba(22,12,6,.15), rgba(40,20,10,.88)); }
.hero__shell { position: relative; z-index: 2; max-width: 1100px; margin: 0 auto; padding: 0 24px; }
.hero__chip {
  display: inline-block; background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.3); color: #FFF4C8;
  font-size: 0.82rem; font-weight: 700; letter-spacing: 1.5px; padding: 7px 14px; border-radius: 999px; margin-bottom: 18px;
}
.hero__title { font-size: clamp(2.3rem, 6vw, 4rem); line-height: 1.14; font-weight: 700; margin: 0 0 14px; letter-spacing: 0.01em; }
.hero__subtitle { font-size: clamp(1.05rem, 2vw, 1.4rem); color: rgba(255,255,255,.92); margin: 0 0 22px; max-width: 760px; margin-left: auto; margin-right: auto; }
.hero__actions { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }

/* ---- Sections ---- */
.sec { padding: 72px 24px; }
.sec-title { font-size: clamp(1.8rem, 3.2vw, 2.5rem); margin: 0 0 12px; font-weight: 700; letter-spacing: 0.01em; }
.sec-sub { color: var(--color-muted); max-width: 700px; margin: 0 auto 34px; line-height: 1.65; }
.eyebrow { display: inline-block; font-size: 0.78rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--accent); margin-bottom: 12px; }

/* ---- Photo sections ---- */
.photo-block { padding: 60px 24px; }
.photo-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 40px; align-items: center; }
.photo-grid__img {
  position: relative; border-radius: var(--radius); overflow: hidden;
  box-shadow: 0 8px 24px rgba(20,12,6,.2); height: 420px; background-size: cover; background-position: center;
}
.photo-grid__img .img__overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(58,31,14,.1), rgba(58,27,14,.6)); }
.photo-grid__img img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }
.photo-grid__body { padding: 30px 0 20px; }
.photo-grid__label { display: inline-block; font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent); padding: 4px 12px; border-radius: 999px; margin-bottom: 10px; }
.photo-grid__title { font-size: 1.5rem; margin: 0 0 8px; }
.photo-grid__desc { color: var(--color-muted); margin: 0; }
.photo-block--lt { background: var(--color-bg); }
.photo-block--gt { background: var(--color-bg-alt); }

/* ---- Intro card ---- */
.intro-card { background: var(--color-surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 32px; max-width: 900px; margin: 0 auto; text-align: center; }
.intro-card .eyebrow { text-align: center; }
.intro-card .sec-sub { max-width: 640px; margin: 0 auto; }

/* ---- About cards grid ---- */
.about-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 20px; }
.about-card { background: var(--color-surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 24px; }
.about-card .icon { font-size: 2rem; margin-bottom: 12px; }
.about-card h3 { font-size: 1.1rem; margin: 0 0 8px; }
.about-card p { color: var(--color-muted); font-size: 0.92rem; margin: 0; }

/* ---- Features / bullets list ---- */
.features { list-style: none; margin: 0; padding: 0; }
.features li { padding: 10px 0; color: var(--color-muted); border-bottom: 1px solid var(--border); }
.features li:last-child { border-bottom: none; }
.features li .check { color: var(--accent); font-weight: 700; margin-right: 8px; }

/* ---- Locations ---- */
.locations { background: var(--color-darker); color: #fff; }
.locations .sec-sub { color: #E8DCC8; }
.locations .sec-title { color: #FFF4C8; }
.locations .grid { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.location { background: var(--color-darker); color: #fff; border: 1px solid var(--border); border-radius: var(--radius); box-shadow: 0 8px 24px rgba(12,8,4,.28); padding: 26px; }
.location .icon { font-size: 2rem; margin-bottom: 12px; }
.location .location__name { font-size: 1.3rem; margin: 0 0 4px; }
.location .location__addr { font-family: var(--font-serif); font-size: 1.05rem; color: #C9A227; margin: 0 0 8px; }
.location .location__city { font-size: .9rem; color: #E8DCC8; margin: 0 0 10px; }
.location .location__time { font-size: 1.45rem; color: #C9A227; margin: 6px 0; }
.location .location__note { color: #D8CFC0; font-size: .9rem; margin: 6px 0 14px; }

/* ---- Contact ---- */
.contact { background: var(--color-bg); }
.contact .grid { grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; }
.contact__info { background: var(--color-surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; box-shadow: var(--shadow); }
.contact__item { display: flex; gap: 14px; align-items: flex-start; margin-bottom: 16px; font-size: .92rem; }
.contact__icon { flex-shrink: 0; width: 40px; height: 40px; background: var(--accent); color: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.contact__label { font-size: .75rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--color-muted); margin: 0; }
.contact__value { color: var(--color-foreground); font-weight: 600; margin: 2px 0 0; }
.contact__form { background: var(--color-surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); }
.contact__form input, .contact__form textarea { background: var(--color-bg); color: var(--color-foreground); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; font-family: var(--font-base); font-size: .92rem; width: 100%; }
.contact__form input:focus, .contact__form textarea:focus { outline: 2px solid var(--accent2); border-color: transparent; }
.contact__note { color: var(--color-muted); font-size: .82rem; margin: 10px 0 0; }

/* ---- Footer ---- */
.footer { background: var(--color-darker); color: #FFF4C8; }
.footer__inner { max-width: 1260px; margin: 0 auto; padding: 44px 24px 32px; }
.footer__grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; }
.footer__col h4 { color: #fff; margin: 0 0 10px; font-size: 1.02rem; }
.footer__col p { color: #FFF4C8; font-size: .86rem; margin: 0; }
.footer__col ul { list-style: none; margin: 0; padding: 0; }
.footer__col li { padding: 5px 0; font-size: .86rem; }
.footer__col li a { color: #FFF4C8; text-decoration: none; }
.footer__col li a:hover { color: #FFD77F; }
.footer__bottom { border-top: 1px solid rgba(255,255,255,.2); margin-top: 32px; padding-top: 20px; text-align: center; font-size: .82rem; color: #FFF4C8; }
.footer__bottom .brand { color: #fff; }

/* ---- CTA section ---- */
.cta-section { text-align: center; }
.cta-section .sec-title { margin-bottom: 14px; }

/* ---- Responsive ---- */
@media (max-width: 860px) {
  .photo-grid { grid-template-columns: 1fr; gap: 20px; }
  .photo-grid__img { height: 320px; }
  .hero__title { font-size: 2.2rem; }
  .locations .grid { grid-template-columns: 1fr; }
  .contact .grid { grid-template-columns: 1fr; }
}

/* Scrollbar (subtle) */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--color-bg); }
::-webkit-scrollbar-thumb { background: var(--color-muted); border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: var(--color-accent); }
"""



HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Jesus Reigns Forever International Ministry Canada — one family, worshiping together in Long Branch &amp; London, Ontario." />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=DM+Serif+Display:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<title>Jesus Reigns Forever International Ministry Canada</title>
<style>
__CSS__
</style>
</head>
<body>

<!-- ===================== Navigation ===================== -->
<header class="topbar">
  <div class="navbar container">
    <a href="#home" class="brand">
      <span class="brand__mark"><img src="__LOGO__" alt="Jesus Reigns Forever logo" /></span>
      <span class="brand__name">Jesus Reigns Forever<br />International Ministry</span>
    </a>
    <nav class="nav__links">
      <a href="#welcome">Welcome</a>
      <a href="#worship">Worship</a>
      <a href="#message">Message</a>
      <a href="#people">Our People</a>
      <a href="#locations">Locations</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="#locations" class="nav__btn">Find a Service</a>
  </div>
</header>

<!-- ===================== Hero ===================== -->
<section class="hero" id="home">
  <div class="hero__img" style="background-image:url('__WorshipBand@')"></div>
  <div class="hero__overlay"></div>
  <div class="container hero__shell">
    <p class="hero__chip">&#127922; &nbsp;One Family &middot; Two Locations &middot; Ontario</p>
    <h1 class="hero__title">Come as you are &mdash; you belong here.</h1>
    <p class="hero__subtitle">Jesus Reigns Forever International Ministry &mdash; a Full Gospel Church in Long Branch &amp; London, Ontario.</p>
    <div class="hero__actions">
      <a href="#locations" class="btn btn--gold">Find your service time</a>
      <a href="#contact" class="btn btn--cream">Get connected</a>
    </div>
  </div>
</section>

<!-- ===================== Welcome / One Family ===================== -->
<section class="sec photo-block photo-block--lt" id="welcome">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="img__overlay"></div>
        <img src="__Family@" alt="Our family at worship" />
      </div>
      <div class="photo-grid__body">
        <p class="eyebrow">Welcome</p>
        <h2 class="sec-title">Come as you are &mdash; you belong here.</h2>
        <p class="sec-sub">Jesus Reigns Forever International Ministry is a Full Gospel Church. We believe in the great commission of winning souls and making disciples. Every Sunday we worship together &mdash; one family, wherever you are from.</p>
        <a href="#locations" class="btn btn--gold">See the times near you</a>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Worship in Progress ===================== -->
<section class="sec photo-block" id="worship">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="img__overlay"></div>
        <img src="__WorshipLeader@" alt="Worship leader" />
      </div>
      <div class="photo-grid__body">
        <p class="eyebrow">Worship</p>
        <h2 class="sec-title">We sing, we feast on His word.</h2>
        <p class="sec-sub">Our worship is led by a team of passionate believers. From the first sermon to the closing song, we gather to honor the King who reigns forever.</p>
        <ul class="features">
          <li><span class="check">&#10003;</span>Weekly services in Long Branch &amp; London</li>
          <li><span class="check">&#10003;</span>Contemporary worship &amp; prayer</li>
          <li><span class="check">&#10003;</span>Community &amp; family ministries</li>
        </ul>
        <a href="#contact" class="btn btn--gold">Join us</a>
      </div>
    </div>
  </div>
</section>

<!-- ===================== The Message ===================== -->
<section class="sec photo-block photo-block--lt" id="message">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__body">
        <p class="eyebrow">The Message</p>
        <h2 class="sec-title">The Word for today.</h2>
        <p class="sec-sub">From the preacher on our platform, we hear the good news of a King who reigns forever. Catch a service, or watch the latest message online.</p>
        <ul class="features">
          <li class="check">Long Branch &mdash; Sunday 3:00 PM</li>
          <li class="check">London &mdash; Sunday 9:30 AM</li>
        </ul>
        <a href="#locations" class="btn btn--gold">Plan your visit</a>
      </div>
      <div class="photo-grid__img">
        <div class="img__overlay"></div>
        <img src="__Preacher@" alt="The preacher" />
      </div>
    </div>
  </div>
</section>

<!-- ===================== Meet the Family ===================== -->
<section class="sec photo-block photo-block--lt" id="people">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="img__overlay"></div>
        <img src="__Congregation@" alt="Our congregation" />
      </div>
      <div class="photo-grid__body">
        <p class="eyebrow">Our People</p>
        <h2 class="sec-title">You are invited into a family.</h2>
        <p class="sec-sub">Here you will find warm welcome, real friendship, and a place to grow in faith &mdash; whether you have been a believer for years or are visiting for the first time.</p>
        <a href="#contact" class="btn btn--gold">Introduce yourself</a>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Locations ===================== -->
<section class="sec locations" id="locations">
  <div class="container">
    <div class="center">
      <p class="eyebrow">Locations</p>
      <h2 class="sec-title">Visit us at either site</h2>
      <p class="sec-sub">One family, two places to belong.</p>
    </div>
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="location">
        <div class="icon">&#127922;</div>
        <h3 class="location__name">Long Branch</h3>
        <p class="location__addr">69 Long Branch Ave</p>
        <p class="location__city">Mississauga, Ontario</p>
        <p class="location__time"><span class="t">Sunday · 3:00 PM</span></p>
        <p class="location__note">A gathering for your family.<br /><a href="tel:+14165626479" style="color:#FFD77F">&#9742; +1 416-562-6479</a></p>
      </div>
      <div class="location">
        <div class="icon">&#127922;</div>
        <h3 class="location__name">London</h3>
        <p class="location__addr">London, Ontario</p>
        <p class="location__city">Ontario</p>
        <p class="location__time"><span class="t">Sunday · 9:30 AM</span></p>
        <p class="location__note">A gathering for your family.<br /><a href="#contact" style="color:#FFD77F">Get in touch</a></p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Contact ===================== -->
<section class="sec contact" id="contact">
  <div class="container">
    <div class="grid">
      <div class="contact__info">
        <p class="eyebrow">Get in touch</p>
        <h2 class="sec-title">We&rsquo;d love to hear from you.</h2>
        <p class="sec-sub">Questions about a service time, giving, or just to say hello &mdash; we&rsquo;d love to hear from you.</p>
        <div class="contact__item">
          <div class="contact__icon">&#128231;</div>
          <div><p class="contact__label">Email</p><p class="contact__value">jrfim@yourchurch.ca</p></div>
        </div>
        <div class="contact__item">
          <div class="contact__icon">&#9742;</div>
          <div><p class="contact__label">Phone</p><p class="contact__value">+1 416-562-6479</p></div>
        </div>
        <div class="contact__item">
          <div class="contact__icon">&#127968;</div>
          <div><p class="contact__label">Visit us</p><p class="contact__value">Long Branch, Mississauga &amp; London, Ontario</p></div>
        </div>
        <p class="sec-sub" style="margin:16px 0 0"><span class="sep" style="color:var(--color-muted)">&#9888;</span> The contact form below is a placeholder &mdash; connect a free form service (Formspree/Netlify) so your messages actually land.</p>
      </div>
      <div class="contact__form">
        <form id="contactForm" style="display:grid;gap:12px">
          <input type="text" name="name" placeholder="Your name" required />
          <input type="email" name="email" placeholder="Your email" required />
          <textarea name="message" placeholder="Your message" rows="5" required></textarea>
          <button type="submit" class="btn btn--gold">Send message</button>
        </form>
        <p class="sec-sub" style="margin:12px 0 0;text-align:center"><span class="sep" style="color:var(--color-muted)">&#9888;</span> Connect a free form backend so your messages actually reach your inbox.</p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Footer ===================== -->
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__grid">
      <div class="footer__col">
        <p class="brand" style="margin:0">JRF</p>
        <p style="margin:0">Jesus Reigns Forever International Ministry Canada</p>
        <p style="margin:0;font-size:.82rem">One family. Two locations. Ontario.</p>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#welcome">Welcome</a></li>
          <li><a href="#worship">Worship</a></li>
          <li><a href="#message">Message</a></li>
          <li><a href="#people">Our People</a></li>
          <li><a href="#locations">Locations</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Visit Us</h4>
        <ul>
          <li><a href="#locations">Long Branch</a></li>
          <li><a href="#locations">London, Ontario</a></li>
          <li><a href="mailto:jrfim@yourchurch.ca">Email</a></li>
          <li><a href="tel:+14165626479">Phone</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4>Connect</h4>
        <ul>
          <li><a href="https://www.facebook.com/jrfimpeel">JRFIM Peel</a></li>
          <li><a href="https://www.facebook.com/JRFIMLondonON">JRFIM London</a></li>
          <li><a href="https://instagram.com/Jrfimlondon">@Jrfimlondon</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p class="brand">JRF</p>
      <p>&copy; <span id="year"></span> All rights reserved. &middot; One family, everywhere.</p>
    </div>
  </div>
</footer>

<script>
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',function(e){
    const t=document.querySelector(this.getAttribute('href'));
    if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});}
  });
});
document.getElementById('contactForm').addEventListener('submit',function(e){
  e.preventDefault();
  const btn=this.querySelector('button[type="submit"]');
  const o=btn.textContent;
  btn.textContent='\u2713 Sent! We\u2019ll be in touch soon.';
  setTimeout(()=>{btn.textContent=o;this.reset();},4000);
});
document.getElementById('year').textContent=new Date().getFullYear();
</script>
</body>
</html>
"""

# Build the final HTML
full = HTML
full = full.replace('__CSS__', CSS)
full = full.replace('__LOGO__', LOGO_URI)
full = full.replace('__WorshipBand@', img_uri('worship_band'))
full = full.replace('__Family@', img_uri('family'))
full = full.replace('__WorshipLeader@', img_uri('worship_leader'))
full = full.replace('__Preacher@', img_uri('preacher'))
full = full.replace('__Congregation@', img_uri('congregation'))

out = Path('C:/Users/ansel/website/jrfim-church.html')
out.write_text(full, encoding='utf-8')
print("wrote", out, len(full), "bytes")
