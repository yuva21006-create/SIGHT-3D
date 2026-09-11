import streamlit as st
import time

st.header("🌉 Bridge Collapse Simulation")

st.write(
    "N-SAGE simulates how increasing rainfall and flood conditions "
    "may affect a bridge."
)

# ---------------- BACK BUTTON ----------------

if st.button("⬅️ BACK TO N-SAGE HOME", key="bridge_back"):
    st.session_state.page = "home"
    st.rerun()

st.divider()

# ---------------- INPUT ----------------

st.subheader("🌧️ Environmental Condition")

rainfall = st.slider(
    "Expected Rainfall (mm)",
    0,
    1000,
    500,
    10,
    key="bridge_rainfall"
)

st.metric("🌧️ Selected Rainfall", f"{rainfall} mm")

# ---------------- SIMULATION ----------------

if st.button(
    "🎬 START BRIDGE SIMULATION",
    use_container_width=True,
    key="start_bridge_simulation"
):

    st.divider()
    st.header("🧠 N-SAGE Bridge Analysis")

    # Water level model
    if rainfall < 200:
        water_level = 0.5 + rainfall * 0.002
    elif rainfall < 400:
        water_level = 0.9 + (rainfall - 200) * 0.004
    elif rainfall < 600:
        water_level = 1.7 + (rainfall - 400) * 0.012
    elif rainfall < 800:
        water_level = 4.1 + (rainfall - 600) * 0.015
    else:
        water_level = 7.1 + (rainfall - 800) * 0.014

    water_level = round(min(water_level, 10), 2)

    # Bridge risk
    rainfall_risk = rainfall / 1000 * 100
    water_risk = water_level / 10 * 100

    bridge_risk = round(
        rainfall_risk * 0.45 +
        water_risk * 0.55,
        1
    )

    # ---------------- STATUS ----------------

    if bridge_risk < 25:
        bridge_status = "STABLE"
        structural_status = "NORMAL"
        collapse = False

    elif bridge_risk < 45:
        bridge_status = "LOW RISK"
        structural_status = "MONITOR"
        collapse = False

    elif bridge_risk < 65:
        bridge_status = "CRITICAL"
        structural_status = "HIGH STRESS"
        collapse = False

    elif bridge_risk < 80:
        bridge_status = "SEVERELY CRITICAL"
        structural_status = "STRUCTURAL FAILURE DETECTED"
        collapse = True

    else:
        bridge_status = "EXTREME FAILURE RISK"
        structural_status = "STRUCTURAL FAILURE DETECTED"
        collapse = True

    # ---------------- METRICS ----------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌧️ Rainfall",
            f"{rainfall} mm"
        )

    with c2:
        st.metric(
            "🌊 Water Level",
            f"{water_level:.2f} m"
        )

    with c3:
        st.metric(
            "⚠️ Bridge Risk",
            f"{bridge_risk}/100"
        )

    with c4:
        st.metric(
            "🌉 Bridge Status",
            bridge_status
        )

    st.divider()

    # ---------------- RISK ----------------

    st.subheader("⚠️ Structural Risk")

    st.progress(
        int(min(bridge_risk, 100))
    )

    st.write(
        f"**Rainfall Risk:** {rainfall_risk:.1f}%"
    )

    st.write(
        f"**Water-Level Risk:** {water_risk:.1f}%"
    )

    st.write(
        f"**Structural Condition:** {structural_status}"
    )

    # ---------------- SCENARIO ----------------

    st.divider()
    st.header("🎬 Bridge Collapse Scenario")

    if collapse:

        st.error(
            "🚨 STRUCTURAL FAILURE DETECTED"
        )

        st.warning(
            "🌊 Extreme flood conditions are affecting "
            "the simulated bridge."
        )

        # Animation
        placeholder = st.empty()

        stages = [
            "🌉 BRIDGE STABLE",
            "🌊 WATER LEVEL RISING",
            "⚠️ BRIDGE UNDER HIGH STRESS",
            "🚨 STRUCTURAL FAILURE DETECTED",
            "💥 BRIDGE COLLAPSE"
        ]

        for stage in stages:

            placeholder.markdown(
                f"""
                <div style="
                    height:220px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:#263238;
                    border-radius:15px;
                    color:white;
                    font-size:30px;
                    font-weight:bold;
                    text-align:center;
                ">
                    {stage}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.8)

        st.error(
            "💥 BRIDGE COLLAPSE SCENARIO ACTIVATED"
        )

        st.success(
            "🗺️ DIVERSION ROUTE RECOMMENDED"
        )

        st.write(
            "The simulated bridge is considered unavailable. "
            "Residents should use the designated alternative route "
            "in this prototype scenario."
        )

        # Simple diversion diagram

        st.markdown(
            """
            <div style="
                background:#eef5ea;
                padding:30px;
                border-radius:15px;
                text-align:center;
                font-size:22px;
            ">

            🏠 RESIDENTIAL AREA

            <br><br>

            ↓

            <br><br>

            🟢 ━━━━━━━━━━━━━━━━ 🟢
            <br>
            SAFE DIVERSION ROUTE
            <br>
            🟢 ━━━━━━━━━━━━━━━━ 🟢

            <br><br>

            🚧 BRIDGE CLOSED

            <br><br>

            🏫 SAFE ZONE

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.success(
            "🟢 NO BRIDGE COLLAPSE DETECTED "
            "UNDER THE CURRENT SIMULATED CONDITION."
        )

        st.info(
            "🌉 Bridge remains operational in this prototype scenario."
        )

    # ---------------- FINAL ----------------

    st.divider()

    st.header("📋 Final Bridge Assessment")

    st.write(
        f"🌧️ **Rainfall:** {rainfall} mm"
    )

    st.write(
        f"🌊 **Estimated Water Level:** {water_level:.2f} m"
    )

    st.write(
        f"⚠️ **Bridge Risk Score:** {bridge_risk}/100"
    )

    st.write(
        f"🌉 **Bridge Condition:** {bridge_status}"
    )

    st.write(
        f"🏗️ **Structural Status:** {structural_status}"
    )

    st.write(
        "💥 **Collapse:** "
        + ("DETECTED" if collapse else "NOT DETECTED")
    )

    st.divider()

    st.info(
        "⚠️ N-SAGE is a prototype demonstration system. "
        "Risk scores, thresholds, simulations, diversion "
        "recommendations and emergency responses are illustrative only."
    )
