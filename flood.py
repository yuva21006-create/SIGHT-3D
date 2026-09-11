import streamlit as st
import time

st.header("🌊 Residential Flood Simulation")

st.write(
    "N-SAGE analyses rainfall conditions and simulates "
    "residential flood risk and emergency response."
)

# ---------------- BACK ----------------

if st.button(
    "⬅️ BACK TO N-SAGE HOME",
    key="flood_back"
):
    st.session_state.page = "home"
    st.rerun()

st.divider()

# ---------------- RAINFALL ----------------

st.subheader("🌧️ Environmental Condition")

rainfall = st.slider(
    "Expected Rainfall (mm)",
    min_value=0,
    max_value=1000,
    value=300,
    step=10,
    key="flood_rainfall"
)

st.metric(
    "🌧️ Selected Rainfall",
    f"{rainfall} mm"
)

# ---------------- SIMULATION ----------------

if st.button(
    "🎬 START FLOOD SIMULATION",
    use_container_width=True,
    key="start_flood_simulation"
):

    # Water level

    if rainfall < 150:
        water_level = 0.4 + rainfall * 0.002

    elif rainfall < 300:
        water_level = 0.7 + rainfall * 0.003

    elif rainfall < 500:
        water_level = 1.6 + (rainfall - 300) * 0.006

    elif rainfall < 700:
        water_level = 2.8 + (rainfall - 500) * 0.012

    elif rainfall < 850:
        water_level = 5.2 + (rainfall - 700) * 0.020

    else:
        water_level = 8.2 + (rainfall - 850) * 0.012

    water_level = round(
        min(water_level, 10),
        2
    )

    # Flood depth

    if rainfall < 200:
        flood_depth = water_level * 0.35

    elif rainfall < 400:
        flood_depth = water_level * 0.50

    elif rainfall < 600:
        flood_depth = water_level * 0.65

    elif rainfall < 800:
        flood_depth = water_level * 0.78

    else:
        flood_depth = water_level * 0.90

    flood_depth = round(
        min(flood_depth, 8),
        2
    )

    # ---------------- RISK ----------------

    rainfall_risk = rainfall / 1000 * 100

    water_risk = min(
        water_level / 10 * 100,
        100
    )

    depth_risk = min(
        flood_depth / 8 * 100,
        100
    )

    risk_score = round(
        rainfall_risk * 0.50
        + water_risk * 0.25
        + depth_risk * 0.25,
        1
    )

    # ---------------- CLASSIFICATION ----------------

    if rainfall < 200:

        flood_status = "LOW"
        house_status = "SAFE"
        road_status = "OPEN"
        emergency = "NORMAL"
        evacuation = False

    elif rainfall < 400:

        flood_status = "MODERATE"
        house_status = "MONITOR"
        road_status = "CAUTION"
        emergency = "WATCH"
        evacuation = False

    elif rainfall < 600:

        flood_status = "HIGH"
        house_status = "AT RISK"
        road_status = "RESTRICTED"
        emergency = "WARNING"
        evacuation = False

    elif rainfall < 800:

        flood_status = "VERY HIGH"
        house_status = "SEVERELY AT RISK"
        road_status = "DANGEROUS"
        emergency = "HIGH ALERT"
        evacuation = True

    else:

        flood_status = "EXTREME"
        house_status = "SEVERELY AFFECTED"
        road_status = "BLOCKED"
        emergency = "EMERGENCY"
        evacuation = True

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
            "🌊 Water Level",
            f"{water_level:.2f} m"
        )

    with c3:
        st.metric(
            "🌊 Flood Depth",
            f"{flood_depth:.2f} m"
        )

    with c4:
        st.metric(
            "🧠 Risk Score",
            f"{risk_score}/100"
        )

    # ---------------- OVERALL ----------------

    st.subheader("📊 Overall Flood Risk")

    st.progress(
        int(min(risk_score, 100))
    )

    if flood_status == "LOW":

        st.success(
            "🟢 SAFE — No critical flood condition detected."
        )

    elif flood_status == "MODERATE":

        st.info(
            "🟡 MODERATE — Flood conditions should be monitored."
        )

    elif flood_status == "HIGH":

        st.warning(
            "🟠 HIGH — Residential areas may experience flooding."
        )

    elif flood_status == "VERY HIGH":

        st.warning(
            "🟠 VERY HIGH — Severe flooding is developing."
        )

    else:

        st.error(
            "🔴 EXTREME — Severe residential flooding detected."
        )

    # ---------------- RISK FACTORS ----------------

    st.divider()

    st.header("🔍 Risk Factors")

    r1, r2 = st.columns(2)

    with r1:

        st.write(
            f"🌧️ **Rainfall Risk:** {rainfall_risk:.1f}%"
        )

        st.progress(
            int(rainfall_risk)
        )

        st.write(
            f"🌊 **Water-Level Risk:** {water_risk:.1f}%"
        )

        st.progress(
            int(water_risk)
        )

    with r2:

        st.write(
            f"🌊 **Flood-Depth Risk:** {depth_risk:.1f}%"
        )

        st.progress(
            int(depth_risk)
        )

        st.write(
            f"🏠 **Residential Impact:** {house_status}"
        )

    # ---------------- RESIDENTIAL ----------------

    st.divider()

    st.header("🏠 Residential Area Assessment")

    h1, h2, h3 = st.columns(3)

    with h1:
        st.metric(
            "🏠 House Condition",
            house_status
        )

    with h2:
        st.metric(
            "🚗 Road Condition",
            road_status
        )

    with h3:
        st.metric(
            "🚨 Emergency Level",
            emergency
        )

    # ---------------- ANIMATION ----------------

    st.divider()

    st.header("🎬 Live Flood Simulation")

    animation = st.empty()

    stages = [
        "🌧️ RAINFALL DETECTED",
        "🌧️ HEAVY RAINFALL DEVELOPING",
        "🌊 WATER LEVEL RISING",
        "🌊 FLOODING RESIDENTIAL AREA",
        "🧠 N-SAGE ANALYSING RISK"
    ]

    for stage in stages:

        animation.markdown(
            f"""
            <div style="
                height:220px;
                background:linear-gradient(#536878,#263238);
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

    animation.markdown(
        f"""
        <div style="
            height:220px;
            background:linear-gradient(#607d8b,#1565c0);
            border-radius:15px;
            display:flex;
            align-items:center;
            justify-content:center;
            color:white;
            font-size:26px;
            font-weight:bold;
            text-align:center;
        ">
            🌊 FLOOD DEPTH: {flood_depth:.2f} m
            <br>
            🧠 RISK: {risk_score}/100
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- EMERGENCY ----------------

    st.divider()

    st.header("🚨 Emergency Response")

    if evacuation:

        st.error(
            "🚨 EVACUATION RECOMMENDED"
        )

        st.warning(
            "Severe simulated flooding detected. "
            "Move toward the designated safe zone."
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

            🏫 SAFE ZONE

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.success(
            "🟢 NO EVACUATION REQUIRED "
            "under the current simulated condition."
        )

    # ---------------- FINAL ----------------

    st.divider()

    st.header("📋 N-SAGE Final Assessment")

    st.write(
        f"🌧️ **Rainfall:** {rainfall} mm"
    )

    st.write(
        f"🌊 **Estimated Water Level:** "
        f"{water_level:.2f} m"
    )

    st.write(
        f"🌊 **Estimated Flood Depth:** "
        f"{flood_depth:.2f} m"
    )

    st.write(
        f"🧠 **N-SAGE Risk Score:** "
        f"{risk_score}/100"
    )

    st.write(
        f"🌊 **Flood Classification:** "
        f"{flood_status}"
    )

    st.write(
        f"🏠 **Residential Condition:** "
        f"{house_status}"
    )

    st.write(
        f"🚗 **Road Condition:** "
        f"{road_status}"
    )

    st.write(
        f"🚨 **Emergency Level:** "
        f"{emergency}"
    )

    st.write(
        "🏃 **Evacuation:** "
        + ("RECOMMENDED" if evacuation else "NOT REQUIRED")
    )

    st.info(
        "⚠️ N-SAGE is a prototype demonstration system. "
        "Risk scores, thresholds, simulations, diversion "
        "recommendations and evacuation responses are "
        "illustrative only."
    )
