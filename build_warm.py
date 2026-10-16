"""
Build: JRFIM premium heritage church website (warm fall palette).
Output: C:/Users/ansel/website/jrfim-church.html
"""
import base64, json, os

# Load the 5 embedded photos (re-encode any recent PNGs back to JPEG B64)
imgs = json.load(open('C:/Users/ansel/website/images_b64.json'))
# Rebuild the base64 strings directly from files to guarantee freshness
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

logo_b64 = None
if os.path.exists('C:/Users/ansel/website/logo_transparent.png'):
    with open('C:/Users/ansel/website/logo_transparent.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('ascii')
    print("Transparent logo loaded:", logo_b64 is not None)
else:
    print("WARNING: transparent logo not found, using fallback")
    if os.path.exists('C:/Users/ansel/website/logo_b64.json'):
        logo_b64 = json.load(open('C:/Users/ansel/website/logo_b64.json'))['logo']

def img_uri(key):
    return f"data:image/jpeg;base64,{full_imgs[key]}"

def logo_uri():
    if logo_b64:
        return f"data:image/png;base64,{logo_b64}"
    return "data:image/jpeg;base64," + full_imgs['preacher']  # fallback

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>JRFIM — Jesus Reigns Forever International Ministry Canada</title>
  <meta name="description" content="Jesus Reigns Forever International Ministry Canada — a Full Gospel Church family welcoming you to worship with us." />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#127967;</text></svg>" />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=DM+Serif+Display:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    :root {{
      --color-bg: #f8f1e3;
      --color-bg-alt: #f3e6d2;
      --color-surface: #ffffff;
      --color-foreground: #3a1f0e;
      --color-secondary: #6b3a2e;
      --color-accent: #c8621b;
      --color-accent2: #d98a3d;
      --color-border: #e6d5b8;
      --color-muted: #8a6b4a;
      --color-white: #ffffff;
      --color-primary: #3a1f0e;
      --color-darker: #2a1a0e;
      --nav-height: 5rem;
      --radius: 12px;
      --font-base: "DM Sans", "Inter", "Segoe UI", Roboto, Arial, sans-serif;
      --font-serif: "DM Serif Display", "Georgia", "Times New Roman", serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: var(--font-base);
      background: var(--color-bg);
      color: var(--color-foreground);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}
    a {{ color: var(--color-foreground); text-decoration: none; }}
    img {{ max-width: 100%; display: block; }}
    :focus-visible {{ outline: 2px solid var(--color-accent); outline-offset: 3px; border-radius: 4px; }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 1.25rem; }}
    .wrap {{ max-width: 720px; margin: 0 auto; }}

    /* ---------- NAV ---------- */
    .nav {{
      position: sticky; top: 0; z-index: 100;
      background: rgba(248,241,227,0.92);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--color-border);
    }}
    .nav__inner {{
      max-width: 1200px; margin: 0 auto; padding: 0.75rem 1.25rem;
      display: flex; align-items: center; justify-content: space-between; gap: 1rem;
    }}
    .brand {{
      font-family: var(--font-serif);
      font-size: 1.15rem; font-weight: 700;
      color: var(--color-foreground); display: flex; align-items: center; gap: 0.6rem;
    }}
    .brand__mark {{ width: 32px; height: 32px; border-radius: 6px; object-fit: cover; }}
    .nav__links {{
      display: flex; gap: 1.1rem; list-style: none;
    }}
    .nav__links a {{
      font-size: 0.85rem; font-weight: 600; color: var(--color-secondary);
      transition: color 0.2s;
    }}
    .nav__links a:hover {{ color: var(--color-accent); }}
    .nav__btn {{
      background: var(--color-foreground); color: #fff; border: none;
      padding: 0.5rem 1rem; border-radius: 6px; font-size: 0.82rem; font-weight: 700; cursor: pointer;
    }}
    .nav__btn:hover {{ background: #2a160c; }}
    .menu-btn {{
      display: none; background: none; border: none; cursor: pointer;
      font-size: 1.4rem; color: var(--color-foreground); line-height: 1;
    }}

    /* ---------- HERO ---------- */
    .hero {{
      position: relative; padding: 4.5rem 1.25rem 3.5rem;
      background: linear-gradient(160deg, rgba(248,241,227,.20), rgba(243,230,210,.92));
      overflow: hidden;
    }}
    .hero__bg {{
      position: absolute; inset: 0;
      background: linear-gradient(160deg, rgba(200,98,27,.15), rgba(107,58,46,.88));
    }}
    .hero__img {{
      position: absolute; inset: 0;
      background-image: url('{img_uri("worship_band")}');
      background-size: cover; background-position: center;
    }}
    .hero__content {{
      position: relative; z-index: 2;
      max-width: 720px; margin: 0 auto;
    }}
    .hero__title {{
      font-family: var(--font-serif);
      font-size: clamp(2.6rem, 6vw, 4.2rem); line-height: 1.1; font-weight: 700;
      margin-bottom: 0.75rem; color: #fff; letter-spacing: 0.01em;
    }}
    .hero__subtitle {{
      font-size: 1.08rem; color: rgba(255,255,255,0.9); font-weight: 400;
      max-width: 580px; margin-bottom: 1.5rem;
    }}
    .hero__btn {{
      display: inline-block; background: var(--color-accent); color: #fff;
      padding: 0.85rem 2rem; border-radius: 8px; font-weight: 700; font-size: 0.95rem;
      box-shadow: 0 4px 14px rgba(0,0,0,0.18); transition: background 0.2s;
    }}
    .hero__btn:hover {{ background: #b05216; }}

    /* ---------- SECTIONS ---------- */
    .section {{ padding: 3.2rem 1.25rem; }}
    .section__title {{
      font-family: var(--font-serif);
      font-size: 2rem; color: var(--color-foreground); margin-bottom: 1.5rem;
      text-align: center;
    }}
    .section--alt {{ background: var(--color-bg-alt); }}

    /* ---------- GRID ---------- */
    .grid {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem; margin-top: 1.5rem;
    }}
    .card {{
      background: #fff; border: 1px solid var(--color-border); border-radius: var(--radius);
      padding: 1.25rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04); transition: box-shadow 0.2s;
    }}
    .card:hover {{ box-shadow: 0 4px 16px rgba(0,0,0,0.08); }}
    .card__img {{
      width: 100%; height: 140px; border-radius: 8px; overflow: hidden;
      background: linear-gradient(135deg, #e8e0d0, #d8ccc0);
    }}
    .card__img img {{ width: 100%; height: 100%; object-fit: cover; }}
    .card__title {{
      font-family: var(--font-serif); font-size: 1.15rem; margin: 0.75rem 0 0.4rem;
      color: var(--color-foreground);
    }}
    .card__desc {{
      font-size: 0.92rem; color: var(--color-muted); line-height: 1.5;
    }}

    /* ---------- CTA ---------- */
    .cta-section {{ text-align: center; }}
    .cta-section .section__title {{ color: #fff; }}
    .cta-section p {{ color: rgba(255,255,255,0.9); margin-bottom: 1.5rem; }}
    .cta-btns {{
      display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;
    }}
    .cta-btns .button {{
      display: inline-block; background: var(--color-accent); color: #fff;
      padding: 0.85rem 1.8rem; border-radius: 8px; font-weight: 700; font-size: 0.95rem;
      box-shadow: 0 4px 14px rgba(0,0,0,0.15); transition: background 0.2s;
    }}
    .cta-btns .button:hover {{ background: #b05216; }}

    /* ---------- FORM ---------- */
    .form {{
      max-width: 560px; margin: 1.5rem auto 0; display: grid; gap: 0.85rem;
    }}
    .form input, .form textarea {{
      padding: 0.85rem 1rem; border: 1px solid var(--color-border); border-radius: 8px;
      font: inherit; font-size: 0.95rem; background: #fff; color: var(--color-foreground);
      width: 100%;
    }}
    .form input:focus, .form textarea:focus {{
      outline: 2px solid var(--color-accent); border-color: transparent;
    }}
    .form textarea {{ resize: vertical; min-height: 120px; }}

    /* ---------- FOOTER ---------- */
    .footer {{
      background: var(--color-primary); color: #fff; padding: 2.8rem 1.25rem 1.8rem;
    }}
    .footer__inner {{
      max-width: 1200px; margin: 0 auto; display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr; gap: 1.5rem;
    }}
    .footer h3 {{
      font-family: var(--font-serif); font-size: 1.05rem; margin-bottom: 0.7rem;
    }}
    .footer ul {{
      list-style: none; display: grid; gap: 0.4rem;
    }}
    .footer ul a {{ color: rgba(255,255,255,0.85); font-size: 0.92rem; }}
    .footer ul a:hover {{ color: #fff; }}
    .footer .copyright {{
      max-width: 1200px; margin: 1.5rem auto 0; padding-top: 1rem;
      border-top: 1px solid rgba(255,255,255,0.2); font-size: 0.82rem; color: rgba(255,255,255,0.7);
    }}
    .footer__brand {{ border-radius: 8px; overflow: hidden; }}
    .footer__brand img {{ width: 100%; height: 60px; object-fit: cover; display: block; }}

    @media (max-width: 768px) {{
      .nav__links {{ display: none; }}
      .menubtn {{ display: block; }}
      .footer__inner {{ grid-template-columns: 1fr; gap: 1rem; }}
      .hero {{ padding: 3rem 1.25rem 2.5rem; }}
    }}
  </style>
</head>
<body>

  <!-- ===================== NAV ===================== -->
  <nav class="nav">
    <div class="nav__inner">
      <a href="#" class="brand">
        <img src="{logo_uri()}" alt="JRFIM" class="brand__mark" />
        Jesus Reigns Forever International Ministry Canada
      </a>
      <ul class="nav__links">
        <li><a href="#welcome">Welcome</a></li>
        <li><a href="#worship">Worship</a></li>
        <li><a href="#message">Message</a></li>
        <li><a href="#people">Our People</a></li>
        <li><a href="#locations">Locations</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="#contact" class="nav__btn">Find a Service</a>
      <button class="menu-btn" aria-label="Toggle menu">&#9776;</button>
    </div>
  </nav>

  <!-- ===================== HERO ===================== -->
  <header class="hero">
    <div class="hero__bg"></div>
    <div class="hero__img"></div>
    <div class="hero__content">
      <h1 class="hero__title">Jesus Reigns Forever International Ministry Canada</h1>
      <p class="hero__subtitle">A Full Gospel Church — a growing family in Christ.<br />
      Many places to meet, one family in the Lord.</p>
      <a href="#locations" class="hero__btn">Find a Service</a>
    </div>
  </header>

  <!-- ===================== WELCOME ===================== -->
  <section class="section" id="welcome">
    <div class="container">
      <h2 class="section__title">Welcome to JRFIM</h2>
      <div class="grid">
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('family')}" alt="Family at JRFIM" />
          </div>
          <h3 class="card__title">One Family in Christ</h3>
          <p class="card__desc">At Jesus Reigns Forever International Ministry, we're a family. Every Sunday, people from all walks of life come together to worship, learn, and grow in faith. You don't have to do this alone — come as you are.</p>
        </article>
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('worship_leader')}" alt="Worship leader at JRFIM" />
          </div>
          <h3 class="card__title">Complete Worship</h3>
          <p class="card__desc">Music, teaching, prayer, and community. Every Sunday at 3PM (Mississauga) and 9:30AM (London), we gather to give glory to God through worship, Word, and fellowship.</p>
        </article>
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('congregation')}" alt="Congregation at JRFIM" />
          </div>
          <h3 class="card__title">Gospel-Centered</h3>
          <p class="card__desc">We believe in the Great Commission — winning souls and making disciples. Our services are designed to help you encounter God, grow in your faith, and connect with a community that cares.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===================== WORSHIP ===================== -->
  <section class="section section--alt" id="worship">
    <div class="container">
      <h2 class="section__title">Worship Service Times</h2>
      <div class="grid">
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('worship_band')}" alt="Worship band at JRFIM" />
          </div>
          <h3 class="card__title">Mississauga — Long Branch</h3>
          <p class="card__desc"><strong>Location:</strong> 69 Long Branch Ave, Mississauga, ON<br />
          <strong>Time:</strong> Sunday @ 3:00 PM<br />
          <strong>Contact:</strong> +1 416-562-6479</p>
        </article>
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('preacher')}" alt="Preacher at JRFIM" />
          </div>
          <h3 class="card__title">London</h3>
          <p class="card__desc"><strong>Location:</strong> JRFIM London (see Facebook for details)<br />
          <strong>Time:</strong> Sunday @ 9:30 AM</p>
        </article>
      </div>
      <p style="text-align:center; margin-top:1.5rem; font-size:0.92rem; color:var(--color-muted);">
        <strong>Instagram:</strong> <a href="https://instagram.com/Jrfimlondon" target="_blank" style="color:var(--color-accent);">@Jrfimlondon</a>
      </p>
    </div>
  </section>

  <!-- ===================== MESSAGE ===================== -->
  <section class="section" id="message">
    <div class="container">
      <h2 class="section__title">The Word for Today</h2>
      <div class="grid">
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('preacher')}" alt="Preacher at JRFIM" />
          </div>
          <h3 class="card__title">Saturday Night Service</h3>
          <p class="card__desc">We welcome you to our weekly services. Come expectant — God is moving, and we can't wait for you to experience what He's doing at JRFIM.</p>
        </article>
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('worship_leader')}" alt="Worship leader at JRFIM" />
          </div>
          <h3 class="card__title">Saturday Night Service</h3>
          <p class="card__desc">We welcome you to our weekly services. Come expectant — God is moving, and we can't wait for you to experience what He's doing at JRFIM.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===================== OUR PEOPLE ===================== -->
  <section class="section section--alt" id="people">
    <div class="container">
      <h2 class="section__title">Join Us</h2>
      <div class="grid">
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('congregation')}" alt="Congregation at JRFIM" />
          </div>
          <h3 class="card__title">You're Invited</h3>
          <p class="card__desc">Whether you're a lifelong believer or just curious, you're welcome here. Come with an open heart, ask questions, and find a community that loves you for who you are.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===================== LOCATIONS ===================== -->
  <section class="section" id="locations">
    <div class="container">
      <h2 class="section__title">Find a Location</h2>
      <div class="grid">
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('worship_band')}" alt="Worship at JRFIM Mississauga" />
          </div>
          <h3 class="card__title">JRFIM Peel Region</h3>
          <p class="card__desc"><strong>Full Gospel Church</strong><br />
          69 Long Branch Ave, Mississauga, ON<br />
          Sunday @ 3:00 PM<br />
          +1 416-562-6479</p>
        </article>
        <article class="card">
          <div class="card__img">
            <img src="{img_uri('preacher')}" alt="JRFIM London" />
          </div>
          <h3 class="card__title">JRFIM London</h3>
          <p class="card__desc"><strong>A Full Gospel Church</strong> — a growing family in Christ.<br />
          Sunday @ 9:30 AM<br />
          Instagram: <a href="https://instagram.com/Jrfimlondon" target="_blank" style="color:var(--color-accent);">@Jrfimlondon</a></p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===================== CONTACT ===================== -->
  <section class="section section--alt" id="contact">
    <div class="container">
      <h2 class="section__title">Get In Touch</h2>
      <p style="max-width:600px; margin:0 auto 1.5rem; text-align:center; color:var(--color-muted);">Have a question or want to know more? Send us a message — we'd love to hear from you.</p>
      <form class="form" action="#" method="post">
        <input type="text" name="name" placeholder="Your name" required />
        <input type="email" name="email" placeholder="Your email" required />
        <textarea name="message" placeholder="Your message" rows="5" required></textarea>
        <button type="submit" class="button">Send message</button>
      </form>
    </div>
  </section>

  <!-- ===================== FOOTER ===================== -->
  <footer class="footer">
    <div class="footer__inner">
      <div>
        <div class="footer__brand">
          <img src="{logo_uri()}" alt="JRFIM" />
        </div>
        <h3>Jesus Reigns Forever</h3>
        <p style="font-size:0.88rem; color:rgba(255,255,255,0.8);">
          Peel Region — Full Gospel Church, Mississauga<br />
          London — Full Gospel Church, Sunday 9:30AM
        </p>
      </div>
      <div>
        <h3>Connect</h3>
        <ul>
          <li><a href="https://www.instagram.com/Jrfimlondon" target="_blank">Instagram: @Jrfimlondon</a></li>
          <li><a href="https://www.facebook.com/JRFIMpeel" target="_blank">Facebook: JRFIM Peel Region</a></li>
          <li><a href="https://www.facebook.com/JRFIMLondonON" target="_blank">Facebook: JRFIM London</a></li>
        </ul>
      </div>
      <div>
        <h3>Visit</h3>
        <ul>
          <li>Peel Region: 69 Long Branch Ave, Mississauga, ON</li>
          <li>London: See Facebook for address</li>
          <li>Peel Region: Sunday @ 3PM</li>
          <li>London: Sunday @ 9:30AM</li>
        </ul>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li>Peel Region: +1 416-562-6479</li>
          <li>London: @Jrfimlondon (Instagram)</li>
          <li>Email: <a href="mailto:info@jrfim.org">info@jrfim.org</a></li>
        </ul>
      </div>
    </div>
    <p class="copyright">&copy; {__import__('datetime').date.today().year} JRFIM Canada. All rights reserved.</p>
  </footer>

  <script>
    const menuBtn = document.querySelector('.menu-btn');
    const navLinks = document.querySelector('.nav__links');
    menuBtn.addEventListener('click', () => {{
      if (navLinks.style.display === 'flex') {{{{
        navLinks.style.display = 'none';
      }} else {{
        navLinks.style.display = 'flex';
      }}
    }});
    document.querySelectorAll('.nav__links a').forEach(a => {{
      a.addEventListener('click', () => {{
        navLinks.style.display = 'none';
      }});
    }});
  </script>
</body>
</html>
"""

with open('C:/Users/ansel/website/jrfim-church.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"Built jrfim-church.html ({len(HTML):,} bytes)")
print(f"Photos embedded: {len(full_imgs)} keys, logo loaded: {bool(logo_b64)}")
