import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Pour Nour ❤️", page_icon="🌹", layout="centered")

# CSS pour le look "Yahya & Nour"
st.markdown("""
    <style>
    .stApp { background-color: #1a1a1a; }
    h1, h2, h3, p, span { color: #FF69B4 !important; text-align: center; font-family: 'Verdana'; }
    .stButton>button { 
        background-color: #FF1493; color: white; border-radius: 20px; 
        width: 100%; border: none; padding: 10px;
    }
    input { background-color: #2b2b2b !important; color: white !important; border: 1px solid #FF69B4 !important; }
    </style>
    """, unsafe_allow_html=True)

# Initialisation de l'état
if 'etape' not in st.session_state:
    st.session_state.etape = 1

# --- ÉTAPE 1 : Identification ---
if st.session_state.etape == 1:
    st.write("# 🌹 Identification")
    prenom = st.text_input("Bonjour... Quel est ton prénom ?", key="name")
    if prenom:
        if st.button("Continuer"):
            st.session_state.prenom = prenom
            st.session_state.etape = 2
            st.rerun()

# --- ÉTAPE 2 : Anniversaire ---
elif st.session_state.etape == 2:
    st.write(f"# 🔐 Accès sécurisé pour {st.session_state.prenom}")
    date = st.text_input("Entre ma date d'anniversaire (JJ MM AAAA) :", key="date")
    if date == "14 04 2004":
        st.success("Accès autorisé. Prépare-toi Nour... ❤️")
        if st.button("Découvrir ma surprise"):
            st.session_state.etape = 3
            st.rerun()
    elif date != "":
        st.error("Code incorrect... réessaie ❤️")

# --- ÉTAPE 3 : Karaoké, Déclaration et Photo ---
elif st.session_state.etape == 3:
    st.balloons()


    # Paroles Karaoké
    paroles = ["I love you, baby,", "And if it's quite alright,", "I need you, baby,", "To warm a lonely night."]
    for p in paroles:
        st.write(f"### *{p}*")
        time.sleep(1.2)

    st.write("---")

    # Ta Déclaration
    st.write("## Nour tu es la femme de ma vie,")
    st.write("## ta présence m‘apaise et me rend plus fort.")
    st.write("## Je serai toujours à tes côtés")
    st.write("## pour le meilleur et pour le pire.")
    st.write("### **Yahya qui t’aime.**")

    st.write("---")

    # Affichage Photo (Fond blanc simulé par un container)
    with st.container():
        st.markdown('<div style="background-color: white; padding: 20px; border-radius: 10px;">',
                    unsafe_allow_html=True)
        try:
            st.image("photo.jpg", use_container_width=True)  # Streamlit utilise .jpg ou .png plus facilement que .gif
        except:
            st.write("📸 (Ta photo ici)")
        st.markdown('</div>', unsafe_allow_html=True)

    time.sleep(2)

    if st.button("Continuer ❤️"):
        st.session_state.etape = 4
        st.rerun()

# --- ÉTAPE 4 : Le Bouquet & Google Form ---
elif st.session_state.etape == 4:
    st.markdown('<style>.stApp { background-color: #FF69B4; }</style>', unsafe_allow_html=True)

    st.write("# 💐 UNE DERNIÈRE CHOSE...")
    st.write("### Je veux te faire livrer un bouquet de")
    st.write("### fleurs pour la Saint-Valentin !")
    st.write("### Écris-moi ton adresse mon amour")
    st.write("## Je t'aime ❤️")

    st.write("---")
    st.write("### Une nouvelle page va s'ouvrir pour noter ton adresse.")

    # Lien Google Form (Clignotant ou Gros bouton)
    url = "https://docs.google.com/forms/d/e/1FAIpQLScSGrAa8EZd9m0_F9v3Bcb8un_rlq0vI6gnAHApRJf_TspBhg/viewform?usp=sf_link"

    st.link_button("👉 CLIQUER ICI POUR MON ADRESSE 👈", url)