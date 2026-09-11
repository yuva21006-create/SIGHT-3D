import streamlit as st

st.set_page_config(
    page_title="N-SAGE Residential Flood",
    page_icon="🌊",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("🛰️ N-SAGE")

st.subheader(
    "AI-Based Residential Flood Risk Analysis & Emergency Response"
)

st.write(
    "Select the expected rainfall and run the simulation. "
    "N-SAGE will automatically analyse the resulting flood "
    "conditions and determine the emergency response."
)

st.divider()

# ============================================================
# RAINFALL INPUT
# ============================================================

st.header("🌧️ Environmental Condition")

rainfall = st.slider(
    "Expected Rainfall (mm)",
    min_value=0,
    max_value=1000,
    value=300,
    step=10
)

st.metric(
    "🌧️ Selected Rainfall",
    f"{rainfall} mm"
)

# ============================================================
# SIMULATION BUTTON
# ============================================================

simulate = st.button(
    "🎬 SIMULATE FLOOD",
    use_container_width=True
)

# ============================================================
# ONLY ANALYSE AFTER BUTTON
# ============================================================

if simulate:

    # ========================================================
    # SIMULATION MODEL
    # ========================================================

    # Rainfall is the primary input.
    # These are prototype simulation relationships.

    if rainfall < 150:

        water_level = round(0.4 + rainfall * 0.002, 2)

    elif rainfall < 300:

        water_level = round(0.7 + rainfall * 0.003, 2)

    elif rainfall < 500:

        water_level = round(1.6 + (rainfall - 300) * 0.006, 2)

    elif rainfall < 700:

        water_level = round(2.8 + (rainfall - 500) * 0.012, 2)

    elif rainfall < 850:

        water_level = round(5.2 + (rainfall - 700) * 0.020, 2)

    else:

        water_level = round(8.2 + (rainfall - 850) * 0.012, 2)

    # Flood depth increases strongly during extreme rainfall.

    if rainfall < 200:

        flood_depth = round(water_level * 0.35, 2)

    elif rainfall < 400:

        flood_depth = round(water_level * 0.50, 2)

    elif rainfall < 600:

        flood_depth = round(water_level * 0.65, 2)

    elif rainfall < 800:

        flood_depth = round(water_level * 0.78, 2)

    else:

        flood_depth = round(water_level * 0.90, 2)

    # ========================================================
    # RISK SCORE
    # ========================================================

    # Rainfall itself is heavily weighted because it is
    # the primary input selected by the user.

    rainfall_risk = (rainfall / 1000) * 100

    water_risk = min(
        (water_level / 10) * 100,
        100
    )

    depth_risk = min(
        (flood_depth / 8) * 100,
        100
    )

    risk_score = round(
        rainfall_risk * 0.50
        + water_risk * 0.25
        + depth_risk * 0.25,
        1
    )

    # ========================================================
    # CLASSIFICATION
    # ========================================================

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

    # ========================================================
    # ANALYSIS
    # ========================================================

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
            "🌊 Estimated Water Level",
            f"{water_level:.2f} m"
        )

    with c3:
        st.metric(
            "🌊 Estimated Flood Depth",
            f"{flood_depth:.2f} m"
        )

    with c4:
        st.metric(
            "🧠 Risk Score",
            f"{risk_score}/100"
        )

    # ========================================================
    # OVERALL RISK
    # ========================================================

    st.subheader("📊 Overall Flood Risk")

    st.progress(
        min(int(risk_score), 100)
    )

    if rainfall < 200:

        st.success(
            "🟢 SAFE — No critical flood condition detected."
        )

    elif rainfall < 400:

        st.info(
            "🟡 MODERATE — Flood conditions should be monitored."
        )

    elif rainfall < 600:

        st.warning(
            "🟠 HIGH — Residential areas may experience flooding."
        )

    elif rainfall < 800:

        st.warning(
            "🟠 VERY HIGH — Severe flooding is developing. "
            "Prepare for evacuation."
        )

    else:

        st.error(
            "🔴 EXTREME — Severe residential flooding detected. "
            "Immediate evacuation response activated."
        )

    # ========================================================
    # RISK FACTORS
    # ========================================================

    st.divider()

    st.header("🔍 Risk Factors")

    r1, r2 = st.columns(2)

    with r1:

        st.write(
            f"🌧️ **Rainfall Risk:** "
            f"{rainfall_risk:.1f}%"
        )

        st.progress(
            int(rainfall_risk)
        )

        st.write(
            f"🌊 **Water-Level Risk:** "
            f"{water_risk:.1f}%"
        )

        st.progress(
            int(water_risk)
        )

    with r2:

        st.write(
            f"🌊 **Flood-Depth Risk:** "
            f"{depth_risk:.1f}%"
        )

        st.progress(
            int(depth_risk)
        )

        st.write(
            f"🏠 **Residential Impact:** "
            f"{house_status}"
        )

    # ========================================================
    # RESIDENTIAL ASSESSMENT
    # ========================================================

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

    # ========================================================
    # SIMULATION LEVEL
    # ========================================================

    if rainfall < 200:

        simulation_level = "low"

    elif rainfall < 400:

        simulation_level = "moderate"

    elif rainfall < 600:

        simulation_level = "high"

    elif rainfall < 800:

        simulation_level = "veryhigh"

    else:

        simulation_level = "extreme"

    # ========================================================
    # LIVE SIMULATION
    # ========================================================

    st.divider()

    st.header("🎬 Live Flood & Residential Simulation")

    html = f"""
<!DOCTYPE html>

<html>

<head>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}}

.scene {{
    position: relative;
    width: 100%;
    height: 650px;
    overflow: hidden;

    background:
        linear-gradient(
            to bottom,
            #25394c 0%,
            #526a7c 50%,
            #87977e 100%
        );
}}

/* CLOUDS */

.cloud {{
    position: absolute;
    width: 230px;
    height: 60px;
    border-radius: 50px;
    background: #37444f;
}}

.cloud::before {{
    content: "";
    position: absolute;
    left: 30px;
    top: -35px;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: #37444f;
}}

.cloud::after {{
    content: "";
    position: absolute;
    right: 25px;
    top: -45px;
    width: 95px;
    height: 95px;
    border-radius: 50%;
    background: #37444f;
}}

.cloud1 {{
    left: 5%;
    top: 75px;
}}

.cloud2 {{
    right: 5%;
    top: 110px;
}}

/* RAIN */

.rain {{
    position: absolute;
    inset: 0;
    z-index: 20;

    background-image:
        repeating-linear-gradient(
            105deg,
            transparent 0px,
            transparent 17px,
            rgba(200,230,255,.45) 18px,
            transparent 21px
        );

    animation:
        rainMove .45s linear infinite;
}}

@keyframes rainMove {{

    from {{
        background-position: 0 0;
    }}

    to {{
        background-position: -30px 100px;
    }}
}}

/* GROUND */

.ground {{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 250px;
    background:
        linear-gradient(
            to bottom,
            #51634d,
            #344438
        );
    z-index: 5;
}}

/* HOUSES */

.house {{
    position: absolute;
    bottom: 180px;
    width: 175px;
    height: 130px;
    background: #d8c29a;
    border: 5px solid #62503e;
    z-index: 30;
}}

.house1 {{
    left: 7%;
}}

.house2 {{
    left: 40%;
}}

.house3 {{
    right: 8%;
}}

.roof {{
    position: absolute;
    left: -20px;
    top: -72px;
    width: 210px;
    height: 100px;
    background: #744a38;

    clip-path:
        polygon(
            0 100%,
            50% 0,
            100% 100%
        );
}}

.window {{
    position: absolute;
    left: 20px;
    top: 30px;
    width: 42px;
    height: 48px;
    background: #8fc3d8;
    border: 5px solid #554737;
}}

.window2 {{
    left: 108px;
}}

.door {{
    position: absolute;
    left: 65px;
    bottom: 0;
    width: 45px;
    height: 72px;
    background: #634833;
    border: 4px solid #453126;
}}

/* ROAD */

.road {{
    position: absolute;
    left: 0;
    bottom: 90px;
    width: 100%;
    height: 80px;
    background: #454746;
    z-index: 15;
}}

.road-line {{
    position: absolute;
    top: 37px;
    width: 100%;
    height: 5px;

    background:
        repeating-linear-gradient(
            90deg,
            #e5d46c 0,
            #e5d46c 45px,
            transparent 45px,
            transparent 85px
        );
}}

/* CAR */

.car {{
    position: absolute;
    left: -120px;
    bottom: 120px;
    width: 105px;
    height: 45px;
    background: #b53232;
    border-radius: 18px 18px 8px 8px;
    z-index: 27;

    animation:
        carMove 7s linear infinite;
}}

.car::before {{
    content: "";
    position: absolute;
    left: 20px;
    top: -22px;
    width: 65px;
    height: 28px;
    background: #b53232;
    border-radius: 15px 15px 0 0;
}}

@keyframes carMove {{

    from {{
        left: -120px;
    }}

    to {{
        left: 110%;
    }}
}}

/* PERSON */

.person {{
    position: absolute;
    left: 67%;
    bottom: 155px;
    font-size: 42px;
    z-index: 35;

    animation:
        personMove 7s ease-in-out infinite;
}}

@keyframes personMove {{

    0%,100% {{
        transform: translateX(0);
    }}

    50% {{
        transform: translateX(120px);
    }}
}}

/* WATER */

.water-low,
.water-moderate,
.water-high,
.water-veryhigh,
.water-extreme {{
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;

    background:
        linear-gradient(
            to bottom,
            rgba(55,155,200,.75),
            rgba(20,82,135,.95)
        );

    border-top:
        5px solid rgba(210,240,255,.8);

    z-index: 40;

    animation:
        waterRise 5s ease-in-out forwards;
}}

.water-low {{
    height: 40px;
}}

.water-moderate {{
    height: 90px;
}}

.water-high {{
    height: 145px;
}}

.water-veryhigh {{
    height: 195px;
}}

.water-extreme {{
    height: 245px;
}}

@keyframes waterRise {{

    from {{
        transform: translateY(100%);
    }}

    to {{
        transform: translateY(0);
    }}
}}

/* WAVES */

.wave {{
    position: absolute;
    left: 0;
    top: -15px;
    width: 100%;
    height: 25px;

    background:
        repeating-radial-gradient(
            ellipse at 50% 100%,
            rgba(220,247,255,.75) 0,
            rgba(220,247,255,.75) 8px,
            transparent 9px,
            transparent 25px
        );

    animation:
        waveMove 2s linear infinite;
}}

@keyframes waveMove {{

    from {{
        background-position: 0 0;
    }}

    to {{
        background-position: 50px 0;
    }}
}}

/* SAFE ZONE */

.shelter {{
    position: absolute;
    right: 4%;
    top: 240px;

    padding: 14px 20px;

    background: #188a43;
    color: white;

    font-weight: bold;

    border-radius: 10px;

    z-index: 70;
}}

/* WARNING */

.warning {{
    position: absolute;
    left: 50%;
    top: 18px;

    transform: translateX(-50%);

    padding: 12px 25px;

    background: rgba(0,0,0,.80);
    color: white;

    border-radius: 10px;

    font-size: 20px;
    font-weight: bold;

    z-index: 100;

    white-space: nowrap;
}}

.info {{
    position: absolute;
    left: 20px;
    bottom: 18px;

    padding: 10px 15px;

    background: rgba(0,0,0,.65);

    color: white;

    border-radius: 8px;

    z-index: 100;
}}

</style>

</head>

<body>

<div class="scene">

<div class="cloud cloud1"></div>

<div class="cloud cloud2"></div>

<div class="rain"></div>

<div class="warning">

🌊 N-SAGE FLOOD SIMULATION

</div>

<div class="ground"></div>

<div class="house house1">

<div class="roof"></div>

<div class="window"></div>

<div class="window window2"></div>

<div class="door"></div>

</div>

<div class="house house2">

<div class="roof"></div>

<div class="window"></div>

<div class="window window2"></div>

<div class="door"></div>

</div>

<div class="house house3">

<div class="roof"></div>

<div class="window"></div>

<div class="window window2"></div>

<div class="door"></div>

</div>

<div class="road">

<div class="road-line"></div>

</div>

<div class="car"></div>

<div class="person">

🚶

</div>

<div class="shelter">

🏫 SAFE ZONE

</div>

<div class="water-{simulation_level}">

<div class="wave"></div>

</div>

<div class="info">

🌧️ Rainfall: {rainfall} mm

<br>

🌊 Water Level: {water_level:.2f} m

<br>

🧠 Risk: {risk_score}/100

</div>

</div>

</body>

</html>
"""

    st.components.v1.html(
        html,
        height=650,
        scrolling=False
    )

    # ========================================================
    # EMERGENCY RESPONSE
    # ========================================================

    st.divider()

    st.header("🚨 Emergency Response")

    if evacuation:

        st.error(
            "🚨 EVACUATION RECOMMENDED"
        )

        st.write(
            "N-SAGE has detected a severe simulated flood "
            "condition. Residents should move toward the "
            "designated safe zone."
        )

        st.success(
            "🗺️ SAFE EVACUATION ROUTE ACTIVATED"
        )

        # ====================================================
        # SIMPLE EVACUATION MAP
        # ====================================================

        route_html = """
<!DOCTYPE html>

<html>

<head>

<style>

body {
    margin: 0;
    overflow: hidden;
    font-family: Arial;
}

.map {

    position: relative;

    width: 100%;

    height: 430px;

    background:
        linear-gradient(
            45deg,
            #dce8d4 25%,
            transparent 25%
        ),
        linear-gradient(
            -45deg,
            #dce8d4 25%,
            transparent 25%
        );

    background-size: 70px 70px;

    background-color: #edf4e8;
}

.road {

    position: absolute;

    left: 0;
    top: 230px;

    width: 100%;
    height: 40px;

    background: #555;

    transform: rotate(-4deg);

    z-index: 5;
}

.flooded {

    position: absolute;

    left: 43%;
    top: 195px;

    width: 140px;
    height: 80px;

    background:
        repeating-linear-gradient(
            45deg,
            #d52222 0,
            #d52222 15px,
            #222 15px,
            #222 30px
        );

    transform: rotate(-4deg);

    z-index: 20;
}

.label {

    position: absolute;

    left: 41%;
    top: 145px;

    padding: 8px 14px;

    background: #d52222;

    color: white;

    font-weight: bold;

    border-radius: 8px;

    z-index: 30;
}

.route {

    position: absolute;

    left: 10%;
    top: 110px;

    width: 80%;
    height: 130px;

    border-top:
        10px dashed #1fa345;

    transform: rotate(7deg);

    z-index: 10;

    animation:
        pulse 1.5s infinite alternate;
}

@keyframes pulse {

    from {
        opacity: .5;
    }

    to {
        opacity: 1;
    }
}

.start {

    position: absolute;

    left: 5%;
    top: 220px;

    padding: 10px 15px;

    background: #1976d2;

    color: white;

    font-weight: bold;

    border-radius: 8px;

    z-index: 40;
}

.safe {

    position: absolute;

    right: 5%;
    top: 65px;

    padding: 15px;

    background: #168d40;

    color: white;

    font-weight: bold;

    border-radius: 10px;

    z-index: 40;
}

</style>

</head>

<body>

<div class="map">

<div class="road"></div>

<div class="flooded"></div>

<div class="label">

🚧 FLOODED ROAD

</div>

<div class="route"></div>

<div class="start">

📍 RESIDENTIAL AREA

</div>

<div class="safe">

🏫 SAFE ZONE

</div>

</div>

</body>

</html>
"""

        st.components.v1.html(
            route_html,
            height=430,
            scrolling=False
        )

    else:

        st.success(
            "🟢 NO EVACUATION REQUIRED under "
            "the current simulated condition."
        )

    # ========================================================
    # FINAL ASSESSMENT
    # ========================================================

    st.divider()

    st.header("📋 N-SAGE Final Assessment")

    f1, f2 = st.columns(2)

    with f1:

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

    with f2:

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
            + (
                "RECOMMENDED"
                if evacuation
                else "NOT REQUIRED"
            )
        )

    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.info(
        "⚠️ N-SAGE is a prototype disaster-risk "
        "visualization. Water level, flood depth, "
        "risk scores and thresholds are simulated "
        "values for demonstration and are not real "
        "flood forecasting or emergency-navigation "
        "predictions."
    )
