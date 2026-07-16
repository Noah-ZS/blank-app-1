import streamlit as st
import pandas as pd

# 100% Completed Data Lists matching React data.ts
MOCK_FOLDERS = [
    { "id": 'tous', "name": 'Tous les dossiers', "parentId": None },
    { "id": 'favoris', "name": 'Favoris', "parentId": 'tous' },
    { "id": 'informatique', "name": 'Informatique', "parentId": 'tous' },
    { "id": 'informatique-prod', "name": 'Production informatique', "parentId": 'informatique' },
    { "id": 'informatique-infocentre', "name": 'Infocentre', "parentId": 'informatique' },
    { "id": 'informatique-tarif', "name": 'Procédure tarifaire', "parentId": 'informatique' },
    { "id": 'informatique-req', "name": 'Nouvelles requêtes', "parentId": 'informatique' },
    { "id": 'nouvelles-req', "name": 'Nouvelles requêtes', "parentId": 'tous' },
    { "id": 'referentiel-article', "name": 'Référentiel Article', "parentId": 'tous' },
    { "id": 'lmh-commercial', "name": 'LMH - Gestion Commerciale', "parentId": 'tous' },
    { "id": 'lmh-financier', "name": 'LMH - Gestion Financière', "parentId": 'tous' },
    { "id": 'lmh-production', "name": 'LMH - Gestion Production', "parentId": 'tous' },
    { "id": 'lmh-plan', "name": 'LMH - Gestion Plan', "parentId": 'tous' },
    { "id": 'lmh-gestion', "name": 'LMH - Gestion', "parentId": 'tous' }
]

MOCK_REPORTS = [
    { "id": 'mesures-nouveaux-produits', "title": 'Mesures des Nouveaux Produits', "code": '1722', "department": 'Logistique - Infolog', "date": '26/03/2026', "isFavorite": True, "folderId": 'informatique-infocentre' },
    { "id": 'suivi-mesures-perf', "title": 'Suivi des mesures et performances produits', "code": '1722', "department": 'Logistique - Infolog', "date": '26/03/2026', "isFavorite": True, "folderId": 'informatique-infocentre' },
    { "id": 'article-coloris-taille', "title": 'Article - Liste des Coloris / Taille', "code": '646', "department": 'Logistique - Infolog', "date": '25/03/2026', "isFavorite": True, "folderId": 'referentiel-article' },
    { "id": 'nouvelles-req-article', "title": 'Nouvelles requêtes - Référentiel Article', "code": '646', "department": 'Logistique - Infolog', "date": '24/03/2026', "isFavorite": True, "folderId": 'referentiel-article' },
    { "id": 'commandes-detail', "title": 'Commandes - Détail', "code": '667', "department": 'Logistique - Infolog', "date": '26/03/2026', "isFavorite": True, "folderId": 'lmh-commercial' },
    { "id": 'nouvelles-req-commercial', "title": 'Nouvelles requêtes - Gestion Commerciale', "code": '667', "department": 'Logistique - Infolog', "date": '23/03/2026', "isFavorite": True, "folderId": 'lmh-commercial' },
    { "id": 'analyse-stocks-luxe', "title": 'Analyse des Stocks Maroquinerie', "code": '1410', "department": 'Gestion Commerciale', "date": '12/03/2026', "isFavorite": False, "folderId": 'lmh-commercial' },
    { "id": 'perf-magasins-europe', "title": 'Performance Magasins Europe', "code": '1502', "department": 'Gestion Financière', "date": '10/03/2026', "isFavorite": False, "folderId": 'lmh-financier' },
    { "id": 'suivi-expeditions-monde', "title": 'Suivi des Expéditions Internationales', "code": '1899', "department": 'Production informatique', "date": '20/03/2026', "isFavorite": False, "folderId": 'informatique-prod' },
    { "id": 'tarifs-saisonniers', "title": 'Grille des Tarifs Saisonniers', "code": '411', "department": 'Procédure tarifaire', "date": '05/03/2026', "isFavorite": False, "folderId": 'informatique-tarif' }
]

MOCK_PRODUCTS = [
    { "code_produit": 'MP0001', "nom_produit": 'Sac Birkin 30 Togo', "categorie": 'Maroquinerie', "longueur_cm": 30.0, "largeur_cm": 16.0, "hauteur_cm": 22.0, "poids_kg": 0.95, "volume_m3": 0.01056, "statut_test": 'Validé', "date_creation": '2026-03-02' },
    { "code_produit": 'MP0002', "nom_produit": 'Carré de Soie 90 - Brides de Gala', "categorie": 'Accessoires', "longueur_cm": 90.0, "largeur_cm": 90.0, "hauteur_cm": 0.2, "poids_kg": 0.065, "volume_m3": 0.0016, "statut_test": 'Validé', "date_creation": '2026-03-05' },
    { "code_produit": 'MP0003', "nom_produit": 'Ceinture H au Carré versible', "categorie": 'Maroquinerie', "longueur_cm": 110.0, "largeur_cm": 3.2, "hauteur_cm": 0.4, "poids_kg": 0.18, "volume_m3": 0.0002, "statut_test": 'En test', "date_creation": '2026-03-11' },
    { "code_produit": 'MP0004', "nom_produit": 'Portefeuille Constance Slim', "categorie": 'Maroquinerie', "longueur_cm": 12.5, "largeur_cm": 10.5, "hauteur_cm": 3.0, "poids_kg": 0.11, "volume_m3": 0.0004, "statut_test": 'Validé', "date_creation": '2026-03-14' },
    { "code_produit": 'MP0005', "nom_produit": "Foulard Twill d'Hermès", "categorie": 'Accessoires', "longueur_cm": 86.0, "largeur_cm": 5.0, "hauteur_cm": 0.1, "poids_kg": 0.015, "volume_m3": 0.0001, "statut_test": 'Rejeté', "date_creation": '2026-03-18' },
    { "code_produit": 'MP0006', "nom_produit": 'Sac Evelyne III 29 PM', "categorie": 'Maroquinerie', "longueur_cm": 29.0, "largeur_cm": 30.0, "hauteur_cm": 8.0, "poids_kg": 0.72, "volume_m3": 0.00696, "statut_test": 'En test', "date_creation": '2026-03-21' },
    { "code_produit": 'MP0007', "nom_produit": 'Gants Cuir d Agneau Souple', "categorie": 'Accessoires', "longueur_cm": 24.0, "largeur_cm": 10.0, "hauteur_cm": 2.0, "poids_kg": 0.11, "volume_m3": 0.0005, "statut_test": 'Validé', "date_creation": '2026-03-25' },
    { "code_produit": 'MP0008', "nom_produit": 'Sac Kelly 28 Sellier Epsom', "categorie": 'Maroquinerie', "longueur_cm": 28.0, "largeur_cm": 12.0, "hauteur_cm": 22.0, "poids_kg": 0.85, "volume_m3": 0.00739, "statut_test": 'Validé', "date_creation": '2026-03-05' },
    { "code_produit": 'MP0009', "nom_produit": 'Portefeuille Béarn Soufflet', "categorie": 'Maroquinerie', "longueur_cm": 17.5, "largeur_cm": 9.0, "hauteur_cm": 2.0, "poids_kg": 0.125, "volume_m3": 0.0003, "statut_test": 'Validé', "date_creation": '2026-03-11' },
    { "code_produit": 'MP0010', "nom_produit": 'Mocassins Paris Cuir Chèvre', "categorie": 'Chaussures', "longueur_cm": 30.0, "largeur_cm": 11.0, "hauteur_cm": 10.0, "poids_kg": 0.8, "volume_m3": 0.0033, "statut_test": 'Validé', "date_creation": '2026-03-14' },
    { "code_produit": 'MP0011', "nom_produit": 'Montre Cape Cod 33mm', "categorie": 'Horlogerie', "longueur_cm": 24.0, "largeur_cm": 3.3, "hauteur_cm": 0.8, "poids_kg": 0.15, "volume_m3": 0.0001, "statut_test": 'Validé', "date_creation": '2026-03-18' },
    { "code_produit": 'MP0012', "nom_produit": 'Bracelet Clic Clac H', "categorie": 'Accessoires', "longueur_cm": 6.0, "largeur_cm": 6.0, "hauteur_cm": 2.0, "poids_kg": 0.045, "volume_m3": 0.0001, "statut_test": 'Validé', "date_creation": '2026-03-18' },
    { "code_produit": 'MP0013', "nom_produit": 'Sac Picotin Lock 18 Clemence', "categorie": 'Maroquinerie', "longueur_cm": 18.0, "largeur_cm": 13.0, "hauteur_cm": 18.0, "poids_kg": 0.48, "volume_m3": 0.00421, "statut_test": 'Validé', "date_creation": '2026-03-20' },
    { "code_produit": 'MP0014', "nom_produit": 'Sandales Oran Epsom', "categorie": 'Chaussures', "longueur_cm": 26.0, "largeur_cm": 9.0, "hauteur_cm": 1.5, "poids_kg": 0.35, "volume_m3": 0.00035, "statut_test": 'Validé', "date_creation": '2026-03-22' },
    { "code_produit": 'MP0015', "nom_produit": 'Vide-poches Mosaïque au 24', "categorie": 'Maison', "longueur_cm": 21.0, "largeur_cm": 17.0, "hauteur_cm": 3.0, "poids_kg": 0.65, "volume_m3": 0.00107, "statut_test": 'Validé', "date_creation": '2026-03-24' }
]

@st.cache_data
def load_folders_and_reports():
    """Returns matching structure for catalog rendering."""
    return MOCK_FOLDERS, MOCK_REPORTS

@st.cache_data(ttl=600)
def fetch_product_data() -> pd.DataFrame:
    """Returns full item specifications."""
    return pd.DataFrame(MOCK_PRODUCTS)