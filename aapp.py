import streamlit as st
import streamlit.components.v1 as components
import os

# --- Page Config ---
st.set_page_config(
    page_title="Aaj Kya Kiya - Digital Fridge",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide completely the default Streamlit UI
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none !important; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        margin: 0 !important;
    }
    iframe {
        width: 100vw;
        height: 100vh;
        border: none;
    }
    .stApp {
        background-color: #f7f8fa;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Safely get Firebase secrets without triggering Streamlit's red warning if missing
firebase_config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": ""
}

secrets_path = os.path.join(os.getcwd(), ".streamlit", "secrets.toml")
if os.path.exists(secrets_path):
    try:
        firebase_config["apiKey"] = st.secrets.get("FIREBASE_API_KEY", "")
        firebase_config["authDomain"] = st.secrets.get("FIREBASE_AUTH_DOMAIN", "")
        firebase_config["projectId"] = st.secrets.get("FIREBASE_PROJECT_ID", "")
        firebase_config["storageBucket"] = st.secrets.get("FIREBASE_STORAGE_BUCKET", "")
        firebase_config["messagingSenderId"] = st.secrets.get("FIREBASE_MESSAGING_SENDER_ID", "")
        firebase_config["appId"] = st.secrets.get("FIREBASE_APP_ID", "")
    except Exception:
        pass

# Load the single page app HTML
html_path = os.path.join(os.path.dirname(__file__), "app_ui.html")
try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("app_ui.html not found. Please ensure it exists in the same directory.")
    st.stop()

# Inject the configuration into the window object
injected_html = f"""
<script>
    window.ENV = {{
        FIREBASE_CONFIG: {firebase_config}
    }};
</script>
{html_content}
"""

# Render the application
components.html(injected_html, height=800, scrolling=False)
