import streamlit as st

st.set_page_config(
    page_title="Juan David Pineda — Músico & Productor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CSS GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Anton&family=Space+Mono:wght@400;700&display=swap');

/* Ocultar UI por defecto de Streamlit */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] { display: none; }
section[data-testid="stSidebar"] { display: none; }
.stApp > header { display: none; }
.block-container { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stVerticalBlock"] { gap: 0 !important; }
div[data-testid="stVerticalBlockBorderWrapper"] { gap: 0 !important; }
div[class*="element-container"] { margin: 0 !important; }

/* Variables */
:root {
    --red: #ec0d0d;
    --red-dark: #8f1018;
    --brick: #693947;
    --mauve: #8c5060;
    --ink: #17151a;
    --charcoal: #262229;
    --paper: #f0f0f6;
    --silver: #a89ca2;
    --line: rgba(240, 240, 246, 0.18);
}

/* Fondo general */
.stApp {
    background:
        radial-gradient(circle at 20% 5%, rgba(236, 13, 13, 0.20), transparent 28rem),
        radial-gradient(circle at 80% 20%, rgba(105, 57, 71, 0.35), transparent 36rem),
        linear-gradient(135deg, #111014 0%, #1e1a20 48%, #0c0b0e 100%);
    color: var(--paper);
    font-family: 'Space Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
}

a { color: inherit; text-decoration: none; }
* { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── TOPBAR ─── */
.topbar {
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    padding: 1rem 3rem;
    background: rgba(17, 16, 20, 0.92);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(236, 13, 13, 0.28);
}
.brand {
    font-family: 'Archivo Black', sans-serif;
    text-transform: uppercase;
    letter-spacing: -0.04em;
    font-size: clamp(1.1rem, 2.4vw, 1.85rem);
    line-height: 0.9;
    color: var(--paper);
}
.brand .red { color: var(--red); text-shadow: 2px 2px 0 #000; }
.navlinks {
    display: flex;
    gap: clamp(.5rem, 2vw, 1.5rem);
    flex-wrap: wrap;
    justify-content: flex-end;
    font-size: .72rem;
    text-transform: uppercase;
    letter-spacing: .12em;
}
.navlinks a {
    color: rgba(240, 240, 246, .76);
    padding: .45rem .1rem;
    border-bottom: 2px solid transparent;
    transition: .2s ease;
}
.navlinks a:hover { color: var(--paper); border-color: var(--red); }

/* ─── SECCIONES BASE ─── */
.section {
    padding: clamp(4rem, 9vw, 7.5rem) clamp(1.5rem, 4vw, 3rem);
}
.section-kicker {
    display: inline-block;
    margin-bottom: 1rem;
    color: var(--red);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .22em;
    font-size: .72rem;
}
.section-title {
    font-family: 'Archivo Black', sans-serif;
    text-transform: uppercase;
    font-size: clamp(2.2rem, 7vw, 6rem);
    line-height: .86;
    letter-spacing: -0.08em;
    text-shadow: 4px 4px 0 #000;
    margin-bottom: 0;
}
.red-word { color: var(--red); }

/* ─── BIO ─── */
.bio-section {
    display: grid;
    grid-template-columns: minmax(0, 1.15fr) minmax(280px, .85fr);
    gap: clamp(2rem, 6vw, 5rem);
    align-items: center;
    min-height: calc(100vh - 68px);
    padding: clamp(4rem, 9vw, 7.5rem) clamp(1.5rem, 4vw, 3rem);
    border-bottom: 1px solid var(--line);
}
.stamp {
    display: inline-flex;
    align-items: center;
    gap: .55rem;
    transform: rotate(-2deg);
    padding: .35rem .6rem;
    border: 2px solid var(--red);
    color: var(--red);
    font-size: .72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .18em;
    margin-bottom: 1.2rem;
    background: rgba(0, 0, 0, .22);
}
.bio-headline {
    font-family: 'Archivo Black', sans-serif;
    font-size: clamp(3rem, 10vw, 8.5rem);
    line-height: .78;
    letter-spacing: -0.09em;
    text-transform: uppercase;
    text-shadow: 6px 6px 0 #000;
    margin-bottom: 1.6rem;
}
.bio-headline .glitch {
    font-family: 'Anton', 'Archivo Black', sans-serif;
    color: var(--red);
    text-shadow: 5px 5px 0 #000;
    letter-spacing: -0.04em;
    line-height: .82;
    display: inline-block;
}
.bio-text {
    font-size: clamp(1rem, 1.7vw, 1.25rem);
    line-height: 1.8;
    color: rgba(240, 240, 246, .82);
    margin-bottom: .85rem;
    max-width: 680px;
}
.bio-text strong { color: var(--paper); }
.role-tags {
    display: flex;
    flex-wrap: wrap;
    gap: .65rem;
    margin-top: 1.3rem;
    margin-bottom: 1.75rem;
}
.tag {
    padding: .42rem .62rem;
    background: rgba(240, 240, 246, .08);
    border: 1px solid rgba(240, 240, 246, .18);
    color: rgba(240, 240, 246, .78);
    text-transform: uppercase;
    font-size: .72rem;
    letter-spacing: .12em;
}
.button-row { display: flex; flex-wrap: wrap; gap: .85rem; }
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: .85rem 1.4rem;
    border: 2px solid var(--paper);
    box-shadow: 5px 5px 0 #000;
    background: var(--red);
    color: var(--paper);
    font-family: 'Archivo Black', sans-serif;
    text-transform: uppercase;
    letter-spacing: .04em;
    transition: transform .18s ease, box-shadow .18s ease;
    cursor: pointer;
}
.btn.secondary { background: transparent; }
.btn:hover { transform: translate(3px, 3px); box-shadow: 2px 2px 0 #000; }
.bio-card {
    position: relative;
    min-height: 520px;
    border: 2px solid var(--paper);
    background: linear-gradient(0deg, rgba(236,13,13,.25), rgba(0,0,0,.1)),
                linear-gradient(135deg, var(--brick), var(--charcoal));
    box-shadow: 18px 18px 0 #000;
    overflow: hidden;
    transform: rotate(1.2deg);
}
.bio-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    filter: contrast(1.08) saturate(0.95);
    transition: transform .35s ease, filter .35s ease;
    display: block;
    min-height: 520px;
}
.bio-card:hover img { transform: scale(1.04); filter: contrast(1.15) saturate(1.05); }
.parental {
    position: absolute;
    right: 1rem;
    bottom: 1rem;
    padding: .35rem .45rem;
    border: 2px solid var(--paper);
    color: var(--paper);
    background: #000;
    font-weight: 900;
    font-size: .75rem;
    line-height: .85;
    text-align: center;
    text-transform: uppercase;
}

/* ─── GRILLA DE IMÁGENES ─── */
.image-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: .9rem;
    margin-top: 2.5rem;
}
.image-card {
    position: relative;
    overflow: hidden;
    border: 2px solid rgba(240, 240, 246, .75);
    box-shadow: 8px 8px 0 #000;
    background: linear-gradient(135deg, rgba(236,13,13,.28), rgba(105,57,71,.5)), var(--charcoal);
}
.image-card:nth-child(1) { grid-column: span 5; min-height: 460px; }
.image-card:nth-child(2) { grid-column: span 4; min-height: 300px; }
.image-card:nth-child(3) { grid-column: span 3; min-height: 300px; }
.image-card:nth-child(4) { grid-column: span 7; min-height: 320px; }
.image-card:nth-child(5) { grid-column: span 5; min-height: 320px; }
.image-card::after {
    content: attr(data-label);
    position: absolute;
    left: .85rem;
    bottom: .85rem;
    background: var(--paper);
    color: #000;
    font-family: 'Archivo Black', sans-serif;
    font-size: clamp(1.2rem, 3vw, 2.5rem);
    text-transform: uppercase;
    line-height: .9;
    padding: .25rem .45rem;
    z-index: 2;
}
.image-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    filter: contrast(1.08) saturate(0.9);
    transition: transform .35s ease, filter .35s ease;
    display: block;
    min-height: inherit;
}
.image-card:hover img { transform: scale(1.06); filter: contrast(1.15) saturate(1.05); }

/* ─── VIDEOS ─── */
.video-layout {
    display: grid;
    grid-template-columns: 1.4fr .9fr;
    gap: 1rem;
    margin-top: 2.5rem;
}
.video-stack { display: grid; gap: 1rem; }
.video-card {
    position: relative;
    min-height: 280px;
    display: grid;
    place-items: center;
    border: 2px solid rgba(240, 240, 246, .8);
    background: linear-gradient(135deg, rgba(0,0,0,.55), rgba(236,13,13,.18)),
                repeating-linear-gradient(0deg, #1b1820 0 6px, #211d25 6px 12px);
    overflow: hidden;
    box-shadow: 8px 8px 0 #000;
    color: var(--paper);
    text-decoration: none;
}
.video-main { min-height: 600px; }
.video-card img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    z-index: 0;
    filter: contrast(1.08) saturate(0.9) brightness(0.68);
    transition: transform .35s ease, filter .35s ease;
    display: block;
}
.video-card:hover img { transform: scale(1.06); filter: contrast(1.15) saturate(1.05) brightness(0.82); }
.video-card::after {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 1;
    background: linear-gradient(to top, rgba(0,0,0,.92) 0%, rgba(0,0,0,.45) 45%, rgba(236,13,13,.14) 100%);
    pointer-events: none;
}
.play-btn {
    width: 78px;
    height: 78px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    border: 3px solid var(--paper);
    color: var(--paper);
    background: var(--red);
    box-shadow: 6px 6px 0 #000;
    font-family: 'Archivo Black', sans-serif;
    font-size: 1.7rem;
    padding-left: .2rem;
    position: relative;
    z-index: 2;
    transition: transform .2s ease;
}
.video-card:hover .play-btn { transform: scale(1.08); }
.video-caption {
    position: absolute;
    left: 1rem;
    right: 1rem;
    bottom: 1rem;
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: flex-end;
    border-top: 1px solid rgba(240, 240, 246, .25);
    padding-top: .8rem;
    z-index: 2;
}
.video-caption h3 {
    font-family: 'Archivo Black', sans-serif;
    text-transform: uppercase;
    font-size: clamp(1.4rem, 3vw, 3rem);
    line-height: .9;
    letter-spacing: -.06em;
}
.video-caption span {
    color: var(--red);
    text-transform: uppercase;
    font-size: .7rem;
    letter-spacing: .14em;
    white-space: nowrap;
}

/* ─── PROYECTO ─── */
.proyecto-section {
    background: linear-gradient(90deg, rgba(236,13,13,.16), transparent 42%), rgba(0,0,0,.18);
    border-top: 1px solid rgba(236, 13, 13, .24);
    border-bottom: 1px solid rgba(236, 13, 13, .24);
    padding: clamp(4rem, 9vw, 7.5rem) clamp(1.5rem, 4vw, 3rem);
}
.project-grid {
    display: grid;
    grid-template-columns: .9fr 1.1fr;
    gap: clamp(1.5rem, 5vw, 4rem);
    align-items: start;
    margin-top: 2.5rem;
}
.project-cover {
    position: sticky;
    top: 6rem;
    min-height: 520px;
    border: 2px solid var(--paper);
    box-shadow: 14px 14px 0 #000;
    overflow: hidden;
}
.project-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    min-height: 520px;
    display: block;
    filter: contrast(1.08) saturate(0.95);
    transition: transform .35s ease, filter .35s ease;
}
.project-cover:hover img { transform: scale(1.04); filter: contrast(1.15) saturate(1.05); }
.project-copy { display: grid; gap: 1rem; }
.manifesto {
    padding: 1.2rem;
    border: 1px solid rgba(240, 240, 246, .16);
    background: rgba(240, 240, 246, .055);
    font-size: clamp(1rem, 1.7vw, 1.22rem);
    line-height: 1.75;
    color: rgba(240, 240, 246, .84);
}
.manifesto strong { color: var(--paper); }
.services {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: .5rem;
}
.service {
    display: block;
    padding: 1rem;
    border: 2px solid rgba(240, 240, 246, .65);
    background: rgba(0, 0, 0, .20);
    box-shadow: 5px 5px 0 #000;
    color: inherit;
    text-decoration: none;
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease, background .18s ease;
}
.service:hover {
    transform: translate(3px, 3px);
    box-shadow: 2px 2px 0 #000;
    border-color: var(--red);
    background: rgba(236, 13, 13, .08);
}
.service h4 {
    font-family: 'Archivo Black', sans-serif;
    color: var(--red);
    text-transform: uppercase;
    font-size: 1.1rem;
    margin-bottom: .55rem;
}
.service p {
    color: rgba(240, 240, 246, .76);
    line-height: 1.55;
    font-size: .92rem;
}

/* ─── REDES ─── */
.social-wall {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-top: 2.5rem;
}
.social-card {
    min-height: 190px;
    padding: 1rem;
    border: 2px solid var(--paper);
    background: var(--red);
    box-shadow: 8px 8px 0 #000;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-decoration: none;
    color: var(--paper);
    transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
}
.social-card:nth-child(even) { background: var(--charcoal); }
.social-card:hover { transform: translate(4px, 4px); box-shadow: 4px 4px 0 #000; background: var(--brick); }
.sc-label {
    font-size: .7rem;
    text-transform: uppercase;
    letter-spacing: .16em;
    color: rgba(240, 240, 246, .76);
    font-family: 'Space Mono', monospace;
}
.sc-name {
    font-family: 'Archivo Black', sans-serif;
    font-size: clamp(1.8rem, 3vw, 3rem);
    text-transform: uppercase;
    line-height: .9;
    letter-spacing: -.06em;
    display: block;
}

/* ─── FOOTER ─── */
.site-footer {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    padding: 2rem clamp(1.5rem, 4vw, 3rem);
    border-top: 1px solid rgba(240, 240, 246, .18);
    color: rgba(240, 240, 246, .64);
    font-size: .75rem;
    text-transform: uppercase;
    letter-spacing: .12em;
}

/* ─── RESPONSIVE ─── */
@media (max-width: 980px) {
    .bio-section, .project-grid, .video-layout { grid-template-columns: 1fr; }
    .bio-card, .project-cover { min-height: 380px; position: relative; top: auto; }
    .bio-card img, .project-cover img { min-height: 380px; }
    .social-wall { grid-template-columns: repeat(2, 1fr); }
    .image-card:nth-child(n) { grid-column: span 6; min-height: 280px; }
}
@media (max-width: 640px) {
    .topbar { align-items: flex-start; flex-direction: column; }
    .image-grid { grid-template-columns: 1fr; }
    .image-card:nth-child(n) { grid-column: auto; }
    .services, .social-wall { grid-template-columns: 1fr; }
    .video-main { min-height: 360px; }
    .video-caption { align-items: flex-start; flex-direction: column; }
    .btn { width: 100%; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  01 — TOPBAR / NAV
# ─────────────────────────────────────────────
st.markdown("""
<nav class="topbar">
    <a class="brand" href="#bio"><span class="red">David</span> Pineda</a>
    <div class="navlinks">
        <a href="#bio">Bio</a>
        <a href="#imagenes">Imágenes</a>
        <a href="#videos">Videos</a>
        <a href="#proyecto">Proyecto</a>
        <a href="#redes">Redes</a>
    </div>
</nav>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  02 — BIOGRAFÍA
# ─────────────────────────────────────────────
st.markdown("""
<section id="bio" class="bio-section">

    <div class="bio-copy">
        <div class="stamp">músico &amp; productor</div>

        <h1 class="bio-headline">
            Groove,<br><span class="glitch">Alma</span><br>identidad.
        </h1>

        <p class="bio-text">
            <strong>Convierto tu alma en música.</strong> Soy productor musical, beatmaker y músico
            enfocado en transformar ideas, emociones y visiones artísticas en proyectos con identidad
            real. Me muevo entre lo orgánico y lo urbano, mezclando influencias del jazz, el hip hop
            y otros lenguajes modernos para crear sonoridades vivas, profundas y diferentes. Busco
            que cada proyecto tenga carácter propio, que conecte emocionalmente y que haga sentir al
            artista realmente representado por su música.
        </p>
        <p class="bio-text">
            Además de la producción, trabajo como arreglista, bajista de sesión y músico en vivo,
            desarrollando desde grooves y armonías hasta estructuras y conceptos completos para cada
            proyecto. Mi enfoque está en entender la esencia de cada artista y convertirla en una
            experiencia sonora auténtica, cuidando tanto la emoción como los detalles musicales que
            hacen única una canción.
        </p>

        <div class="role-tags">
            <span class="tag">Bajista de sesión</span>
            <span class="tag">Productor musical</span>
            <span class="tag">Beatmaker</span>
            <span class="tag">Arreglista</span>
            <span class="tag">Hip-hop</span>
            <span class="tag">Jazz / Rock / R&amp;B</span>
        </div>

        <div class="button-row">
            <a class="btn" href="#redes">Ver redes</a>
            <a class="btn secondary" href="#proyecto">Proyecto personal</a>
        </div>
    </div>

    <aside class="bio-card">
        <img
            src="https://i.pinimg.com/736x/86/0d/79/860d79bdaf4655315dd87553952f73f7.jpg"
            alt="Juan David Pineda"
        />
        <div class="parental">Original<br>Groove<br>Content</div>
    </aside>

</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  03 — IMÁGENES
# ─────────────────────────────────────────────
st.markdown("""
<section id="imagenes" class="section">
    <span class="section-kicker">02 / Imagen visual</span>
    <h2 class="section-title">Fotos, estética y <span class="red-word">universo</span>.</h2>

    <div class="image-grid">
        <article class="image-card" data-label="Live">
            <img
                src="https://i.pinimg.com/736x/36/25/d9/3625d966695bb11b73a264aa40bb730e.jpg"
                alt="Press shot"
            />
        </article>
        <article class="image-card" data-label="Studio">
            <img
                src="https://i.pinimg.com/736x/c1/16/3d/c1163d9709a92765a73b77d228c256d2.jpg"
                alt="Estudio"
            />
        </article>
        <article class="image-card" data-label="Live">
            <img
                src="https://i.pinimg.com/736x/3d/4e/12/3d4e1260525308ad698817b782a7a468.jpg"
                alt="En vivo"
            />
        </article>
        <article class="image-card" data-label="Dirección">
            <img
                src="https://i.pinimg.com/736x/ff/c8/2c/ffc82c53f240cb29ccddbbe8fc03dc8b.jpg"
                alt="Moodboard"
            />
        </article>
        <article class="image-card" data-label="Arreglos">
            <img
                src="https://i.pinimg.com/736x/42/ef/8d/42ef8dbbc4625969554a3f613b886ac9.jpg"
                alt="Proceso creativo"
            />
        </article>
    </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  04 — VIDEOS
#  Miniaturas de YouTube pre-calculadas a partir del video ID
# ─────────────────────────────────────────────
VIDEOS = [
    {
        "id": "YCxhXTU4NrE",
        "url": "https://www.youtube.com/watch?v=YCxhXTU4NrE",
        "title": "Grabaciones de estudio",
        "sub": "Mr / LOS FAROS",
        "main": True,
    },
    {
        "id": "r7QvKXb2bo4",
        "url": "https://youtube.com/shorts/r7QvKXb2bo4",
        "title": "Arreglos",
        "sub": "YouTube",
        "main": False,
    },
    {
        "id": "7lq5X5ncoKE",
        "url": "https://www.youtube.com/shorts/7lq5X5ncoKE",
        "title": "Live Sevijazz 2025",
        "sub": "Latin jazz / Bass Impro",
        "main": False,
    },
]

def video_card(v: dict) -> str:
    thumb = f"https://img.youtube.com/vi/{v['id']}/hqdefault.jpg"
    cls   = "video-card video-main" if v["main"] else "video-card"
    return f"""
    <a class="{cls}" href="{v['url']}" target="_blank" rel="noopener">
        <img src="{thumb}" alt="{v['title']}" />
        <div class="play-btn">&#9654;</div>
        <div class="video-caption">
            <h3>{v['title']}</h3>
            <span>{v['sub']}</span>
        </div>
    </a>"""

sidebar_cards = "".join(video_card(v) for v in VIDEOS[1:])

st.markdown(f"""
<section id="videos" class="section">
    <span class="section-kicker">03 / Videos</span>
    <h2 class="section-title">Sesiones, reels y <span class="red-word">performance</span>.</h2>

    <div class="video-layout">
        {video_card(VIDEOS[0])}
        <div class="video-stack">
            {sidebar_cards}
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  05 — PROYECTO PERSONAL
# ─────────────────────────────────────────────
st.markdown("""
<section id="proyecto" class="proyecto-section">
    <span class="section-kicker">04 / Proyecto personal</span>
    <h2 class="section-title">Mi lado más <span class="red-word">personal</span>.</h2>

    <div class="project-grid">

        <div class="project-cover">
            <img
                src="https://i.pinimg.com/736x/94/8c/e7/948ce7e13a94c03b0f8783794f0be3dd.jpg"
                alt="Proyecto personal"
            />
        </div>

        <div class="project-copy">
            <p class="manifesto">
                Mi proyecto personal nace de la unión entre el <strong>hip-hop old school</strong>,
                el sampling, el bajo eléctrico y la sensibilidad armónica del jazz. Es un espacio
                para contar historias desde el groove: beats con textura, melodías oscuras, baterías
                con peso y una estética cruda, directa y emocional.
            </p>
            <p class="manifesto">
                Más que producir por producir, busco construir una identidad completa: portada,
                sonido, narrativa, referencias, arreglos e intención. Cada canción tiene que
                sentirse como una escena, una calle, una noche o una memoria.
            </p>

            <div class="services">
                <a class="service"
                   href="https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq?si=76fceaf982c049c5"
                   target="_blank" rel="noopener">
                    <h4>Spotify</h4>
                    <p>Escucha mis lanzamientos oficiales, colaboraciones y producciones disponibles en plataformas digitales.</p>
                </a>
                <a class="service"
                   href="https://www.youtube.com/@Pinedamusic.wav6"
                   target="_blank" rel="noopener">
                    <h4>YouTube</h4>
                    <p>Mira live sessions, presentaciones, contenido visual y procesos detrás de cada proyecto.</p>
                </a>
                <a class="service"
                   href="https://soundcloud.com/sin-oficio-688647778"
                   target="_blank" rel="noopener">
                    <h4>SoundCloud</h4>
                    <p>Encuentra demos, beats, ideas en proceso y material experimental que complementa mi universo sonoro.</p>
                </a>
                <a class="service"
                   href="https://www.instagram.com/pinedamusic.wav/?hl=es"
                   target="_blank" rel="noopener">
                    <h4>Instagram</h4>
                    <p>Sigue mi proceso creativo, contenido visual, reels, sesiones y momentos del día a día como músico y productor.</p>
                </a>
            </div>
        </div>

    </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  06 — REDES
# ─────────────────────────────────────────────
st.markdown("""
<section id="redes" class="section">
    <span class="section-kicker">05 / Links</span>
    <h2 class="section-title">Conecta conmigo en <span class="red-word">redes</span>.</h2>

    <div class="social-wall">
        <a class="social-card"
           href="https://www.instagram.com/pinedamusic.wav/?hl=es"
           target="_blank" rel="noopener">
            <span class="sc-label">Fotos / reels / proceso</span>
            <strong class="sc-name">Instagram</strong>
        </a>
        <a class="social-card"
           href="https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq"
           target="_blank" rel="noopener">
            <span class="sc-label">Lanzamientos / música</span>
            <strong class="sc-name">Spotify</strong>
        </a>
        <a class="social-card"
           href="https://www.youtube.com/@Pinedamusic.wav6"
           target="_blank" rel="noopener">
            <span class="sc-label">Videos / sesiones</span>
            <strong class="sc-name">YouTube</strong>
        </a>
        <a class="social-card"
           href="https://soundcloud.com/sin-oficio-688647778"
           target="_blank" rel="noopener">
            <span class="sc-label">Beats / demos / ideas</span>
            <strong class="sc-name">SoundCloud</strong>
        </a>
    </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<footer class="site-footer">
    <p>© 2026 — Juan David Pineda Ramirez</p>
    <p>Músico · Productor · Beatmaker · Bajista</p>
</footer>
""", unsafe_allow_html=True)
