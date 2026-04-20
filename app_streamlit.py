import streamlit as st
import requests

# ---------- CONFIGURATION PAGE ----------
st.set_page_config(
    page_title="Prédiction Abandon Scolaire",
    layout="wide",
    page_icon="🎓",
    initial_sidebar_state="collapsed"
)

# ---------- STYLE CSS SOPHISTIQUÉ ----------
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&display=swap');
    
    /* Couleurs principales */
    :root {
        --primary-dark: #0A2540;
        --primary-light: #4B9CE2;
        --secondary: #2E8B57;
        --accent: #FFD700;
        --bg-light: #F8FAFC;
        --white: #FFFFFF;
        --gray: #64748B;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #F0F7FF 0%, #E6F0FA 100%);
    }
    
    /* En-tête personnalisé */
    .header-container {
        background: linear-gradient(90deg, var(--primary-dark) 0%, var(--primary-light) 100%);
        border-radius: 1rem;
        padding: 1rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    
    .header-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: white;
        margin: 0;
        letter-spacing: -0.02em;
    }
    
    .header-subtitle {
        font-size: 1rem;
        color: rgba(255,255,255,0.85);
        margin: 0;
    }
    
    /* Cartes et conteneurs */
    .stContainer > div {
        background: var(--white);
        border-radius: 1rem;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
        transition: transform 0.2s ease;
    }
    
    .stContainer > div:hover {
        transform: translateY(-2px);
    }
    
    /* Bouton principal */
    div.stButton > button {
        background: linear-gradient(90deg, var(--primary-dark), var(--primary-light));
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 2rem;
        padding: 0.6rem 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        background: linear-gradient(90deg, #0F3B5C, #5DADE2);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Onglets personnalisés */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: var(--bg-light);
        border-radius: 2rem;
        padding: 0.25rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 2rem;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        color: var(--primary-dark);
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-light);
        color: white;
    }
    
    /* Métriques */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-dark);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.8rem;
        color: var(--gray);
        border-top: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- BANNIÈRE AVEC IMAGE IA (placeholder) ----------
# Remplacez l'URL ci-dessous par votre propre image générée par IA (DALL-E, Midjourney, etc.)
# Dimensions recommandées : 1200x300 pixels
import base64
import streamlit as st

# Lecture de l'image locale
with open("banniere.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Construction de l'URL data
data_url = f"data:image/jpeg;base64,{encoded_string}"

st.markdown(f"""
<div style="background-image: url('{data_url}'); 
            background-size: cover; 
            background-position: center; 
            border-radius: 1rem; 
            padding: 2rem; 
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
    <div style="background: rgba(10,37,64,0.7); border-radius: 1rem; padding: 1rem;">
        <h1 style="color: white; text-align: center; margin:0;">🎓 Système d'Alerte Précoce</h1>
        <p style="color: #FFD700; text-align: center; font-size: 1.2rem;">Détection des risques d'abandon scolaire par IA</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- FORMULAIRE (aucune modification logique) ----------
with st.container():
    st.markdown("### 📋 Informations de l'étudiant")
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        age = st.number_input("Âge de l'étudiant", min_value=10, max_value=40, value=18, step=1)
        gender = st.selectbox("Sexe", ["Male", "Female"])
        average_grade = st.slider("Moyenne générale (/20)", 0.0, 20.0, 10.0, 0.5)
        absenteeism_rate = st.slider("Taux d'absence (0 à 0.5)", 0.0, 0.5, 0.1, 0.01)
    
    with col2:
        internet_access = st.selectbox("Accès à internet", ["Yes", "No"])
        study_time_hours = st.number_input("Temps d'étude journalier (heures)", 0.0, 12.0, 2.0, 0.5)
        extra_activities = st.selectbox("Activités extrascolaires", ["Yes", "No"])
    
    # Feature Engineering (inchangé)
    interaction_moyenne_absence = absenteeism_rate * (20 - average_grade)
    ratio_pres_abs = (1 - absenteeism_rate) / (absenteeism_rate if absenteeism_rate > 0 else 0.01)
    
    st.markdown("---")
    submitted = st.button("🚀 Lancer l'analyse du profil", use_container_width=True)

# ---------- ANALYSE APRÈS SOUMISSION ----------
if submitted:
    # Encodage (identique)
    gender_Male = 1 if gender == "Male" else 0
    internet_access_Yes = 1 if internet_access == "Yes" else 0
    extra_activities_Yes = 1 if extra_activities == "Yes" else 0

    taux_presence = 1 - absenteeism_rate
    absence_pour_ratio = absenteeism_rate if absenteeism_rate > 0 else 0.01
    ratio_pres_abs = taux_presence / absence_pour_ratio
    interaction_moyenne_absence = absenteeism_rate * (20 - average_grade)

    data_features = [
        age, average_grade, absenteeism_rate, study_time_hours,
        taux_presence, absence_pour_ratio, ratio_pres_abs,
        interaction_moyenne_absence, gender_Male, internet_access_Yes, extra_activities_Yes
    ]

    try:
        # ⚠️ SEUL CHANGEMENT ICI : l'URL de l'API
        response = requests.post("https://dropout-project-1.onrender.com/predict", json={"features": data_features})
        res = response.json()
        prob = res.get('probabilité', res.get('probabilite', res.get('probability', 0.0)))
        prediction = res.get('abandon', res.get('prediction', res.get('dropout', 0)))

        # ---------- RÉSULTATS ORGANISÉS EN ONGLETS ----------
        st.markdown("---")
        st.markdown("## 📊 Résultats de l'analyse")
        
        tab1, tab2, tab3 = st.tabs(["📈 Analyse du risque", "🔍 Explication détaillée", "📋 Recommandations"])
        
        with tab1:
            # Métriques
            col_met1, col_met2, col_met3 = st.columns(3)
            with col_met1:
                st.metric("Probabilité d'abandon", f"{prob*100:.1f}%")
            with col_met2:
                if prob < 0.3:
                    niveau = "🟢 Faible"
                elif prob < 0.7:
                    niveau = "🟠 Moyen"
                else:
                    niveau = "🔴 Élevé"
                st.metric("Niveau de risque", niveau)
            with col_met3:
                decision = "⚠️ Intervention recommandée" if prob > 0.5 else "✅ Suivi normal"
                st.metric("Décision", decision)
            
            # Jauge de risque améliorée
            st.markdown("#### Évolution du risque")
            color = "green" if prob < 0.3 else "orange" if prob < 0.7 else "red"
            st.markdown(f"""
            <div style="background-color: #E2E8F0; border-radius: 20px; padding: 4px; margin: 15px 0;">
                <div style="width: {prob*100}%; background-color: {color}; border-radius: 20px; padding: 10px; text-align: right; color: white; font-weight: bold;">
                    {prob*100:.1f}%
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Verdict final
            if prob < 0.3:
                st.success("🟢 **Verdict : Risque faible** – L'étudiant est bien engagé. Continuer à suivre régulièrement.")
            elif prob < 0.7:
                st.warning("🟠 **Verdict : Risque moyen** – Des signaux d'alerte modérés. Une attention particulière est conseillée.")
            else:
                st.error("🔴 **Verdict : Risque élevé** – Danger d'abandon. Intervention pédagogique nécessaire rapidement.")
        
        with tab2:
            st.markdown("### 🔍 Pourquoi ce résultat ?")
            if prob > 0.5:
                st.write("**Facteurs critiques détectés :**")
                if absenteeism_rate > 0.3:
                    st.write("- ❌ Le *taux d'absentéisme* dépasse le seuil de vigilance (30%).")
                if average_grade < 10:
                    st.write("- ❌ La *moyenne actuelle* est insuffisante pour sécuriser le parcours (moins de 10/20).")
                if interaction_moyenne_absence > 5:
                    st.write("- ❌ L'*interaction Risque* (Absence × Échec) est très élevée (aggrave le risque).")
                if study_time_hours < 1:
                    st.write("- ⚠️ Le *temps d'étude quotidien* est très faible.")
                if internet_access_Yes == 0:
                    st.write("- ⚠️ L'absence d'accès à internet peut limiter les ressources.")
            else:
                st.success("✨ Aucun facteur critique majeur détecté. L'étudiant présente des facteurs de protection solides (assiduité, notes suffisantes).")
            
            with st.expander("📖 Comment l'IA a calculé ce risque ?"):
                st.markdown("""
                Notre modèle **XGBoost** analyse en temps réel plusieurs indicateurs :
                - Performance académique (moyenne, absentéisme)
                - Engagement (temps d'étude, accès internet, activités extrascolaires)
                - Indices composites (interaction absence × échec, ratio présence/absence)
                
                La probabilité affichée est le résultat direct du modèle entraîné sur des données historiques d'étudiants.
                """)
        
        with tab3:
            st.markdown("### 📋 Recommandations personnalisées")
            if prob < 0.3:
                risque_categorie = "faible"
            elif prob < 0.7:
                risque_categorie = "moyen"
            else:
                risque_categorie = "eleve"
            
            if risque_categorie == "faible":
                st.markdown("""
                **✅ Recommandations pour un risque faible :**
                - Maintenir un suivi régulier (pointage mensuel).
                - Encourager l'étudiant à continuer ses bonnes habitudes.
                - Proposer des défis académiques pour maintenir l'engagement.
                - Vérifier périodiquement l'accès aux ressources numériques.
                """)
            elif risque_categorie == "moyen":
                st.markdown("""
                **⚠️ Recommandations pour un risque moyen :**
                - Organiser un entretien avec l'étudiant pour comprendre les difficultés.
                - Mettre en place un tutorat ou un soutien scolaire ciblé.
                - Améliorer l'assiduité : contacter la famille si nécessaire.
                - Proposer des ateliers de gestion du temps et des révisions.
                - Vérifier l'accès à internet et aux équipements.
                - Suivi rapproché (toutes les 2 semaines).
                """)
            else:
                st.markdown("""
                **🚨 Recommandations pour un risque élevé (urgence) :**
                - **Intervention immédiate** : contacter l'étudiant et sa famille.
                - Mettre en place un plan de soutien intensif (tutorat plusieurs fois par semaine).
                - Réduire la charge de travail si possible (adaptation pédagogique).
                - Proposer un accompagnement psychologique si nécessaire.
                - Améliorer drastiquement l'assiduité : contrat d'engagement.
                - Réunion avec l'équipe pédagogique pour un suivi personnalisé.
                - Orienter vers des dispositifs d'aide (bourses, aide au logement, etc.).
                """)
            
            st.markdown("**Conseils supplémentaires spécifiques à ce profil :**")
            if absenteeism_rate > 0.2:
                st.write("- 📌 *Absentéisme notable* : contacter l'étudiant pour comprendre les causes (santé, transport, motivation).")
            if average_grade < 12:
                st.write("- 📌 *Notes à améliorer* : proposer des ressources complémentaires (exercices, vidéos, groupes d'étude).")
            if study_time_hours < 1.5:
                st.write("- 📌 *Temps d'étude faible* : aider l'étudiant à organiser son emploi du temps.")
            if internet_access_Yes == 0:
                st.write("- 📌 *Pas d'accès internet* : orienter vers des espaces numériques gratuits (bibliothèque, cybercafé scolaire).")
            if extra_activities_Yes == 0:
                st.write("- 📌 *Absence d'activités extrascolaires* : encourager l'inscription à un club ou atelier pour renforcer le lien avec l'établissement.")
    
    except Exception as e:
        st.error(f"Erreur de connexion : {e}")
        print(e)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <p>🔬 Analyse prédictive basée sur XGBoost | Données anonymisées | Interface conçue avec ♥ pour l'éducation</p>
</div>
""", unsafe_allow_html=True)