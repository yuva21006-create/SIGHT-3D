import streamlit as st

# ============================================================
# N-SAGE MAIN APPLICATION
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
    # FLOOD
    # ========================================================

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall conditions, estimated water level, "
        "flood depth, residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD SIMULATION",
        use_container_width=True,
        key="open_flood_button"
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    # ========================================================
    # LANDSLIDE
    # ========================================================

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse landslide conditions and terrain-related risks."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE SIMULATION",
        use_container_width=True,
        key="open_landslide_button"
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

    # Unique key
    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="back_home_flood"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    st.header("🌊 Residential Flood Simulation")

    # ========================================================
    # LOAD FLOOD MODULE
    # ========================================================

    try:

        import flood

    except Exception as e:

        st.error("❌ Unable to load flood.py")

        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    # Unique key
    if st.button(
        "⬅️ BACK TO N-SAGE HOME",
        key="back_home_landslide"
    ):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    st.header("⛰️ Landslide Simulation")

    # ========================================================
    # LOAD LANDSLIDE MODULE
    # ========================================================

    try:

        import landslide

    except Exception as e:

        st.error("❌ Unable to load landslide.py")

        st.exception(e)
