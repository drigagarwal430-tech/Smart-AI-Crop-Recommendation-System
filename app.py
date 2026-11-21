
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from modules.prediction_engine import recommend_crop
from modules.explanation import explain_prediction
from database.save_records import save_farmer_record

from modules.knowledge_graph import (
    get_crop_factors,
    get_crop_subgraph,
    compare_crop_conditions
)


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌱",
    layout="wide"
)

# =====================================
# PREMIUM SMARTCROP AI DESIGN
# =====================================

st.markdown("""
<style>

/* SmartCrop dashboard theme */
:root {
    --ink: #17352b;
    --muted: #687b71;
    --green: #28734e;
    --line: #e3ebe4;
    --surface: #ffffff;
    --font-sans: "Segoe UI", "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: radial-gradient(ellipse at 88% 0%, #edf6ee 0%, transparent 34%), #f5f8f5;
    color: var(--ink);
    font-family: var(--font-sans);
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 2rem;
}

/* Hide default Streamlit decoration */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Main content spacing */
.block-container {
    padding: 2.2rem 2.5rem 3.5rem;
    max-width: 1500px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #153b2e 0%, #1c4b37 100%);
    border-right: 1px solid rgba(255,255,255,.08);
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Main headings */
h1, h2, h3 {
    color: var(--ink) !important;
    font-weight: 700 !important;
    letter-spacing: -0.025em;
    line-height: 1.2 !important;
}

h1 { font-size: clamp(2rem, 3vw, 2.8rem) !important; }
h2 { font-size: 1.65rem !important; }
h3 { font-size: 1.15rem !important; }
[data-testid="stMarkdownContainer"] p { color: var(--muted); line-height: 1.65; }
[data-testid="stVerticalBlockBorderWrapper"] { background: var(--surface); border: 1px solid var(--line); border-radius: 16px; box-shadow: 0 8px 26px rgba(24, 62, 43, .045); }

/* Sidebar section links */
.side-nav-link {
    align-items: center;
    border: 1px solid transparent;
    border-radius: 10px;
    color: #e4efe7 !important;
    display: flex;
    gap: 0.8rem;
    margin: 0.25rem 0;
    padding: 0.72rem 0.8rem;
    text-decoration: none !important;
    transition: background-color 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
}

.side-nav-link:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.12);
    color: #ffffff !important;
    transform: translateX(2px);
}

.side-nav-index {
    color: #a9cbb4 !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.08em;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #28734e, #205c40);
    color: white;
    border: none;
    border-radius: 11px;
    min-height: 2.8rem;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    box-shadow: 0 5px 14px rgba(40, 115, 78, .18);
    transition: transform .18s ease, box-shadow .18s ease;
}

.stButton > button:hover {
    background: #173f32;
    color: white;
    border: none;
    transform: translateY(-1px);
    box-shadow: 0 8px 18px rgba(40, 115, 78, .24);
}

/* Input fields */
.stTextInput input,
.stNumberInput input {
    border-radius: 10px;
    border: 1px solid #d8e3da;
    background-color: #FFFFFF;
    min-height: 2.75rem;
}

[data-testid="stTextInput"] label, [data-testid="stNumberInput"] label { color: #355345; font-weight: 600; }
[data-testid="stMetric"] { background: #f7faf7; border: 1px solid var(--line); padding: 15px 18px; border-radius: 13px; }
[data-testid="stMetricValue"] { color: var(--ink); }

/* Data tables */
[data-testid="stDataFrame"] {
    border: 1px solid #E0E8DE;
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #e2ebe3;
    margin: 1.8rem 0;
}

@media (max-width: 760px) { .block-container { padding: 1.2rem 1rem 2rem; } }

</style>
""", unsafe_allow_html=True)


# =====================================
# SIDEBAR BRANDING
# =====================================

with st.sidebar:

    st.markdown("# 🌱 SmartCrop AI")

    st.caption("INTELLIGENT AGRICULTURE")

    st.divider()

    st.markdown("### Navigation")

    navigation_links = (
        ("01", "🌾 Crop Recommendation", "section-crop-recommendation"),
        ("02", "🧪 Soil Analysis", "section-soil-analysis"),
        ("03", "🤖 Explainable AI", "section-explainable-ai"),
        ("04", "🌐 Knowledge Graph", "section-knowledge-graph"),
        ("05", "📊 Farmer Analysis", "section-farmer-analysis"),
        ("06", "💾 Database", "section-database"),
    )
    st.markdown(
        "".join(
            f'<a class="side-nav-link" href="#{anchor}">'
            f'<span class="side-nav-index">{number}</span>'
            f'<span>{label}</span></a>'
            for number, label, anchor in navigation_links
        ),
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("Powered by Machine Learning")
    st.caption("B.Tech Minor Project | 2026")


# =====================================
# APPLICATION HEADING
# =====================================




# =====================================
# APPLICATION HEADING
# =====================================


st.html("""
<div style="
    background: linear-gradient(120deg, #173F32, #367A50);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    color: white;
">
    <div style="font-size:13px; letter-spacing:2px; color:#D8E9D8;">
        SMART AGRICULTURE PLATFORM
    </div>

    <h1 style="color:#FFFFFF !important; font-size:36px; margin:12px 0;">
        🌱 SmartCrop AI
    </h1>

    <p style="color:#E2F0E3; font-size:16px;">
        Intelligent Crop Recommendation & Soil Analysis
    </p>

    <p style="color:#D0E4D2; font-size:13px;">
        Explainable AI Using Soil-Crop Knowledge Graph
    </p>
</div>
""")

st.write(
    "Make informed crop decisions using soil nutrients, "
    "weather conditions and machine learning."
)

st.divider()


st.divider()


# =====================================
# 1. FARMER INFORMATION
# =====================================


# =====================================
# 1. FARMER INFORMATION
# =====================================

st.markdown("""
<div style="background:#FFFFFF; padding:22px;
border:1px solid #E1E9DF; border-radius:15px;
margin-bottom:15px;">
    <h3 style="color:#173F32;">👨‍🌾 Farmer Information</h3>
    <p style="color:#718078; font-size:13px;">
        Enter the farmer's basic details and land information.
    </p>
</div>
""", unsafe_allow_html=True)

farmer_col1, farmer_col2 = st.columns(2)

with farmer_col1:
    farmer_name = st.text_input(
        "Farmer Name",
        placeholder="Enter farmer's full name"
    )

with farmer_col2:
    location = st.text_input(
        "Location",
        placeholder="Village, district or city"
    )

field_area = st.number_input(
    "Land Area (acres)",
    min_value=0.0,
    value=1.0,
    step=0.5
)

st.divider()



# =====================================
# 2. SOIL INFORMATION
# =====================================

st.html('<div id="section-soil-analysis"></div>')


# =====================================
# 2. SOIL INFORMATION
# =====================================

st.markdown("""
<div style="background:#FFFFFF; padding:22px;
border:1px solid #E1E9DF; border-radius:15px;
margin-bottom:15px;">
    <h3 style="color:#173F32;">🌱 Soil Information</h3>
    <p style="color:#718078; font-size:13px;">
        Enter the nutrient levels and pH of the agricultural soil.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=90.0,
        help="Nitrogen level in the soil."
    )

with col2:
    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=42.0,
        help="Phosphorus level in the soil."
    )

with col3:
    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=43.0,
        help="Potassium level in the soil."
    )

ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5,
    help="Soil pH value, from 0 to 14."
)

st.divider()



# =====================================
# 3. WEATHER INFORMATION
# =====================================


# =====================================
# 3. WEATHER INFORMATION
# =====================================

st.markdown("""
<div style="background:#FFFFFF; padding:22px;
border:1px solid #E1E9DF; border-radius:15px;
margin-bottom:15px;">
    <h3 style="color:#173F32;">🌦️ Weather Information</h3>
    <p style="color:#718078; font-size:13px;">
        Enter the current environmental and rainfall conditions.
    </p>
</div>
""", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    temperature = st.number_input(
        "Temperature (°C)",
        value=20.87,
        help="Environmental temperature in degrees Celsius."
    )

with col5:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=82.0,
        help="Relative humidity percentage."
    )

with col6:
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=202.93,
        help="Rainfall measured in millimetres."
    )

st.divider()



# =====================================
# 4. CROP RECOMMENDATION
# =====================================

st.html('<div id="section-crop-recommendation"></div>')


# =====================================
# 4. CROP RECOMMENDATION
# =====================================

st.markdown("""
<div style="
    background: #FFFFFF;
    border: 1px solid #E1E9DF;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 18px;
">
    <h3 style="color:#173F32;">🔍 Crop Recommendation</h3>
    <p style="color:#718078; font-size:13px;">
        Analyze your farm conditions and discover a suitable crop
        using our trained machine learning model.
    </p>
</div>
""", unsafe_allow_html=True)

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:
    recommend_clicked = st.button(
        "🌱  Analyze & Recommend Crop",
        type="primary",
        use_container_width=True
    )

if recommend_clicked:


    if not farmer_name.strip() or not location.strip():

        st.warning(
            "Please enter farmer name and location."
        )

    elif field_area <= 0:

        st.warning(
            "Please enter a valid land area."
        )

    else:

        # =====================================
        # RANDOM FOREST PREDICTION
        # =====================================

        prediction, results = recommend_crop(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        
        # =====================================
        # PREMIUM CROP RECOMMENDATION RESULT
        # =====================================

        
 

        st.html(f"""
        <div style="
            background: linear-gradient(120deg, #173F32, #367A50);
            padding: 28px;
            border-radius: 16px;
            margin-top: 20px;
            color: white;
        ">
            <p style="color:#D8E9D8; font-size:13px;
                    letter-spacing:2px; font-weight:bold;">
                YOUR SMART CROP RECOMMENDATION
            </p>
            <h2 style="color: #FFFFFF !important; font-size: 20px;">
    🌾 Recommended Crop
</h2>
<h1 style="
    color: #FFFFFF !important;
    font-size: 42px;
    font-weight: 800;
">
    {prediction.capitalize()}
</h1>
            <p style="color:#E2F0E3; font-size:14px;">
                Selected by the trained Random Forest model
            </p>
        </div>
        """)



        st.subheader("🏆 Top 5 Recommended Crops")

        for rank, (crop, score) in enumerate(results, start=1):

            st.markdown(
                f"**{rank}. {crop.capitalize()}**"
                f"&nbsp;&nbsp; {score * 100:.2f}%",
                unsafe_allow_html=True
            )

            st.progress(float(score))

        st.info(
            "These scores are model probability estimates, "
            "not guarantees of successful cultivation."
        )


        
    # =====================================
    # 5. EXPLAINABLE AI - FEATURE SENSITIVITY
    # =====================================

        st.html('<div id="section-explainable-ai"></div>')
        st.divider()

        st.header("🤖 Explainable AI (Feature Sensitivity Analysis)")

        predicted_crop, explanation = explain_prediction(
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        )

        # =====================================
        # SAVE RECORDS TO MYSQL DATABASE
        # =====================================

        st.html('<div id="section-database"></div>')
        database_saved = save_farmer_record(
            farmer_name=farmer_name,
            location=location,
            land_area=field_area,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall,
            recommended_crop=predicted_crop
        )

        if database_saved:
            st.success("Farmer details and crop recommendation saved to MySQL!")
        else:
            st.warning(
                "Crop recommendation generated, but database saving failed. "
                "Check MYSQL_PASSWORD and confirm database/schema.sql has been applied."
            )

        st.write(
            f"The model recommended "
            f"**{predicted_crop.capitalize()}** "
            "based on the entered soil and weather conditions."
        )

        st.subheader("📊 Feature Sensitivity Results")

        st.dataframe(
            explanation[
                ["Feature", "Input Value", "Impact", "Importance"]
            ],
            use_container_width=True,
            hide_index=True
        )

        st.subheader("📈 Feature Importance")

        # A compact horizontal chart makes feature importance easier to scan.
        chart_data = explanation.sort_values("Importance", ascending=True)
        fig, ax = plt.subplots(figsize=(9, max(3.2, len(chart_data) * 0.48)), dpi=120)
        fig.patch.set_facecolor("#ffffff")
        ax.set_facecolor("#ffffff")
        bar_colors = ["#75ad83" if value >= 0 else "#d98b70" for value in chart_data["Impact"]]
        ax.barh(chart_data["Feature"], chart_data["Importance"], color=bar_colors,
                height=0.48, edgecolor="none", zorder=3)
        ax.scatter(chart_data["Importance"], chart_data["Feature"], color="#205c40",
                   s=30, zorder=4, edgecolors="white", linewidths=1)
        ax.set_xlabel("Relative importance", color="#687b71", labelpad=10)
        ax.grid(axis="x", color="#e7eee8", linewidth=0.9, zorder=0)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color("#dce6dd")
        ax.tick_params(axis="y", length=0, colors="#355345", labelsize=10, pad=9)
        ax.tick_params(axis="x", colors="#829188", labelsize=9)
        ax.set_axisbelow(True)
        fig.tight_layout(pad=1.5)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
        st.caption("Bar color reflects sensitivity direction: green is positive, terracotta is negative.")

        st.subheader("🔍 Understanding the Explanation")

        st.write(
            "Feature sensitivity analysis measures how the "
            "predicted crop probability changes when one input "
            "feature is replaced with its dataset median value."
        )

        st.write(
            "A positive impact means the original input supports "
            "a higher predicted probability compared with the "
            "median-replaced input."
        )

        st.write(
            "A negative impact means the median-replaced input "
            "produces a higher predicted probability."
        )

        st.write(
            "A larger absolute impact indicates a stronger "
            "sensitivity of the model prediction to that feature."
        )

        most_influential = explanation.iloc[0]["Feature"]

        st.success(
            f"Most influential feature for this prediction: "
            f"**{most_influential}**"
        )

        # =====================================
        # 6. SOIL-CROP KNOWLEDGE GRAPH
        # =====================================

        st.html('<div id="section-knowledge-graph"></div>')
        st.divider()

        st.header("🌐 Soil-Crop Knowledge Graph")

        st.write(
            "Explore the soil and weather information "
            "associated with the recommended crop."
        )

        crop_knowledge = get_crop_factors(predicted_crop)

        if crop_knowledge:

            st.subheader(
                f"Knowledge Graph Insights: "
                f"{predicted_crop.capitalize()}"
            )

            knowledge_df = pd.DataFrame(crop_knowledge)

            st.dataframe(
                knowledge_df,
                use_container_width=True,
                hide_index=True
            )

            st.success(
                f"The Knowledge Graph contains "
                f"{len(crop_knowledge)} factor relationships "
                f"for {predicted_crop.capitalize()}."
            )

            st.caption(
                "Dataset averages and ranges represent observed "
                "values, not scientifically validated optimum "
                "growing requirements."
            )

            # =====================================
            # 7. FARMER CONDITION COMPARISON
            # =====================================

            st.html('<div id="section-farmer-analysis"></div>')
            st.divider()

            st.subheader("📋 Farmer Condition Analysis")

            input_values = {
                "N": nitrogen,
                "P": phosphorus,
                "K": potassium,
                "temperature": temperature,
                "humidity": humidity,
                "ph": ph,
                "rainfall": rainfall
            }

            comparison_results = compare_crop_conditions(
                predicted_crop,
                input_values
            )

            comparison_df = pd.DataFrame(comparison_results)

            st.write(
                "Comparison of farmer-entered values with "
                "the observed dataset ranges for "
                f"{predicted_crop.capitalize()}."
            )

            st.dataframe(
                comparison_df,
                use_container_width=True,
                hide_index=True
            )

            within_count = sum(
                item["Status"] == "Within observed range"
                for item in comparison_results
            )

            below_count = sum(
                item["Status"] == "Below observed range"
                for item in comparison_results
            )

            above_count = sum(
                item["Status"] == "Above observed range"
                for item in comparison_results
            )

            col1, col2, col3 = st.columns(3)

            col1.metric("Within Range", within_count)
            col2.metric("Below Range", below_count)
            col3.metric("Above Range", above_count)

            st.caption(
                "These comparisons use observed dataset ranges. "
                "They are not scientifically validated crop-growing "
                "limits and do not guarantee successful cultivation."
            )

            # =====================================
            # 8. COMPACT VISUAL KNOWLEDGE GRAPH
            # =====================================

            st.divider()

            st.subheader("🌐 Visual Soil-Crop Knowledge Graph")

            crop_graph = get_crop_subgraph(predicted_crop)

            if crop_graph.number_of_nodes() > 0:

                factor_nodes = [
                    node
                    for node, data in crop_graph.nodes(data=True)
                    if data.get("node_type") == "factor"
                ]

                crop_nodes = [
                    node
                    for node, data in crop_graph.nodes(data=True)
                    if data.get("node_type") == "crop"
                ]

                positions = {
                    predicted_crop: (0, 0),
                    "Nitrogen": (0, 2.3),
                    "Phosphorus": (2.2, 1.4),
                    "Potassium": (2.35, -1.0),
                    "Temperature": (0, -2.3),
                    "Humidity": (-2.35, -1.0),
                    "Soil pH": (-2.2, 1.4),
                    "Rainfall": (-2.75, 0)
                }

                fig, ax = plt.subplots(
                    figsize=(10, 7),
                    dpi=140
                )
                fig.patch.set_facecolor("#f8fbf8")
                ax.set_facecolor("#f8fbf8")

                # Draw relationships
                nx.draw_networkx_edges(
                    crop_graph,
                    positions,
                    arrows=True,
                    arrowstyle="-|>",
                    arrowsize=11,
                    width=1.5,
                    edge_color="#91b59a",
                    alpha=0.8,
                    ax=ax
                )

                # Draw factor boxes
                for node in factor_nodes:

                    x, y = positions[node]

                    ax.text(
                        x, y,
                        node,
                        fontsize=8.5,
                        fontweight="bold",
                        ha="center",
                        va="center",
                        color="#244536",
                        bbox=dict(
                            boxstyle="round,pad=0.65,rounding_size=0.18",
                            facecolor="#e4f1e6",
                            edgecolor="#a9cfaf",
                            linewidth=1.2
                        )
                    )

                # Draw crop box
                for node in crop_nodes:

                    x, y = positions[node]

                    ax.text(
                        x, y,
                        node.capitalize(),
                        fontsize=12,
                        fontweight="bold",
                        ha="center",
                        va="center",
                        color="#ffffff",
                        bbox=dict(
                            boxstyle="round,pad=0.8",
                            facecolor="#205c40",
                            edgecolor="#16442f",
                            linewidth=1.8
                        )
                    )

                ax.set_xlim(-3.45, 3.15)
                ax.set_ylim(-2.9, 2.9)

                ax.set_aspect("equal")
                ax.axis("off")

                fig.tight_layout(pad=1.8)

                st.pyplot(
                    fig,
                    use_container_width=True
                )

                plt.close(fig)

                st.caption(
                    "Dark green: Recommended crop | "
                    "Light green: Soil and weather factors"
                )

            else:

                st.warning(
                    "Knowledge Graph could not be generated."
                )

        else:

            st.warning(
                "No Knowledge Graph information found "
                "for this crop."
            )


# =====================================
# APPLICATION FOOTER
# =====================================

st.divider()

st.caption(
    "Smart Crop Recommendation System | B.Tech Minor Project"
)
