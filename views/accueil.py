import streamlit as st
from components.metrics import render_kpi
from components.typography import render_page_title
from components.cards import render_list_card

def open_tab(report_id):
    """Binds item targets cleanly to local workspace view instances."""
    report = next((r for r in st.session_state.reports if r["id"] == report_id), None)
    if not report: return
    
    existing = next((t for t in st.session_state.open_tabs if t.get("reportId") == report_id), None)
    if existing:
        st.session_state.active_tab_id = existing["id"]
    else:
        new_id = f"tab-{report_id}"
        st.session_state.open_tabs.append({
            "id": new_id,
            "title": report["title"],
            "type": "report",
            "reportId": report_id
        })
        st.session_state.active_tab_id = new_id
    st.session_state.active_page = "liste_rapports"
    st.rerun()

def render_accueil():
    # User Profile Header using custom typography
    h_col1, h_col2 = st.columns([8, 2])
    with h_col1:
        render_page_title(
            title="Bienvenue sur votre Infocentre", 
            subtitle="Votre portail de Business Intelligence dédié à la performance."
        )
        
    with h_col2:
        with st.popover("👤 NJ", use_container_width=True):
            st.markdown("**Neeraj J.**")
            st.caption("neeraj@datasoluva.com")
            st.divider()
            st.caption("Rôle: Production Manager")
            st.caption("Statut: 🟢 Connecté (Production)")
            if st.button("Se déconnecter", type="primary", use_container_width=True):
                st.session_state.is_logged_in = False
                st.rerun()

    st.divider()

    # KPI Layout
    k_col1, k_col2, k_col3 = st.columns(3)
    with k_col1:
        render_kpi("Rapports générés ce mois", "142", "🟢 +12% vs mois précédent", "📈")
    with k_col2:
        render_kpi("Temps moyen d'exécution", "1.8 s", "🟢 -0.4s vs prévisions", "⚙️")
    with k_col3:
        fav_num = sum(1 for r in st.session_state.reports if r["isFavorite"])
        render_kpi("Rapports favoris", str(fav_num), "🟢 En hausse", "⭐")

    st.divider()

    # Split workspace lists
    col_rec, col_fav = st.columns([5, 7])
    
    with col_rec:
        st.markdown("### 📋 Rapports Récents")
        recents = [
            {"title": "Commandes - Détail", "category": "Gestion Commerciale", "time": "Il y a 2 h"},
            {"title": "Suivi des mesures et performances", "category": "Logistique - Infolog", "time": "Il y a 4 h"},
            {"title": "Analyse des Stocks Maroquinerie", "category": "Gestion Commerciale", "time": "Il y a 6 h"},
            {"title": "Tarifs Saisonniers", "category": "Procédure tarifaire", "time": "Il y a 1 j"}
        ]
        
        for idx, item in enumerate(recents):
            with st.container(border=True):
                sc1, sc2 = st.columns([8, 2], vertical_alignment="center")
                with sc1:
                    render_list_card(title=item['title'], subtitle=item["category"], metadata=item["time"], icon="📄")
                with sc2:
                    rep_match = next((r for r in st.session_state.reports if item["title"].lower() in r["title"].lower()), None)
                    if rep_match:
                        if st.button("Ouvrir", key=f"rec_nav_{idx}", use_container_width=True):
                            open_tab(rep_match["id"])

    with col_fav:
        st.markdown("### ⭐ Vos Favoris")
        favorites = [r for r in st.session_state.reports if r["isFavorite"]]
        
        if not favorites:
            st.info("Aucun rapport dans vos favoris.")
        else:
            for r in favorites:
                with st.container(border=True):
                    sc1, sc2 = st.columns([8, 2], vertical_alignment="center")
                    with sc1:
                        render_list_card(title=r['title'], subtitle=r["department"], metadata=f"Code: {r['code']}", icon="⭐")
                    with sc2:
                        with st.popover("⚙️", use_container_width=True):
                            if st.button("Ouvrir le rapport", key=f"open_fav_pop_{r['id']}", use_container_width=True):
                                open_tab(r["id"])
                            if st.button("Retirer des favoris", key=f"rem_fav_pop_{r['id']}", use_container_width=True, type="primary"):
                                r["isFavorite"] = False
                                st.rerun()