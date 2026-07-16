import streamlit as st

def render_sidebar():
    """Navigation sidebar with authentic custom branding."""
    with st.sidebar:
        st.markdown(
            """
            <div style='text-align: center; margin-bottom: 20px;'>
                <h1 style='color: #E85F1E; margin-bottom: -5px; font-size: 24px; font-family: "Cormorant Garamond", serif; letter-spacing: 2px;'>HERMÈS</h1>
                <span style='font-family: "Cormorant Garamond", serif; font-size: 10px; tracking: 0.25em; color: gray;'>PARIS</span>
                <p style='font-size: 18px; margin-top: 5px; color: #292524;'>Infocentre</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.divider()
        
        pages = {
            "accueil": "🏠 Accueil",
            "liste_rapports": "📋 Liste des rapports",
            "suivi_exploit": "📈 Suivi de l'exploit",
            "open_to_buy": "🛍️ Open to buy",
            "password_change": "🔒 Changer votre mot de passe"
        }
        


        
        for p_id, label in pages.items():
            is_active = st.session_state.active_page == p_id
            if st.button(label, key=f"nav_btn_{p_id}", use_container_width=True,
                         type="primary" if is_active else "secondary"):
                st.session_state.active_page = p_id
                st.rerun()
                
        st.divider()
        st.selectbox("Langue", ["Français (fr)", "English (en)", "Italiano (it)", "Español (es)"], key="language_selector")
        st.caption("Production Manager • v5.2.1")