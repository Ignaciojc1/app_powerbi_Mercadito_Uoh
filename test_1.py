import streamlit as st
import streamlit.components.v1 as components
import base64

# Función para cargar un logo local y codificarlo en base64
def load_logo_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Ajusta el nombre de archivo de tu logo aquí (debe estar en la misma carpeta)
logo_path = "favicon_1.png"
logo_base64 = load_logo_base64(logo_path)

# Configuración de la página sin márgenes laterales
st.set_page_config(page_title="Power BI Embed", layout="wide")

# Header con fondo azul y logo a la izquierda
header_html = f"""
<div style="background-color:#0078d4; padding:10px 20px; display:flex; align-items:center; width:100%; box-sizing:border-box;">
    <img src="data:image/png;base64,{logo_base64}" height="40" style="margin-right:10px;">
    <h2 style="color:white; margin:0;"> Dashboard Power BI Integrado</h2>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# URL fijo de Power BI (Publish to web)
embed_url = (
    "https://app.powerbi.com/view?r="
    "eyJrIjoiMjRjZDY2MDUtOWMyOC00NWM1LTg4YWMtZmMwN2FmYTE4MmNjIiwidCI6IjUzMGM5NWRiLTMzMTEtNDI3Mi1hYzcxLTgyZmJhNjAwZTBiMSIsImMiOjR9"
)

# Embed del iframe que ocupa todo el ancho con altura fija
height = 800  # altura fija en píxeles
iframe_html = f"""
<div style="width:100%; height:{height}px; margin:0; padding:0;">
  <iframe src="{embed_url}" frameborder="0" allowFullScreen style="width:100%; height:100%; border:none;">
  </iframe>
</div>
"""
components.html(iframe_html, height=height)

# Footer reducido
st.markdown("---")
st.caption("Dashboard Power BI")
