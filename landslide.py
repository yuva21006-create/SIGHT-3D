import streamlit as st
import time

st.header("⛰️ Landslide Simulation")

st.write(
    "N-SAGE analyses rainfall and terrain conditions "
    "to simulate landslide risk."
)

# ---------------- BACK ----------------

if st.button(
    "⬅️ BACK TO N-SAGE HOME",
    key="landslide_back"
):
    st.session_state.page = "home"
    st.rerun()

st.divider()

# ---------------- INPUTS ----------------

st.subheader("🌧️ Environmental Conditions")

rainfall = st.slider(
    "Expected Rainfall (mm)",
    min_value=0,
    max_value=1000,
    value=500,
    step=10,
    key="landslide_rainfall"
)

terrain_slope = st.slider(
    "Terrain Slope (°)",
    min_value=0,
    max_value=60,
    value=30,
    step=1,
    key="landslide_slope"
)

st.metric("🌧️ Rainfall", f"{rainfall} mm")
st.metric("⛰️ Terrain Slope", f"{terrain_slope}°")

# ---------------- SIMULATION ----------------

if st.button(
    "🎬 START LANDSLIDE SIMULATION",
    use_container_width=True,
    key="start_landslide_simulation"
):

    # Rainfall contribution
    rainfall_risk = rainfall / 1000 * 100

    # Slope contribution
    slope_risk = terrain_slope / 60 * 100

    # Combined risk
    risk_score = round(
        rainfall_risk * 0.55 +
        slope_risk * 0.45,
        1
    )

    # ---------------- CLASSIFICATION ----------------

    if risk_score < 25:

        landslide_status = "LOW"
        terrain_status = "STABLE"
        warning = "NORMAL"
        landslide = False

    elif risk_score < 45:

        landslide_status = "MODERATE"
        terrain_status = "MONITOR"
        warning = "WATCH"
        landslide = False

    elif risk_score < 65:

        landslide_status = "HIGH"
        terrain_status = "UNSTABLE"
        warning = "WARNING"
        landslide = False

    elif risk_score < 80:

        landslide_status = "VERY HIGH"
        terrain_status = "HIGHLY UNSTABLE"
        warning = "HIGH ALERT"
        landslide = True

    else:

        landslide_status = "EXTREME"
        terrain_status = "CRITICALLY UNSTABLE"
        warning = "EMERGENCY"
        landslide = True

    # ---------------- DASHBOARD ----------------

    st.divider()

    st.header("🧠 N-SAGE Automatic Analysis")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌧️ Rainfall",
            f"{rainfall} mm"
        )

    with c2:
        st.metric(
            "⛰️ Slope",
            f"{terrain_slope}°"
        )

    with c3:
        st.metric(
            "⚠️ Risk Score",
            f"{risk_score}/100"
        )

    with c4:
        st.metric(
            "⛰️ Status",
            landslide_status
        )

    # ---------------- RISK ----------------

    st.divider()

    st.subheader("📊 Landslide Risk")

    st.progress(
        int(min(risk_score, 100))
    )

    st.write(
        f"🌧️ **Rainfall Risk:** {rainfall_risk:.1f}%"
    )

    st.progress(
        int(rainfall_risk)
    )

    st.write(
        f"⛰️ **Slope Risk:** {slope_risk:.1f}%"
    )

    st.progress(
        int(slope_risk)
    )

    # ---------------- STATUS ----------------

    if landslide_status == "LOW":

        st.success(
            "🟢 LOW RISK — Terrain is simulated as stable."
        )

    elif landslide_status == "MODERATE":

        st.info(
            "🟡 MODERATE RISK — Monitor terrain conditions."
        )

    elif landslide_status == "HIGH":

        st.warning(
            "🟠 HIGH RISK — Terrain is becoming unstable."
        )

    elif landslide_status == "VERY HIGH":

        st.warning(
            "🟠 VERY HIGH RISK — Landslide scenario activated."
        )

    else:

        st.error(
            "🔴 EXTREME RISK — Severe landslide scenario activated."
        )

    # ---------------- TERRAIN ----------------

    st.divider()

    st.header("⛰️ Terrain Assessment")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.metric(
            "⛰️ Terrain Condition",
            terrain_status
        )

    with t2:
        st.metric(
            "🚨 Warning Level",
            warning
        )

    with t3:
        st.metric(
            "💥 Landslide",
            "DETECTED" if landslide else "NOT DETECTED"
        )

    # ---------------- ANIMATION ----------------

    st.divider()

    st.header("🎬 Landslide Scenario")

    animation = st.empty()

    stages = [
        "🌧️ RAINFALL DETECTED",
        "🌧️ WATER SATURATION INCREASING",
        "⛰️ TERRAIN STRESS INCREASING",
        "⚠️ SLOPE INSTABILITY DETECTED",
        "🧠 N-SAGE ANALYSING TERRAIN"
    ]

    for stage in stages:

        animation.markdown(
            f"""
            <div style="
                height:220px;
                background:linear-gradient(#546e7a,#263238);
                border-radius:15px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:28px;
                font-weight:bold;
                text-align:center;
            ">
                {stage}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.6)

    if landslide:

        animation.markdown(
            """
            <div style="
                height:220px;
                background:linear-gradient(#795548,#3e2723);
                border-radius:15px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:30px;
                font-weight:bold;
                text-align:center;
            ">
                💥 LANDSLIDE DETECTED
            </div>
            """,
            unsafe_allow_html=True
        )

        st.error(
            "🚨 LANDSLIDE SCENARIO ACTIVATED"
        )

        st.warning(
            "⛰️ The simulated terrain has become unstable."
        )

        st.success(
            "🗺️ SAFE DIVERSION ROUTE ACTIVATED"
        )

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

            🟢 ━━━━━━━━━━━━━━━━━ 🟢
            <br>
            SAFE DIVERSION ROUTE
            <br>
            🟢 ━━━━━━━━━━━━━━━━━ 🟢

            <br><br>

            ⛰️ LANDSLIDE ZONE 🚧

            <br><br>

            🏫 SAFE ZONE

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        animation.markdown(
            """
            <div style="
                height:220px;
                background:linear-gradient(#607d8b,#37474f);
                border-radius:15px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:30px;
                font-weight:bold;
                text-align:center;
            ">
                🟢 TERRAIN STABLE
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            "🟢 NO LANDSLIDE DETECTED "
            "UNDER THE CURRENT SIMULATED CONDITION."
        )

    # ---------------- FINAL ----------------

    st.divider()

    st.header("📋 N-SAGE Final Assessment")

    st.write(
        f"🌧️ **Rainfall:** {rainfall} mm"
    )

    st.write(
        f"⛰️ **Terrain Slope:** {terrain_slope}°"
    )

    st.write(
        f"⚠️ **Risk Score:** {risk_score}/100"
    )

    st.write(
        f"⛰️ **Terrain Condition:** {terrain_status}"
    )

    st.write(
        f"🚨 **Warning Level:** {warning}"
    )

    st.write(
        "💥 **Landslide:** "
        + ("DETECTED" if landslide else "NOT DETECTED")
    )

    st.info(
        "⚠️ N-SAGE is a prototype demonstration system. "
        "Risk scores, thresholds, simulations, diversion "
        "recommendations and emergency responses are "
        "illustrative only."
    )
