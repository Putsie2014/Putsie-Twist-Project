import streamlit as st

# Pagina configuratie voor een console-look
st.set_page_config(
    page_title="Project Chimera OS",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS voor het "Switch 2" gevoel en thema's
def apply_theme(theme_color):
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {theme_color};
        }}
        .game-card {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: 0.3s;
        }}
        .game-card:hover {{
            border: 2px solid #FF4B4B;
            transform: scale(1.05);
        }}
        </style>
    """, unsafe_allow_html=True)

# Thema selectie (voor je Twist-Caske integratie later)
theme = st.sidebar.selectbox("Selecteer Thema", ["Donker", "Zelda Goud", "Metroid Blauw", "Klassiek Rood"])
themes = {
    "Donker": "#121212",
    "Zelda Goud": "#2D2A1E",
    "Metroid Blauw": "#0A192F",
    "Klassiek Rood": "#8B0000"
}
apply_theme(themes[theme])

# Header
st.title("🎮 Project Chimera III")
st.subheader(f"Systeemmodus: Handheld | Thema: {theme}")

# Game Grid (Je "Switch" menu)
cols = st.columns(4)

games = [
    {"name": "Zelda: Tears of the Kingdom", "icon": "🛡️"},
    {"name": "Metroid Prime 4", "icon": "🚀"},
    {"name": "Elden Ring", "icon": "💍"},
    {"name": "Hollow Knight", "icon": "⚔️"}
]

for i, game in enumerate(games):
    with cols[i % 4]:
        st.markdown(f"""
            <div class="game-card">
                <h1>{game['icon']}</h1>
                <p><b>{game['name']}</b></p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Start {game['name']}", key=i):
            st.success(f"Laden van {game['name']} via ChimeraOS...")

# Systeem status onderaan (Data vanuit de Ryzen 9 APU)
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("CPU Temp", "42°C", "-2°C")
col2.metric("Batterij", "88%", "Laden (65W)")
col3.metric("FPS (Menu)", "120", "VRR Active")
