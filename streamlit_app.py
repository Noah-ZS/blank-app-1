
import streamlit as st
import pandas as pd
 
# 1. Configuration Globale
st.set_page_config(page_title="Portail Hermès", layout="wide", initial_sidebar_state="expanded")
 
# Gestion de la navigation (Système de routage interne)
if 'page_actuelle' not in st.session_state:
    st.session_state.page_actuelle = "Accueil"
 
def naviguer_vers(page):
    st.session_state.page_actuelle = page
 
# 2. Données Fictives
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Numéro": ["CMD-1024", "CMD-1025", "CMD-1026", "CMD-1027"],
        "Date": ["01/07/2026", "02/07/2026", "02/07/2026", "03/07/2026"],
        "Statut": ["Expédié", "En attente", "Expédié", "Annulé"],
        "Montant": ["1 250 €", "3 400 €", "890 €", "150 €"]
    })
 
# ==========================================
# 3. BARRE LATÉRALE (L'ancre corporative)
# ==========================================
st.sidebar.markdown("## 🐴 **HERMÈS** GROUP")
st.sidebar.markdown("*Portail Sécurisé*")
st.sidebar.markdown("---")
 
# Bouton de retour à l'accueil
if st.sidebar.button("🏠 Accueil", use_container_width=True):
    naviguer_vers("Accueil")
 
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("### 📁 DOSSIERS")
 
# Regroupement par dossiers intelligents (Expanders)
with st.sidebar.expander("💻 Informatique"):
    st.button("Rapport PEGASE", on_click=naviguer_vers, args=("Rapport PEGASE",), use_container_width=True)
 
with st.sidebar.expander("📦 Logistique (Infolog)", expanded=True):
    st.button("Commandes Détail", on_click=naviguer_vers, args=("Commandes Détail",), use_container_width=True)
    st.button("Articles - Douanes", on_click=naviguer_vers, args=("Articles - Douanes",), use_container_width=True)
 
with st.sidebar.expander("💶 Finance"):
    st.button("Analyse Chiffre d'Affaires", on_click=naviguer_vers, args=("Analyse CA",), use_container_width=True)
 
# ==========================================
# 4. ZONE PRINCIPALE (L'identité de l'outil)
# ==========================================
col_logo, col_user = st.columns([4, 1])
with col_logo:
    st.markdown("## 📊 **INFOCENTRE**")
with col_user:
    st.markdown("👤 **P. Dubois** | *Prod M3*")
st.markdown("---")
 
# ==========================================
# 5. ROUTAGE : AFFICHAGE DU CONTENU
# ==========================================
if st.session_state.page_actuelle == "Accueil":
    # --- ÉTAT 1 : PAGE D'ACCUEIL ---
    st.markdown("### Bonjour, Pierre. Que cherchez-vous aujourd'hui ?")
    # Barre de recherche globale
    tous_les_rapports = ["-- Rechercher un rapport --", "Commandes Détail", "Articles - Douanes", "Rapport PEGASE", "Analyse CA"]
    recherche = st.selectbox("🔍 Recherche rapide :", tous_les_rapports, label_visibility="collapsed")
    # Redirection automatique si un rapport est cherché
    if recherche != "-- Rechercher un rapport --":
        naviguer_vers(recherche)
        st.rerun()
 
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("#### 📌 VOS RAPPORTS FAVORIS")
    # Cartes de raccourcis pour les favoris
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("📄 Commandes Détail\n\n*Dernière vue : 10h00*", use_container_width=True):
            naviguer_vers("Commandes Détail")
            st.rerun()
    with col2:
        if st.button("📄 Articles - Douanes\n\n*Dernière vue : Hier*", use_container_width=True):
            naviguer_vers("Articles - Douanes")
            st.rerun()
 
else:
    # --- ÉTAT 2 : VUE D'UN RAPPORT SÉLECTIONNÉ ---
    nom_rapport = st.session_state.page_actuelle
    df = load_data()
    # Fil d'Ariane (Breadcrumbs)
    st.caption(f"🏠 Accueil / 📁 Dossier / **{nom_rapport}**")
    # En-tête du rapport et boutons d'action
    c_titre, c_actions = st.columns([3, 2])
    with c_titre:
        st.markdown(f"### 📄 {nom_rapport}")
    with c_actions:
        b1, b2 = st.columns(2)
        with b1:
            st.button("⭐ Ajouter aux favoris", use_container_width=True)
        with b2:
            # Bouton d'export fonctionnel
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Exporter CSV", data=csv, file_name=f"{nom_rapport}.csv", use_container_width=True)
    # Tableau de données moderne
    st.dataframe(df, use_container_width=True, hide_index=True)
 
 
 