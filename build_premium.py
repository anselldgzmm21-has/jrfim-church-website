from pathlib import Path
import json

# ---- Read the embedded logo ----
with open('C:/Users/ansel/website/logo_b64.json') as f:
    info = json.load(f)
LOGO = info['b64']
LOGO_URI = f"data:image/jpeg;base64,{LOGO}"

# ---- Brand + content (from Facebook Peel Region page, London from you) ----
BRAND = "Jesus Reigns Forever International Ministry Canada"
SECTION = "Jesus Reigns Forever International Ministry"
WELCOME = ("Jesus Reigns Forever International Ministry (JRFIM) is a Full Gospel Church. "
           "We believe in the great commission of winning souls and making disciples. "
           "Every Sunday we worship together in Long Branch & London, Ontario.")
LONG_BRANCH_ADDR = "69 Long Branch Ave, Mississauga, ON, Canada"
LONG_BRANCH_TIME = "Sunday &bull; 3:00 PM"
LONDON_TIME = "Sunday &bull; 9:30 AM"
PHONE = "+1 416-562-6479"

CSS = """
:root {
  --coffee:#3a1f0e; --dark:#5c3a22; --accent:#c8621b; --orange:#d98a3d;
  --gold:#e8b44a; --rust:#b5512a; --cream:#faf3e2; --cream2:#f3e6d2;
  --card:#ffffff; --border:#e6d5b8; --muted:#8a6b4a;
  --shadow:0 1px 3px rgba(60,35,15,.12),0 6px 18px rgba(60,35,15,.08);
  --radius:16px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--coffee);line-height:1.7;background:var(--cream);-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none}
h1,h2,h3,.hero__title,.brand__name{font-family:Georgia,"Times New Roman",serif;font-weight:700;color:var(--coffee)}
img{max-width:100%;display:block}
:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.container{max-width:1200px;margin:0 auto;padding:0 26px}
.btn{display:inline-block;border-radius:999px;font-weight:700;font-size:.95rem;padding:14px 26px;cursor:pointer;border:none;transition:.2s}
.btn--primary{background:var(--accent);color:#fff}
.btn--primary:hover{background:var(--orange)}
.btn--ghost{background:transparent;color:var(--coffee);border:2px solid var(--border)}
.btn--ghost:hover{border-color:var(--accent);background:rgba(200,98,27,.06)}
.eyebrow{font-size:.78rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--accent)}
.hero{padding:80px 26px 64px;position:relative;overflow:hidden;text-align:center;color:#fff}
.hero__bg{position:absolute;inset:0;
  background:
    radial-gradient(130% 90% at 88% 6%,rgba(217,138,61,.32),transparent 60%),
    radial-gradient(130% 90% at 4% 94%,rgba(181,81,42,.34),transparent 60%),
    linear-gradient(160deg,#3a1f0e 0%,#5c3a22 45%,#8a4f22 100%);
  filter:saturate(.9)}
.hero__shell{position:relative;z-index:2}
.hero__chip{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.35);color:var(--gold);font-size:.85rem;font-weight:700;letter-spacing:1px;padding:8px 16px;border-radius:999px;margin-bottom:20px}
.hero__title{font-size:clamp(2.3rem,6vw,4rem);line-height:1.12;margin:0 0 18px}
.hero__subtitle{font-size:clamp(1.1rem,2.2vw,1.45rem);color:rgba(255,255,255,.93);margin:0 0 28px}
.hero__actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.sec{padding:76px 26px}
.sec-title{font-family:Georgia,serif;font-size:clamp(1.7rem,3.2vw,2.4rem);margin:0 0 10px}
.sec-sub{color:var(--muted);max-width:700px;margin:0 auto 36px}
.eyebrow-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:8px}
.eyebrow-row .sep{color:var(--muted);font-size:.85rem}
.eyebrow-row .sep::before{content:"\\00B7";color:var(--gold)}
.grid{display:grid;gap:20px}
.feat{display:grid;grid-template-columns:1.15fr .85fr;gap:32px;align-items:center}
.feat__img{height:320px;border-radius:var(--radius);margin-bottom:6px;position:relative;overflow:hidden}
.feat__img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.feat__img .overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(58,31,14,.05),rgba(58,31,14,.45))}
.feat__body{position:relative}
.feat__label{display:inline-block;background:var(--coffee);color:#fff;font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:5px 12px;border-radius:999px;margin-bottom:10px}
.feat__title{font-size:1.5rem;margin:0 0 8px}
.feat__desc{color:var(--muted);margin:0}
.experiences .grid{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.experience{text-align:center;padding:22px}
.experience .icon{font-size:2.2rem;height:56px;display:flex;align-items:center;justify-content:center;background:var(--coffee);color:#fff;border-radius:50%;width:56px;margin-bottom:14px}
.experience h3{font-size:1.15rem;margin:0 0 6px}
.experience p{color:var(--muted);font-size:.92rem;margin:0 0 14px}
.experience .link{font-weight:700;color:var(--coffee)}
.ministries .grid{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.ministry{text-align:center;padding:22px;border:1px solid var(--border);border-radius:var(--radius);background:#fff}
.ministry .icon{font-size:2rem;height:52px;display:flex;align-items:center;justify-content:center;background:var(--gold);color:var(--coffee);border-radius:50%;width:52px;margin-bottom:12px}
.ministry h3{font-size:1rem;margin:0 0 6px}
.ministry p{color:var(--muted);font-size:.86rem;margin:0}
.getinvolved .grid{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.getinvolved .card{padding:26px;border-top:4px solid var(--gold)}
.getinvolved h3{font-size:1.2rem;margin:0 0 8px}
.getinvolved p{color:var(--muted);margin:0 0 14px}
.getinvolved .link{font-weight:700;color:var(--coffee)}
.locations-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.location-card{background:var(--dark);color:#fff;border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:24px}
.location-card .icon{font-size:2rem;margin-bottom:10px}
.location-card__name{font-size:1.3rem;margin:0 0 4px}
.location-card__addr{font-family:Georgia,serif;font-size:1.05rem;color:var(--gold);margin:0 0 8px}
.location-card__city{font-size:.9rem;color:rgba(255,255,255,.75);margin:0 0 10px}
.location-card__time{font-size:1.5rem;color:var(--gold);font-family:Georgia,serif;margin:4px 0}
.location-card__time .t::before{content:"\\1F552  "}
.location-card__note{color:rgba(255,255,255,.75);font-size:.9rem;margin:0 0 14px}
.footer{background:var(--coffee);color:rgba(255,255,255,.85)}
.footer__inner{max-width:1200px;margin:0 auto;padding:0 26px;padding-top:48px}
.footer__grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px}
.footer__col h4{font-family:Georgia,serif;font-size:1.05rem;color:#fff;margin:0 0 10px}
.footer__col p{font-size:.86rem;color:rgba(255,255,255,.8)}
.footer__col ul{list-style:none;margin:0;padding:0}
.footer__col li{padding:5px 0;font-size:.86rem}
.footer__col li a{color:rgba(255,255,255,.85)}
.footer__col li a:hover{color:#fff}
.footer__bottom{border-top:1px solid rgba(255,255,255,.2);margin-top:32px;padding-top:20px;text-align:center;font-size:.82rem}
.footer__bottom .brand{font-family:Georgia,serif;font-size:1.05rem;color:#fff;margin:0 0 6px}
.mob-nav{display:none}
@media (max-width:860px){
  .experiences .grid{grid-template-columns:repeat(2,1fr)}
  .feat{grid-template-columns:1fr}
  .feat__img{height:220px}
  .sec{padding:56px 26px}
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

<!-- Navigation -->
<header>
  <div class="container nav">
    <a href="#home" class="brand">
      <span class="brand__mark"><img src="__LOGO__" alt="JRF logo" /></span>
      <span class="brand__name">Jesus Reigns Forever<br />International Ministry</span>
    </a>
    <nav class="nav__links" id="navLinks">
      <a href="#story">Our Story</a>
      <a href="#experience">Services</a>
      <a href="#ministry">Ministry</a>
      <a href="#getinvolved">Get Involved</a>
      <a href="#contact">Contact</a>
    </nav>
    <a href="#locations" class="btn btn--primary mob-nav">Find a Service</a>
  </div>
</header>

<!-- Hero -->
<section class="hero" id="home">
  <div class="hero__bg"></div>
  <div class="container hero__shell">
    <p class="hero__chip">&#127922; &nbsp;One Family &middot; Two Locations &middot; Ontario</p>
    <h1 class="hero__title">Come as you are &mdash; you belong here.</h1>
    <p class="hero__subtitle">
      <span class="brand__name" style="color:#fff">Jesus Reigns Forever International Ministry</span><br />
      We worship together in <span style="color:#fff">Long Branch</span> &amp; <span style="color:#fff">London, Ontario</span>.
    </p>
    <div class="hero__actions">
      <a href="#experience" class="btn btn--primary">Find your service time</a>
      <a href="#contact" class="btn btn--ghost">Get connected</a>
    </div>
  </div>
</section>

<!-- What We Believe -->
<section class="sec" id="story">
  <div class="container">
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="card" style="padding:26px">
        <p class="eyebrow">Our Story</p>
        <h2 class="sec-title" style="margin:0 0 12px">One family. One gospel. Many places.</h2>
        <p style="color:var(--dark);margin:0">
          <span class="highlight" style="color:var(--accent)">Jesus Reigns Forever International Ministry (JRFIM)</span> is a Full Gospel Church.
          We believe in the great commission of winning souls and making disciples.
          Every Sunday we worship together &mdash; and we&rsquo;d love to worship with you.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- Experience -->
<section class="sec experiences" id="experience">
  <div class="container">
    <div class="sec__inner" style="text-align:center">
      <p class="eyebrow">Find Your Experience</p>
      <h2 class="sec-title">Find the right experience for you</h2>
      <p class="sec-sub">No matter where you are, online or in person, become a part of all God is doing.</p>
    </div>
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="experience">
        <div class="icon">&#127922;</div>
        <h3>Physical Campus</h3>
        <p>Worship with us in person at one of our locations &mdash; a place built for family.</p>
        <a href="#locations" class="link">Long Branch &amp; London &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128253;</div>
        <h3>Live Streams</h3>
        <p>eFam is our online community who stream church from wherever they are.</p>
        <a href="#experience" class="link">Find a time &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128248;</div>
        <h3>Watch Party</h3>
        <p>Watch Parties are groups that stream the worship experience together.</p>
        <a href="#experience" class="link">Find a watch party &nbsp;&#8594;</a>
      </div>
      <div class="experience">
        <div class="icon">&#128254;</div>
        <h3>Pop-Up</h3>
        <p>A Pop-Up is where we bring church to different places across the area.</p>
        <a href="#experience" class="link">Find a pop-up &nbsp;&#8594;</a>
      </div>
    </div>
  </div>
</section>

<!-- Story / Latest Sermon -->
<section class="sec" id="story">
  <div class="container">
    <div class="feat">
      <div class="feat__img">
        <div class="overlay"></div>
        <div class="inner"></div>
        <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='1000' height='420' viewBox='0 0 1000 420'%3E%3Crect fill='%23d98a3d' width='1000' height='420'/%3E%3Crect fill='%23b5512a' width='1000' height='420' opacity='.35'/%3E%3Ctext x='50' y='220' font-family='sans-serif' font-size='24' fill='%23fff' opacity='.9'>Your family photo here%3C/text%3E%3C/svg%3E" alt="Featured message"/>
      </div>
      <div class="feat__body">
        <p class="eyebrow">Story</p>
        <h2 class="sec-title">Lasting words for today</h2>
        <p class="sec-sub" style="max-width:600px">A message to carry with you this week.</p>
        <div class="card" style="padding:22px">
          <p class="feat__label">Latest message</p>
          <h3 style="font-size:1.25rem;margin:0 0 8px">He Hasn&rsquo;t Forgotten You</h3>
          <p class="feat__desc" style="margin:0 0 16px">A message on hope, perseverance, and the love that stays steady no matter what.</p>
          <a href="#contact" class="btn btn--ghost" style="border-color:var(--accent);color:var(--accent)">Watch message &nbsp;&#8594;</a>
        </div>
        <p class="sec-sub" style="max-width:560px"><em><em>Note:</em>&nbsp; Add your own sermon title, speaker photo, and message link here.</em></p>
      </div>
    </div>
  </div>
</section>

<!-- Ministry -->
<section class="sec" id="ministry" style="background:var(--cream2)">
  <div class="container">
    <div class="sec__inner" style="text-align:center">
      <p class="eyebrow">Ministries</p>
      <h2 class="sec-title">Ministries that shape us</h2>
      <p class="sec-sub">From worship to next generation, every part of the family has a place here.</p>
    </div>
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="ministry">
        <div class="icon">&#127937;</div>
        <h3>Worship</h3>
        <p>Inspiring your faith and creating an atmosphere of worship to God.</p>
        <a href="#getinvolved" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="ministry">
        <div class="icon">&#128101;</div>
        <h3>Community &amp; Family</h3>
        <p>Connecting people and activating faith in small groups.</p>
        <a href="#getinvolved" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="ministry">
        <div class="icon">&#128680;</div>
        <h3>NextGen</h3>
        <p>Partnering with parents to build generational faith in children &amp; students.</p>
        <a href="#getinvolved" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="ministry">
        <div class="icon">&#128640;</div>
        <h3>Outreach</h3>
        <p>Making an impact locally and globally through service.</p>
        <a href="#getinvolved" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="ministry">
        <div class="icon">&#128181;</div>
        <h3>Prayer &amp; Care</h3>
        <p>Supporting one another through faith and life&rsquo;s seasons.</p>
        <a href="#contact" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="ministry">
        <div class="icon">&#128222;</div>
        <h3>Give</h3>
        <p>Gentleness and generosity as an offering to the King.</p>
        <a href="#contact" class="link">Learn more &nbsp;&#8594;</a>
      </div>
    </div>
  </div>
</section>

<!-- Get Involved -->
<section class="sec getinvolved" id="getinvolved">
  <div class="container">
    <div class="grid" style="max-width:1180px;margin:0 auto">
      <div class="card" style="padding:26px">
        <div class="icon" style="background:var(--orange);margin-bottom:14px;height:58px;width:58px">&#128181;</div>
        <h3>Volunteer</h3>
        <p style="margin:0 0 14px">Participate in the mission to advance the gospel by serving on a volunteer team.</p>
        <a href="#contact" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="card" style="padding:26px">
        <div class="icon" style="background:var(--rust);margin-bottom:14px;height:58px;width:58px">&#128305;</div>
        <h3>Lead</h3>
        <p style="margin:0 0 14px">Lead an eGroup, host a Watch Party, or become a student leader.</p>
        <a href="#contact" class="link">Learn more &nbsp;&#8594;</a>
      </div>
      <div class="card" style="padding:26px">
        <div class="icon" style="background:var(--gold);margin-bottom:14px;height:58px;width:58px">&#128176;</div>
        <h3>Give</h3>
        <p style="margin:0 0 14px">Give generously &mdash; online, by envelope, or through giving at service.</p>
        <a href="#contact" class="link">Learn more &nbsp;&#8594;</a>
      </div>
    </div>
  </div>
</section>

<!-- Locations -->
<section class="sec" id="locations">
  <div class="container">
    <div class="sec__inner" style="text-align:center">
      <p class="eyebrow">Locations</p>
      <h2 class="sec-title">Visit us at either site</h2>
      <p class="sec-sub">One family, two places to belong.</p>
    </div>
    <div class="locations-grid" style="max-width:1180px;margin:0 auto">
      <div class="location-card">
        <div class="icon">&#127922;</div>
        <h3 class="location-card__name">Long Branch</h3>
        <p class="location-card__addr">69 Long Branch Ave</p>
        <p class="location-card__city">Mississauga, Ontario</p>
        <p class="location-card__time"><span class="t">3:00 PM</span></p>
        <p class="location-card__note">Sunday service &mdash; our gathering for your family.</p>
        <a href="tel:+14165626479" class="btn btn--ghost btn--sm">Call us</a>
      </div>
      <div class="location-card">
        <div class="icon">&#127922;</div>
        <h3 class="location-card__name">London</h3>
        <p class="location-card__addr">London, Ontario</p>
        <p class="location-card__city">Ontario</p>
        <p class="location-card__time"><span class="t">9:30 AM</span></p>
        <p class="location-card__note">Sunday service &mdash; our gathering for your family.</p>
        <a href="#contact" class="btn btn--ghost btn--sm">Contact us</a>
      </div>
    </div>
    <p class="sec-sub" style="margin-top:24px"><span class="sep">&#9888;</span> <em>Addresses and phone numbers shown are from your Facebook page (JRFIM Peel Region).</em></p>
  </div>
</section>

<!-- Contact -->
<section class="sec" id="contact">
  <div class="container">
    <div class="feat" style="text-align:center">
      <div class="feat__body">
        <p class="eyebrow">Contact</p>
        <h2 class="sec-title">Get in touch</h2>
        <p class="sec-sub" style="margin:0 0 12px">Questions about a service time, giving, or just want to say hello? We&rsquo;d love to hear from you.</p>
        <div class="card" style="padding:22px;text-align:left">
          <div style="display:flex;gap:14px;font-size:.92rem;align-items:flex-start;margin-bottom:10px">
            <span style="font-size:1.2rem;flex-shrink:0;background:var(--coffee);color:#fff;border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center">&#128231;</span>
            <div><strong style="color:var(--coffee)">Long Branch</strong><br /><a href="tel:+14165626479" style="color:var(--accent)">+1 416-562-6479</a></div>
          </div>
          <div style="display:flex;gap:14px;font-size:.92rem;align-items:flex-start;margin-bottom:10px">
            <span style="font-size:1.2rem;flex-shrink:0;background:var(--coffee);color:#fff;border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center">&#127968;</span>
            <div><strong style="color:var(--coffee)">Long Branch address</strong><br />69 Long Branch Ave, Mississauga, ON</div>
          </div>
          <div style="display:flex;gap:14px;font-size:.92rem;align-items:flex-start">
            <span style="font-size:1.2rem;flex-shrink:0;background:var(--coffee);color:#fff;border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center">&#127968;</span>
            <div><strong style="color:var(--coffee)">London</strong><br />London, Ontario &nbsp;·&nbsp; Sunday 9:30 AM</div>
          </div>
        </div>
        <p class="sec-sub" style="margin:16px 0 0"><span style="color:var(--rust)">&#9888;</span> The contact form below is a placeholder &mdash; connect a free form service (Formspree/Netlify) so your messages actually land.</p>
      </div>
      <div class="feat__img" style="height:320px;border-radius:var(--radius)">
        <div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(58,31,14,.85),rgba(181,81,42,.7))"></div>
        <div style="position:relative;z-index:2;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:left;color:#fff">
          <p style="font-size:.85rem;letter-spacing:2px;text-transform:uppercase;opacity:.8">Send us a message</p>
          <form class="contact-form" style="display:grid;gap:12px;max-width:460px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);border-radius:12px;padding:18px">
            <input type="text" name="name" placeholder="Your name" style="background:#fff;color:#fff;border:1px solid rgba(255,255,255,.4);border-radius:8px;padding:10px 14px;font:inherit" />
            <input type="email" name="email" placeholder="Your email" style="background:#fff;color:#fff;border:1px solid rgba(255,255,255,.4);border-radius:8px;padding:10px 14px;font:inherit" />
            <textarea name="message" placeholder="Your message" rows="4" style="background:#fff;color:#fff;border:1px solid rgba(255,255,255,.4);border-radius:8px;padding:10px 14px;font:inherit"></textarea>
            <button type="submit" class="btn" style="background:var(--accent);color:#fff;border:none;border-radius:999px;cursor:pointer;font-weight:700">Send message</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="footer__inner">
    <div class="footer__grid">
      <div class="footer__col">
        <p class="brand" style="color:#fff;margin:0 0 6px">JRF &mdash; Jesus Reigns Forever International Ministry Canada</p>
        <p style="margin:0">One family. Two locations. Ontario.</p>
      </div>
      <div class="footer__col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#experience">Services</a></li>
          <li><a href="#ministry">Ministry</a></li>
          <li><a href="#getinvolved">Get Involved</a></li>
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
      <p class="brand">JRF &mdash; Jesus Reigns Forever International Ministry Canada</p>
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
document.getElementById('year').textContent=new Date().getFullYear();
</script>
</body>
</html>
"""

out = Path('C:/Users/ansel/website/jrfim-church.html')
css = CSS.replace('__CSS__', CSS)
html = HTML.replace('__CSS__', CSS).replace('__LOGO__', LOGO_URI)

full = html
full = full.replace('__CSS__', CSS)
full = full.replace('__LOGO__', LOGO_URI)
out.write_text(full, encoding='utf-8')
print("wrote", out, len(full), "bytes")
print("has logo URI:", "data:image/jpeg;base64" in full)
