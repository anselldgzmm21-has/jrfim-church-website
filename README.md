# Jesus Reigns Forever International Ministry Canada

A warm, fall-themed, mobile-first website for **Jesus Reigns Forever International Ministry Canada**.

## What's inside

- `index.html` — the whole site (one page, 7 sections)
- `styles.css` — all styling, themeable via the `:root` color variables
- `README.md` — this file

## Sections

1. **Hero** — ministry name + "one family, two locations"
2. **Welcome** — intro + a warm quote card
3. **About** — our ministry + "family" stats
4. **Services** — weekly service times at both locations
5. **Locations** — Long Branch & London, with service times
6. **Sermons** — curated recent messages (placeholders)
7. **Give** — how to support the ministry
8. **Contact** — contact details + message form

## Where to fill in your real details

Everything is editable in `index.html` / `styles.css`. In particular:

| What | Where to change it |
| --- | --- |
| Phone number | `index.html` → Contact section, `<p class="contact__value">` |
| Email address | `index.html` → Contact section, `<p class="contact__value">` |
| Full street address for Long Branch | `index.html` → Locations section (`69 Long Branch`) |
| Sermon links | `index.html` → Sermons section, `<a href="#">` |
| Colors | `styles.css` → `:root` variable block at the top |
| Photos | Replace the `.card__img`, `.sermon-card__img`, `.give__card .card__img` blocks (or drop in `<img>` tags) |

> You shared "69 Long Branch" as the Long Branch address. I kept it exactly as you wrote it
> (no invented street/route). If it needs a full address or a specific city/route, just send it
> and I'll update it. I also left a small "addresses confirmed by you" note on the Locations page
> so the site is honest until you confirm.

## Design notes (why it feels "one family")

- **Warm fall palette** — deep coffee browns, rust, autumn orange, gold, and cream. Lights up
  and feels like gathering around a fall table.
- **Serif headings (Georgia)** — a classic, warm, familiar read.
- **Contrast** — the Locations section is dark so the "2 locations / 2 services" cards pop.
- **Accessible** — `:focus-visible` outlines, semantic HTML, plain-language contrast, keyboard
  friendly, no autoplay, no popups.

## Free hosting (GitHub Pages)

I used plain HTML + CSS with **no build step**, so the only free options are straightforward:

1. Create a free GitHub account at https://github.com/join
2. Create a repo named `yourname.github.io` (or any repo name)
3. Upload `index.html`, `styles.css`, and `README.md` into the repo
4. Go to **Settings → Pages** → "Deploy from a branch" → `main` / `/root` → Save
5. Done: your site is live at `https://yourname.github.io`

Then set the custom domain:

- In the repo **Settings → Pages**, paste `jrfim` (or `jrfim.ca`) under **Custom domain**
- On some hosts you'll also add a `CNAME` file with `jrfim.com` (or whatever you choose)
- Buy the domain from any registrar if you don't have it yet

### About the domain `jrfim`

`jrfim` is a short slug — on GitHub Pages it would be something like
`https://jrfim.github.io`. If you want a clean short URL like `https://jrfim.com` or
`https://jrfim.ca`, you'd buy a short domain name (~$10–15/yr) and point/redirect it to
GitHub Pages (or Netlify/Vercel, which make custom domains painless).

## Making the contact form actually send email (free)

Static GitHub Pages doesn't process forms by itself. Pick one and tell me which you'd like:

- **Formspree** (free tier, ~50 submissions/mo): change the form `action` to
  `https://formspree.io/f/YOUR_ID` and drop your email in their dashboard.
- **Netlify Forms** (if you ever move to Netlify): just name the form elements `name`, `email`,
  `message` and Netlify captures submissions for free.
- **Your own email + a mailto fallback**: the page currently shows a "thank-you" message after
  submit. The README notes the same, and we can add a simple server-less route (Vercel/Netlify)
  that emails your inbox.

## Going beyond this page

If you'd like, I can add any of these next (still free, same GitHub Pages host):

- Separate **About** and **Sermons** pages
- A **calendar** of event dates (e.g., "fortnightly services", outreach nights)
- A **Sunday bulletins / event archive** section
- **Photo gallery** of your family (add your own photos)
- A **sidebar** with your real contact card and an "upcoming events" list
- Mobile menu (the hamburger is already wired in the CSS)

Just say the word and I'll build it out.
