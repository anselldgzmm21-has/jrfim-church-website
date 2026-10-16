"""
Build: JRFIM Premium Redesign v2
Dark cinematic + warm champagne color system
Location names updated: JRFIM Toronto/Peel, JRFIM London
Output: C:/Users/ansel/website/jrfim-church.html
"""
import base64, json, os

# Load photos
photo_keys = {
    'worship_band': 'worship_band.jpg',
    'family': 'family.jpg',
    'worship_leader': 'worship_leader.jpg',
    'preacher': 'preacher.jpg',
    'congregation': 'congregation.jpg',
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

# Read CSS from file
css_path = 'C:/Users/ansel/website/build_styles.css'
if os.path.exists(css_path):
    with open(css_path, 'r') as f:
        CSS = f.read()
else:
    CSS = ""  # fallback

# Build HTML parts
def build_html():
    html = []
    html.append('<!DOCTYPE html>')
    html.append('<html lang="en">')
    html.append('<head>')
    html.append('  <meta charset="UTF-8" />')
    html.append('  <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
    html.append('  <meta name="description" content="Jesus Reigns Forever International Ministry Canada &mdash; a Full Gospel Church with two Ontario locations. One family, two locations, united in Christ." />')
    html.append('  <title>Jesus Reigns Forever International Ministry Canada</title>')
    html.append('  <link rel="preconnect" href="https://fonts.googleapis.com">')
    html.append('  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">')
    html.append(f'  <style>{CSS}</style>')
    html.append('</head>')
    html.append('<body>')

    # NAVIGATION
    html.append('  <nav class="nav">')
    html.append('    <div class="nav__inner">')
    html.append(f'      <a href="#home" class="brand">')
    html.append(f'        <img src="{logo_uri()}" alt="JRFIM" class="brand__mark" />')
    html.append('        <span class="brand__text">')
    html.append('          <span class="label">Jesus Reigns Forever</span>')
    html.append('          <span class="name">International Ministry Canada</span>')
    html.append('        </span>')
    html.append('      </a>')
    html.append('      <ul class="nav__links">')
    html.append('        <li><a href="#welcome">Welcome</a></li>')
    html.append('        <li><a href="#locations">Locations</a></li>')
    html.append('        <li><a href="#worship">Worship</a></li>')
    html.append('        <li><a href="#messages">Messages</a></li>')
    html.append('        <li><a href="#ministries">Ministries</a></li>')
    html.append('        <li><a href="#events">Events</a></li>')
    html.append('        <li><a href="#contact">Contact</a></li>')
    html.append('      </ul>')
    html.append('      <a href="#contact" class="nav__btn">Plan Your Visit</a>')
    html.append('      <button class="menu-btn" aria-label="Menu" onclick="toggleMenu()">&#9776;</button>')
    html.append('    </div>')
    html.append('  </nav>')

    # HERO
    html.append('  <header class="hero" id="home">')
    html.append(f'    <video class="hero__video" autoplay muted loop playsinline>')
    html.append(f'      <source src="{img_uri("worship_band")}" type="video/mp4" />')
    html.append('      Your browser does not support video.')
    html.append('    </video>')
    html.append('    <div class="hero__overlay"></div>')
    html.append('    <div class="hero__content">')
    html.append('      <p class="hero__label">One Family<br/>Two Locations</p>')
    html.append('      <h1 class="hero__title">A Place to<br/>Belong.<br/>A Faith to Grow.</h1>')
    html.append('      <p class="hero__subtitle">Jesus Reigns Forever International Ministry is a Full Gospel Church &mdash; one family, two locations, united in Christ.</p>')
    html.append('      <div class="hero__actions">')
    html.append('        <a href="#locations" class="btn">Plan Your Visit</a>')
    html.append('        <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 24px;">Watch Live</a>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </header>')

    # WELCOME / OUR CHURCH
    html.append('  <section class="sec sec-center sec-light" id="welcome">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Welcome</p>')
    html.append('      <h2 class="sec-title">More Than a Church.<br/>We Are Family.</h2>')
    html.append('      <p class="sec-sub">Jesus Reigns Forever International Ministry is a Full Gospel Christian community committed to sharing the Gospel, growing in faith, winning souls, and making disciples. We are a place where you belong.</p>')
    html.append('      <p style="max-width:640px; margin:0 auto 24px; color:var(--color-muted);">')
    html.append('        We gather in Long Branch and London &mdash; two locations, one family. Whether you\'re looking for worship, community, or a place to grow in faith, you\'re welcome here.')
    html.append('      </p>')
    html.append('      <a href="#locations" class="btn">Discover Our Church</a>')
    html.append('    </div>')
    html.append('  </section>')

    # TWO LOCATIONS
    html.append('  <section class="sec sec-alt locations" id="locations">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Our Locations</p>')
    html.append('      <h2 class="sec-title">One Family.<br/>Two Locations.</h2>')
    html.append('      <div class="grid" style="max-width:1000px; margin:0 auto;">')
    html.append(f'        <div class="locations__panel">')
    html.append(f'          <img src="{img_uri("family")}" alt="JRFIM Toronto/Peel" />')
    html.append('          <h3 class="location__name">JRFIM Toronto/Peel</h3>')
    html.append('          <p class="location__addr">69 Long Branch Avenue</p>')
    html.append('          <p class="location__city">Etobicoke, Toronto, Ontario</p>')
    html.append('          <p class="location__time">Sunday Worship: 3:00 PM</p>')
    html.append('          <p class="location__note">Full Gospel Church &middot; Peel Region</p>')
    html.append('          <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn">Get Directions</a>')
    html.append('        </div>')
    html.append(f'        <div class="locations__panel">')
    html.append(f'          <img src="{img_uri("congregation")}" alt="JRFIM London" />')
    html.append('          <h3 class="location__name">JRFIM London</h3>')
    html.append('          <p class="location__addr">London, Ontario</p>')
    html.append('          <p class="location__city">London, Ontario</p>')
    html.append('          <p class="location__time">Sunday Worship: 9:30 AM</p>')
    html.append('          <p class="location__note">Full Gospel Church &middot; London Region</p>')
    html.append('          <a href="https://www.facebook.com/JRFIMLondonON" target="_blank" class="btn">Get Directions</a>')
    html.append('        </div>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # WORSHIP EXPERIENCE
    html.append('  <section class="sec sec-center sec-light" id="worship">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Worship</p>')
    html.append('      <h2 class="sec-title">We Were Made to Worship.</h2>')
    html.append('      <div class="grid" style="max-width:1100px; margin:0 auto;">')
    html.append('        <div style="grid-column: 1 / -1; display:grid; grid-template-columns: 1fr 1fr; gap:24px; align-items:center;">')
    html.append('          <div style="max-width:600px;">')
    html.append('            <p class="sec-sub">')
    html.append('              At JRFIM, we gather to worship God together &mdash; through music, prayer, Scripture, and fellowship. Whether you\'re visiting or a member, you\'re invited into a community that loves you and wants to see you grow in your faith.')
    html.append('            </p>')
    html.append('            <p style="color:var(--color-muted);">')
    html.append('              Two services each week: <strong style="color:var(--color-light);">Long Branch: Sunday 3:00 PM</strong> and <strong style="color:var(--color-light);">London: Sunday 9:30 AM</strong>. All are welcome &mdash; come as you are.')
    html.append('            </p>')
    html.append('          </div>')
    html.append(f'          <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">')
    html.append(f'            <img src="{img_uri("worship_leader")}" alt="Worship leader at JRFIM" style="width:100%; max-width:400px; border-radius:12px; box-shadow:0 8px 24px rgba(0,0,0,0.3);" />')
    html.append('          </div>')
    html.append('        </div>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # WATCH LIVE BANNER
    html.append('  <section class="sec" id="messages">')
    html.append('    <div class="container">')
    html.append('      <div class="watch-banner">')
    html.append('        <h2 class="banner-title">Watch Our Live Service</h2>')
    html.append('        <p class="banner-sub">Stream our services live from both locations. Stay connected with the church wherever you are.</p>')
    html.append('        <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">')
    html.append('          <a href="https://www.facebook.com/JRFIMpeel" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 28px;">JRFIM Toronto/Peel (3PM)</a>')
    html.append('          <a href="https://www.facebook.com/JRFIMLondonON" target="_blank" class="btn" style="background:transparent; color:var(--color-light); border:1px solid var(--color-accent); padding:14px 28px;">JRFIM London (9:30AM)</a>')
    html.append('        </div>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # MINISTRIES
    html.append('  <section class="sec sec-light ministries" id="ministries">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Ministries</p>')
    html.append('      <h2 class="sec-title">Find Your Place.<br/>Grow in Faith.</h2>')
    html.append('      <div class="ministries__grid">')
    html.append('        <div class="ministry-card">')
    html.append('          <div class="icon">&#127919;</div>')
    html.append('          <h3>Worship</h3>')
    html.append('          <p>Weekly gospel preaching and music that glorifies God. Join us Sunday at either location.</p>')
    html.append('        </div>')
    html.append('        <div class="ministry-card">')
    html.append('          <div class="icon">&#128100;</div>')
    html.append('          <h3>Life Groups</h3>')
    html.append('          <p>Small groups that meet together to study the Bible, pray, and encourage one another in faith.</p>')
    html.append('        </div>')
    html.append('        <div class="ministry-card">')
    html.append('          <div class="icon">&#127968;</div>')
    html.append('          <h3>Youth &amp; Children</h3>')
    html.append('          <p>Special gatherings and discipleship programs for the next generation. We want every child to know they are loved.</p>')
    html.append('        </div>')
    html.append('        <div class="ministry-card">')
    html.append('          <div class="icon">&#128123;</div>')
    html.append('          <h3>Outreach</h3>')
    html.append('          <p>Community events, food drives, and services that show God\'s love to the neighbourhood around us.</p>')
    html.append('        </div>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # EVENTS
    html.append('  <section class="sec sec-alt" id="events">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Upcoming</p>')
    html.append('      <h2 class="sec-title">Life Happens Together.</h2>')
    html.append('      <div class="events__grid">')
    html.append(f'        <div class="event-card">')
    html.append(f'          <div class="event-card__img"><img src="{img_uri("worship_band")}" alt="JRFIM Worship" /></div>')
    html.append('          <div class="event-card__body">')
    html.append('            <span class="event-card__date">Sunday Service</span>')
    html.append('            <h3 class="event-card__title">Sunday Service &mdash; Long Branch</h3>')
    html.append('            <p class="event-card__desc">3:00 PM at 69 Long Branch Avenue, Etobicoke. Join us for worship and Bible teaching.</p>')
    html.append('          </div>')
    html.append('        </div>')
    html.append(f'        <div class="event-card">')
    html.append(f'          <div class="event-card__img"><img src="{img_uri("worship_band")}" alt="JRFIM Worship" /></div>')
    html.append('          <div class="event-card__body">')
    html.append('            <span class="event-card__date">Sunday Service</span>')
    html.append('            <h3 class="event-card__title">Sunday Service &mdash; London</h3>')
    html.append('            <p class="event-card__desc">9:30 AM at London, Ontario. Please contact the London office for the exact meeting location.</p>')
    html.append('          </div>')
    html.append('        </div>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # CONTACT
    html.append('  <section class="sec" id="contact">')
    html.append('    <div class="container">')
    html.append('      <p class="eyebrow">Contact</p>')
    html.append('      <h2 class="sec-title">There\'s a Place<br/>for You Here.</h2>')
    html.append('      <div class="contact__grid">')
    html.append('        <div class="contact__info">')
    html.append('          <div class="contact__item">')
    html.append('            <div class="contact__icon">&#127913;</div>')
    html.append('            <div>')
    html.append('              <p class="contact__label">JRFIM Toronto / Peel</p>')
    html.append('              <p class="contact__value"><strong>69 Long Branch Avenue, Etobicoke, Toronto, Ontario</strong></p>')
    html.append('              <p class="contact__value"><strong>Sunday Service: 3:00 PM</strong></p>')
    html.append('            </div>')
    html.append('          </div>')
    html.append('          <div class="contact__item">')
    html.append('            <div class="contact__icon">&#127913;</div>')
    html.append('            <div>')
    html.append('              <p class="contact__label">JRFIM London</p>')
    html.append('              <p class="contact__value"><strong>London, Ontario</strong></p>')
    html.append('              <p class="contact__value"><strong>Sunday Service: 9:30 AM</strong></p>')
    html.append('            </div>')
    html.append('          </div>')
    html.append('          <div class="contact__item">')
    html.append('            <div class="contact__icon">&#128231;</div>')
    html.append('            <div>')
    html.append('              <p class="contact__label">Instagram</p>')
    html.append('              <p class="contact__value"><a href="https://www.instagram.com/Jrfimlondon">@Jrfimlondon</a></p>')
    html.append('            </div>')
    html.append('          </div>')
    html.append('          <div class="contact__item">')
    html.append('            <div class="contact__icon">&#9993;</div>')
    html.append('            <div>')
    html.append('              <p class="contact__label">Email</p>')
    html.append('              <p class="contact__value"><a href="mailto:info@jrfim.org">info@jrfim.org</a></p>')
    html.append('            </div>')
    html.append('          </div>')
    html.append('        </div>')
    html.append('        <form class="contact__form" action="#" method="post">')
    html.append('          <input type="text" name="name" placeholder="Your name" required />')
    html.append('          <input type="email" name="email" placeholder="Your email" required />')
    html.append('          <select name="location" style="width:auto; padding:14px 16px; font-family:var(--font-body); font-size:0.95rem; background:var(--color-bg); color:var(--color-light); border:1px solid rgba(183,168,138,0.2); border-radius:10px;">')
    html.append('            <option value="toronto">JRFIM Toronto / Peel &mdash; Long Branch (3PM)</option>')
    html.append('            <option value="london">JRFIM London (9:30AM)</option>')
    html.append('          </select>')
    html.append('          <textarea name="message" placeholder="Your message" rows="5" required></textarea>')
    html.append('          <button type="submit">Send Message</button>')
    html.append('        </form>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('  </section>')

    # FOOTER
    html.append('  <footer>')
    html.append('    <div class="footer__inner">')
    html.append('      <div class="footer__col">')
    html.append(f'        <div class="footer__logo"><img src="{logo_uri()}" alt="JRFIM" /><div class="logo-text"><span class="label">Jesus Reigns Forever</span><span class="name">International Ministry Canada</span></div></div>')
    html.append('        <p>A Full Gospel Church &mdash; one family, two locations, united in Christ.</p>')
    html.append('        <ul><li><a href="#locations">Toronto / Peel</a></li><li><a href="#locations">London</a></li></ul>')
    html.append('      </div>')
    html.append('      <div class="footer__col">')
    html.append('        <h4>Quick Links</h4>')
    html.append('        <ul><li><a href="#welcome">Welcome</a></li><li><a href="#locations">Locations</a></li><li><a href="#worship">Worship</a></li><li><a href="#ministries">Ministries</a></li></ul>')
    html.append('      </div>')
    html.append('      <div class="footer__col">')
    html.append('        <h4>JRFIM Toronto / Peel</h4>')
    html.append('        <ul><li>69 Long Branch Avenue, Etobicoke, Toronto, Ontario</li><li>Sunday Worship: 3:00 PM</li><li><a href="https://www.facebook.com/JRFIMpeel">Facebook</a></li></ul>')
    html.append('      </div>')
    html.append('      <div class="footer__col">')
    html.append('        <h4>JRFIM London</h4>')
    html.append('        <ul><li>London, Ontario</li><li>Sunday Worship: 9:30 AM</li><li><a href="https://www.facebook.com/JRFIMLondonON">Facebook</a></li><li><a href="https://www.instagram.com/Jrfimlondon">@Jrfimlondon</a></li></ul>')
    html.append('      </div>')
    html.append('    </div>')
    html.append('    <div class="footer__bottom">')
    html.append('      <p>&copy; 2026 Jesus Reigns Forever International Ministry Canada. All rights reserved.</p>')
    html.append('      <p>Full Gospel Church &middot; One family, two locations</p>')
    html.append('    </div>')
    html.append('  </footer>')

    html.append('  <script>')
    html.append('    function toggleMenu() {')
    html.append('      document.querySelector(\'.nav__links\').classList.toggle(\'open\');')
    html.append('    }')
    html.append('    // Close menu on link click')
    html.append('    document.querySelectorAll(\'.nav__links a\').forEach(function(a) {')
    html.append('      a.addEventListener(\'click\', function() {')
    html.append('        document.querySelector(\'.nav__links\').classList.remove(\'open\');')
    html.append('      });')
    html.append('    });')
    html.append('  </script>')
    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)

# Write CSS to file
css_path = 'C:/Users/ansel/website/build_styles.css'
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(CSS)

# Build and write HTML
html_content = build_html()
with open('C:/Users/ansel/website/jrfim-church.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Built jrfim-church.html ({len(html_content):,} bytes)")
