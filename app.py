import streamlit as st
import os

# ============================================================
# N-SAGE MAIN DASHBOARD
# ============================================================

st.set_page_config(
    page_title="N-SAGE",
    page_icon="🛰️",
    layout="wide"
)

# Multi-Page Navigation - Session State Maintenance
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 58px;
    font-weight: 900;
    margin-bottom: 0;
}

.subtitle {
    font-size: 23px;
    margin-top: 5px;
    margin-bottom: 25px;
    color: #777;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(
        135deg,
        rgba(40,100,160,0.15),
        rgba(30,30,30,0.08)
    );
    border: 1px solid rgba(120,120,120,0.3);
}

.card {
    padding: 25px;
    border-radius: 20px;
    min-height: 230px;
    border: 1px solid rgba(120,120,120,0.3);
    background: rgba(120,120,120,0.07);
}

.card-title {
    font-size: 27px;
    font-weight: 800;
}

.card-text {
    font-size: 16px;
    line-height: 1.7;
    color: #777;
}

.flow {
    padding: 18px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid rgba(120,120,120,0.25);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION CONTROLLER
# ============================================================

def run_selected_page(page_name):
    base_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_folder, page_name)
    
    if os.path.exists(file_path):
        if st.sidebar.button("⬅️ Back to Main Dashboard", type="secondary"):
            st.session_state.page = "dashboard"
            st.rerun()
        
        st.sidebar.divider()
        st.sidebar.info(f"Currently Running: **{page_name}**")
        
        # Selected python file-ஐ இயக்க
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
            exec(code, globals())
    else:
        st.error(f"❌ {page_name} does not exist.")
        st.warning("Create the required Python file in the same folder as app.py.")
        if st.button("⬅️ Return to Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

# ============================================================
# MAIN DASHBOARD VIEW
# ============================================================

if st.session_state.page == "dashboard":

    # HEADER
    st.markdown('<div class="main-title">🛰️ N-SAGE</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">AI-Based Multi-Disaster Risk Analysis & Emergency Response System</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
    <b>N-SAGE</b> is a prototype disaster-risk simulation platform designed to analyse environmental conditions and demonstrate possible disaster scenarios.
    <br><br>
    🌧️ Environmental Conditions → 🧠 Risk Analysis → 🎬 Disaster Simulation → 🚨 Emergency Assessment → 🗺️ Response
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # DISASTER SELECTION
    st.header("🚨 Select Disaster Scenario")

    disaster = st.radio(
        "Choose the disaster you want to analyse:",
        [
            "🌉 Bridge Collapse",
            "⛰️ Landslide",
            "🏠 Residential Flood"
        ],
        horizontal=True
    )

    st.divider()

    # DISASTER CARDS
    if disaster == "🌉 Bridge Collapse":
        st.markdown("""
        <div class="card">
        <div class="card-title">🌉 Bridge Collapse</div>
        <br>
        <div class="card-text">
        Simulates the effect of extreme rainfall and rising water conditions on a bridge.
        <br><br>
        🌧️ Rainfall / Water Level → 🌊 Flood Condition → 🌉 Bridge Risk → 💥 Structural Failure Simulation → 🛣️ Traffic Diversion
        </div>
        </div>
        """, unsafe_allow_html=True)
        selected_file = "bridge.py"

    elif disaster == "⛰️ Landslide":
        st.markdown("""
        <div class="card">
        <div class="card-title">⛰️ Landslide</div>
        <br>
        <div class="card-text">
        Simulates rainfall-induced slope instability and possible road blockage.
        <br><br>
        🌧️ Rainfall → ⛰️ Slope Instability → 🪨 Landslide Simulation → 🚧 Road Blockage → 🛣️ Safe Diversion
        </div>
        </div>
        """, unsafe_allow_html=True)
        selected_file = "landslide.py"

    else:
        st.markdown("""
        <div class="card">
        <div class="card-title">🏠 Residential Flood</div>
        <br>
        <div class="card-text">
        Simulates increasing rainfall, flood depth and residential impact.
        <br><br>
        🌧️ Rainfall → 🌊 Flood Formation → 🏠 Residential Impact → 🚨 Emergency Assessment → 🧭 Evacuation Response
        </div>
        </div>
        """, unsafe_allow_html=True)
        selected_file = "flood.py"

    # SIMULATION CONTROL
    st.divider()
    st.header("🎬 Simulation Control")
    st.write(f"### Selected Scenario: {disaster}")

    if st.button("🚀 START SELECTED SIMULATION", use_container_width=True, type="primary"):
        st.session_state.page = selected_file
        st.rerun()

    # SYSTEM OVERVIEW
    st.divider()
    st.header("🧠 N-SAGE Disaster Intelligence")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🌉 Infrastructure", "Bridge Collapse")
        st.caption("Flood-induced bridge failure simulation")
    with c2:
        st.metric("⛰️ Geohazard", "Landslide")
        st.caption("Rainfall-induced slope failure simulation")
    with c3:
        st.metric("🏠 Urban", "Residential Flood")
        st.caption("Residential flood and evacuation simulation")

    # COMMON WORKFLOW
    st.divider()
    st.header("⚙️ N-SAGE Common Workflow")

    steps = st.columns(5)
    with steps[0]:
        st.markdown('<div class="flow"><h2>🌧️</h2><b>Environmental Input</b><br><small>Rainfall / water conditions</small></div>', unsafe_allow_html=True)
    with steps[1]:
        st.markdown('<div class="flow"><h2>🧠</h2><b>Risk Analysis</b><br><small>Risk score calculation</small></div>', unsafe_allow_html=True)
    with steps[2]:
        st.markdown('<div class="flow"><h2>🎬</h2><b>Simulation</b><br><small>Visual disaster scenario</small></div>', unsafe_allow_html=True)
    with steps[3]:
        st.markdown('<div class="flow"><h2>🚨</h2><b>Emergency Assessment</b><br><small>Severity detection</small></div>', unsafe_allow_html=True)
    with steps[4]:
        st.markdown('<div class="flow"><h2>🗺️</h2><b>Response</b><br><small>Diversion / evacuation</small></div>', unsafe_allow_html=True)

    # MODULE STATUS
    st.divider()
    st.header("📡 System Module Status")

    base_folder = os.path.dirname(os.path.abspath(__file__))
    modules = [
        ("🌉 Bridge Collapse", "bridge.py"),
        ("⛰️ Landslide", "landslide.py"),
        ("🏠 Residential Flood", "flood.py")
    ]

    for module_name, filename in modules:
        path = os.path.join(base_folder, filename)
        if os.path.exists(path):
            st.success(f"🟢 {module_name} — READY")
        else:
            st.warning(f"🟡 {module_name} — FILE NOT FOUND")

    # DISCLAIMER
    st.divider()
    st.info(
        "⚠️ N-SAGE is a prototype demonstration system. "
        "Risk scores, thresholds, simulations, diversion "
        "recommendations and evacuation responses are "
        "illustrative only and must not be treated as real "
        "structural engineering predictions or real-world "
        "emergency-navigation instructions."
    )

# ============================================================
# MODULE EXECUTION VIEW
# ============================================================
else:
    run_selected_page(st.session_state.page)
