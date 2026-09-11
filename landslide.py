import streamlit as st

st.set_page_config(
    page_title="N-SAGE Landslide",
    page_icon="🏔️",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

if "diversion" not in st.session_state:
    st.session_state.diversion = False

# ============================================================
# HEADER
# ============================================================

st.title("🛰️ N-SAGE")

st.subheader(
    "AI-Based Landslide Risk Analysis & Smart Diversion System"
)

st.write(
    "Select the rainfall level. N-SAGE automatically evaluates "
    "landslide risk, road safety and emergency response."
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
    value=100,
    step=10
)

st.metric(
    "🌧️ Selected Rainfall",
    f"{rainfall} mm"
)

# ============================================================
# RISK CALCULATION
# ============================================================

soil_saturation = min(rainfall / 10, 100)

slope_stress = min(rainfall * 0.11, 100)

landslide_index = min(rainfall * 0.12, 100)

overall_risk = round(
    soil_saturation * 0.25
    + slope_stress * 0.30
    + landslide_index * 0.45,
    1
)

# ============================================================
# RISK CLASSIFICATION
# ============================================================

if rainfall < 200:

    slope_status = "STABLE"
    affected_zone = "MINIMAL"
    emergency_level = "NORMAL"

    warning = False
    road_blocked = False
    evacuation = False

elif rainfall < 400:

    slope_status = "MONITORING"
    affected_zone = "LOW"
    emergency_level = "WATCH"

    warning = False
    road_blocked = False
    evacuation = False

elif rainfall < 600:

    slope_status = "UNSTABLE"
    affected_zone = "MODERATE"
    emergency_level = "WARNING"

    warning = True
    road_blocked = False
    evacuation = False

elif rainfall < 750:

    slope_status = "CRITICAL"
    affected_zone = "HIGH"
    emergency_level = "ALERT"

    warning = True
    road_blocked = True
    evacuation = True

else:

    slope_status = "CRITICAL"
    affected_zone = "VERY HIGH"
    emergency_level = "EMERGENCY"

    warning = True
    road_blocked = True
    evacuation = True

# ============================================================
# ANALYSE BUTTON
# ============================================================

if st.button(
    "🔍 ANALYSE & START SIMULATION",
    use_container_width=True
):

    # Reset diversion when a new analysis starts
    st.session_state.diversion = False

    st.divider()

    # ========================================================
    # AUTOMATIC ANALYSIS
    # ========================================================

    st.header("🧠 N-SAGE Automatic Analysis")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌧️ Rainfall",
            f"{rainfall} mm"
        )

    with c2:
        st.metric(
            "💧 Soil Saturation",
            f"{soil_saturation:.0f}%"
        )

    with c3:
        st.metric(
            "⚠️ Slope Stress",
            f"{slope_stress:.0f}%"
        )

    with c4:
        st.metric(
            "🏔️ Landslide Risk",
            f"{landslide_index:.0f}%"
        )

    # ========================================================
    # OVERALL RISK
    # ========================================================

    st.subheader("📊 Overall Risk")

    st.progress(
        min(int(overall_risk), 100)
    )

    st.write(
        f"### 🧠 N-SAGE Risk Score: **{overall_risk}/100**"
    )

    if overall_risk < 25:

        st.success(
            "🟢 SAFE — No critical landslide condition detected."
        )

    elif overall_risk < 50:

        st.info(
            "🟡 MONITOR — Increased slope monitoring recommended."
        )

    elif overall_risk < 75:

        st.warning(
            "🟠 HIGH RISK — Significant slope instability detected."
        )

    else:

        st.error(
            "🔴 EXTREME — Critical landslide scenario detected."
        )

    # ========================================================
    # RISK FACTORS
    # ========================================================

    st.header("🔍 Risk Factors")

    r1, r2 = st.columns(2)

    with r1:

        st.write(
            f"🌧️ **Rainfall Risk:** "
            f"{min(rainfall / 10, 100):.1f}%"
        )

        st.progress(
            min(int(rainfall / 10), 100)
        )

        st.write(
            f"💧 **Soil Saturation:** "
            f"{soil_saturation:.1f}%"
        )

        st.progress(
            int(soil_saturation)
        )

    with r2:

        st.write(
            f"⚠️ **Slope Stress:** "
            f"{slope_stress:.1f}%"
        )

        st.progress(
            int(slope_stress)
        )

        st.write(
            f"🏔️ **Landslide Index:** "
            f"{landslide_index:.1f}%"
        )

        st.progress(
            int(landslide_index)
        )

    # ========================================================
    # SLOPE ASSESSMENT
    # ========================================================

    st.divider()

    st.header("🏔️ Slope Assessment")

    if slope_status == "STABLE":

        st.success(
            "🟢 Slope Status: STABLE"
        )

    elif slope_status == "MONITORING":

        st.info(
            "🟡 Slope Status: UNDER MONITORING"
        )

    elif slope_status == "UNSTABLE":

        st.warning(
            "🟠 Slope Status: UNSTABLE"
        )

    else:

        st.error(
            "🔴 Slope Status: CRITICAL"
        )

    # ========================================================
    # IMPACT ANALYSIS
    # ========================================================

    st.header("📍 Potential Impact Zone")

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "📍 Affected Zone",
            affected_zone
        )

    with p2:

        st.metric(
            "🚧 Infrastructure Risk",
            "HIGH" if road_blocked else "LOW"
        )

    with p3:

        st.metric(
            "🚨 Emergency Level",
            emergency_level
        )

    # ========================================================
    # EMERGENCY RESPONSE
    # ========================================================

    st.header("🚨 Emergency Response")

    if evacuation:

        st.error(
            "🚨 CRITICAL LANDSLIDE CONDITION"
        )

        st.write(
            "🏃 **Evacuation:** RECOMMENDED"
        )

        st.write(
            "🚧 **Road Access:** RESTRICTED"
        )

        st.write(
            "📡 **Emergency Alert:** ACTIVATED"
        )

        st.write(
            "👀 **Continuous Monitoring:** REQUIRED"
        )

    elif warning:

        st.warning(
            "⚠️ WARNING — Slope instability detected."
        )

        st.write(
            "👀 Increase slope and rainfall monitoring."
        )

        st.write(
            "🚧 Prepare for possible road restrictions."
        )

    else:

        st.success(
            "🟢 NORMAL — No emergency response activated."
        )

    # ========================================================
    # LIVE SIMULATION
    # ========================================================

    st.divider()

    st.header("🎬 Live Landslide Simulation")

    if rainfall >= 600:

        slide_state = "slide-active"
        rock_state = "rock-active"
        dust_state = "dust-active"
        debris_state = "debris-active"
        blockage_state = "blockage-active"

    else:

        slide_state = "slide-stable"
        rock_state = "rock-stable"
        dust_state = "dust-stable"
        debris_state = "debris-stable"
        blockage_state = "blockage-stable"

    if rainfall >= 400:

        crack_state = "crack-active"

    else:

        crack_state = "crack-hidden"

    if rainfall >= 750:

        status_text = "🔴 MAJOR LANDSLIDE — DIVERSION REQUIRED"

    elif rainfall >= 600:

        status_text = "🔴 LANDSLIDE SCENARIO ACTIVATED"

    elif rainfall >= 400:

        status_text = "🟠 SLOPE INSTABILITY DETECTED"

    elif rainfall >= 200:

        status_text = "🟡 SLOPE UNDER MONITORING"

    else:

        status_text = "🟢 SLOPE STABLE"

    # ========================================================
    # LANDSLIDE ANIMATION
    # ========================================================

    html = f"""
<!DOCTYPE html>

<html>

<head>

<style>

* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    font-family: Arial, sans-serif;
}}

.scene {{
    position: relative;
    width: 100%;
    height: 700px;
    overflow: hidden;

    background:
        linear-gradient(
            to bottom,
            #071322 0%,
            #172b42 48%,
            #344535 100%
        );
}}

.moon {{
    position: absolute;
    right: 12%;
    top: 85px;

    width: 70px;
    height: 70px;

    border-radius: 50%;

    background: #e5e1c9;

    box-shadow:
        0 0 35px rgba(230,230,200,.25);

    opacity: .8;

    z-index: 2;
}}

.cloud {{
    position: absolute;

    width: 220px;
    height: 55px;

    background: #374653;

    border-radius: 50px;

    opacity: .85;

    z-index: 5;
}}

.cloud::before {{
    content: "";

    position: absolute;

    width: 90px;
    height: 90px;

    left: 30px;
    top: -45px;

    border-radius: 50%;

    background: #374653;
}}

.cloud::after {{
    content: "";

    position: absolute;

    width: 110px;
    height: 110px;

    right: 20px;
    top: -55px;

    border-radius: 50%;

    background: #374653;
}}

.cloud1 {{
    left: 4%;
    top: 100px;
}}

.cloud2 {{
    right: 5%;
    top: 145px;
}}

.rain {{
    position: absolute;

    inset: 0;

    z-index: 15;

    background-image:
        repeating-linear-gradient(
            105deg,
            transparent 0px,
            transparent 17px,
            rgba(170,220,255,.38) 18px,
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
        background-position: -35px 110px;
    }}
}}

.ground {{
    position: absolute;

    left: 0;
    bottom: 0;

    width: 100%;
    height: 185px;

    background:
        linear-gradient(
            to bottom,
            #3c4d3c,
            #202b23
        );

    z-index: 8;
}}

.mountain {{
    position: absolute;

    left: 4%;
    bottom: 140px;

    width: 92%;
    height: 440px;

    background:
        linear-gradient(
            145deg,
            #78806e 0%,
            #626958 28%,
            #505646 55%,
            #3d4237 78%,
            #292e28 100%
        );

    clip-path:
        polygon(
            0% 100%,
            5% 90%,
            11% 80%,
            15% 72%,
            21% 67%,
            27% 53%,
            32% 47%,
            37% 34%,
            42% 28%,
            47% 14%,
            51% 4%,
            54% 13%,
            59% 25%,
            63% 31%,
            68% 44%,
            73% 48%,
            79% 61%,
            84% 70%,
            91% 84%,
            96% 91%,
            100% 100%
        );

    z-index: 10;
}}

.mountain-light {{
    position: absolute;

    left: 4%;
    bottom: 140px;

    width: 92%;
    height: 440px;

    background:
        linear-gradient(
            115deg,
            rgba(170,175,150,.38),
            transparent 46%
        );

    clip-path:
        polygon(
            0% 100%,
            5% 90%,
            11% 80%,
            15% 72%,
            21% 67%,
            27% 53%,
            32% 47%,
            37% 34%,
            42% 28%,
            47% 14%,
            51% 4%,
            54% 13%,
            59% 25%,
            63% 31%,
            68% 44%,
            73% 48%,
            79% 61%,
            84% 70%,
            91% 84%,
            96% 91%,
            100% 100%
        );

    z-index: 11;
}}

.rock-layer {{
    position: absolute;

    background: #343931;

    opacity: .75;

    z-index: 14;

    clip-path:
        polygon(
            0 20%,
            25% 0,
            60% 20%,
            100% 10%,
            80% 100%,
            20% 90%
        );
}}

.rock1 {{
    left: 13%;
    bottom: 305px;

    width: 260px;
    height: 80px;

    transform: rotate(-12deg);
}}

.rock2 {{
    left: 64%;
    bottom: 295px;

    width: 300px;
    height: 85px;

    transform: rotate(9deg);
}}

.rock3 {{
    left: 28%;
    bottom: 400px;

    width: 180px;
    height: 60px;

    transform: rotate(-6deg);
}}

.tree {{
    position: absolute;

    width: 5px;
    height: 35px;

    background: #27362a;

    z-index: 22;
}}

.tree::before {{
    content: "";

    position: absolute;

    left: -13px;
    top: -18px;

    width: 32px;
    height: 32px;

    border-radius: 50%;

    background: #314c32;
}}

.tree1 {{
    left: 17%;
    bottom: 285px;
}}

.tree2 {{
    left: 25%;
    bottom: 345px;

    transform: scale(.8);
}}

.tree3 {{
    left: 74%;
    bottom: 295px;

    transform: scale(.9);
}}

.tree4 {{
    left: 83%;
    bottom: 255px;

    transform: scale(.7);
}}

.soil {{
    position: absolute;

    left: 37%;
    bottom: 245px;

    width: 34%;
    height: 155px;

    background:
        linear-gradient(
            145deg,
            #80694d,
            #654d37 45%,
            #3f3024
        );

    clip-path:
        polygon(
            0 20%,
            16% 9%,
            34% 0,
            53% 12%,
            74% 5%,
            100% 31%,
            86% 100%,
            23% 91%
        );

    z-index: 28;
}}

.stream {{
    position: absolute;

    width: 7px;

    border-radius: 20px;

    background:
        linear-gradient(
            to bottom,
            rgba(190,230,250,.85),
            rgba(70,150,190,.65)
        );

    transform-origin: top;

    z-index: 32;

    animation:
        waterDown 2.2s linear infinite;
}}

.stream1 {{
    left: 42%;
    top: 240px;

    height: 150px;

    transform: rotate(14deg);
}}

.stream2 {{
    left: 49%;
    top: 270px;

    height: 180px;

    transform: rotate(-4deg);

    animation-delay: .4s;
}}

.stream3 {{
    left: 57%;
    top: 305px;

    height: 150px;

    transform: rotate(-18deg);

    animation-delay: .8s;
}}

@keyframes waterDown {{

    0% {{
        opacity: .25;

        transform:
            translateY(-15px)
            scaleY(.65)
            rotate(10deg);
    }}

    50% {{
        opacity: .85;
    }}

    100% {{
        opacity: .15;

        transform:
            translateY(55px)
            scaleY(1)
            rotate(10deg);
    }}
}}

.slide-stable,
.slide-active {{

    position: absolute;

    left: 41%;
    bottom: 280px;

    width: 27%;
    height: 145px;

    background:
        linear-gradient(
            145deg,
            #806c52,
            #654e38,
            #3d3026
        );

    clip-path:
        polygon(
            0 15%,
            20% 4%,
            40% 0,
            65% 11%,
            100% 37%,
            84% 100%,
            24% 90%
        );

    z-index: 38;
}}

.slide-active {{
    animation:
        naturalSlide
        8s
        cubic-bezier(.35,.05,.2,1)
        forwards;
}}

@keyframes naturalSlide {{

    0% {{
        transform: translate(0,0) rotate(0deg);
    }}

    20% {{
        transform: translate(-2px,5px) rotate(.5deg);
    }}

    38% {{
        transform: translate(-10px,25px) rotate(1deg);
    }}

    55% {{
        transform: translate(-35px,70px) rotate(4deg);
    }}

    72% {{
        transform: translate(-75px,135px) rotate(8deg);
    }}

    88% {{
        transform: translate(-120px,205px) rotate(13deg);
    }}

    100% {{
        transform: translate(-165px,270px) rotate(18deg);
    }}
}}

.crack-hidden {{
    opacity: 0;
}}

.crack-active {{

    position: absolute;

    left: 50%;
    bottom: 335px;

    width: 5px;
    height: 120px;

    background: #171512;

    transform: rotate(18deg);

    z-index: 50;

    animation:
        crackAppear
        8s
        ease-in
        forwards;
}}

@keyframes crackAppear {{

    0%,25% {{
        opacity: 0;
        height: 0;
    }}

    42% {{
        opacity: 1;
        height: 45px;
    }}

    55% {{
        opacity: 1;
        height: 120px;
    }}

    100% {{
        opacity: 0;
    }}
}}

.road {{

    position: absolute;

    left: -3%;
    bottom: 42px;

    width: 106%;
    height: 90px;

    background:
        linear-gradient(
            to bottom,
            #555754,
            #353936
        );

    transform: rotate(-2deg);

    z-index: 55;
}}

.road::after {{

    content: "";

    position: absolute;

    top: 42px;
    left: 0;

    width: 100%;
    height: 5px;

    background:
        repeating-linear-gradient(
            90deg,
            #e4cf68 0px,
            #e4cf68 42px,
            transparent 42px,
            transparent 80px
        );
}}

.debris-active {{

    position: absolute;

    left: 35%;
    bottom: 55px;

    width: 430px;
    height: 150px;

    z-index: 72;

    opacity: 0;

    animation:
        debrisAppear
        8s
        ease-out
        forwards;
}}

.debris-active::before {{

    content: "";

    position: absolute;

    width: 70px;
    height: 45px;

    left: 70px;
    bottom: 25px;

    border-radius: 50%;

    background: #594635;

    box-shadow:
        80px -20px 0 #66513c,
        150px 5px 0 #44362a,
        225px -10px 0 #72583e,
        300px 20px 0 #4d3b2c;
}}

@keyframes debrisAppear {{

    0%,65% {{
        opacity: 0;
        transform: translateY(-80px);
    }}

    80% {{
        opacity: .7;
        transform: translateY(-10px);
    }}

    100% {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.dust-active {{

    position: absolute;

    left: 18%;
    bottom: 70px;

    width: 600px;
    height: 270px;

    background:
        radial-gradient(
            ellipse at center,
            rgba(190,180,155,.72),
            rgba(150,140,120,.42) 35%,
            rgba(100,95,85,.18) 60%,
            transparent 76%
        );

    filter: blur(5px);

    z-index: 80;

    opacity: 0;

    animation:
        dustExplosion
        8s
        ease-out
        forwards;
}}

@keyframes dustExplosion {{

    0%,62% {{
        opacity: 0;
        transform: scale(.2);
    }}

    72% {{
        opacity: .35;
        transform: scale(.65);
    }}

    83% {{
        opacity: .75;
        transform: scale(1);
    }}

    94% {{
        opacity: .8;
        transform: scale(1.35);
    }}

    100% {{
        opacity: .5;
        transform: scale(1.6);
    }}
}}

.blockage-active {{

    position: absolute;

    left: 37%;
    bottom: 50px;

    width: 370px;
    height: 130px;

    background:
        linear-gradient(
            145deg,
            #70563c,
            #4e3929,
            #33271e
        );

    clip-path:
        polygon(
            0 60%,
            12% 25%,
            28% 33%,
            42% 5%,
            60% 27%,
            78% 12%,
            100% 58%,
            90% 100%,
            12% 100%
        );

    z-index: 82;

    opacity: 0;

    animation:
        blockageAppear
        8s
        ease-out
        forwards;
}}

@keyframes blockageAppear {{

    0%,72% {{
        opacity: 0;
        transform: translateY(-80px);
    }}

    84% {{
        opacity: .7;
        transform: translateY(-15px);
    }}

    100% {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.warning-active {{

    position: absolute;

    left: 12%;
    bottom: 230px;

    font-size: 55px;

    z-index: 100;

    animation:
        warningPulse
        1s
        infinite
        alternate;
}}

@keyframes warningPulse {{

    from {{
        transform: scale(1);
    }}

    to {{
        transform: scale(1.18);
    }}
}}

.title {{

    position: absolute;

    top: 18px;

    width: 100%;

    text-align: center;

    color: white;

    font-size: 27px;

    font-weight: bold;

    z-index: 150;

    text-shadow:
        0 3px 8px black;
}}

.status {{

    position: absolute;

    top: 62px;
    left: 50%;

    transform: translateX(-50%);

    padding: 10px 22px;

    border-radius: 10px;

    background:
        rgba(0,0,0,.78);

    color: white;

    font-weight: bold;

    z-index: 150;

    white-space: nowrap;
}}

.rain-label {{

    position: absolute;

    right: 25px;
    bottom: 20px;

    color: white;

    font-size: 18px;

    font-weight: bold;

    z-index: 150;

    text-shadow:
        0 2px 5px black;
}}

.timeline {{

    position: absolute;

    left: 25px;
    bottom: 20px;

    color: white;

    background:
        rgba(0,0,0,.55);

    padding: 8px 12px;

    border-radius: 7px;

    font-size: 14px;

    z-index: 150;
}}

</style>

</head>

<body>

<div class="scene">

<div class="moon"></div>

<div class="cloud cloud1"></div>

<div class="cloud cloud2"></div>

<div class="rain"></div>

<div class="title">
🏔️ N-SAGE LANDSLIDE SIMULATION
</div>

<div class="status">
{status_text}
</div>

<div class="ground"></div>

<div class="mountain"></div>

<div class="mountain-light"></div>

<div class="rock-layer rock1"></div>

<div class="rock-layer rock2"></div>

<div class="rock-layer rock3"></div>

<div class="tree tree1"></div>

<div class="tree tree2"></div>

<div class="tree tree3"></div>

<div class="tree tree4"></div>

<div class="soil"></div>

<div class="stream stream1"></div>

<div class="stream stream2"></div>

<div class="stream stream3"></div>

<div class="{slide_state}"></div>

<div class="{crack_state}"></div>

<div class="{debris_state}"></div>

<div class="{dust_state}"></div>

<div class="{blockage_state}"></div>

<div class="road"></div>

{
    '<div class="warning-active">⚠️</div>'
    if warning
    else ''
}

<div class="timeline">

🌧️ Rain
→ 💧 Saturation
→ ⚠️ Instability
→ 🏔️ Landslide
→ 🚧 Road Block
→ ↪️ Diversion

</div>

<div class="rain-label">

🌧️ RAINFALL: {rainfall} mm

</div>

</div>

</body>

</html>
"""

    st.components.v1.html(
        html,
        height=700,
        scrolling=False
    )

    # ========================================================
    # ROAD MAP
    # ========================================================

    st.divider()

    st.header("🗺️ N-SAGE Road Network")

    if road_blocked:

        st.error(
            "🚧 MAIN ROAD BLOCKED — LANDSLIDE DEBRIS DETECTED"
        )

        map_html = """
<!DOCTYPE html>

<html>

<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

.map {

    position: relative;

    width: 100%;
    height: 500px;

    background:
        linear-gradient(
            45deg,
            #d9e4d0 25%,
            transparent 25%
        ),
        linear-gradient(
            -45deg,
            #d9e4d0 25%,
            transparent 25%
        ),
        linear-gradient(
            45deg,
            transparent 75%,
            #d9e4d0 75%
        ),
        linear-gradient(
            -45deg,
            transparent 75%,
            #d9e4d0 75%
        );

    background-size: 80px 80px;

    background-color: #edf2e8;
}

.river {

    position: absolute;

    width: 100%;
    height: 75px;

    top: 190px;

    background: #7ab7d8;

    transform: rotate(-7deg);

    opacity: .8;
}

.main-road {

    position: absolute;

    width: 100%;
    height: 25px;

    top: 235px;

    background: #444;

    transform: rotate(-7deg);

    z-index: 5;
}

.road-line {

    position: absolute;

    width: 100%;
    height: 4px;

    top: 10px;

    background:
        repeating-linear-gradient(
            90deg,
            #fff 0px,
            #fff 35px,
            transparent 35px,
            transparent 65px
        );
}

.blocked {

    position: absolute;

    width: 150px;
    height: 45px;

    left: 44%;
    top: 205px;

    z-index: 20;

    transform: rotate(-7deg);

    background:
        repeating-linear-gradient(
            45deg,
            #e53935 0px,
            #e53935 15px,
            #222 15px,
            #222 30px
        );

    border: 3px solid white;

    box-shadow:
        0 0 15px rgba(255,0,0,.6);
}

.blocked-text {

    position: absolute;

    left: 42%;
    top: 155px;

    z-index: 30;

    background: #d71919;

    color: white;

    padding: 8px 14px;

    border-radius: 7px;

    font-weight: bold;
}

.diversion {

    position: absolute;

    width: 75%;
    height: 18px;

    left: 12%;
    top: 105px;

    border-top:
        9px dashed #20a84a;

    transform: rotate(10deg);

    z-index: 10;
}

.diversion-text {

    position: absolute;

    left: 25%;
    top: 55px;

    background: #168c3d;

    color: white;

    padding: 8px 15px;

    border-radius: 8px;

    font-weight: bold;

    z-index: 30;
}

.start {

    position: absolute;

    left: 8%;
    top: 215px;

    background: #1976d2;

    color: white;

    padding: 8px 12px;

    border-radius: 7px;

    z-index: 40;

    font-weight: bold;
}

.destination {

    position: absolute;

    right: 7%;
    top: 215px;

    background: #7b1fa2;

    color: white;

    padding: 8px 12px;

    border-radius: 7px;

    z-index: 40;

    font-weight: bold;
}

.landslide {

    position: absolute;

    left: 42%;
    top: 295px;

    font-size: 50px;

    z-index: 30;
}

.legend {

    position: absolute;

    right: 20px;
    bottom: 20px;

    background:
        rgba(255,255,255,.95);

    padding: 15px;

    border-radius: 10px;

    z-index: 50;

    line-height: 1.8;
}

</style>

</head>

<body>

<div class="map">

<div class="river"></div>

<div class="main-road">

<div class="road-line"></div>

</div>

<div class="start">
📍 START
</div>

<div class="destination">
🏁 DESTINATION
</div>

<div class="blocked-text">
🚧 ROAD BLOCKED
</div>

<div class="blocked"></div>

<div class="landslide">
🏔️
</div>

<div class="diversion"></div>

<div class="diversion-text">
↪️ SAFE DIVERSION
</div>

<div class="legend">

<b>🗺️ N-SAGE MAP</b>

<br>

🔴 Blocked road

<br>

🟢 Alternative route

<br>

🏔️ Landslide zone

</div>

</div>

</body>

</html>
"""

        st.components.v1.html(
            map_html,
            height=500,
            scrolling=False
        )

        # ====================================================
        # DIVERSION BUTTON
        # ====================================================

        st.write("### 🚨 Route Decision")

        if st.button(
            "↪️ TAKE DIVERSION",
            use_container_width=True
        ):

            st.session_state.diversion = True

        if st.session_state.diversion:

            st.success(
                "🟢 DIVERSION ACTIVATED"
            )

            d1, d2, d3 = st.columns(3)

            with d1:

                st.metric(
                    "🚧 Main Road",
                    "BLOCKED"
                )

            with d2:

                st.metric(
                    "🛣️ Alternative Route",
                    "OPEN"
                )

            with d3:

                st.metric(
                    "🚗 Traffic",
                    "REDIRECTED"
                )

            st.info(
                "↪️ N-SAGE has activated the simulated "
                "alternative route to avoid the landslide zone."
            )

    else:

        st.success(
            "🟢 MAIN ROAD OPEN — NO DIVERSION REQUIRED"
        )

    # ========================================================
    # FINAL ASSESSMENT
    # ========================================================

    st.divider()

    st.header("📋 N-SAGE Final Disaster Assessment")

    f1, f2 = st.columns(2)

    with f1:

        st.write(
            f"🌧️ **Rainfall:** {rainfall} mm"
        )

        st.write(
            f"💧 **Soil Saturation:** "
            f"{soil_saturation:.1f}%"
        )

        st.write(
            f"⚠️ **Slope Stress:** "
            f"{slope_stress:.1f}%"
        )

        st.write(
            f"🏔️ **Landslide Risk:** "
            f"{landslide_index:.1f}%"
        )

    with f2:

        st.write(
            f"📍 **Affected Zone:** "
            f"{affected_zone}"
        )

        st.write(
            f"🚨 **Emergency Level:** "
            f"{emergency_level}"
        )

        st.write(
            f"🧠 **N-SAGE Risk Score:** "
            f"{overall_risk}/100"
        )

        st.write(
            "🚧 **Main Road:** "
            + (
                "BLOCKED"
                if road_blocked
                else "OPEN"
            )
        )

        st.write(
            "↪️ **Diversion:** "
            + (
                "ACTIVATED"
                if st.session_state.diversion
                else "NOT ACTIVATED"
            )
        )

    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.info(
        "⚠️ N-SAGE is a prototype disaster-risk visualization. "
        "The rainfall thresholds, risk scores, landslide animation "
        "and diversion route are illustrative. They are not real "
        "geological, geotechnical or navigation predictions."
    )
