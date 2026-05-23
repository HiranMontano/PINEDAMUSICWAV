import streamlit as st

st.set_page_config(
    page_title="Juan David Pineda — Músico & Productor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════
st.markdown("# 🎸 DAVID PINEDA")
st.markdown("**Músico · Productor · Beatmaker · Bajista de Sesión**")
st.divider()

# ═══════════════════════════════════════════════════════
#  NAVEGACIÓN — TABS
# ═══════════════════════════════════════════════════════
tab_bio, tab_img, tab_vid, tab_proy, tab_redes = st.tabs(
    ["Bio", "Imágenes", "Videos", "Proyecto", "Redes"]
)


# ───────────────────────────────────────────────────────
#  01 / BIO
# ───────────────────────────────────────────────────────
with tab_bio:
    st.caption("01 / MÚSICO & PRODUCTOR")

    col_texto, col_foto = st.columns([3, 2], gap="large")

    with col_texto:
        st.markdown("## Groove, Alma, identidad.")

        st.markdown(
            "**Convierto tu alma en música.** Soy productor musical, beatmaker y músico "
            "enfocado en transformar ideas, emociones y visiones artísticas en proyectos "
            "con identidad real. Me muevo entre lo orgánico y lo urbano, mezclando "
            "influencias del jazz, el hip hop y otros lenguajes modernos para crear "
            "sonoridades vivas, profundas y diferentes. Busco que cada proyecto tenga "
            "carácter propio, que conecte emocionalmente y que haga sentir al artista "
            "realmente representado por su música."
        )

        st.markdown(
            "Además de la producción, trabajo como arreglista, bajista de sesión y músico "
            "en vivo, desarrollando desde grooves y armonías hasta estructuras y conceptos "
            "completos para cada proyecto. Mi enfoque está en entender la esencia de cada "
            "artista y convertirla en una experiencia sonora auténtica, cuidando tanto la "
            "emoción como los detalles musicales que hacen única una canción."
        )

        st.markdown("")
        st.markdown(
            "`Bajista de sesión`  `Productor musical`  `Beatmaker`  "
            "`Arreglista`  `Hip-hop`  `Jazz / Rock / R&B`"
        )
        st.markdown("")

        b1, b2 = st.columns(2)
        with b1:
            st.link_button(
                "Ver redes →",
                "https://www.instagram.com/pinedamusic.wav/",
                use_container_width=True,
            )
        with b2:
            st.link_button(
                "Proyecto personal →",
                "https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq",
                use_container_width=True,
            )

    with col_foto:
        st.image(
            "https://i.pinimg.com/736x/86/0d/79/860d79bdaf4655315dd87553952f73f7.jpg",
            caption="Juan David Pineda — Original Groove Content",
            use_container_width=True,
        )


# ───────────────────────────────────────────────────────
#  02 / IMÁGENES
# ───────────────────────────────────────────────────────
with tab_img:
    st.caption("02 / IMAGEN VISUAL")
    st.markdown("## Fotos, estética y universo.")
    st.markdown("")

    r1c1, r1c2, r1c3 = st.columns([5, 4, 3], gap="small")
    r1c1.image(
        "https://i.pinimg.com/736x/36/25/d9/3625d966695bb11b73a264aa40bb730e.jpg",
        caption="Live",
        use_container_width=True,
    )
    r1c2.image(
        "https://i.pinimg.com/736x/c1/16/3d/c1163d9709a92765a73b77d228c256d2.jpg",
        caption="Studio",
        use_container_width=True,
    )
    r1c3.image(
        "https://i.pinimg.com/736x/3d/4e/12/3d4e1260525308ad698817b782a7a468.jpg",
        caption="Live",
        use_container_width=True,
    )

    st.markdown("")

    r2c1, r2c2 = st.columns([7, 5], gap="small")
    r2c1.image(
        "https://i.pinimg.com/736x/ff/c8/2c/ffc82c53f240cb29ccddbbe8fc03dc8b.jpg",
        caption="Dirección",
        use_container_width=True,
    )
    r2c2.image(
        "https://i.pinimg.com/736x/42/ef/8d/42ef8dbbc4625969554a3f613b886ac9.jpg",
        caption="Arreglos",
        use_container_width=True,
    )


# ───────────────────────────────────────────────────────
#  03 / VIDEOS
# ───────────────────────────────────────────────────────
with tab_vid:
    st.caption("03 / VIDEOS")
    st.markdown("## Sesiones, reels y performance.")
    st.markdown("")

    col_main, col_stack = st.columns([3, 2], gap="medium")

    with col_main:
        st.markdown("**Grabaciones de estudio — Mr / LOS FAROS**")
        st.video("https://www.youtube.com/watch?v=YCxhXTU4NrE")

    with col_stack:
        st.markdown("**Arreglos**")
        st.video("https://youtube.com/shorts/r7QvKXb2bo4")

        st.markdown("")
        st.markdown("**Live — Sevijazz 2025 · Latin jazz / Bass Impro**")
        st.video("https://www.youtube.com/shorts/7lq5X5ncoKE")


# ───────────────────────────────────────────────────────
#  04 / PROYECTO PERSONAL
# ───────────────────────────────────────────────────────
with tab_proy:
    st.caption("04 / PROYECTO PERSONAL")
    st.markdown("## Mi lado más personal.")
    st.markdown("")

    col_cover, col_copy = st.columns([2, 3], gap="large")

    with col_cover:
        st.image(
            "https://i.pinimg.com/736x/94/8c/e7/948ce7e13a94c03b0f8783794f0be3dd.jpg",
            use_container_width=True,
        )

    with col_copy:
        st.markdown(
            "Mi proyecto personal nace de la unión entre el **hip-hop old school**, "
            "el sampling, el bajo eléctrico y la sensibilidad armónica del jazz. "
            "Es un espacio para contar historias desde el groove: beats con textura, "
            "melodías oscuras, baterías con peso y una estética cruda, directa y emocional."
        )
        st.markdown(
            "Más que producir por producir, busco construir una identidad completa: "
            "portada, sonido, narrativa, referencias, arreglos e intención. Cada canción "
            "tiene que sentirse como una escena, una calle, una noche o una memoria."
        )

        st.divider()
        st.markdown("### Escúchame en las plataformas")
        st.markdown("")

        pc1, pc2 = st.columns(2, gap="medium")

        with pc1:
            st.link_button(
                "🎵  Spotify",
                "https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq?si=76fceaf982c049c5",
                use_container_width=True,
            )
            st.caption("Lanzamientos oficiales, colaboraciones y producciones en plataformas digitales.")

            st.markdown("")
            st.link_button(
                "☁️  SoundCloud",
                "https://soundcloud.com/sin-oficio-688647778",
                use_container_width=True,
            )
            st.caption("Demos, beats, ideas en proceso y material experimental.")

        with pc2:
            st.link_button(
                "▶️  YouTube",
                "https://www.youtube.com/@Pinedamusic.wav6",
                use_container_width=True,
            )
            st.caption("Live sessions, presentaciones, contenido visual y procesos de cada proyecto.")

            st.markdown("")
            st.link_button(
                "📸  Instagram",
                "https://www.instagram.com/pinedamusic.wav/?hl=es",
                use_container_width=True,
            )
            st.caption("Proceso creativo, reels, sesiones y momentos del día a día.")


# ───────────────────────────────────────────────────────
#  05 / REDES
# ───────────────────────────────────────────────────────
with tab_redes:
    st.caption("05 / LINKS")
    st.markdown("## Conecta conmigo en redes.")
    st.markdown("")

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        st.markdown("### Instagram")
        st.markdown("Fotos · Reels · Proceso creativo")
        st.link_button(
            "Ir a Instagram →",
            "https://www.instagram.com/pinedamusic.wav/?hl=es",
            use_container_width=True,
        )

    with c2:
        st.markdown("### Spotify")
        st.markdown("Lanzamientos · Música")
        st.link_button(
            "Ir a Spotify →",
            "https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq",
            use_container_width=True,
        )

    with c3:
        st.markdown("### YouTube")
        st.markdown("Videos · Sesiones en vivo")
        st.link_button(
            "Ir a YouTube →",
            "https://www.youtube.com/@Pinedamusic.wav6",
            use_container_width=True,
        )

    with c4:
        st.markdown("### SoundCloud")
        st.markdown("Beats · Demos · Ideas")
        st.link_button(
            "Ir a SoundCloud →",
            "https://soundcloud.com/sin-oficio-688647778",
            use_container_width=True,
        )


# ───────────────────────────────────────────────────────
#  FOOTER
# ───────────────────────────────────────────────────────
st.divider()
fc1, fc2 = st.columns(2)
fc1.caption("© 2026 — Juan David Pineda Ramirez")
fc2.caption("Músico · Productor · Beatmaker · Bajista")
