import streamlit as st
import pandas as pd
from services.db_client import fetch_product_data

# Recursive child verification logic representing React state engine
def is_descendant(f_id, target_id, folders):
    if target_id == 'tous': return True
    if target_id == 'favoris': return False
    if f_id == target_id: return True
    
    current = next((f for f in folders if f["id"] == f_id), None)
    while current and current["parentId"]:
        if current["parentId"] == target_id:
            return True
        current = next((f for f in folders if f["id"] == current["parentId"]), None)
    return False

def render_liste_rapports():
    st.title("Catalogue des Rapports")
    
    # Render state-driven tab system
    tab_titles = [t["title"] for t in st.session_state.open_tabs]
    st_tabs = st.tabs(tab_titles)
    
    for i, tab_data in enumerate(st.session_state.open_tabs):
        with st_tabs[i]:
            if tab_data["type"] == "list":
                render_catalogue()
            else:
                render_report_details(tab_data)

def render_catalogue():
    # Toolbar Filters
    col_search, col_dept = st.columns(2)
    search_q = col_search.text_input("🔍 Rechercher un rapport...", key="cat_search_input")
    
    depts = ["Tous"] + list(set(r["department"] for r in st.session_state.reports))
    selected_dept = col_dept.selectbox("Filtrer par Département", depts)

    st.divider()

    col_tree, col_grid = st.columns([3, 9])

    with col_tree:
        st.markdown("### 📁 Répertoires")
        folder_names = {f["id"]: f["name"] for f in st.session_state.folders}
        selected_folder_name = st.selectbox("Sélectionner un répertoire", list(folder_names.values()), key="f_tree_select")
        selected_folder_id = next((k for k, v in folder_names.items() if v == selected_folder_name), "tous")

    with col_grid:
        # Complex dynamic sorting logic matching ListeRapports.tsx
        sort_by = st.selectbox("Trier par", ["Nom (A-Z)", "Nom (Z-A)", "Code", "Date de création"])
        
        filtered = st.session_state.reports
        
        # Filter by selected folder structure
        if selected_folder_id == "favoris":
            filtered = [r for r in filtered if r["isFavorite"]]
        elif selected_folder_id != "tous":
            filtered = [r for r in filtered if is_descendant(r["folderId"], selected_folder_id, st.session_state.folders)]

        # Search Query
        if search_q:
            filtered = [r for r in filtered if search_q.lower() in r["title"].lower() or search_q in r["code"]]

        # Department Filter
        if selected_dept != "Tous":
            filtered = [r for r in filtered if r["department"] == selected_dept]

        # Order logic
        if sort_by == "Nom (A-Z)":
            filtered = sorted(filtered, key=lambda x: x["title"])
        elif sort_by == "Nom (Z-A)":
            filtered = sorted(filtered, key=lambda x: x["title"], reverse=True)
        elif sort_by == "Code":
            filtered = sorted(filtered, key=lambda x: x["code"])
        elif sort_by == "Date de création":
            filtered = sorted(filtered, key=lambda x: x["date"], reverse=True)

        st.caption(f"{len(filtered)} rapport(s) trouvé(s)")

        for r in filtered:
            with st.container(border=True):
                sc1, sc2 = st.columns([8, 2])
                sc1.markdown(f"#### {r['title']} (Code: `{r['code']}`)")
                sc1.caption(f"{r['department']} • {r['date']}")
                
                with sc2.popover("Actions", use_container_width=True):
                    # Action 1: Open Tab
                    if st.button("Ouvrir", key=f"op_cat_{r['id']}", use_container_width=True):
                        existing = next((t for t in st.session_state.open_tabs if t.get("reportId") == r["id"]), None)
                        if not existing:
                            st.session_state.open_tabs.append({
                                "id": f"tab-{r['id']}",
                                "title": r["title"],
                                "type": "report",
                                "reportId": r["id"]
                            })
                        st.rerun()
                    
                    # Action 2: Toggle favorite status
                    fav_txt = "Retirer favoris" if r["isFavorite"] else "Ajouter favoris"
                    if st.button(fav_txt, key=f"fav_cat_{r['id']}", use_container_width=True):
                        r["isFavorite"] = not r["isFavorite"]
                        st.rerun()

def render_report_details(tab_data):
    st.subheader(tab_data["title"])
    st.caption("Portail d'analyse technique et de contrôle géométrique des collections de maroquinerie, horlogerie, et accessoires.")
    
    # Load fully mocked product database matching data.ts
    df = fetch_product_data()

    f1, f2, f3 = st.columns(3)
    cats = ["Toutes"] + df["categorie"].unique().tolist()
    cat_filter = f1.selectbox("Catégorie", cats, key=f"cat_sel_{tab_data['id']}")
    status_filter = f2.selectbox("Statut", ["Tous", "Validé", "En test", "Rejeté"], key=f"stat_sel_{tab_data['id']}")
    search_p = f3.text_input("Rechercher un produit (Code ou Nom)", key=f"search_prod_{tab_data['id']}")

    # Apply filters
    filtered_df = df.copy()
    if cat_filter != "Toutes":
        filtered_df = filtered_df[filtered_df["categorie"] == cat_filter]
    if status_filter != "Tous":
        filtered_df = filtered_df[filtered_df["statut_test"] == status_filter]
    if search_p:
        filtered_df = filtered_df[
            filtered_df["nom_produit"].str.contains(search_p, case=False) |
            filtered_df["code_produit"].str.contains(search_p, case=False)
        ]

    # Action Trigger Buttons
    c1, c2, c3 = st.columns([2, 2, 8])
    with c1:
        st.button("Afficher", key=f"display_{tab_data['id']}", use_container_width=True, type="primary")
    with c2:
        if st.button("Réinitialiser", key=f"reset_{tab_data['id']}", use_container_width=True):
            st.rerun()
    with c3:
        # Simulate local spreadsheet conversion and export
        if st.button("Exporter au format Excel", key=f"export_{tab_data['id']}"):
            st.toast("Préparation du fichier d'export...", icon="📥")
            st.success("Téléchargement initié avec succès (Fichier Excel généré).")

    # Display dataset
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    st.divider()
    if st.button("Fermer l'onglet", key=f"close_btn_{tab_data['id']}", type="secondary"):
        st.session_state.open_tabs = [t for t in st.session_state.open_tabs if t["id"] != tab_data["id"]]
        st.rerun()