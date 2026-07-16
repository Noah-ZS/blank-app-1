import streamlit as st
from core.state import initialize_state
from components.sidebar import render_sidebar
from services.db_client import load_folders_and_reports

# Lazy page imports
from views.accueil import render_accueil
from views.liste_rapports import render_liste_rapports
from views.suivi_exploit import render_suivi_exploit
from views.open_to_buy import render_open_to_buy
from views.password_change import render_password_change

st.set_page_config(
    page_title="Hermès Infocentre",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Render Global Styling overrides
st.markdown("""
<style>
    .hermes-text { color: #E85F1E; font-family: 'Cormorant Garamond', serif; }
</style>
""", unsafe_allow_html=True)

# Load original catalog configurations matching types.ts
folders, reports = load_folders_and_reports()
initialize_state(folders, reports)

def render_login_view():
    """Beautiful central login gate."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <div style='text-align: center; margin-bottom: 20px;'>
                <h1 class='hermes-text' style='font-size: 3.5rem; letter-spacing: 3px;'>HERMÈS</h1>
                <p style='color: gray;'>Portail d'Intelligence d'Affaires & Gestion de la Performance</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        with st.form("login_gateway"):
            u_email = st.text_input("Identifiant professionnel", value="neeraj@datasoluva.com")
            u_pw = st.text_input("Mot de passe", type="password", value="password")
            remember = st.checkbox("Se souvenir de moi", value=True)
            
            if st.form_submit_button("Se connecter", use_container_width=True):
                if u_email and u_pw:
                    st.session_state.is_logged_in = True
                    st.session_state.active_page = "accueil"
                    st.rerun()

def main():
    if not st.session_state.is_logged_in:
        render_login_view()
    else:
        render_sidebar()
        
        # Route to views
        page = st.session_state.active_page
        if page == "accueil":
            render_accueil()
        elif page == "liste_rapports":
            render_liste_rapports()
        elif page == "suivi_exploit":
            render_suivi_exploit()
        elif page == "open_to_buy":
            render_open_to_buy()
        elif page == "password_change":
            render_password_change()

if __name__ == "__main__":
    main()