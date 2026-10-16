from pathlib import Path
import json

with open('C:/Users/ansel/website/logo_b64.json') as f:
    info = json.load(f)
LOGO = info['b64']
LOGO_URI = f"data:image/jpeg;base64,{LOGO}"

BRAND = "Jesus Reigns Forever International Ministry Canada"
WELCOME = ("Jesus Reigns Forever International Ministry (JRFIM) is a Full Gospel Church. "
           "We believe in the great commission of winning souls and making disciples. "
           "Every Sunday we worship together in Long Branch &amp; London, Ontario.")
PHONE = "+1 416-562-6479"

# ---- Premium heritage palette (cream paper + black + warm brown accents) ----
CSS = r"""
:root {
  --paper:#F5EFDF;        /* warm ivory */
  --paper2:#FBF6E9;
  --ink:#2A190E;          /* deep warm brown-black */
  --ink-navy:#160C06;      /* near-black hero */
  --accent:#A8531F;        /* burnt amber */
  --accent2:#B8860B;       /* dark goldenrod */
  --gold:#C9A227;
  --card:#FFFFFF;
  --border:#E0D4BE;
  --muted:#6E5A48;
  --footer:#3A1B0E;
  --shadow:0 1px 2px rgba(58,31,14,.08), 0 6px 18px rgba(58,31,14,.10);
  --radius:18px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,"Times New Roman",serif;color:var(--ink);line-height:1.7;background:var(--paper);-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
h1,h2,h3,.hero__title,.brand__name,.footer__brand{font-family:Georgia,"Times New Roman",serif}
h1,h2,h3{font-weight:700;letter-spacing:.3px}
img{max-width:100%;display:block}
:focus-visible{outline:2px solid var(--accent2);outline-offset:2px}
.container{max-width:1180px;margin:0 auto;padding:0 26px}
.btn{display:inline-block;border-radius:999px;font-weight:700;font-size:.95rem;padding:14px 28px;cursor:pointer;border:none;transition:.25s}
.btn--gold{background:var(--accent);color:#fff}
.btn--gold:hover{background:var(--accent2)}
.btn--cream{background:#fff;color:var(--ink)}
.btn--cream:hover{background:#fff;border-color:var(--accent)}
.btn--sm{padding:10px 20px;font-size:.88rem}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent)}
.sec{padding:74px 26px}
.sec-title{font-size:clamp(1.7rem,3.2vw,2.4rem);margin:0 0 12px}
.sec-sub{color:var(--muted);max-width:680px;margin:0 auto 34px}
.eyebrow-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:10px}
.eyebrow-row .sep{color:var(--muted);font-size:.85rem}
.eyebrow-row .sep::before{content:"\00B7";color:var(--accent)}
.hero{padding:110px 26px 90px;position:relative;overflow:hidden;text-align:center;color:#fff}
.hero__bg{position:absolute;inset:0;
  background:
    radial-gradient(130% 100% at 88% 6%,rgba(181,81,42,.30),transparent 60%),
    radial-gradient(130% 100% at 4% 94%,rgba(120,65,30,.32),transparent 60%),
    linear-gradient(160deg,#160C06 0%,#2A190E 55%,#3A1B0E 100%);}
.hero__shell{position:relative;z-index:2}
.hero__chip{display:inline-block;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);color:#FFF6D8;font-size:.82rem;font-weight:700;letter-spacing:1.5px;padding:7px 14px;border-radius:999px;margin-bottom:22px}
.hero__title{font-size:clamp(2.4rem,6vw,4rem);line-height:1.12;margin:0 0 16px}
.hero__subtitle{font-size:clamp(1.15rem,2.2vw,1.45rem);color:rgba(255,255,255,.92);margin:0 0 30px}
.hero__actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.hero__logo{margin:0 auto;width:170px;opacity:.9;}
.hero__tag{font-style:italic;color:#FFF4C8;margin-top:18px;font-size:1.05rem}
.sec{padding:74px 26px}
.center{text-align:center}
.card{background:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:26px}
.sec.card{padding:56px 26px}
.eyebrow-line{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-bottom:6px}
.eyebrow-line .sep{color:var(--muted);font-size:.85rem}
.eyebrow-line .sep::before{content:"\00B7";color:var(--accent)}
.services .grid{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.experience{background:var(--paper);border-radius:var(--radius);padding:30px;border:1px solid var(--border);box-shadow:var(--shadow)}
.experience .icon{font-size:2.1rem;height:54px;display:flex;align-items:center;justify-content:center;background:var(--ink);color:#fff;border-radius:50%;width:54px;margin-bottom:14px}
.experience h3{font-size:1.15rem;margin:0 0 6px}
.experience p{color:var(--muted);margin:0 0 14px}
.experience .link{font-weight:700;color:var(--ink)}
.ministries .grid{grid-template-columns:repeat(auto-fit,minmax(165px,1fr))}
.ministry{text-align:center;padding:24px;border:1px solid var(--border);border-radius:var(--radius);transition:.25s}
.ministry:hover{border-color:var(--accent);transform:translateY(-3px)}
.ministry .icon{font-size:1.9rem;height:50px;display:flex;align-items:center;justify-content:center;background:var(--accent);color:#fff;border-radius:50%;width:50px;margin-bottom:12px}
.ministry h3{font-size:1rem;margin:0 0 6px}
.ministry p{color:var(--muted);font-size:.86rem;margin:0}
.locations .grid{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.location{background:var(--ink);color:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:0 8px 24px rgba(18,12,6,.25);padding:28px}
.location .icon{font-size:2rem;margin-bottom:12px}
.location__name{font-size:1.3rem;margin:0 0 4px}
.location__addr{font-family:Georgia,serif;font-size:1.05rem;color:#C9A227;margin:0 0 8px}
.location__city{font-size:.9rem;color:#E8DCC8;margin:0 0 10px}
.location__time{font-size:1.45rem;color:#C9A227;font-family:Georgia,serif;margin:6px 0}
.location__note{color:#D8CFC0;font-size:.9rem;margin:0 0 14px}
.contact{background:var(--paper)}
.contact .grid{grid-template-columns:1fr 1fr;gap:36px;align-items:start}
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
.nav{background:var(--ink);position:sticky;top:0;z-index:50;border-bottom:3px solid var(--accent)}
.nav__inner{max-width:1180px;margin:0 auto;padding:16px 26px;display:flex;justify-content:space-between;align-items:center;gap:16px}
.brand{display:flex;align-items:center;gap:12px;color:#FFF4C8}
.brand__mark{width:42px;height:42px;border-radius:10px;overflow:hidden;flex-shrink:0}
.brand__mark img{width:100%;height:100%;object-fit:cover}
.brand__name{display:block;font-size:.95rem}
.nav__links{display:flex;gap:4px;flex-wrap:wrap}
.nav__links a{color:#FFF4C8;font-size:.92rem;padding:6px 4px;border-bottom:2px solid transparent;transition:.2s}
.nav__links a:hover{color:#FFD77F;border-color:var(--accent2)}
.nav__btn{background:var(--accent);color:#FFF4C8;padding:10px 18px;border-radius:999px;font-size:.9rem;font-weight:700;white-space:nowrap}
.nav__btn:hover{background:var(--accent2)}
.mob-nav{display:none}
@media (max-width:860px){
  .hero{padding:70px 20px 60px}
  .hero__logo{width:120px}
  .services .grid{grid-template-columns:1fr}
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
      <a href="#story">Our Story</a>
      <a href="#experience">Services</a>
      <a href="#ministry">Ministry</a>
      <a href="#getinvolved">Get Involved</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="#locations" class="btn btn--gold nav__btn">Find a Service</a>
  </div>
</header>

<!-- ===================== Hero ===================== -->
<section class="hero" id="home">
  <div class="container hero__shell">
    <img class="hero__logo" src="__LOGO__" alt="Jesus Reigns Forever International Ministry logo" />
    <p class="hero__subtitle" style="font-style:italic;color:#FFF4C8;font-size:1.1rem">Full Gospel Church &middot; Mississauga &amp; London</p>
    <h1 class="hero__title">Come as you are — you belong here.</h1>
    <p class="hero__tag">One family. Two locations. Ontario.</p>
    <div class="hero__actions">
      <a href="#experience" class="btn btn--gold">Find your service time</a>
      <a href="#contact" class="btn btn--cream">Get connected</a>
    </div>
  </div>
</section>

<!-- ===================== What We Believe ===================== -->
<section class="sec center">
  <div class="container">
    <div class="card" style="padding:30px">
      <p class="eyebrow" style="text-align:center">Our Story</p>
      <h2 class="sec-title" style="text-align:center;margin:0 0 14px">One family. One gospel. Many places.</h2>
      <p class="sec-sub" style="text-align:center;margin:0">
        <span class="highlight" style="color:var(--accent)">Jesus Reigns Forever International Ministry (JRFIM)</span> is a Full Gospel Church.
        We believe in the great commission of winning souls and making disciples.
      </p>
    </div>
  </div>
</section>

<!-- ===================== Experience ===================== -->
<section class="sec" id="experience" style="background:var(--paper)">
  <div class="container">
    <div class="center">
      <p class="eyebrow">Find Your Experience</p>
      <h2 class="sec-title">Find the right experience for you</h2>
      <p class="sec-sub">No matter where you are, online or in person, become a part of all God is doing.</p>
    </div>
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="experience">
        <div class="icon">&#127922;</div>
        <h3>Physical Campus</h3>
        <p>Worship with us in person &mdash; a place built for family.</p>
        <a href="#locations" class="link">Long Branch &amp; London &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128253;</div>
        <h3>Live Streams</h3>
        <p>eFam streams church from wherever you are.</p>
        <a href="#experience" class="link">Find a time &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128248;</div>
        <h3>Watch Party</h3>
        <p>Groups that stream the worship experience together.</p>
        <a href="#experience" class="link">Find a watch party &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128254;</div>
        <h3>Pop-Up</h3>
        <p>We bring church to different places across the area.</p>
        <a href="#experience" class="link">Find a pop-up &nbsp;&#8594;</a>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Ministries ===================== -->
<section class="sec" style="background:var(--paper2)">
  <div class="container">
    <div class="center">
      <p class="eyebrow">Ministries</p>
      <h2 class="sec-title">Ministries that shape us</h2>
      <p class="sec-sub">From worship to the next generation, every part of the family has a place here.</p>
    </div>
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="ministry">
        <div class="icon">&#127937;</div>
        <h3>Worship</h3>
        <p>An atmosphere of worship to God.</p>
      </div>
      <div class="ministry">
        <div class="icon">&#128101;</div>
        <h3>Community &amp; Family</h3>
        <p>Small groups that activate faith.</p>
      </div>
      <div class="ministry">
        <div class="icon">&#128680;</div>
        <h3>NextGen</h3>
        <p>Building generational faith in children &amp; students.</p>
      </div>
      <div class="ministry">
        <div class="icon">&#128640;</div>
        <h3>Outreach</h3>
        <p>Making an impact locally and globally.</p>
      </div>
      <div class="ministry">
        <div class="icon">&#128181;</div>
        <h3>Prayer &amp; Care</h3>
        <p>Supporting one another through life&rsquo;s seasons.</p>
      </div>
      <div class="ministry">
        <div class="icon">&#128222;</div>
        <h3>Give</h3>
        <p>Offering generosity to the King.</p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Locations ===================== -->
<section class="sec" id="locations" style="background:var(--ink)">
  <div class="container">
    <div class="center">
      <p class="eyebrow" style="color:#C9A227">Locations</p>
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
        <p class="location__note">Our gathering for your family.<br /><a href="tel:+14165626479" style="color:#FFD77F">&#9742; +1 416-562-6479</a></p>
      </div>
      <div class="location">
        <div class="icon">&#127922;</div>
        <h3 class="location__name">London</h3>
        <p class="location__addr">London, Ontario</p>
        <p class="location__city">Ontario</p>
        <p class="location__time"><span class="t">Sunday · 9:30 AM</span></p>
        <p class="location__note">Our gathering for your family.<br /><a href="#contact" style="color:#FFD77F">Get in touch</a></p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Contact ===================== -->
<section class="sec contact" id="contact" style="background:var(--paper)">
  <div class="container">
    <div class="grid">
      <div class="contact__info">
        <p class="eyebrow">Get in touch</p>
        <h2 class="sec-title" style="margin:0 0 14px">We&rsquo;d love to hear from you.</h2>
        <p class="sec-sub" style="margin:0 0 20px">Questions about service times, giving, or just to say hello &mdash; we&rsquo;ll reply as soon as we can.</p>
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
        <p class="sec-sub" style="margin:12px 0 0;text-align:center"><span class="sep" style="color:var(--muted)">&#9888;</span> Register a free form backend (e.g. Formspree) so your messages actually reach your inbox.</p>
      </div>
    </div>
  </div>
</section>

<!-- ===================== Footer ===================== -->
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__grid">
      <div class="footer__col">
        <p class="brand">JRF</p>
        <p style="margin:0">Jesus Reigns Forever International Ministry Canada</p>
        <p style="margin:0;font-size:.82rem">One family. Two locations. Ontario.</p>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#experience">Services</a></li>
          <li><a href="#ministry">Ministry</a></li>
          <li><a href="#contact">Contact</a></li>
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
        <h4>Give</h4>
        <ul>
          <li><a href="#contact">Online giving</a></li>
          <li><a href="#contact">By envelope</a></li>
          <li><a href="#contact">At service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p class="brand">JRF</p>
      <p>&copy; <span id="year"></span> All rights reserved. &middot; One family, everywhere.</p>
      <p style="margin-top:6px;color:#FFD77F">Connect: <a href="https://www.facebook.com/jrfimpeel" style="color:#FFD77F">jrfimpeel</a> &middot; <a href="https://www.facebook.com/JRFIMLondonON" style="color:#FFD77F">JRFIM London</a> &middot; <a href="https://instagram.com/Jrfimlondon" style="color:#FFD77F">@Jrfimlondon</a></p>
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
  btn.textContent='&#10003; Sent! We&rsquo;ll be in touch soon.';
  setTimeout(()=>{btn.textContent=o;this.reset();},4000);
});
document.getElementById('year').textContent=new Date().getFullYear();
</script>
</body>
</html>
"""

out = Path('C:/Users/ansel/website/jrfim-church.html')
full = HTML.replace('__CSS__', CSS).replace('__LOGO__', LOGO_URI)
out.write_text(full, encoding='utf-8')
print("wrote", out, len(full), "bytes")
