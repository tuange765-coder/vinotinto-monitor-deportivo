import streamlit as st
import os

# Configuración de la página
st.set_page_config(
    page_title="Vinotinto Global",
    page_icon="🇻🇪",
    layout="wide"
)

# Estilos CSS para que sea "hermosa y llamativa"
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .hero-container {
        background: linear-gradient(rgba(74, 14, 14, 0.8), rgba(74, 14, 14, 0.8)), url('https://images.unsplash.com/photo-1574629810360-7efbbe195018?auto=format&fit=crop&q=80');
        background-size: cover;
        padding: 60px;
        border-radius: 20px;
        text-align: center;
        border-bottom: 5px solid #ffcc00;
        margin-bottom: 40px;
    }
    .main-title {
        color: white;
        font-size: 4rem !important;
        font-weight: 800;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        margin-bottom: 0px;
    }
    .sub-title {
        color: #ffcc00;
        font-size: 1.5rem;
        font-weight: 400;
    }
    .section-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 15px;
        border-top: 4px solid #722f37;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# BARRA LATERAL - MENÚ DE COMPETENCIAS
with st.sidebar:
    st.markdown("<h2 style='color: #ffcc00;'>🏆 COMPETENCIAS</h2>", unsafe_allow_html=True)
    menu = st.radio(
        "Selecciona un torneo:",
        ["Inicio", "Eliminatorias 2026", "MLB (Venezolanos)", "Fútbol Femenino", "Ligas Europeas", "Otras Disciplinas", "Liga FUTVE", "Baloncesto"]
    )
    st.write("---")
    st.caption("Reflexiones de Willian Almenar")

# PANTALLA DE INICIO
if menu == "Inicio":
    # Fila para el Logo y Título
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Aquí se agrega el logo de la vinotinto
        if os.path.exists("logo_vinotinto.png"):
            st.image("logo_vinotinto.png", use_container_width=True)
        else:
            # Si no has subido la imagen aún, mostrará este escudo grande
            st.markdown("<h1 style='text-align: center; font-size: 100px;'>🇻🇪</h1>", unsafe_allow_html=True)

    # Hero Banner
    st.markdown(f"""
        <div class="hero-container">
            <h1 class="main-title">VINOTINTO GLOBAL</h1>
            <p class="sub-title">El latido del deporte venezolano en 2026</p>
        </div>
        """, unsafe_allow_html=True)

    # Menú visual de acceso rápido
    st.markdown("### 🏟️ Vista General")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="section-card"><h3>⚽ Fútbol</h3><p>Camino al Mundial 2026</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="section-card"><h3>⚾ Béisbol</h3><p>Nuestras estrellas en MLB</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="section-card"><h3>🏀 Otros</h3><p>Baloncesto y más...</p></div>', unsafe_allow_html=True)

# PÁGINAS DE COMPETENCIAS
elif menu == "Eliminatorias 2026":
    st.header("⚽ Eliminatorias Sudamericanas - Masculino Absoluto")
    st.info("Calendario de seguimiento con antelación de 8 horas")
    st.table({
        "Atleta/Equipo": ["Vinotinto Absoluta", "Yeferson Soteldo", "Salomón Rondón"],
        "Evento": ["vs Brasil", "vs Argentina", "vs Uruguay"],
        "Horario (Ven)": ["17:00", "19:00", "18:00"],
        "Transmisión": ["Televen / TVES", "Televen / TVES", "Televen / TVES"]
    })

elif menu == "MLB (Venezolanos)":
    st.header("⚾ Venezolanos en las Mayores")
    st.write("Seguimiento diario de nuestras estrellas en la Gran Carpa.")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Luis Arráez (Padres)", value=".315 AVG", delta="Líder Bateo")
        st.write("**Próximo juego:** vs Dodgers (19:10)")
    with col_b:
        st.metric(label="José Altuve (Astros)", value="15 HR", delta="Actuación Individual")
        st.write("**Próximo juego:** vs Yankees (20:05)")

elif menu == "Fútbol Femenino":
    st.header("⚽ Vinotinto Femenina - Todas las Categorías")
    st.write("Seguimiento de nuestras guerreras en el exterior y selección.")
    st.success("Actuación destacada: Deyna Castellanos (Bay FC)")
    st.table({
        "Jugadora": ["Deyna Castellanos", "Oriana Altuve", "Joemar Guarecuco"],
        "Liga / Categoría": ["NWSL (USA)", "Liga F (España)", "Selección Sub-20"],
        "Próxima Actuación": ["Hoy 21:00", "Mañana 12:00", "Sábado 15:00"],
        "Estatus": ["Titular", "Convocada", "Entrenamiento"]
    })

elif menu == "Ligas Europeas":
    st.header("🇪🇺 Venezolanos en Europa")
    st.write("Cronograma de legionarios en ligas internacionales.")
    st.table({
        "Jugador": ["Yangel Herrera", "Jhonder Cádiz", "Darwin Machís"],
        "Club": ["Girona (ESP)", "León (MEX)", "Real Valladolid (ESP)"],
        "Competición": ["La Liga", "Liga MX", "La Liga"],
        "Horario": ["15:00", "22:00", "14:00"]
    })

elif menu == "Otras Disciplinas":
    st.header("🏅 Polideportivo Internacional")
    st.write("Venezolanos en Atletismo, Pesas, BMX y más.")
    st.info("Seguimiento especial: Clasificatorios Olímpicos y Mundiales")
    st.table({
        "Atleta": ["Yulimar Rojas", "Keydomar Vallenilla", "Daniel Dhers"],
        "Especialidad": ["Triple Salto", "Pesas", "BMX Freestyle"],
        "Evento": ["Diamond League", "Panamericano", "X-Games"],
        "Hora Local": ["13:30", "16:00", "18:45"]
    })

else:
    st.header(f"📊 Información sobre {menu}")
    st.write("Sección en desarrollo para la temporada 2026. Datos actualizados cada 8 horas.")
