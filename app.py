import streamlit as st
import pandas as pd
import feedparser
import os
import json

# ============================================================
# CONFIGURACIÓN
# ============================================================
st.set_page_config(
    page_title="Vinotinto Global 2026",
    page_icon="🇻🇪",
    layout="wide"
)

st.warning(
    "⚠️ **Aviso:** Desactiva la traducción automática de tu navegador "
    "(Google Translate, etc.) para evitar errores críticos."
)

st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #4a0e0e; color: white; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stApp { background-color: #0e1117; color: white; }
    .news-card {
        background-color: #1f2937; padding: 20px; border-radius: 10px;
        border-left: 5px solid #ffcc00; margin-bottom: 15px;
    }
    a { color: #ffcc00 !important; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)


# ============================================================
# FUNCIÓN RSS (ÚNICA FUENTE DINÁMICA REAL DISPONIBLE)
# ============================================================
@st.cache_data(ttl=300)
def obtener_noticias_reales():
    url_feed = "https://www.liderendeportes.com/feed/"
    try:
        feed = feedparser.parse(url_feed)
        noticias = []
        for entry in feed.entries[:15]:
            noticias.append({
                "Título": entry.title,
                "Link": entry.link,
                "Publicado": getattr(entry, 'published', 'Fecha no disponible')
            })
        return noticias
    except Exception:
        return []


# ============================================================
# MENÚ LATERAL
# ============================================================
with st.sidebar:
    st.markdown("# 🏆 MENÚ")
    if os.path.exists("logo_vinotinto.png"):
        st.image("logo_vinotinto.png", use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>🇻🇪</h1>", unsafe_allow_html=True)

    st.write("---")
    menu = st.radio(
        "SELECCIONE UNA CATEGORÍA:",
        [
            "🏠 Inicio / Noticias",
            "⚾ MLB Venezolanos",
            "⚾ Béisbol Venezolano (LVBP)",
            "⚽ Fútbol Internacional",
            "⚽ Fútbol Nacional (FUTVE)",
            "🏅 Polideportivo"
        ]
    )
    st.write("---")
    st.markdown("### Reflexiones de Willian Almenar")


# ============================================================
# 1. NOTICIAS (RSS EN VIVO — se actualiza cada 5 minutos)
# ============================================================
if menu == "🏠 Inicio / Noticias":
    st.title("🇻🇪 NOTICIAS EN VIVO - ATLETAS VENEZOLANOS")
    st.write(f"Actualizado al: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M')}")
    st.caption("Fuente: RSS de Líder en Deportes. Se actualiza automáticamente cada 5 minutos.")

    noticias = obtener_noticias_reales()
    if noticias:
        for n in noticias:
            st.markdown(f"""
            <div class="news-card" translate="no">
                <h4>{n['Título']}</h4>
                <p style='font-size: 0.8rem; color: #aaa;'>Publicado: {n['Publicado']}</p>
                <a href="{n['Link']}" target="_blank">Leer noticia completa →</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No se pudieron cargar noticias desde el feed RSS en este momento.")


# ============================================================
# 2. MLB VENEZOLANOS
# ============================================================
elif menu == "⚾ MLB Venezolanos":
    st.header("⚾ Venezolanos en MLB")
    st.caption("Datos verificables de reportes de prensa. NO es tiempo real de partidos en curso.")

    st.subheader("🏆 Título de Bateo — Liga Nacional (reporte del 09/09/2026)")
    st.markdown("""
    Según la Agencia Venezolana de Noticias (AVN) [citation:26]:
    - **Luis Arráez** lideraba el bateo de la Liga Nacional y de toda la MLB con promedio de **.317**.
    - Alcanzó los **1.200 hits** en su carrera, convirtiéndose en el trigésimo venezolano en lograrlo.
    - Acumulaba 172 imparables en la temporada (136 con Gigantes, 36 con Filis).
    """)

    st.subheader("📋 Venezolanos debutantes en MLB 2026 (reporte del 24/05/2026)")
    st.markdown("Según Venezolana de Televisión (VTV) [citation:19]:")
    st.table([
        {"Jugador": "Jedixson Páez (P)", "Equipo": "Medias Blancas", "Debut": "26/03/2026"},
        {"Jugador": "Jeferson Quero (C)", "Equipo": "Cerveceros", "Debut": "29/03/2026"},
        {"Jugador": "José Franco (P)", "Equipo": "Rojos", "Debut": "30/03/2026"},
        {"Jugador": "José Fernández (SS)", "Equipo": "D-backs", "Debut": "31/03/2026"},
        {"Jugador": "Yohendrick Piñango (OF)", "Equipo": "Azulejos", "Debut": "26/04/2026"},
        {"Jugador": "Jesús Rodríguez (C)", "Equipo": "Gigantes", "Debut": "04/05/2026"},
        {"Jugador": "Omar Martínez (C)", "Equipo": "Angelinos", "Debut": "08/05/2026"},
        {"Jugador": "Gabriel González (OF)", "Equipo": "Mellizos", "Debut": "22/05/2026"},
        {"Jugador": "Víctor Bericoto (OF)", "Equipo": "Gigantes", "Debut": "22/05/2026"},
        {"Jugador": "Pedro Ramírez (IF)", "Equipo": "Cachorros", "Debut": "23/05/2026"}
    ])

    st.info("💡 **Para estadísticas en tiempo real:** MLB StatsAPI (statsapi.mlb.com) es pública y gratuita, pero no filtra por nacionalidad. Debes obtener la lista de IDs de jugadores venezolanos y consultar sus stats individualmente. Consulta también [MLB.com](https://www.mlb.com) o [Baseball-Reference](https://www.baseball-reference.com).")


# ============================================================
# 3. LVBP
# ============================================================
elif menu == "⚾ Béisbol Venezolano (LVBP)":
    st.header("⚾ Liga Venezolana de Béisbol Profesional (LVBP)")
    st.caption("Datos de reportes de prensa. NO es tiempo real.")

    st.subheader("📊 Tabla de Posiciones (reporte del 19/10/2026)")
    st.markdown("Según La iguana TV [citation:25]:")
    st.table([
        {"Pos": "1", "Equipo": "Tigres de Aragua", "Récord": "5-1"},
        {"Pos": "2", "Equipo": "Cardenales de Lara", "Récord": "4-1"},
        {"Pos": "3", "Equipo": "Bravos de Margarita", "Récord": "4-1"},
        {"Pos": "4", "Equipo": "Caribes de Anzoátegui", "Récord": "4-2"},
        {"Pos": "5", "Equipo": "Leones del Caracas", "Récord": "2-4"},
        {"Pos": "6", "Equipo": "Águilas del Zulia", "Récord": "2-4"},
        {"Pos": "7", "Equipo": "Tiburones de La Guaira", "Récord": "2-4"},
        {"Pos": "8", "Equipo": "Navegantes del Magallanes", "Récord": "0-6"}
    ])

    st.subheader("📱 Fuentes para seguimiento en vivo")
    st.markdown("""
    - **App oficial LVBP:** Actualizaciones minuto a minuto, tabla de posiciones y estadísticas en tiempo real [citation:6].
    - **Beisbol VE:** App con scores en vivo, boxscores y play-by-play de la temporada 2026-2027 .
    - **Web:** [LVBP.com](https://lvbp.com) o [Meridiano.net](https://meridiano.net)
    """)
    st.info("💡 No existe una API pública oficial de la LVBP. El scraping de sitios como Flashscore o Meridiano es posible pero frágil y puede violar términos de uso.")


# ============================================================
# 4. FÚTBOL INTERNACIONAL
# ============================================================
elif menu == "⚽ Fútbol Internacional":
    st.header("⚽ Fútbol Internacional - Selecciones Venezolanas")
    st.caption("Datos de reportes de prensa. NO es tiempo real.")

    st.subheader("👩 Vinotinto Femenina Sub-17 — Mundial 2026")
    st.markdown("""
    Según Diario de Los Andes y Meridiano [citation:30][citation:16]:
    - **Venezuela 1 - 0 Alemania** (28/10/2026): Gol de Diana Bravo. La Vinotinto clasificó a cuartos de final del Mundial Sub-17 Femenino en Marruecos, eliminando a la vigente campeona de Europa.
    """)

    st.subheader("👨 Vinotinto Masculina — Amistosos Noviembre 2026")
    st.markdown("""
    Según reportes de prensa:
    - **14/11/2026:** Venezuela vs País Vasco (San Mamés, Bilbao)
    - **17/11/2026:** Venezuela vs Rusia (FC Krasnodar, Rusia)
    """)

    st.subheader("📱 Fuentes para calendario y resultados en vivo")
    st.markdown("""
    - **Tribuna.com:** Calendario y resultados de la Selección de Venezuela, actualizado en tiempo real [citation:4].
    - **365Scores:** Resultados en vivo, alineaciones y estadísticas de ligas y selecciones.
    - **FVF:** [fvf.com.ve](https://www.fvf.com.ve)
    """)
    st.info("💡 Para horarios exactos y resultados en vivo de todas las categorías (Sub-15, Sub-17, Sub-20, mayores), la fuente más confiable es la cuenta oficial de la FVF en redes o 365Scores.")


# ============================================================
# 5. FÚTBOL NACIONAL (FUTVE)
# ============================================================
elif menu == "⚽ Fútbol Nacional (FUTVE)":
    st.header("⚽ Liga FUTVE - Fase Final Clausura 2026")
    st.caption("Datos de reportes de prensa. NO es tiempo real.")

    st.subheader("📊 Cuadrangulares — Tabla de Posiciones (reporte del 26/10/2026)")
    st.markdown("Según 365Scores [citation:3]:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Grupo A**")
        st.table([
            {"Pos": "1", "Equipo": "Carabobo", "PJ": "1", "Pts": "3"},
            {"Pos": "2", "Equipo": "Metropolitanos", "PJ": "1", "Pts": "1"},
            {"Pos": "3", "Equipo": "La Guaira", "PJ": "1", "Pts": "1"},
            {"Pos": "4", "Equipo": "Portuguesa", "PJ": "1", "Pts": "0"}
        ])
    with col2:
        st.markdown("**Grupo B**")
        st.table([
            {"Pos": "1", "Equipo": "Puerto Cabello", "PJ": "1", "Pts": "3"},
            {"Pos": "2", "Equipo": "Táchira", "PJ": "1", "Pts": "3"},
            {"Pos": "3", "Equipo": "Caracas", "PJ": "1", "Pts": "0"},
            {"Pos": "4", "Equipo": "Monagas", "PJ": "1", "Pts": "0"}
        ])

    st.subheader("📅 Partidos de la Fecha 2 (27/10/2026)")
    st.markdown("""
    - **Puerto Cabello vs Caracas** — Estadio La Bombonerita [citation:7]
    - **Táchira vs Monagas** — Estadio Polideportivo de Pueblo Nuevo, 20:30 hs [citation:15]
    """)

    st.subheader("📱 Fuentes para resultados en vivo")
    st.markdown("""
    - **365Scores:** Sigue resultados en vivo, estadísticas y alineaciones de la Liga FUTVE [citation:3][citation:7].
    - **App Liga FUTVE:** Transmisión y resultados oficiales.
    - **Web:** [ligafutve.org](https://ligafutve.org)
    """)
    st.info("💡 No hay API pública gratuita de la Liga FUTVE. 365Scores ofrece la cobertura en vivo más completa, pero no expone una API pública para integración directa.")


# ============================================================
# 6. POLIDEPORTIVO
# ============================================================
else:  # 🏅 Polideportivo
    st.header("🏅 Polideportivo")
    st.caption("Información verificable disponible. NO hay horarios en tiempo real unificados.")

    st.subheader("🏃 Atletismo")
    st.markdown("""
    Según Correo del Orinoco [citation:27]:
    - **Diego Vera:** Mejor tiempo (5:50) en aguas abiertas de los Juegos Centroamericanos y del Caribe Santo Domingo 2026.
    """)

    st.subheader("🥋 Judo")
    st.markdown("""
    Según Correo del Orinoco [citation:27]:
    - **Karen León:** Medalla de oro en la Copa Centroamericana y del Caribe Senior.
    """)

    st.subheader("🤸 Gimnasia Rítmica")
    st.markdown("""
    Según Correo del Orinoco [citation:27]:
    - **Susana Valbuena:** Bronce en el Grand Prix Internacional de Gimnasia Rítmica en Marbella, España.
    """)

    st.subheader("🎯 Tiro Olímpico")
    st.markdown("""
    Según libro de resultados de la Federación Venezolana de Tiro [citation:20]:
    - **Nicole Saavedra:** Primer lugar en Pistola 25m Femenino (Precisión + Rápida), 1era Válida Nacional 2026.
    """)

    st.subheader("📱 Fuentes para horarios en tiempo real")
    st.markdown("""
    No existe una API unificada para todos los deportes. Consulta directamente:
    - **Comité Olímpico Venezolano:** [cov.org.ve](https://cov.org.ve)
    - **Federación Venezolana de Atletismo:** [fva.org.ve](https://fva.org.ve)
    - **Ministerio del Deporte:** [mindeporte.gob.ve](https://www.mindeporte.gob.ve)
    - **Meridiano.net** y **Líder en Deportes** para cobertura de eventos multideportivos.
    """)
    st.info("💡 Los horarios de participación de atletas venezolanos en deportes individuales se publican típicamente en las cuentas de las federaciones y en la prensa deportiva el mismo día del evento, no en una API centralizada.")
