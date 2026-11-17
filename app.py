
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

/* Main application background */
.stApp {
    background-color: #F7F9F5;
    color: #24382D;
}

/* Hide default Streamlit decoration */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #173F32;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Main headings */
h1, h2, h3 {
    color: #173F32 !important;
    font-weight: 700 !important;
}

/* Buttons */
.stButton > button {
    background-color: #26734D;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background-color: #173F32;
    color: white;
    border: none;
}

/* Input fields */
.stTextInput input,
.stNumberInput input {
    border-radius: 8px;
    border: 1px solid #D6E1D5;
    background-color: #FFFFFF;
}

/* Data tables */
[data-testid="stDataFrame"] {
    border: 1px solid #E0E8DE;
    border-radius: 10px;
}

/* Dividers */
hr {
    border-color: #DFE8DC;
}

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

    st.markdown("""
    🌾 Crop Recommendation

    🧪 Soil Analysis

    🤖 Explainable AI

    🌐 Knowledge Graph

    📊 Farmer Analysis

    💾 Database
    """)

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
                "Please check the MySQL connection."
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

        st.bar_chart(
            explanation.set_index("Feature")["Importance"]
        )

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
                    "Nitrogen": (0, 1.0),
                    "Phosphorus": (0.78, 0.62),
                    "Potassium": (0.78, -0.62),
                    "Temperature": (0, -1.0),
                    "Humidity": (-0.78, -0.62),
                    "Soil pH": (-0.78, 0.62),
                    "Rainfall": (-1.05, 0)
                }

                fig, ax = plt.subplots(
                    figsize=(6, 4),
                    dpi=90
                )

                # Draw relationships
                nx.draw_networkx_edges(
                    crop_graph,
                    positions,
                    arrows=True,
                    arrowstyle="-|>",
                    arrowsize=12,
                    width=1.2,
                    edge_color="gray",
                    ax=ax
                )

                # Draw factor boxes
                for node in factor_nodes:

                    x, y = positions[node]

                    ax.text(
                        x, y,
                        node,
                        fontsize=8,
                        fontweight="bold",
                        ha="center",
                        va="center",
                        bbox=dict(
                            boxstyle="round,pad=0.45",
                            facecolor="lightgreen",
                            edgecolor="green",
                            linewidth=1.3
                        )
                    )

                # Draw crop box
                for node in crop_nodes:

                    x, y = positions[node]

                    ax.text(
                        x, y,
                        node.capitalize(),
                        fontsize=10,
                        fontweight="bold",
                        ha="center",
                        va="center",
                        bbox=dict(
                            boxstyle="round,pad=0.65",
                            facecolor="orange",
                            edgecolor="darkorange",
                            linewidth=2
                        )
                    )

                ax.set_xlim(-1.55, 1.25)
                ax.set_ylim(-1.35, 1.35)

                ax.set_aspect("equal")
                ax.axis("off")

                plt.tight_layout(pad=1)

                st.pyplot(
                    fig,
                    use_container_width=False
                )

                plt.close(fig)

                st.caption(
                    "Orange box: Recommended crop | "
                    "Green boxes: Soil and weather factors"
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
