import streamlit as st

# ============================================================
# N-SAGE
# AI-Based Flood & Bridge Failure Analysis
# ============================================================

st.set_page_config(
    page_title="N-SAGE",
    page_icon="🛰️",
    layout="wide"
)

# ============================================================
# PAGE STYLE
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 0;
}

.subtitle {
    font-size: 20px;
    color: #777;
    margin-bottom: 20px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 20px;
}

.emergency-box {
    padding: 25px;
    border-radius: 15px;
    background: #350707;
    border: 2px solid #ff3333;
    color: white;
    text-align: center;
}

.safe-box {
    padding: 25px;
    border-radius: 15px;
    background: #063b18;
    border: 2px solid #22cc66;
    color: white;
    text-align: center;
}

.route-box {
    padding: 25px;
    border-radius: 15px;
    background: #071f35;
    border: 2px solid #249cff;
    color: white;
    text-align: center;
    margin-top: 15px;
}

.big-route {
    font-size: 32px;
    font-weight: bold;
    margin: 20px 0;
}

.route-arrow {
    font-size: 35px;
    margin: 5px;
}

.alert-text {
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🛰️ N-SAGE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Based Flood & Bridge Failure Analysis System'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "N-SAGE analyses simulated flood conditions, "
    "evaluates bridge risk and generates an "
    "emergency response scenario."
)

st.divider()


# ============================================================
# WATER LEVEL INPUT
# ============================================================

st.markdown(
    '<div class="section-title">🌊 Select Water Level</div>',
    unsafe_allow_html=True
)

water_level = st.slider(
    "Water Level (metres)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.1
)

st.metric(
    "Selected Water Level",
    f"{water_level:.1f} m"
)

analyse = st.button(
    "🔍 ANALYSE & START N-SAGE",
    use_container_width=True
)


# ============================================================
# RISK ENGINE
# ============================================================

def analyse_risk(level):

    flood_risk = min(level * 10, 100)

    bridge_risk = min(level * 11, 100)

    structural_stress = min(level * 12, 100)

    river_risk = min(level * 10, 100)

    risk_score = (
        flood_risk * 0.25
        + bridge_risk * 0.30
        + structural_stress * 0.30
        + river_risk * 0.15
    )

    risk_score = min(risk_score, 100)

    # Flood classification

    if level < 2:
        flood_status = "LOW"

    elif level < 4:
        flood_status = "MODERATE"

    elif level < 6:
        flood_status = "HIGH"

    elif level < 8:
        flood_status = "SEVERE"

    else:
        flood_status = "MASSIVE"

    # Bridge classification

    if level < 3:

        bridge_status = "STABLE"
        collapse = False

    elif level < 5:

        bridge_status = "AT RISK"
        collapse = False

    elif level < 7:

        bridge_status = "CRITICAL"
        collapse = False

    else:

        bridge_status = "FAILURE SCENARIO"
        collapse = True

    return (
        flood_risk,
        bridge_risk,
        structural_stress,
        river_risk,
        risk_score,
        flood_status,
        bridge_status,
        collapse
    )


# ============================================================
# ANALYSIS
# ============================================================

if analyse:

    (
        flood_risk,
        bridge_risk,
        structural_stress,
        river_risk,
        risk_score,
        flood_status,
        bridge_status,
        collapse
    ) = analyse_risk(water_level)


    # ========================================================
    # AUTOMATIC ANALYSIS
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🧠 N-SAGE Automatic Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🌊 Flood",
            flood_status
        )

    with c2:

        st.metric(
            "🌉 Bridge Risk",
            f"{bridge_risk:.0f}%"
        )

    with c3:

        st.metric(
            "⚠️ Structural Stress",
            f"{structural_stress:.0f}%"
        )

    with c4:

        st.metric(
            "🧠 Risk Score",
            f"{risk_score:.1f}/100"
        )


    # ========================================================
    # OVERALL RISK
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '📊 Overall Risk'
        '</div>',
        unsafe_allow_html=True
    )

    st.progress(int(risk_score))

    if risk_score < 25:

        st.success(
            "🟢 SAFE — No critical flood condition detected."
        )

    elif risk_score < 50:

        st.warning(
            "🟡 WARNING — Increased monitoring recommended."
        )

    elif risk_score < 75:

        st.warning(
            "🟠 CRITICAL — Significant simulated flood stress."
        )

    else:

        st.error(
            "🔴 EXTREME — Simulated bridge failure condition."
        )


    # ========================================================
    # RISK FACTORS
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '🔍 Risk Factors'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"🌧️ **Flood Risk:** {flood_risk:.1f}%"
        )

        st.progress(int(flood_risk))

        st.write(
            f"🌊 **River Risk:** {river_risk:.1f}%"
        )

        st.progress(int(river_risk))

    with col2:

        st.write(
            f"🌉 **Bridge Risk:** {bridge_risk:.1f}%"
        )

        st.progress(int(bridge_risk))

        st.write(
            f"⚠️ **Structural Stress:** "
            f"{structural_stress:.1f}%"
        )

        st.progress(int(structural_stress))


    # ========================================================
    # BRIDGE ASSESSMENT
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🌉 Bridge Assessment'
        '</div>',
        unsafe_allow_html=True
    )

    if collapse:

        st.error("🔴 BRIDGE FAILURE CONDITION")

        st.error(
            "⚠️ STRUCTURAL FAILURE DETECTED"
        )

        st.error(
            "💥 COLLAPSE SCENARIO ACTIVATED"
        )

    elif water_level >= 5:

        st.warning(
            "🟠 BRIDGE CRITICAL — "
            "High simulated structural stress."
        )

    elif water_level >= 3:

        st.warning(
            "🟡 BRIDGE AT RISK — "
            "Monitoring recommended."
        )

    else:

        st.success(
            "🟢 BRIDGE STABLE"
        )


    # ========================================================
    # AI ANALYSIS
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '🧠 N-SAGE AI Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    if collapse:

        st.error(
            f"At {water_level:.1f} m water level, "
            "the simulated conditions have entered "
            "the bridge-failure zone."
        )

        st.write(
            "🌊 **Flood condition:** MASSIVE"
        )

        st.write(
            "⚠️ **Structural condition:** "
            "EXTREME SIMULATED STRESS"
        )

        st.write(
            "🌉 **Bridge decision:** "
            "CLOSE BRIDGE"
        )

        st.write(
            "🚨 **Emergency response:** "
            "ACTIVATED"
        )

    elif water_level >= 5:

        st.warning(
            "High simulated flood stress detected. "
            "Continuous monitoring is recommended."
        )

    else:

        st.success(
            "The selected water level is below the "
            "prototype failure threshold."
        )


    # ========================================================
    # REALISTIC BRIDGE SIMULATION
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🎬 Live Flood & Bridge Simulation'
        '</div>',
        unsafe_allow_html=True
    )


    if collapse:

        animation_mode = "collapse"

        status_text = (
            "⚠️ STRUCTURAL FAILURE DETECTED"
        )

    else:

        animation_mode = "normal"

        status_text = (
            "🌉 BRIDGE UNDER FLOOD MONITORING"
        )


    # ========================================================
    # SIMULATION
    # ========================================================

    simulation_html = f"""
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

    height: 620px;

    overflow: hidden;

    background:
        linear-gradient(
            to bottom,
            #101a28,
            #293f51,
            #17242e
        );
}}


/* CAMERA SHAKE */

.collapse {{
    animation:
        cameraShake 7s forwards;
}}

@keyframes cameraShake {{

    0%,55% {{
        transform: translate(0,0);
    }}

    60% {{
        transform: translate(-2px,2px);
    }}

    62% {{
        transform: translate(3px,-2px);
    }}

    64% {{
        transform: translate(-3px,1px);
    }}

    66% {{
        transform: translate(2px,-2px);
    }}

    70%,100% {{
        transform: translate(0,0);
    }}
}}


/* TITLE */

.title {{
    position: absolute;

    top: 18px;

    width: 100%;

    text-align: center;

    color: white;

    font-size: 27px;

    font-weight: bold;

    z-index: 100;

    text-shadow:
        0 3px 8px black;
}}


/* STATUS */

.status {{
    position: absolute;

    top: 65px;

    left: 50%;

    transform:
        translateX(-50%);

    padding:
        10px 22px;

    border-radius: 8px;

    background:
        rgba(190,0,0,.9);

    color: white;

    font-weight: bold;

    z-index: 100;

    white-space: nowrap;
}}


/* CLOUDS */

.cloud {{
    position: absolute;

    width: 190px;

    height: 55px;

    background: #3b4854;

    border-radius: 50px;

    z-index: 5;
}}

.cloud.one {{
    top: 85px;
    left: 7%;
}}

.cloud.two {{
    top: 105px;
    right: 7%;
}}


/* RAIN */

.rain {{
    position: absolute;

    width: 100%;
    height: 100%;

    background-image:
        repeating-linear-gradient(
            105deg,
            transparent 0px,
            transparent 13px,
            rgba(220,240,255,.45) 14px,
            transparent 17px
        );

    animation:
        rainMove .3s linear infinite;

    z-index: 8;
}}

@keyframes rainMove {{

    from {{
        background-position: 0 0;
    }}

    to {{
        background-position: -35px 120px;
    }}
}}


/* LAND */

.land {{
    position: absolute;

    bottom: 270px;

    left: 0;

    width: 100%;

    height: 155px;

    background:
        linear-gradient(
            145deg,
            #465744,
            #20352b
        );

    clip-path:
        polygon(
            0 62%,
            12% 35%,
            23% 57%,
            36% 25%,
            48% 52%,
            61% 28%,
            74% 53%,
            86% 26%,
            100% 43%,
            100% 100%,
            0 100%
        );

    z-index: 2;
}}


/* WATER */

.water {{
    position: absolute;

    left: 0;

    bottom: 0;

    width: 100%;

    height: 285px;

    background:
        linear-gradient(
            to bottom,
            #168ce5,
            #0969ba,
            #043f7b
        );

    z-index: 5;

    animation:
        waterRise 7s ease-in forwards,
        waterCurrent 1.4s ease-in-out infinite alternate;
}}

@keyframes waterRise {{

    0% {{
        height: 220px;
    }}

    50% {{
        height: 250px;
    }}

    100% {{
        height: 315px;
    }}
}}

@keyframes waterCurrent {{

    from {{
        transform: translateX(-3px);
    }}

    to {{
        transform: translateX(7px);
    }}
}}


/* WAVES */

.wave {{
    position: absolute;

    left: -5%;

    width: 110%;

    height: 25px;

    border-top:
        6px solid rgba(210,245,255,.8);

    border-radius: 50%;

    z-index: 26;

    animation:
        waveMove 1s linear infinite;
}}

.wave.one {{
    bottom: 285px;
}}

.wave.two {{
    bottom: 250px;

    opacity: .45;
}}

@keyframes waveMove {{

    0% {{
        transform: translateX(-35px);
    }}

    50% {{
        transform: translateX(35px);
    }}

    100% {{
        transform: translateX(-35px);
    }}
}}


/* PIERS */

.pier {{
    position: absolute;

    top: 295px;

    width: 58px;

    height: 230px;

    background:
        linear-gradient(
            90deg,
            #303438,
            #b9bdc0,
            #65696c,
            #303438
        );

    z-index: 22;

    transform-origin:
        bottom center;
}}

.pier.left {{
    left: 27%;
}}

.pier.right {{
    right: 27%;
}}


/* PIER FAILURE */

.collapse .pier.left {{
    animation:
        pierFailure 7s forwards;
}}

@keyframes pierFailure {{

    0%,48% {{
        transform: rotate(0deg);
    }}

    55% {{
        transform: rotate(-2deg);
    }}

    62% {{
        transform: rotate(-8deg);
    }}

    70% {{
        transform: rotate(-18deg);
    }}

    100% {{
        transform: rotate(-24deg);
    }}
}}


/* BRIDGE DECK */

.deck {{
    position: absolute;

    top: 240px;

    height: 58px;

    background:
        linear-gradient(
            to bottom,
            #d2d4d5,
            #777b7d,
            #424648
        );

    border-bottom:
        5px solid #25282a;

    z-index: 30;

    box-shadow:
        0 6px 12px rgba(0,0,0,.7);
}}


/* ROAD */

.deck::before {{
    content: "";

    position: absolute;

    top: 7px;
    left: 0;

    width: 100%;
    height: 12px;

    background:
        #202224;
}}


/* ROAD MARKING */

.deck::after {{
    content: "";

    position: absolute;

    top: 11px;
    left: 0;

    width: 100%;
    height: 4px;

    background:
        repeating-linear-gradient(
            90deg,
            #f4d45b 0px,
            #f4d45b 28px,
            transparent 28px,
            transparent 52px
        );
}}


/* SECTIONS */

.deck.left {{
    left: 8%;
    width: 42%;

    transform-origin:
        right center;
}}

.deck.middle {{
    left: 50%;

    width: 17%;

    transform:
        translateX(-50%);

    transform-origin:
        center center;
}}

.deck.right {{
    right: 8%;

    width: 42%;

    transform-origin:
        left center;
}}


/* LEFT FAILURE */

.collapse .deck.left {{
    animation:
        leftFailure 7s forwards;
}}

@keyframes leftFailure {{

    0%,45% {{
        transform: rotate(0deg);
    }}

    52% {{
        transform: rotate(-1deg);
    }}

    60% {{
        transform: rotate(-5deg);
    }}

    68% {{
        transform:
            rotate(-12deg)
            translateY(25px);
    }}

    82% {{
        transform:
            rotate(-22deg)
            translateY(100px);
    }}

    100% {{
        transform:
            rotate(-34deg)
            translateY(210px);
    }}
}}


/* CENTER FAILURE */

.collapse .deck.middle {{
    animation:
        middleFailure 7s forwards;
}}

@keyframes middleFailure {{

    0%,45% {{
        transform:
            translateX(-50%)
            rotate(0deg);
    }}

    52% {{
        transform:
            translateX(-50%)
            rotate(1deg);
    }}

    60% {{
        transform:
            translateX(-50%)
            rotate(7deg)
            translateY(20px);
    }}

    72% {{
        transform:
            translateX(-50%)
            rotate(22deg)
            translateY(100px);
    }}

    86% {{
        transform:
            translateX(-50%)
            rotate(45deg)
            translateY(220px);
    }}

    100% {{
        transform:
            translateX(-50%)
            rotate(70deg)
            translateY(380px);
    }}
}}


/* RIGHT FAILURE */

.collapse .deck.right {{
    animation:
        rightFailure 7s forwards;
}}

@keyframes rightFailure {{

    0%,50% {{
        transform: rotate(0deg);
    }}

    60% {{
        transform: rotate(3deg);
    }}

    70% {{
        transform:
            rotate(10deg)
            translateY(30px);
    }}

    84% {{
        transform:
            rotate(21deg)
            translateY(110px);
    }}

    100% {{
        transform:
            rotate(33deg)
            translateY(210px);
    }}
}}


/* CRACKS */

.crack {{
    position: absolute;

    top: 228px;

    width: 5px;

    height: 72px;

    background:
        #e31c1c;

    z-index: 60;

    opacity: 0;

    transform:
        rotate(15deg);

    box-shadow:
        0 0 8px red;

    animation:
        crackAppear 7s forwards;
}}

.crack.one {{
    left: 48%;
}}

.crack.two {{
    left: 52%;

    height: 58px;

    transform:
        rotate(-18deg);
}}

@keyframes crackAppear {{

    0%,42% {{
        opacity: 0;
    }}

    50% {{
        opacity: .2;
    }}

    57% {{
        opacity: .8;
    }}

    65%,100% {{
        opacity: 1;
    }}
}}


/* DEBRIS */

.debris {{
    position: absolute;

    width: 18px;

    height: 12px;

    background:
        #777;

    z-index: 45;

    opacity: 0;
}}

.debris.one {{
    left: 47%;
    top: 270px;
}}

.debris.two {{
    left: 53%;
    top: 275px;
}}

.debris.three {{
    left: 50%;
    top: 260px;
}}

.collapse .debris.one {{
    animation:
        debrisFall 7s forwards;
}}

.collapse .debris.two {{
    animation:
        debrisFall2 7s forwards;
}}

.collapse .debris.three {{
    animation:
        debrisFall3 7s forwards;
}}

@keyframes debrisFall {{

    0%,60% {{
        opacity: 0;

        transform:
            translate(0,0)
            rotate(0deg);
    }}

    70% {{
        opacity: 1;
    }}

    100% {{
        opacity: 1;

        transform:
            translate(-100px,300px)
            rotate(180deg);
    }}
}}

@keyframes debrisFall2 {{

    0%,60% {{
        opacity: 0;

        transform:
            translate(0,0)
            rotate(0deg);
    }}

    70% {{
        opacity: 1;
    }}

    100% {{
        opacity: 1;

        transform:
            translate(120px,310px)
            rotate(220deg);
    }}
}}

@keyframes debrisFall3 {{

    0%,60% {{
        opacity: 0;

        transform:
            translate(0,0)
            rotate(0deg);
    }}

    70% {{
        opacity: 1;
    }}

    100% {{
        opacity: 1;

        transform:
            translate(10px,340px)
            rotate(270deg);
    }}
}}


/* SPLASH */

.splash {{
    position: absolute;

    left: 50%;

    bottom: 55px;

    width: 220px;

    height: 120px;

    transform:
        translateX(-50%);

    opacity: 0;

    z-index: 65;

    animation:
        splashAppear 7s forwards;
}}

.splash::before,
.splash::after {{

    content: "";

    position: absolute;

    bottom: 0;

    width: 28px;

    height: 90px;

    border-left:
        7px solid rgba(220,250,255,.9);

    border-radius: 50%;
}}

.splash::before {{
    left: 35px;

    transform:
        rotate(-30deg);
}}

.splash::after {{
    right: 35px;

    transform:
        rotate(30deg);
}}

@keyframes splashAppear {{

    0%,68% {{
        opacity: 0;

        transform:
            translateX(-50%)
            scale(.4);
    }}

    75% {{
        opacity: 1;

        transform:
            translateX(-50%)
            scale(1.2);
    }}

    88%,100% {{
        opacity: .75;

        transform:
            translateX(-50%)
            scale(1);
    }}
}}


/* FINAL MESSAGE */

.final-message {{
    position: absolute;

    left: 50%;

    bottom: 150px;

    transform:
        translateX(-50%);

    padding:
        14px 25px;

    background:
        rgba(160,0,0,.92);

    border:
        2px solid #ff5b5b;

    border-radius: 10px;

    color: white;

    font-size: 21px;

    font-weight: bold;

    z-index: 120;

    opacity: 0;

    animation:
        finalMessage 7s forwards;
}}

@keyframes finalMessage {{

    0%,78% {{
        opacity: 0;
    }}

    85%,100% {{
        opacity: 1;
    }}
}}


/* WATER LABEL */

.water-label {{
    position: absolute;

    bottom: 20px;

    left: 20px;

    color: white;

    font-size: 19px;

    font-weight: bold;

    z-index: 110;

    text-shadow:
        0 2px 6px black;
}}

</style>

</head>

<body>

<div class="scene {animation_mode}">

    <div class="cloud one"></div>

    <div class="cloud two"></div>

    <div class="rain"></div>

    <div class="title">
        🌊 N-SAGE FLOOD FAILURE SIMULATION
    </div>

    <div class="status">
        {status_text}
    </div>

    <div class="land"></div>

    <div class="pier left"></div>

    <div class="pier right"></div>

    <div class="deck left"></div>

    <div class="deck middle"></div>

    <div class="deck right"></div>

    <div class="crack one"></div>

    <div class="crack two"></div>

    <div class="debris one"></div>

    <div class="debris two"></div>

    <div class="debris three"></div>

    <div class="water"></div>

    <div class="wave one"></div>

    <div class="wave two"></div>

    <div class="splash"></div>

    <div class="final-message">
        💥 BRIDGE COLLAPSE DETECTED
    </div>

    <div class="water-label">
        🌊 WATER LEVEL: {water_level:.1f} m
    </div>

</div>

</body>

</html>
"""

    st.components.v1.html(
        simulation_html,
        height=640,
        scrolling=False
    )


    # ========================================================
    # SIMULATION RESULT
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '📊 Simulation Result'
        '</div>',
        unsafe_allow_html=True
    )

    if collapse:

        st.error(
            "💥 SIMULATION COMPLETE — "
            "BRIDGE COLLAPSE SCENARIO DETECTED"
        )

    else:

        st.success(
            f"🌉 SIMULATION COMPLETE — "
            f"BRIDGE STATUS: {bridge_status}"
        )


    # ========================================================
    # 🚨 AUTOMATIC BRIDGE CLOSURE + DIVERSION
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🚨 Emergency Traffic Management'
        '</div>',
        unsafe_allow_html=True
    )

    if collapse:

        st.markdown(
            """
            <div class="emergency-box">

                <div class="alert-text">
                    🚨 BRIDGE CLOSED
                </div>

                <p>
                    N-SAGE has automatically activated
                    the simulated emergency traffic response.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="route-box">

                <div class="big-route">
                    ❌ 🌉
                </div>

                <div class="route-arrow">
                    ↓ DIVERSION ↓
                </div>

                <div class="big-route">
                    🚗 ─────────────────→
                </div>

                <div style="font-size:24px;">
                    🟢 SAFE ROUTE
                </div>

                <br>

                <div style="font-size:18px;">
                    📍 Alternative crossing identified
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("### 🛣️ Traffic Response")

        t1, t2, t3 = st.columns(3)

        with t1:

            st.error(
                "🚧 BRIDGE CLOSED"
            )

            st.write(
                "Access restricted in the simulated scenario."
            )

        with t2:

            st.info(
                "↪️ DIVERSION ACTIVATED"
            )

            st.write(
                "Traffic redirected toward an alternative crossing."
            )

        with t3:

            st.success(
                "🟢 SAFE ROUTE"
            )

            st.write(
                "Alternative route recommended."
            )

        st.write("### 📡 Emergency Status")

        st.success(
            "✅ Flood risk analysed"
        )

        st.success(
            "✅ Bridge risk assessed"
        )

        st.success(
            "✅ Failure scenario detected"
        )

        st.success(
            "✅ Bridge closure activated"
        )

        st.success(
            "✅ Traffic diversion generated"
        )

        st.success(
            "✅ Alternative crossing identified"
        )

    else:

        st.markdown(
            """
            <div class="safe-box">

                <h2>🟢 BRIDGE OPEN</h2>

                <p>
                    No emergency traffic diversion
                    is required under the current
                    simulated conditions.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # RISK MAP
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '🗺️ N-SAGE Flood & Traffic Risk Map'
        '</div>',
        unsafe_allow_html=True
    )

    if water_level < 2:

        zone_size = 120
        zone_status = "🟢 SAFE ZONE"
        road_status = "🟢 ROAD OPEN"

    elif water_level < 4:

        zone_size = 180
        zone_status = "🟡 MONITORING ZONE"
        road_status = "🟡 MONITORING"

    elif water_level < 6:

        zone_size = 250
        zone_status = "🟠 HIGH-RISK FLOOD ZONE"
        road_status = "🟠 PREPARE CLOSURE"

    elif water_level < 8:

        zone_size = 320
        zone_status = "🔴 CRITICAL BRIDGE ZONE"
        road_status = "🔴 ROAD CLOSURE"

    else:

        zone_size = 390
        zone_status = "🚨 EXTREME EMERGENCY ZONE"
        road_status = "🚨 BRIDGE CLOSED"


    # ========================================================
    # MAP HTML
    # ========================================================

    map_html = f"""
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
}}

.map {{
    position: relative;

    width: 100%;

    height: 500px;

    overflow: hidden;

    border-radius: 15px;

    border: 3px solid #555;

    background:
        linear-gradient(
            135deg,
            #c8d8b0,
            #a8c49a
        );
}}

.road {{
    position: absolute;

    background: #454545;

    z-index: 2;
}}

.horizontal {{
    top: 225px;

    left: 0;

    width: 100%;

    height: 70px;
}}

.vertical {{
    left: 48%;

    top: 0;

    width: 75px;

    height: 100%;
}}

.flood {{
    position: absolute;

    left: 50%;

    top: 260px;

    width: {zone_size}px;

    height: {zone_size}px;

    transform:
        translate(-50%, -50%);

    border-radius: 50%;

    background:
        rgba(20,130,230,.45);

    border:
        4px solid rgba(0,80,200,.8);

    z-index: 5;
}}

.critical {{
    position: absolute;

    left: 50%;

    top: 260px;

    width: 145px;

    height: 145px;

    transform:
        translate(-50%, -50%);

    border-radius: 50%;

    background:
        rgba(220,30,30,.4);

    border:
        3px solid red;

    z-index: 7;
}}

.bridge {{
    position: absolute;

    left: 50%;

    top: 235px;

    width: 145px;

    height: 52px;

    transform:
        translateX(-50%);

    background:
        linear-gradient(
            #ddd,
            #777
        );

    border:
        4px solid #333;

    z-index: 20;
}}

.bridge::after {{
    content: "🌉";

    position: absolute;

    left: 50%;

    top: 5px;

    transform:
        translateX(-50%);

    font-size: 28px;
}}

.label {{
    position: absolute;

    left: 50%;

    top: 175px;

    transform:
        translateX(-50%);

    padding:
        8px 15px;

    border-radius: 8px;

    background:
        rgba(0,0,0,.85);

    color: white;

    font-weight: bold;

    z-index: 30;

    white-space: nowrap;
}}

.status {{
    position: absolute;

    left: 20px;

    top: 20px;

    padding:
        12px 18px;

    border-radius: 10px;

    background:
        rgba(0,0,0,.85);

    color: white;

    font-weight: bold;

    z-index: 50;
}}

.level {{
    position: absolute;

    bottom: 20px;

    left: 20px;

    padding:
        12px 18px;

    border-radius: 10px;

    background:
        rgba(0,70,150,.9);

    color: white;

    font-weight: bold;

    z-index: 50;
}}

.roadstatus {{
    position: absolute;

    bottom: 20px;

    right: 20px;

    padding:
        12px 18px;

    border-radius: 10px;

    background:
        rgba(0,0,0,.85);

    color: white;

    font-weight: bold;

    z-index: 50;
}}

</style>

</head>

<body>

<div class="map">

    <div class="road horizontal"></div>

    <div class="road vertical"></div>

    <div class="flood"></div>

    <div class="critical"></div>

    <div class="bridge"></div>

    <div class="label">
        🌉 BRIDGE
    </div>

    <div class="status">
        {zone_status}
    </div>

    <div class="level">
        🌊 WATER LEVEL:
        {water_level:.1f} m
    </div>

    <div class="roadstatus">
        {road_status}
    </div>

</div>

</body>

</html>
"""

    st.components.v1.html(
        map_html,
        height=520,
        scrolling=False
    )


    # ========================================================
    # FINAL ASSESSMENT
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-title">'
        '📋 N-SAGE Final Assessment'
        '</div>',
        unsafe_allow_html=True
    )

    f1, f2 = st.columns(2)

    with f1:

        st.write(
            f"🌊 **Water Level:** "
            f"{water_level:.1f} m"
        )

        st.write(
            f"🌊 **Flood Severity:** "
            f"{flood_status}"
        )

        st.write(
            f"🧠 **Risk Score:** "
            f"{risk_score:.1f}/100"
        )

    with f2:

        st.write(
            f"🌉 **Bridge Status:** "
            f"{bridge_status}"
        )

        st.write(
            f"⚠️ **Structural Stress:** "
            f"{structural_stress:.1f}%"
        )

        if collapse:

            st.write(
                "🚨 **Emergency:** "
                "BRIDGE CLOSED"
            )

            st.write(
                "↪️ **Traffic:** "
                "DIVERSION ACTIVATED"
            )

        else:

            st.write(
                "🟢 **Emergency:** "
                "NORMAL"
            )


    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.divider()

    st.info(
        "⚠️ N-SAGE is a prototype simulation. "
        "Risk thresholds, calculations, bridge-failure "
        "animation, traffic diversion and emergency "
        "responses are illustrative. They must not be "
        "treated as real structural engineering predictions "
        "or real emergency navigation instructions."
    )

