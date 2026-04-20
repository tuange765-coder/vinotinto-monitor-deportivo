import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Vinotinto Global", page_icon="🇻🇪", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTable { background-color: #1f2937; border-radius: 10px; }
    .atleta-card {
        background: #2d0a0a;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ DE COMPETENCIAS ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/48/Flag_of_Venezuela.svg", width=100)
    st.title("Monitor Deportivo")
    menu = st.selectbox(
        "Seleccione Disciplina:",
        ["Portada", "Fútbol Masculino (Legionarios)", "Fútbol Femenino (Mundial)", "MLB (Grandes Ligas)", "Baloncesto (Mundial)", "Polideportivo (Olímpicos)", "Liga FUTVE"]
    )
    st.write("---")
    st.caption("Reflexiones de Willian Almenar © 2026")

# --- LÓGICA DE CONTENIDO ---

if menu == "Portada":
    st.title("🇻🇪 BIENVENIDO A VINOTINTO GLOBAL")
    st.subheader("El registro más completo de atletas venezolanos en el mundo.")
    if os.path.exists("logo_vinotinto.png"):
        st.image("logo_vinotinto.png", width=300)
    st.info("Utilice el menú de la izquierda para desplegar la lista de atletas activos por disciplina.")

elif menu == "Fútbol Masculino (Legionarios)":
    st.header("⚽ Legionarios Vinotinto (Europa, América y Asia)")
    st.write("Seguimiento de jugadores activos en ligas internacionales.")
    
    st.table([
        {"Jugador": "Salomón Rondón", "Club": "Pachuca (MEX)", "Estatus": "Activo - Goleador"},
        {"Jugador": "Yeferson Soteldo", "Club": "Grêmio (BRA)", "Estatus": "Activo - Titular"},
        {"Jugador": "Yangel Herrera", "Club": "Girona (ESP)", "Estatus": "Activo - La Liga"},
        {"Jugador": "Jefferson Savarino", "Club": "Botafogo (BRA)", "Estatus": "Activo - Titular"},
        {"Jugador": "Jhonder Cádiz", "Club": "León (MEX)", "Estatus": "Activo - Goleador"},
        {"Jugador": "Jon Aramburu", "Club": "Real Sociedad (ESP)", "Estatus": "Activo - Promesa"},
        {"Jugador": "Telasco Segovia", "Club": "Casa Pia (POR)", "Estatus": "Activo - Europa"}
    ])

elif menu == "Fútbol Femenino (Mundial)":
    st.header("👩 Guerreras Vinotinto (Todas las Categorías)")
    st.write("Venezolanas destacadas en el fútbol femenino mundial.")
    
    st.table([
        {"Jugadora": "Deyna Castellanos", "Club": "Bay FC (USA)", "Liga": "NWSL"},
        {"Jugadora": "Oriana Altuve", "Club": "Real Betis (ESP)", "Liga": "Liga F"},
        {"Jugadora": "Mariana Speckmaier", "Club": "Wellington Phoenix", "Liga": "A-League"},
        {"Jugadora": "Ysaura Viso", "Club": "Colo-Colo (CHI)", "Liga": "Primera División"},
        {"Jugadora": "Verónica Herrera", "Club": "Costa Adeje Tenerife", "Liga": "Liga F"},
        {"Jugadora": "Bárbara Olivieri", "Club": "Houston Dash (USA)", "Liga": "NWSL"}
    ])

elif menu == "MLB (Grandes Ligas)":
    st.header("⚾ Venezolanos en la MLB")
    st.write("Nuestras estrellas en el mejor béisbol del mundo.")
    
    st.table([
        {"Nombre": "Luis Arráez", "Equipo": "San Diego Padres", "Rol": "Infielder"},
        {"Nombre": "José Altuve", "Equipo": "Houston Astros", "Rol": "Segunda Base"},
        {"Nombre": "Anthony Santander", "Equipo": "Baltimore Orioles", "Rol": "Outfielder"},
        {"Nombre": "Salvador Pérez", "Equipo": "Kansas City Royals", "Rol": "Receptor"},
        {"Nombre": "William Contreras", "Equipo": "Milwaukee Brewers", "Rol": "Receptor"},
        {"Nombre": "Jackson Chourio", "Equipo": "Milwaukee Brewers", "Rol": "Outfielder"},
        {"Nombre": "Pablo López", "Equipo": "Minnesota Twins", "Rol": "Lanzador Abridor"}
    ])

elif menu == "Baloncesto (Mundial)":
    st.header("🏀 Baloncesto: Venezolanos por el Mundo")
    st.table([
        {"Jugador": "Michael Carrera", "Equipo": "Movistar Estudiantes (ESP)", "Liga": "LEB Oro"},
        {"Jugador": "Fabrizio Pugliatti", "Equipo": "Stella Azzurra (ITA)", "Liga": "Serie B"},
        {"Jugador": "Gregory Vargas", "Equipo": "Gladiadores", "Liga": "SPB / BCLA"},
        {"Jugador": "Garly Sojo", "Estatus": "Memoria Eterna", "Nota": "Referente Vinotinto"}
    ])

elif menu == "Polideportivo (Olímpicos)":
    st.header("🏅 Atletas de Élite - Diversas Disciplinas")
    st.write("Venezolanos compitiendo en el ciclo olímpico e internacional.")
    
    st.table([
        {"Atleta": "Yulimar Rojas", "Disciplina": "Triple Salto", "Estatus": "Campeona Mundial"},
        {"Atleta": "Keydomar Vallenilla", "Disciplina": "Halterofilia", "Estatus": "Medallista Olímpico"},
        {"Atleta": "Julio Mayora", "Disciplina": "Halterofilia", "Estatus": "Medallista Olímpico"},
        {"Atleta": "Daniel Dhers", "Disciplina": "BMX Freestyle", "Estatus": "Leyenda Activa"},
        {"Atleta": "Rubén Limardo", "Disciplina": "Esgrima", "Estatus": "Campeón Olímpico"},
        {"Atleta": "Anriquelis Barrios", "Disciplina": "Judo", "Estatus": "Élite Mundial"},
        {"Atleta": "Yohandri Granado", "Disciplina": "Taekwondo", "Estatus": "Clasificado"}
    ])

elif menu == "Liga FUTVE":
    st.header("🇻🇪 Fútbol Nacional - Liga FUTVE")
    st.write("Equipos y jugadores destacados localmente.")
    st.table([
        {"Equipo": "Deportivo Táchira", "Sede": "San Cristóbal", "Estatus": "Primera División"},
        {"Equipo": "Caracas FC", "Sede": "Caracas", "Estatus": "Primera División"},
        {"Equipo": "Academia Puerto Cabello", "Sede": "Carabobo", "Estatus": "Primera División"},
        {"Equipo": "Portuguesa FC", "Sede": "Acarigua", "Estatus": "Primera División"}
    ])
