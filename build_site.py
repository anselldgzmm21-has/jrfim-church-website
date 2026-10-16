from pathlib import Path
import json

with open('C:/Users/ansel/website/images_b64.json') as f:
    imgs = json.load(f)

def img_uri(key):
    return "data:image/jpeg;base64," + imgs[key]

LOGO = img_uri('worship_leader')  # reuse worship leader as brand mark? No - use a small placeholder

# The JRF logo (grunge white-on-black) is used as the brand mark in the header.
# We embed it from the existing brand file via the logo data URI (already in images.json would need a key).
# For the brand mark we use a compact version: we reuse the worship_leader image is a proxy, but to keep
# the identity clean we craft a dedicated small logo; here we use the pre-embedded logo from the previous build:
# Reload logo_b64.json for the original JRF mark.
with open('C:/Users/ansel/website/logo_b64.json') as f:
    logo_info = json.load(f)
LOGO_URI = "data:image/jpeg;base64," + logo_info['b64']

CSS = r"""
:root {
  --paper:#F5EFDF; --paper2:#FBF6E9; --ink:#2A190E; --ink-navy:#160C06;
  --accent:#A8531F; --accent2:#B8860B; --gold:#C9A227;
  --card:#FFFFFF; --border:#E0D4BE; --muted:#6E5A48; --footer:#3A1B0E;
  --shadow:0 1px 2px rgba(58,31,14,.08), 0 6px 18px rgba(58,31,15,.10);
  --radius:18px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,"Times New Roman",serif;color:var(--ink);line-height:1.7;background:var(--paper);-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
h1,h2,h3,.hero__title,.footer__brand,.brand__name{font-family:Georgia,"Times New Roman",serif;font-weight:700}
h1,h2,h3{font-weight:700;letter-spacing:.3px}
img{max-width:100%;display:block}
:focus-visible{outline:2px solid var(--accent2);outline-offset:2px}
.container{max-width:1180px;margin:0 auto;padding:0 26px}
.btn{display:inline-block;border-radius:999px;font-weight:700;font-size:.95rem;padding:14px 28px;cursor:pointer;border:none;transition:.25s}
.btn--gold{background:var(--accent);color:#fff}
.btn--gold:hover{background:var(--accent2)}
.btn--cream{background:#fff;color:var(--ink)}
.btn--cream:hover{background:#fff}
.btn--primary{font-size:.9rem}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent)}
.sec{padding:76px 26px}
.sec-title{font-size:clamp(1.7rem,3.2vw,2.4rem);margin:0 0 10px}
.sec-sub{color:var(--muted);max-width:680px;margin:0 auto 34px}
.hero{padding:80px 26px 90px;position:relative;overflow:hidden;text-align:center;color:#fff}
.hero__img{position:absolute;inset:0;background-size:cover;background-position:center}
.hero__overlay{position:absolute;inset:0;background:linear-gradient(160deg,rgba(22,12,6,.15),rgba(58,27,14,.82));}
.hero__shell{position:relative;z-index:2;text-align:center}
.hero__chip{display:inline-block;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);color:#FFF4C8;font-size:.82rem;font-weight:700;letter-spacing:1.5px;padding:7px 14px;border-radius:999px;margin-bottom:20px}
.hero__title{font-size:clamp(2.3rem,6vw,4rem);line-height:1.12;margin:0 0 16px}
.hero__subtitle{font-size:clamp(1.1rem,2.2vw,1.45rem);color:rgba(255,255,255,.93);margin:0 0 18px}
.hero__tag{font-style:italic;color:#FFF4C8;margin:0 0 26px;font-size:1.05rem}
.btn-group{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.center{text-align:center}
.card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:26px;transition:.25s}
.card:hover{border-color:var(--accent);transform:translateY(-3px)}
.sec{padding:76px 26px}
.sec-title{font-size:clamp(1.7rem,3.2vw,2.4rem);margin:0 0 10px}
.sec-sub{color:var(--muted);max-width:700px;margin:0 auto 34px}
.photo-section{padding:90px 26px}
.photo-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 40px;align-items:center}
.photo-grid__img{position:relative;border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);height:520px;background-size:cover;background-position:center}
.photo-grid__img .overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(58,31,18,.15),rgba(58,27,14,.55))}
.photo-grid__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.photo-grid__body{padding:40px 0 20px}
.photo-grid__label{display:inline-block;background:var(--accent);color:#fff;font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:5px 12px;border-radius:999px;margin-bottom:10px}
.photo-grid__title{font-size:1.5rem;margin:0 0 6px}
.photo-grid__desc{color:var(--muted);margin:0}
.photo-section--lt{background:var(--paper)}
.photo-section--gt{background:var(--paper2)}
.locations{background:var(--ink);color:#fff}
.locations .sec{padding:76px 26px}
.locations .grid{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.location{background:var(--ink);color:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 24px rgba(18,12,6,.25);padding:26px}
.location .icon{font-size:2rem;margin-bottom:12px}
.contact{background:var(--paper)}
.contact .grid{grid-template-columns:1fr 1fr;gap:40px;align-items:start}
.contact__info{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:28px;box-shadow:var(--shadow)}
.contact__item{display:flex;gap:14px;font-size:.92rem;align-items:flex-start;margin-bottom:16px}
.contact__icon{font-size:1.3rem;flex-shrink:0;width:40px;height:40px;background:var(--accent);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center}
.contact__label{font-size:.75rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);margin:0}
.contact__value{color:var(--ink);font-weight:600;margin:2px 0 0}
.contact__form{background:#fff;border:1px solid var(--border);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow)}
.contact__form input,.contact__form textarea{background:#fff;color:var(--ink);border:1px solid var(--border);border-radius:10px;padding:12px 14px;font-family:inherit;font-size:.92rem;width:100%}
.contact__form input:focus,.contact__form textarea:focus{outline:2px solid var(--accent2);border-color:transparent}
.footer{background:var(--footer);color:#FFF4C8}
.footer__inner{max-width:1180px;margin:0 auto;padding:0 26px;padding-top:44px}
.footer__grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px}
.footer__col h4{font-family:Georgia,serif;font-size:1.05rem;margin:0 0 10px}
.footer__col p{font-size:.86rem;color:#FFF4C8}
.footer__col ul{list-style:none;margin:0;padding:0}
.footer__col li{padding:5px 0;font-size:.86rem}
.footer__col li a{color:#FFF4C8}
.footer__col li a:hover{color:#FFD77F}
.footer__bottom{border-top:1px solid rgba(255,255,255,.2);margin-top:32px;padding-top:20px;text-align:center;font-size:.82rem}
.footer__bottom .brand{font-family:Georgia,serif;font-size:1.05rem;color:#FFF4C8;margin:0}
@media (max-width:860px){
  .photo-grid{grid-template-columns:1fr;gap:20px}
  .photo-grid__img{height:360px}
  .locations .grid{grid-template-columns:1fr}
  .contact .grid{grid-template-columns:1fr}
}
"""

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Jesus Reigns Forever International Ministry Canada — one family, worshiping together in Long Branch &amp; London, Ontario." />
<title>Jesus Reigns Forever International Ministry Canada</title>
<style>
__CSS__
</style>
</head>
<body>

<!-- ===================== Navigation ===================== -->
<header class="nav">
  <div class="container nav__inner">
    <a href="#home" class="brand">
      <span class="brand__mark"><img src="__LOGO__" alt="JRF logo" /></span>
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
    <a href="#locations" class="btn btn--gold nav__btn">Find a Service</a>
  </div>
</header>

<!-- ===================== Hero ===================== -->
<section class="hero" id="home">
  <div class="hero__img" style="background-image:url('__WorshipBand@');background-size:cover;background-position:center;"></div>
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
<section class="sec photo-section photo-section--lt" id="welcome">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="overlay"></div>
        <img src="__Family@" alt="Family at worship" />
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
<section class="sec photo-section" id="worship">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="overlay"></div>
        <img src="__WorshipLeader@" alt="Worship leader" />
      </div>
      <div class="photo-grid__body">
        <p class="eyebrow">Worship</p>
        <h2 class="sec-title">We sing, we feast on His word.</h2>
        <p class="sec-sub">Our worship is led by a team of passionate believers. From the first sermon to the closing song, we gather to honor the King who reigns forever.</p>
        <ul class="center" style="list-style:none;margin:0 0 18px;padding:0">
          <li style="padding:6px 0">&#10003; Weekly services in Long Branch &amp; London</li>
          <li style="padding:6px 0">&#10003; Contemporary worship &amp; prayer</li>
          <li style="padding:6px 0">&#10003; Community &amp; family ministries</li>
        </ul>
        <a href="#contact" class="btn btn--gold">Join us</a>
      </div>
    </div>
  </div>
</section>

<!-- ===================== The Message ===================== -->
<section class="sec photo-section photo-section--lt" id="message">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__body">
        <p class="eyebrow">The Message</p>
        <h2 class="sec-title">The Word for today.</h2>
        <p class="sec-sub">From the preacher on our platform, we hear the good news of a King who reigns forever. Catch a service, or watch the latest message online.</p>
        <ul class="center" style="list-style:none;margin:0 0 18px;padding:0">
          <li style="padding:6px 0"><span class="accent">&#127917;</span> Long Branch &mdash; Sunday 3:00 PM</li>
          <li style="padding:6px 0"><span class="accent">&#127917;</span> London &mdash; Sunday 9:30 AM</li>
        </ul>
        <a href="#locations" class="btn btn--gold">Plan your visit</a>
      </div>
      <div class="photo-grid__img">
        <div class="overlay"></div>
        <img src="__Preacher@" alt="The preacher" />
      </div>
    </div>
  </div>
</section>

<!-- ===================== Meet the Family ===================== -->
<section class="sec photo-section photo-section--lt" id="people">
  <div class="container">
    <div class="photo-grid">
      <div class="photo-grid__img">
        <div class="overlay"></div>
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
      <h2 class="sec-title" style="color:#FFF4C8">Visit us at either site</h2>
      <p class="sec-sub" style="color:#E8DCC8">One family, two places to belong.</p>
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
        <p class="eyebrow">Contact</p>
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
        <p class="sec-sub" style="margin:16px 0 0"><span class="sep" style="color:var(--muted)">&#9888;</span> The contact form below is a placeholder &mdash; connect a free form service (Formspree/Netlify) so your messages actually land.</p>
      </div>
      <div class="contact__form">
        <form id="contactForm" style="display:grid;gap:12px">
          <input type="text" name="name" placeholder="Your name" required />
          <input type="email" name="email" placeholder="Your email" required />
          <textarea name="message" placeholder="Your message" rows="5" required></textarea>
          <button type="submit" class="btn btn--gold">Send message</button>
        </form>
        <p class="sec-sub" style="margin:12px 0 0;text-align:center"><span class="sep" style="color:var(--muted)">&#9888;</span> Connect a free form backend so your messages actually reach your inbox.</p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Footer ===================== -->
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__grid">
      <div class="footer__col">
        <p class="brand" style="color:#FFF4C8;margin:0">JRF</p>
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

# Replace placeholders
CSS_final = CSS.replace('__CSS__', CSS).replace('__LOGO__', LOGO_URI)
# Note: we need image replacements; build final HTML below
html = HTML.replace('__CSS__', CSS).replace('__LOGO__', LOGO_URI)
# Replace image placeholders after the template is fully assembled
html = html.replace('__WorshipBand@', img_uri('worship_band'))
html = html.replace('__Family@', img_uri('family'))
html = html.replace('__WorshipLeader@', img_uri('worship_leader'))
html = html.replace('__Preacher@', img_uri('preacher'))
html = html.replace('__Congregation@', img_uri('congregation'))

out = Path('C:/Users/ansel/website/jrfim-church.html')
out.write_text(html, encoding='utf-8')
print("wrote", out, len(html), "bytes")
print("image count in file:", html.count('src="data:image/jpeg;base64,'))
