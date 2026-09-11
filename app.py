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
# HOME
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

    # --------------------------------------------------------
    # FLOOD
    # --------------------------------------------------------

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall, water level, flood depth, "
        "residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD",
        key="open_flood",
        use_container_width=True
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # BRIDGE
    # --------------------------------------------------------

    st.header("🌉 Bridge Collapse Analysis")

    st.write(
        "Analyse rainfall, flooding and bridge "
        "structural failure."
    )

    if st.button(
        "🌉 OPEN BRIDGE COLLAPSE",
        key="open_bridge",
        use_container_width=True
    ):
        st.session_state.page = "bridge"
        st.rerun()

    st.divider()

    # --------------------------------------------------------
    # LANDSLIDE
    # --------------------------------------------------------

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse rainfall and terrain-related "
        "landslide conditions."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE",
        key="open_landslide",
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

    st.title("🌊 Residential Flood Analysis")

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="back_flood"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import flood

    except Exception as e:

        st.error("❌ Error loading flood.py")

        st.exception(e)


# ============================================================
# BRIDGE PAGE
# ============================================================

elif st.session_state.page == "bridge":

    st.title("🌉 Bridge Collapse Analysis")

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="back_bridge"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import bridge

    except Exception as e:

        st.error("❌ Error loading bridge.py")

        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    st.title("⛰️ Landslide Analysis")

    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="back_landslide"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:
        import landslide

    except Exception as e:

        st.error("❌ Error loading landslide.py")

        st.exception(e)
