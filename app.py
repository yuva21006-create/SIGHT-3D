import streamlit as st

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
    st.subheader("AI-Based Disaster Risk Analysis & Emergency Response")

    st.write(
        "N-SAGE analyses environmental conditions and "
        "simulates possible disaster scenarios."
    )

    st.divider()

    # --------------------------------------------------------
    # FLOOD
    # --------------------------------------------------------

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall, water level, flood depth, "
        "residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD SIMULATION",
        use_container_width=True,
        key="home_flood_button"
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # LANDSLIDE
    # --------------------------------------------------------

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse rainfall and terrain-related landslide risk."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE SIMULATION",
        use_container_width=True,
        key="home_landslide_button"
    ):
        st.session_state.page = "landslide"
        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # BRIDGE
    # --------------------------------------------------------

    st.header("🌉 Bridge Collapse Analysis")

    st.write(
        "Analyse rainfall, flood conditions, bridge risk "
        "and structural failure."
    )

    if st.button(
        "🌉 OPEN BRIDGE COLLAPSE SIMULATION",
        use_container_width=True,
        key="home_bridge_button"
    ):
        st.session_state.page = "bridge"
        st.rerun()

    st.divider()

    st.info(
        "⚠️ N-SAGE is a prototype demonstration system. "
        "Risk scores, thresholds, simulations, diversion "
        "recommendations and evacuation responses are "
        "illustrative only."
    )


# ============================================================
# FLOOD PAGE
# ============================================================

elif st.session_state.page == "flood":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="app_flood_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import flood

    except Exception as e:
        st.error("❌ Unable to load flood.py")
        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="app_landslide_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import landslide

    except Exception as e:
        st.error("❌ Unable to load landslide.py")
        st.exception(e)


# ============================================================
# BRIDGE PAGE
# ============================================================

elif st.session_state.page == "bridge":

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="app_bridge_back_button"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import bridge

    except Exception as e:
        st.error("❌ Unable to load bridge.py")
        st.exception(e)
