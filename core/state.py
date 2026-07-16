import streamlit as st

def initialize_state(folders, reports):
    """Initializes global session states with absolute parity to React state structures."""
    if "is_logged_in" not in st.session_state:
        st.session_state.is_logged_in = True  # True by default for mock preview as in React
        
    if "active_page" not in st.session_state:
        st.session_state.active_page = "accueil"
        
    if "language" not in st.session_state:
        st.session_state.language = "fr"
        
    if "reports" not in st.session_state:
        st.session_state.reports = reports
        
    if "folders" not in st.session_state:
        st.session_state.folders = folders
        
    if "open_tabs" not in st.session_state:
        st.session_state.open_tabs = [{"id": "list", "title": "Liste des rapports", "type": "list"}]
        
    if "active_tab_id" not in st.session_state:
        st.session_state.active_tab_id = "list"