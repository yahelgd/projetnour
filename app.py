import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Pour Nour ❤️", page_icon="🌹", layout="centered")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .stApp { background-color: #1a1a1a; }
    h1, h2, h3, p, span { color: #FF69B4 !important; text-align: center; font-family: 'Verdana'; }
    .stButton>button { 
        background-color: #FF1493; color: white; border-radius: 20px; 
        width: 100%; border: none; padding: 10px; font-weight: bold;
    }
    input { background-color: #2b2b2b !important; color: white !important; border: 1px solid #FF69B4 !important; }
    
    .declaration-box {
        padding: 25px; 
        border-left: 5px solid #FF1493; 
        background-color: #2b2b2b; 
        border-radius: 15px; 
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    .declaration-text {
        font-size: 20px; 
        font-style: italic; 
        line-height: 1.6; 
        color: white !important;
    }
    .photo-frame {
        border: 2px solid #FF69B4; 
        padding: 10px; 
        border-radius: 15px;
        background-color: #000;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialisation de la mémoire
if 'etape' not in st.session_state:
    st.session_state.etape = 1

# --- ÉTAPE 1 : IDENTIFICATION ---
if st.session_state.etape == 1:
    st.write("# 🌹 Identification")
    st.write("### Je dois vérifier que c'est bien toi...")
    prenom = st.text_input("Quel est ton prénom ?", key="name_input")
    
    if prenom:
        if prenom.lower() == "nour":
            st.success("Accès autorisé... ❤️")
            if st.button("Découvrir mon message"):
                st.session_state.etape = 2
                st.rerun()
        else:
            st.error("Désolé, ce message n'est pas pour toi... 🥀")

# --- ÉTAPE 2 : PAGE 1 ---
elif st.session_state.etape == 2:
    st.write("# Pour toi, Nour... ❤️")
    st.markdown("""
        <div class="declaration-box">
            <p class="declaration-text">
                "Nour, tu es la femme de ma vie. Tu es radieuse et tu illumines ma vie avec ton énergie et ta bonne humeur. 
                Quant à ta tendresse, elle adoucit mon cœur.<br><br>
                <b>Pour moi, tu es un cadeau de Dieu et la raison pour laquelle je souhaite devenir un homme meilleur.</b>"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image("photo1.jpg", use_container_width=True)
    except:
        st.info("📸 (Ajoute 'photo1.jpg' ici)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Continuer... ✨"):
        st.session_state.etape = 3
        st.rerun()

# --- ÉTAPE 3 : PAGE 2 ---
elif st.session_state.etape == 3:
    st.write("# Mon pilier... ✨")
    st.markdown("""
        <div class="declaration-box">
            <p class="declaration-text">
                "Tu m'as apporté réconfort et tendresse pendant mes nuits de doute et de tristesse.<br><br>
                Tu as transformé mon manque de confiance en assurance. Tes belles paroles m'illuminent et me relèvent de mon lit de malheur."
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image("photo2.jpg", use_container_width=True)
    except:
        st.info("📸 (Ajoute 'photo2.jpg' ici)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("La suite... ❤️"):
        st.session_state.etape = 4
        st.rerun()

# --- ÉTAPE 4 : PAGE 3 ---
elif st.session_state.etape == 4:
    st.write("# Un nouveau voyage... 🚀")
    st.markdown("""
        <div class="declaration-box">
            <p class="declaration-text">
                "Tu es celle qui a brisé la routine qui me détruisait. <br><br>
                Regarder tes yeux est pour moi synonyme de voyage au milieu des étoiles.<br><br>
                <b>Avec toi, j'ai enlevé la barrière, le rétro et la marche arrière.</b>"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image("photo3.jpg", use_container_width=True)
    except:
        st.info("📸 (Ajoute 'photo3.jpg' ici)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Presque fini... ✨"):
        st.session_state.etape = 5
        st.rerun()

# --- ÉTAPE 5 : PAGE 4 (FINAL) ---
elif st.session_state.etape == 5:
    st.write("# Mon serment pour l'éternité... ♾️")
    st.markdown("""
        <div class="declaration-box" style="box-shadow: 0px 0px 20px #FF1493; border-left: none; border: 2px solid #FF1493;">
            <p class="declaration-text" style="text-align: center;">
                "J'ai juré devant Dieu que je t'apporterai amour, fidélité et protection malgré les vagues et les flots de la vie.<br><br>
                Tu es ma femme et la flamme qui réchauffe mon cœur qui était refroidi par la dureté de l'existence.<br><br>
                <b>Reste avec moi mon amour et nous écrirons un livre que nous lirons ensemble à la fin de nos jours.</b>"
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="photo-frame">', unsafe_allow_html=True)
    try:
        st.image("photo4.jpg", use_container_width=True)
    except:
        st.info("📸 (Ajoute 'photo4.jpg' ici)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("### Je t'aime plus que tout. ❤️")
    
    if st.button("Revoir depuis le début 🔄"):
        st.session_state.etape = 1
        st.rerun()