import streamlit as st
import time

def render_password_change():
    st.title("Changer le mot de passe")
    st.caption("Modifiez votre identifiant de sécurité d'accès au portail Infocentre.")
    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("password_reset_form"):
            old_p = st.text_input("Mot de passe actuel *", type="password")
            new_p = st.text_input("Nouveau mot de passe *", type="password")
            conf_p = st.text_input("Confirmer le nouveau mot de passe *", type="password")
            
            submit = st.form_submit_button("Enregistrer", use_container_width=True)
            
            if submit:
                if not old_p or not new_p or not conf_p:
                    st.error("Veuillez renseigner tous les champs obligatoires.")
                elif new_p != conf_p:
                    st.error("La confirmation du mot de passe ne correspond pas au nouveau mot de passe.")
                elif len(new_p) < 8:
                    st.error("Le nouveau mot de passe doit contenir au moins 8 caractères.")
                else:
                    with st.spinner("Enregistrement en cours..."):
                        time.sleep(1.5)
                    st.success("Mot de passe modifié avec succès !")