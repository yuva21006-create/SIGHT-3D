import streamlit as st
import time

st.set_page_config(
    page_title="N-SAGE Bridge Collapse",
    page_icon="🌉",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("🌉 N-SAGE — Bridge Collapse Analysis")

st.subheader(
    "AI-Based Flood-Induced Bridge Failure Simulation"
)

st.write(
    "Select the expected rainfall. N-SAGE will analyse "
    "the flood condition and simulate the possible impact "
    "on the bridge."
)

st.divider()

# ============================================================
# RAINFALL
# ============================================================

st.header("🌧️ Environmental Condition")

rainfall = st.slider(
    "Expected Rainfall (mm)",
    min_value=0,
    max_value=1000,
    value=500,
    step=10
)

st.metric(
    "🌧️ Selected Rainfall",
    f"{rainfall} mm"
)

# ============================================================
# SIMULATION
# ============================================================

if st.button(
    "🎬 START BRIDGE COLLAPSE SIMULATION",
    use_container_width=True
):

    # --------------------------------------------------------
    # FLOOD CALCULATION
    # --------------------------------------------------------

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

    water_level = round(water_level, 2)

    # --------------------------------------------------------
    # FLOOD DEPTH
    # --------------------------------------------------------

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

    flood_depth = round(flood_depth, 2)

    # --------------------------------------------------------
    # BRIDGE RISK
    # --------------------------------------------------------

    rainfall_risk = rainfall / 1000 * 100

    water_risk = min(
        water_level / 10 * 100,
        100
    )

    depth_risk = min(
        flood_depth / 8 * 100,
        100
    )

    bridge_risk = round(
        rainfall_risk * 0.35
        + water_risk * 0.30
        + depth_risk * 0.35,
        1
    )

    # --------------------------------------------------------
    # BRIDGE CONDITION
    # --------------------------------------------------------

    if bridge_risk < 25:

        bridge_status = "STABLE"
        structural_status = "NORMAL"
        collapse = False

    elif bridge_risk < 50:

        bridge_status = "MONITOR"
        structural_status = "STRESS DEVELOPING"
        collapse = False

    elif bridge_risk < 70:

        bridge_status = "CRITICAL"
        structural_status = "STRUCTURAL FAILURE RISK"
        collapse = False

    else:

        bridge_status = "CRITICAL"
        structural_status = "STRUCTURAL FAILURE DETECTED"
        collapse = True

    # ========================================================
    # RESULTS
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
            "🌉 Bridge Risk",
            f"{bridge_risk}/100"
        )

    # ========================================================
    # STATUS
    # ========================================================

    st.divider()

    st.header("🌉 Bridge Structural Assessment")

    b1, b2, b3 = st.columns(3)

    with b1:
        st.metric(
            "🌉 Bridge Condition",
            bridge_status
        )

    with b2:
        st.metric(
            "🏗️ Structural Status",
            structural_status
        )

    with b3:

        if collapse:
            st.metric(
                "🚨 Final Status",
                "COLLAPSE"
            )
        else:
            st.metric(
                "✅ Final Status",
                "NO COLLAPSE"
            )

    # ========================================================
    # WARNING
    # ========================================================

    if bridge_risk < 25:

        st.success(
            "🟢 BRIDGE STABLE — No critical structural "
            "failure detected in the simulation."
        )

    elif bridge_risk < 50:

        st.info(
            "🟡 MONITOR — Structural stress is developing. "
            "Continuous monitoring is recommended."
        )

    elif bridge_risk < 70:

        st.warning(
            "🟠 BRIDGE CRITICAL — Structural failure risk "
            "has been detected."
        )

    else:

        st.error(
            "🔴 STRUCTURAL FAILURE DETECTED — "
            "Bridge collapse scenario activated."
        )

    # ========================================================
    # SIMULATION ANIMATION
    # ========================================================

    st.divider()

    st.header("🎬 Live Bridge Simulation")

    # --------------------------------------------------------
    # HTML SCENE
    # --------------------------------------------------------

    if collapse:

        bridge_animation = """
        <style>

        .scene {
            position: relative;
            height: 500px;
            overflow: hidden;
            background:
                linear-gradient(
                    to bottom,
                    #283747,
                    #536878 55%,
                    #66785b
                );
            border-radius: 15px;
        }

        .rain {
            position: absolute;
            inset: 0;

            background-image:
                repeating-linear-gradient(
                    105deg,
                    transparent 0px,
                    transparent 16px,
                    rgba(210,235,255,.5) 17px,
                    transparent 20px
                );

            animation:
                rainmove .4s linear infinite;
        }

        @keyframes rainmove {

            from {
                background-position: 0 0;
            }

            to {
                background-position: -30px 100px;
            }

        }

        .water {

            position: absolute;

            bottom: 0;
            left: 0;

            width: 100%;
            height: 220px;

            background:
                linear-gradient(
                    to bottom,
                    #399bc7,
                    #125181
                );

        }

        .bridge {

            position: absolute;

            left: 15%;
            top: 230px;

            width: 70%;
            height: 35px;

            background: #777;

            z-index: 10;

            animation:
                collapsebridge 3s ease-in-out forwards;

        }

        @keyframes collapsebridge {

            0% {
                transform:
                    rotate(0deg)
                    translateY(0);
            }

            45% {
                transform:
                    rotate(0deg)
                    translateY(0);
            }

            70% {
                transform:
                    rotate(15deg)
                    translateY(35px);
            }

            100% {
                transform:
                    rotate(45deg)
                    translateY(150px);
                opacity: .3;
            }

        }

        .pillar1,
        .pillar2 {

            position: absolute;

            top: 265px;

            width: 30px;
            height: 130px;

            background: #555;

            z-index: 8;

        }

        .pillar1 {
            left: 30%;
        }

        .pillar2 {
            right: 30%;
        }

        .wave {

            position: absolute;

            left: 0;
            top: 0;

            width: 100%;
            height: 30px;

            background:
                repeating-radial-gradient(
                    ellipse at 50% 100%,
                    rgba(220,247,255,.8) 0,
                    rgba(220,247,255,.8) 8px,
                    transparent 9px,
                    transparent 25px
                );

            animation:
                wave 1.5s linear infinite;

        }

        @keyframes wave {

            from {
                background-position: 0 0;
            }

            to {
                background-position: 50px 0;
            }

        }

        .warning {

            position: absolute;

            top: 20px;
            left: 50%;

            transform:
                translateX(-50%);

            background:
                rgba(180,0,0,.9);

            color: white;

            padding: 15px 25px;

            border-radius: 10px;

            font-size: 22px;

            font-weight: bold;

            z-index: 50;

        }

        </style>

        <div class="scene">

            <div class="rain"></div>

            <div class="warning">
                🚨 BRIDGE COLLAPSE DETECTED
            </div>

            <div class="pillar1"></div>
            <div class="pillar2"></div>

            <div class="bridge"></div>

            <div class="water">
                <div class="wave"></div>
            </div>

        </div>
        """

    else:

        bridge_animation = """
        <style>

        .scene {

            position: relative;

            height: 500px;

            overflow: hidden;

            background:
                linear-gradient(
                    to bottom,
                    #78909c,
                    #b0bec5 55%,
                    #607d5b
                );

            border-radius: 15px;

        }

        .rain {

            position: absolute;

            inset: 0;

            background-image:
                repeating-linear-gradient(
                    105deg,
                    transparent 0px,
                    transparent 18px,
                    rgba(220,240,255,.4) 19px,
                    transparent 22px
                );

            animation:
                rainmove .5s linear infinite;

        }

        @keyframes rainmove {

            from {
                background-position: 0 0;
            }

            to {
                background-position: -30px 100px;
            }

        }

        .water {

            position: absolute;

            bottom: 0;

            left: 0;

            width: 100%;

            height: 150px;

            background:
                linear-gradient(
                    to bottom,
                    #48a9d4,
                    #14527e
                );

        }

        .bridge {

            position: absolute;

            left: 15%;

            top: 230px;

            width: 70%;

            height: 35px;

            background: #777;

            z-index: 10;

        }

        .pillar1,
        .pillar2 {

            position: absolute;

            top: 265px;

            width: 30px;

            height: 130px;

            background: #555;

            z-index: 8;

        }

        .pillar1 {
            left: 30%;
        }

        .pillar2 {
            right: 30%;
        }

        .wave {

            position: absolute;

            top: 0;

            width: 100%;

            height: 30px;

            background:
                repeating-radial-gradient(
                    ellipse at 50% 100%,
                    rgba(220,247,255,.8) 0,
                    rgba(220,247,255,.8) 8px,
                    transparent 9px,
                    transparent 25px
                );

        }

        .warning {

            position: absolute;

            top: 20px;

            left: 50%;

            transform:
                translateX(-50%);

            background:
                rgba(0,0,0,.75);

            color: white;

            padding: 15px 25px;

            border-radius: 10px;

            font-size: 22px;

            font-weight: bold;

            z-index: 50;

        }

        </style>

        <div class="scene">

            <div class="rain"></div>

            <div class="warning">
                🌉 BRIDGE UNDER MONITORING
            </div>

            <div class="pillar1"></div>
            <div class="pillar2"></div>

            <div class="bridge"></div>

            <div class="water">
                <div class="wave"></div>
            </div>

        </div>
        """

    st.components.v1.html(
        bridge_animation,
        height=500,
        scrolling=False
    )

    # ========================================================
    # EVENT SEQUENCE
    # ========================================================

    if collapse:

        st.divider()

        st.header("🚨 N-SAGE Event Sequence")

        st.write("🌧️ **1. Heavy rainfall detected**")
        st.write("🌊 **2. Flood conditions increased**")
        st.write("🌉 **3. Bridge reached critical condition**")
        st.write("🏗️ **4. Structural failure detected**")
        st.write("💥 **5. Bridge collapse scenario activated**")
        st.write("🚨 **6. Road closure recommended**")

        st.error(
            "🚧 BRIDGE CLOSED — Alternative route required."
        )

    else:

        st.divider()

        st.header("📋 N-SAGE Assessment")

        st.write(
            f"🌧️ Rainfall: **{rainfall} mm**"
        )

        st.write(
            f"🌊 Water Level: **{water_level:.2f} m**"
        )

        st.write(
            f"🌊 Flood Depth: **{flood_depth:.2f} m**"
        )

        st.write(
            f"🌉 Bridge Risk: **{bridge_risk}/100**"
        )

        st.write(
            f"🌉 Bridge Condition: **{bridge_status}**"
        )

        st.write(
            f"🏗️ Structural Status: **{structural_status}**"
        )

    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.divider()

    st.info(
        "⚠️ N-SAGE Bridge Collapse is a prototype "
        "disaster-risk visualization. The water levels, "
        "risk scores and structural thresholds are simulated "
        "values for demonstration and are not real "
        "engineering or emergency predictions."
    )
