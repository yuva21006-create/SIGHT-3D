import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="N-SAGE",
    page_icon="🛰️",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    st.title("🛰️ N-SAGE")

    st.subheader(
        "AI-Based Disaster Risk Analysis & Emergency Response"
    )

    st.write(
        "N-SAGE analyses environmental conditions and "
        "simulates possible disaster scenarios."
    )

    st.divider()

    # ========================================================
    # RESIDENTIAL FLOOD
    # ========================================================

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall conditions, estimated water level, "
        "flood depth, residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD SIMULATION",
        key="open_flood_button",
        use_container_width=True
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    # ========================================================
    # BRIDGE COLLAPSE
    # ========================================================

    st.header("🌉 Bridge Collapse Analysis")

    st.write(
        "Analyse extreme rainfall, flood conditions, "
        "bridge risk and structural failure."
    )

    if st.button(
        "🌉 OPEN BRIDGE COLLAPSE SIMULATION",
        key="open_bridge_button",
        use_container_width=True
    ):
        st.session_state.page = "bridge"
        st.rerun()

    st.divider()

    # ========================================================
    # LANDSLIDE
    # ========================================================

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse rainfall and terrain-related "
        "landslide risks."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE SIMULATION",
        key="open_landslide_button",
        use_container_width=True
    ):
        st.session_state.page = "landslide"
        st.rerun()

    st.divider()

    st.info(
        "🛰️ N-SAGE is a prototype disaster-risk "
        "visualization system."
    )


# ============================================================
# FLOOD PAGE
# ============================================================

elif st.session_state.page == "flood":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="flood_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    # Import the flood module
    try:

        import flood

        flood.show_flood()

    except Exception as e:

        st.error("❌ Flood simulation could not be loaded.")

        st.exception(e)


# ============================================================
# BRIDGE COLLAPSE PAGE
# ============================================================

elif st.session_state.page == "bridge":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="bridge_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    # Import the bridge module
    try:

        import bridge

        bridge.show_bridge()

    except Exception as e:

        st.error("❌ Bridge simulation could not be loaded.")

        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="landslide_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    # Import the landslide module
    try:

        import landslide

        landslide.show_landslide()

    except Exception as e:

        st.error("❌ Landslide simulation could not be loaded.")

        st.exception(e)
