import streamlit as st

st.header("🌉 Bridge Collapse Simulation")

if st.button("⬅️ BACK TO N-SAGE HOME", key="bridge_home"):
    st.session_state.page = "home"
    st.rerun()

st.divider()

rainfall = st.slider(
    "🌧️ Rainfall (mm)",
    0,
    1000,
    500,
    10,
    key="bridge_rain"
)

water_level = st.slider(
    "🌊 Water Level (m)",
    0.0,
    10.0,
    5.0,
    0.1,
    key="bridge_water"
)

bridge_condition = st.slider(
    "🌉 Bridge Condition (%)",
    0,
    100,
    70,
    5,
    key="bridge_condition"
)

st.divider()

if st.button(
    "🚀 START BRIDGE SIMULATION",
    use_container_width=True,
    key="bridge_start"
):

    rainfall_risk = rainfall / 10
    water_risk = water_level * 10
    condition_risk = 100 - bridge_condition

    risk = (
        rainfall_risk * 0.35
        + water_risk * 0.40
        + condition_risk * 0.25
    )

    risk = round(min(max(risk, 0), 100), 1)

    st.subheader("🧠 N-SAGE Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌧️ Rainfall", f"{rainfall} mm")

    with col2:
        st.metric("🌊 Water Level", f"{water_level:.1f} m")

    with col3:
        st.metric("⚠️ Risk Score", f"{risk}/100")

    with col4:
        st.metric(
            "🌉 Bridge Condition",
            f"{bridge_condition}%"
        )

    st.divider()

    st.subheader("📊 Structural Risk")

    st.progress(int(risk))

    if risk < 30:

        st.success("🟢 BRIDGE STABLE")

        st.write(
            "Structural failure is NOT detected "
            "under the current simulated condition."
        )

    elif risk < 50:

        st.info("🟡 BRIDGE UNDER MONITORING")

        st.write(
            "The bridge is experiencing increasing "
            "simulated environmental stress."
        )

    elif risk < 70:

        st.warning("🟠 BRIDGE CRITICAL")

        st.write(
            "High simulated stress detected. "
            "Structural monitoring is required."
        )

    else:

        st.error("🔴 STRUCTURAL FAILURE DETECTED")

        st.error("💥 BRIDGE COLLAPSE SCENARIO ACTIVATED")

        st.subheader("🌉 Bridge Status")

        st.markdown(
            """
            <div style="
                padding:40px;
                text-align:center;
                border-radius:15px;
                background:#263238;
                color:white;
                font-size:30px;
                font-weight:bold;
            ">
            🌉 BRIDGE
            <br><br>
            🚧 CLOSED
            <br><br>
            💥 COLLAPSE DETECTED
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.success("🗺️ SAFE DIVERSION ROUTE")

        st.markdown(
            """
            🏠 Residential Area
            <br><br>
            ↓
            <br><br>
            🟢 ━━━━━━━━━━━━━━━ 🟢
            <br>
            SAFE DIVERSION ROUTE
            <br>
            🟢 ━━━━━━━━━━━━━━━ 🟢
            <br><br>
            🏫 Safe Zone
            """,
            unsafe_allow_html=True
        )

st.divider()

st.info(
    "⚠️ N-SAGE is a prototype demonstration system. "
    "All risk scores and simulations are illustrative only "
    "and must not be treated as real structural predictions."
)
