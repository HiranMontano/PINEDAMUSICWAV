import json
import re

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Juan David Pineda — Músico & Productor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --- Extraer partes del HTML ---
style_match = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
style_content = style_match.group(1) if style_match else ""

body_match = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL)
body_content = body_match.group(1) if body_match else html

scripts = re.findall(r"<script[^>]*>(.*?)</script>", body_content, re.DOTALL)
body_no_scripts = re.sub(r"<script[^>]*>.*?</script>", "", body_content, flags=re.DOTALL)

# --- Ocultar chrome de Streamlit + inyectar CSS del portafolio ---
st.markdown(
    f"""
<style>
#MainMenu, header, footer {{
    visibility: hidden;
    height: 0;
}}
.block-container {{
    padding: 0 !important;
    max-width: 100% !important;
}}
[data-testid="stVerticalBlock"] {{
    gap: 0 !important;
}}
{style_content}
</style>
""",
    unsafe_allow_html=True,
)

# --- Inyectar Google Fonts en el <head> del documento padre ---
components.html(
    """
<script>
var preconnect1 = document.createElement("link");
preconnect1.rel = "preconnect";
preconnect1.href = "https://fonts.googleapis.com";
window.parent.document.head.appendChild(preconnect1);

var preconnect2 = document.createElement("link");
preconnect2.rel = "preconnect";
preconnect2.href = "https://fonts.gstatic.com";
preconnect2.crossOrigin = "anonymous";
window.parent.document.head.appendChild(preconnect2);

var fontLink = document.createElement("link");
fontLink.rel = "stylesheet";
fontLink.href = "https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bebas+Neue&family=Anton&family=Space+Mono:wght@400;700&display=swap";
window.parent.document.head.appendChild(fontLink);
</script>
""",
    height=0,
)

# --- Renderizar contenido HTML del portafolio ---
st.markdown(body_no_scripts, unsafe_allow_html=True)

# --- Inyectar scripts en el documento padre ---
for script in scripts:
    if script.strip():
        components.html(
            f"""<script>
var s = window.parent.document.createElement("script");
s.textContent = {json.dumps(script)};
window.parent.document.body.appendChild(s);
</script>""",
            height=0,
        )
