import streamlit as st

st.set_page_config(
    page_title="N-SAGE",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ N-SAGE")
st.subheader("AI-Based Disaster Risk Analysis & Emergency Response")

st.write(
    "Select a disaster scenario to begin the N-SAGE simulation."
)

st.divider()

# ============================================================
# RESIDENTIAL FLOOD
# ============================================================

st.header("🌊 Residential Flood")

st.write(
    "Analyse rainfall, water level, flood depth, "
    "residential impact and emergency response."
)

if st.button(
    "🌊 START RESIDENTIAL FLOOD",
    key="home_flood",
    use_container_width=True
):
    st.switch_page("flood.py")


st.divider()


# ============================================================
# BRIDGE COLLAPSE
# ============================================================

st.header("🌉 Bridge Collapse")

st.write(
    "Analyse extreme rainfall, flood conditions "
    "and bridge structural failure."
)

if st.button(
    "🌉 START BRIDGE COLLAPSE",
    key="home_bridge",
    use_container_width=True
):
    st.switch_page("bridge.py")


st.divider()


# ============================================================
# LANDSLIDE
# ============================================================

st.header("⛰️ Landslide")

st.write(
    "Analyse rainfall and terrain-related "
    "landslide conditions."
)

if st.button(
    "⛰️ START LANDSLIDE",
    key="home_landslide",
    use_container_width=True
):
    st.switch_page("landslide.py")


st.divider()

st.info(
    "🛰️ N-SAGE is a prototype disaster-risk "
    "visualization system."
)
