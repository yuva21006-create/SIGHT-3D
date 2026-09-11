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

    st.subheader(
        "AI-Based Disaster Risk Analysis & Emergency Response"
    )

    st.write(
        "N-SAGE analyses environmental conditions and "
        "simulates possible disaster scenarios."
    )

    st.divider()

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall conditions, estimated water level, "
        "flood depth, residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD SIMULATION",
        use_container_width=True
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse landslide conditions and terrain-related risks."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE SIMULATION",
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

    if st.button("⬅️ BACK TO N-SAGE HOME"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    # Import flood.py only when the flood page is opened.
    try:

        import flood

    except Exception as e:

        st.error("❌ Unable to load flood.py")

        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    if st.button("⬅️ BACK TO N-SAGE HOME"):
        st.session_state.page = "home"
        st.rerun()
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

    st.subheader(
        "AI-Based Disaster Risk Analysis & Emergency Response"
    )

    st.write(
        "N-SAGE analyses environmental conditions and "
        "simulates possible disaster scenarios."
    )

    st.divider()

    st.header("🌊 Residential Flood Analysis")

    st.write(
        "Analyse rainfall conditions, estimated water level, "
        "flood depth, residential impact and emergency response."
    )

    if st.button(
        "🌊 OPEN RESIDENTIAL FLOOD SIMULATION",
        use_container_width=True
    ):
        st.session_state.page = "flood"
        st.rerun()

    st.divider()

    st.header("⛰️ Landslide Analysis")

    st.write(
        "Analyse landslide conditions and terrain-related risks."
    )

    if st.button(
        "⛰️ OPEN LANDSLIDE SIMULATION",
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

    if st.button("⬅️ BACK TO N-SAGE HOME"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    # Import flood.py only when the flood page is opened.
    try:

        import flood

    except Exception as e:

        st.error("❌ Unable to load flood.py")

        st.exception(e)


# ============================================================
# LANDSLIDE PAGE
# ============================================================

elif st.session_state.page == "landslide":

    if st.button("⬅️ BACK TO N-SAGE HOME"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()

    try:

        import landslide

    except Exception as e:

        st.error("❌ Unable to load landslide.py")

        st.exception(e)
    st.divider()

    try:

        import landslide

    except Exception as e:

        st.error("❌ Unable to load landslide.py")

        st.exception(e)
