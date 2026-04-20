import streamlit as st
import pandas as pd
import feedparser
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Vinotinto Global 2026",
    page_icon="🇻🇪",
    layout="wide"
)

# 2. ESTILO CSS PARA ASEGURAR QUE EL MENÚ SE VEA (Fondo oscuro, letras claras)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #4a0e0e;
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .news-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
        margin-bottom: 15px;
    }
    a { color: #ffcc00 !important; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNCIÓN PARA OBTENER NOTICIAS REALES (RSS)
def obtener_noticias_reales():
    # Usamos el feed de una fuente deportiva que cubre atletas venezolanos
    url_feed = "https://www.liderendeportes.com/feed/" 
    feed = feedparser.parse(url_feed)
    noticias = []
    for entry in feed.entries[:10]: # Tomamos las últimas 10 noticias reales
        noticias.append({
            "Título": entry.title,
            "Link": entry.link,
            "Publicado": entry.published
        })
    return noticias

# 4. MENÚ LATERAL (CORREGIDO)
with st.sidebar:
    st.markdown("# 🏆 MENÚ")
    if os.path.exists("logo_vinotinto.png"):
        st.image("logo_vinotinto.png", use_container_width=True)
    else:
        st.markdown("<h1 style='text-align: center;'>🇻🇪</h1>", unsafe_allow_html=True)
    
    st.write("---")
    menu = st.radio(
        "SELECCIONE UNA CATEGORÍA:",
        ["🏠 Inicio / Noticias", "⚾ MLB Venezolanos", "⚽ Fútbol Nacional/Int.", "🏅 Polideportivo", "👩 Femenino"]
    )
    st.write("---")
    st.markdown("### Reflexiones de Willian Almenar")

# 5. LÓGICA DE PANTALLA PRINCIPAL
if menu == "🏠 Inicio / Noticias":
    st.title("🇻🇪 NOTICIAS EN VIVO - ATLETAS VENEZOLANOS")
    st.write(f"Actualizado al: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M')}")
    
    try:
        noticias = obtener_noticias_reales()
        for n in noticias:
            st.markdown(f"""
            <div class="news-card">
                <h4>{n['Título']}</h4>
                <p style='font-size: 0.8rem; color: #aaa;'>Publicado: {n['Publicado']}</p>
                <a href="{n['Link']}" target="_blank">Leer noticia completa →</a>
            </div>
            """, unsafe_allow_html=True)
    except:
        st.error("Hubo un problema al conectar con las noticias en vivo. Intenta refrescar la página.")

elif menu == "⚾ MLB Venezolanos":
    st.header("⚾ Seguimiento MLB (Datos Reales 2026)")
    st.write("Principales estrellas activas hoy:")
    st.table([
        {"Atleta": "Luis Arráez", "Equipo": "Padres", "Detalle": "Lucha por el título de bateo"},
        {"Atleta": "José Altuve", "Equipo": "Astros", "Detalle": "Líder en hits de la franquicia"},
        {"Atleta": "Anthony Santander", "Equipo": "Orioles", "Detalle": "Poder jononero activo"},
        {"Atleta": "William Contreras", "Equipo": "Brewers", "Detalle": "Receptor estelar"}
    ])

elif menu == "⚽ Fútbol Nacional/Int.":
    st.header("⚽ Fútbol Masculino")
    st.markdown("### 🌍 Legionarios Destacados")
    st.info("Próximos compromisos eliminatorias: Ver noticias en Inicio")
    st.table([
        {"Jugador": "Salomón Rondón", "Liga": "MX", "Club": "Pachuca"},
        {"Jugador": "Yeferson Soteldo", "Liga": "BRA", "Club": "Grêmio"},
        {"Jugador": "Yangel Herrera", "Liga": "ESP", "Club": "Girona"}
    ])

elif menu == "👩 Femenino":
    st.header("👩 Vinotinto Femenina")
    st.markdown("### 🏆 Representación Mundial")
    st.table([
        {"Jugadora": "Deyna Castellanos", "Club": "Bay FC (USA)"},
        {"Jugadora": "Oriana Altuve", "Club": "Betis (ESP)"},
        {"Jugadora": "Verónica Herrera", "Club": "Tenerife (ESP)"}
    ])

else:
    st.header(f"🏅 {menu}")
    st.write("Consulta la sección de noticias para resultados de atletismo, pesas y más.")
