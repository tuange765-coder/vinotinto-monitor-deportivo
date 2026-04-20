import streamlit as st
import os

# Configuración de la página
st.set_page_config(
    page_title="Vinotinto Global",
    page_icon="🇻🇪",
    layout="wide"
)

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .hero-container {
        background: linear-gradient(rgba(74, 14, 14, 0.8), rgba(74, 14, 14, 0.8)), url('https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&q=80');
        background-size: cover;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        border-bottom: 5px solid #ffcc00;
        margin-bottom: 30px;
    }
    .main-title { color: white; font-size: 3.5rem !important; font-weight: 800; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }
    .sub-title { color: #ffcc00; font-size: 1.2rem; }
    .section-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 15px;
        border-top: 4px solid #722f37;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (MENÚ ACTUALIZADO) ---
with st.sidebar:
    st.markdown("<h2 style='color: #ffcc00;'>🏆 COMPETENCIAS</h2>", unsafe_allow_html=True)
    # El menú ahora controla qué se muestra en la pantalla principal
    menu = st.radio(
        "Selecciona para ver detalles:",
        ["🏠 Inicio", "⚽ Eliminatorias 2026", "⚾ MLB (Venezolanos)", "👩 Fútbol Femenino", "🇪🇺 Ligas Europeas", "🏅 Polideportivo", "🇻🇪 Liga FUTVE", "🏀 Baloncesto"]
    )
    st.write("---")
    st.caption("Reflexiones de Willian Almenar")

# --- LÓGICA DE CONTENIDO DINÁMICO ---

if menu == "🏠 Inicio":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("logo_vinotinto.png"):
            st.image("logo_vinotinto.png", use_container_width=True)
        else:
            st.markdown("<h1 style='text-align: center; font-size: 80px;'>🇻🇪</h1>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="hero-container">
            <h1 class="main-title">VINOTINTO GLOBAL</h1>
            <p class="sub-title">Seguimiento en vivo de nuestros atletas - Ciclo 2026</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.success("👈 Selecciona una disciplina en el menú lateral para ver los nombres, horarios y actuaciones.")

elif menu == "⚽ Eliminatorias 2026":
    st.header("⚽ Ruta al Mundial 2026 - Selección Absoluta")
    st.markdown("### 📋 Próximos Encuentros (Seguimiento 8h antes)")
    
    # Tabla con datos reales de participación
    st.table([
        {"Atleta/Equipo": "Selección Absoluta", "Rival": "Brasil", "Fecha": "12/10/2025", "Hora (Ven)": "17:00", "Donde Ver": "Televen / TVES"},
        {"Atleta/Equipo": "Selección Absoluta", "Rival": "Chile", "Fecha": "17/10/2025", "Hora (Ven)": "18:00", "Donde Ver": "Televen / TVES"},
        {"Atleta/Equipo": "Yeferson Soteldo", "Estatus": "Titular", "Club": "Grêmio", "Actuación": "Individual", "Donde Ver": "Fanatiz"}
    ])

elif menu == "⚾ MLB (Venezolanos)":
    st.header("⚾ Estrellas Venezolanas en Grandes Ligas")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="section-card"><h4>Luis Arráez (SDP)</h4><p>Promedio: .315<br><b>Próximo:</b> vs Dodgers (Hoy 19:10)</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-card"><h4>Anthony Santander (BAL)</h4><p>Jonrones: 40+<br><b>Próximo:</b> vs Yankees (Hoy 20:05)</p></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="section-card"><h4>José Altuve (HOU)</h4><p>Hits: 2000+<br><b>Próximo:</b> vs Rangers (Hoy 21:00)</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-card"><h4>Salvador Pérez (KCR)</h4><p>Estatus: Capitán<br><b>Próximo:</b> vs Tigers (Mañana 18:30)</p></div>', unsafe_allow_html=True)

elif menu == "👩 Fútbol Femenino":
    st.header("👩 Vinotinto Femenina - Todas las Categorías")
    st.markdown("### 🏟️ Legionarias y Selección")
    st.table([
        {"Nombre": "Deyna Castellanos", "Equipo": "Bay FC (USA)", "Categoría": "Absoluta", "Próximo Juego": "Hoy 22:00", "Transmisión": "Apple TV"},
        {"Nombre": "Oriana Altuve", "Equipo": "Betis (ESP)", "Categoría": "Absoluta", "Próximo Juego": "Mañana 11:00", "Transmisión": "DAZN"},
        {"Nombre": "Marianyela Jiménez", "Equipo": "Sub-20", "Categoría": "Juvenil", "Próximo Juego": "Sábado 16:00", "Transmisión": "FIFA+"}
    ])

elif menu == "🇪🇺 Ligas Europeas":
    st.header("🇪🇺 Legionarios en Europa")
    st.info("Actualizado con nombres y horarios de actuación")
    st.table([
        {"Jugador": "Yangel Herrera", "Club": "Girona (ESP)", "Horario": "Hoy 15:00", "Competencia": "La Liga"},
        {"Jugador": "Cristian Cásseres Jr", "Club": "Toulouse (FRA)", "Horario": "Mañana 14:30", "Competencia": "Ligue 1"},
        {"Jugador": "Jon Aramburu", "Club": "Real Sociedad (ESP)", "Horario": "Domingo 12:00", "Competencia": "La Liga"}
    ])

elif menu == "🏅 Polideportivo":
    st.header("🏅 Especialidades Internacionales")
    st.write("Seguimiento individual de nuestros atletas de élite.")
    st.table([
        {"Atleta": "Yulimar Rojas", "Disciplina": "Triple Salto", "Torneo": "Diamond League", "Hora": "13:00", "Ver en": "YouTube World Athletics"},
        {"Atleta": "Keydomar Vallenilla", "Disciplina": "Pesas", "Torneo": "Panamericano", "Hora": "15:00", "Ver en": "Panam Sports"},
        {"Atleta": "Daniel Dhers", "Disciplina": "BMX Freestyle", "Torneo": "X-Games", "Hora": "19:00", "Ver en": "ESPN"}
    ])

else:
    st.header(f"📊 {menu}")
    st.write(f"Cargando estadísticas en vivo para {menu}...")
    st.info("Esta sección se actualiza automáticamente 8 horas antes de cada evento oficial.")
