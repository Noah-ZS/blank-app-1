import streamlit as st

def render_open_to_buy():
    st.title("Open to Buy (OTB)")
    st.markdown("Planifiez vos achats saisonniers de maroquinerie d'après la formule standard de gestion des stocks.")
    st.divider()

    col_form, col_result = st.columns([5, 7])

    with col_form:
        with st.container(border=True):
            st.subheader("Paramètres de Planification")
            season = st.selectbox("Saison", ["Automne / Hiver 2025 (AW25)", "Printemps / Été 2026 (SS26)", "Automne / Hiver 2026 (AW26)"])
            planned_sales = st.number_input("Ventes Prévisionnelles (Planned Sales)", value=3500000)
            planned_markdowns = st.number_input("Dépréciations Prévues (Planned Markdowns)", value=150000)
            planned_ending_inv = st.number_input("Stock de Fin Période Souhaité (Planned Ending Inv)", value=5800000)
            st.divider()
            starting_inv = st.number_input("Stock de Début Réel (Starting Inventory)", value=4200000)
            on_order = st.number_input("Commandes en Cours d'Acheminement (On Order)", value=1200000)

    with col_result:
        # Exact calculation replication matching otherpages.tsx
        total_needs = planned_sales + planned_markdowns + planned_ending_inv
        total_commitment = starting_inv + on_order
        calculated_otb = total_needs - total_commitment

        with st.container(border=True):
            st.markdown("<div style='text-align: center; color: gray;'>Limite d'achat calculée (Open to buy)</div>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; color: #E85F1E;'>€ {calculated_otb:,.0f}</h1>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            c1.metric("Besoins Totaux", f"€ {total_needs:,.0f}")
            c2.metric("Stocks Engagés", f"€ {total_commitment:,.0f}")

        st.info("La gestion d'Open to buy (OTB) est primordiale pour maintenir la désirabilité de nos collections en adaptant l'approvisionnement à la vélocité commerciale constatée en boutique.")