import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="NutriVision - Smart Diet Planner",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS Styling ---
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Content container */
    .block-container {
        padding: 2rem 2rem 3rem 2rem;
        max-width: 100%;
    }
    
    /* Header styling */
    h1 {
        color: #667eea !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Subheader styling */
    h2, h3 {
        color: #2d3436 !important;
        font-weight: 600 !important;
    }
    
    /* Metric cards styling */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #667eea !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        color: #636e72 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.8rem !important;
        color: #95a5a6 !important;
    }
    
    div[data-testid="stMetric"] {
        background: white;
        padding: 1.5rem 1rem;
        border-radius: 12px;
        border: 1px solid #e1e8ed;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: white !important;
    }
    
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 700 !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton > button:hover {
        opacity: 0.9;
        border: none;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        width: 100%;
    }
    
    .stDownloadButton > button:hover {
        opacity: 0.9;
        border: none;
    }
    
    /* Custom divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
    
    /* Chart containers */
    [data-testid="stPlotlyChart"] {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }
</style>
""", unsafe_allow_html=True)

# --- Data Loading ---
DATA_FILE = 'FOOD-DATA-GROUP1_cleaned.csv'

@st.cache_data
def load_data(file_path):
    """Loads the cleaned food data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file {file_path} was not found.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

# Load the data
df = load_data(DATA_FILE)

# --- Sidebar ---
st.sidebar.markdown("## 🎛️ Control Panel")
st.sidebar.markdown("---")

# Food search
st.sidebar.markdown("### 🔍 Search Foods")
search_query = st.sidebar.text_input("Search for a food item:", "")

# Nutrient filters
st.sidebar.markdown("### 🎚️ Nutrient Filters")
calorie_range = st.sidebar.slider(
    "Calorie Range (kcal)",
    int(df['Caloric Value'].min()),
    int(df['Caloric Value'].max()),
    (int(df['Caloric Value'].min()), int(df['Caloric Value'].max()))
)

protein_range = st.sidebar.slider(
    "Protein Range (g)",
    float(df['Protein'].min()),
    float(df['Protein'].max()),
    (float(df['Protein'].min()), float(df['Protein'].max()))
)

# Chart selection
st.sidebar.markdown("### 📊 Visualization Options")
chart_type = st.sidebar.selectbox(
    "Distribution Chart Type",
    ["Violin Plot", "Box Plot", "Histogram"]
)

top_n = st.sidebar.slider("Top N Foods to Display", 5, 20, 10)

# Data view options
st.sidebar.markdown("---")
show_raw_data = st.sidebar.checkbox("📋 Show Raw Data Table")
show_statistics = st.sidebar.checkbox("📈 Show Detailed Statistics", value=True)

st.sidebar.markdown("---")
st.sidebar.info(
    "**NutriVision** - Your intelligent nutrition companion. "
    "Analyze, compare, and discover the nutritional content of thousands of foods."
)

# --- Apply Filters ---
filtered_df = df.copy()

# Apply search filter
if search_query:
    filtered_df = filtered_df[filtered_df['food'].str.contains(search_query, case=False, na=False)]

# Apply nutrient filters
filtered_df = filtered_df[
    (filtered_df['Caloric Value'] >= calorie_range[0]) &
    (filtered_df['Caloric Value'] <= calorie_range[1]) &
    (filtered_df['Protein'] >= protein_range[0]) &
    (filtered_df['Protein'] <= protein_range[1])
]

# --- Dashboard Header ---
st.markdown("<h1>🥗 NutriVision</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #636e72; margin-bottom: 2rem;'>Smart Nutrition Analysis & Diet Planning Dashboard</p>", unsafe_allow_html=True)
st.markdown("---")

# --- KPI Metrics ---
if not filtered_df.empty:
    avg_calories = filtered_df['Caloric Value'].mean()
    avg_protein = filtered_df['Protein'].mean()
    avg_fat = filtered_df['Fat'].mean()
    avg_carbs = filtered_df['Carbohydrates'].mean()
    total_foods = filtered_df['food'].nunique()
else:
    avg_calories = avg_protein = avg_fat = avg_carbs = total_foods = 0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="🍽️ Total Foods", value=f"{total_foods:,}")

with col2:
    st.metric(label="🔥 Avg Calories", value=f"{avg_calories:.0f}", delta="kcal")

with col3:
    st.metric(label="💪 Avg Protein", value=f"{avg_protein:.1f}", delta="g")

with col4:
    st.metric(label="🥑 Avg Fat", value=f"{avg_fat:.1f}", delta="g")

with col5:
    st.metric(label="🌾 Avg Carbs", value=f"{avg_carbs:.1f}", delta="g")

st.markdown("---")

# --- Top Foods Analysis ---
st.markdown("## 🏆 Top Nutritional Foods")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 💪 Top {top_n} High-Protein Foods")
    top_protein = filtered_df.nlargest(top_n, 'Protein').sort_values('Protein', ascending=True)
    
    fig_protein = go.Figure()
    fig_protein.add_trace(go.Bar(
        y=top_protein['food'],
        x=top_protein['Protein'],
        orientation='h',
        marker=dict(
            color=top_protein['Protein'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Protein (g)")
        ),
        text=top_protein['Protein'].round(1),
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Protein: %{x:.1f}g<extra></extra>'
    ))
    
    fig_protein.update_layout(
        title=dict(text=f'Top {top_n} High-Protein Foods', x=0.5, xanchor='center', font=dict(size=16, color='#2d3436')),
        xaxis_title="Protein (g)",
        yaxis_title="",
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=11, color='#2d3436'),
        margin=dict(l=10, r=10, t=50, b=40),
        showlegend=False
    )
    
    st.plotly_chart(fig_protein, use_container_width=True)

with col2:
    st.markdown(f"### 🌾 Top {top_n} High-Carb Foods")
    top_carbs = filtered_df.nlargest(top_n, 'Carbohydrates').sort_values('Carbohydrates', ascending=True)
    
    fig_carbs = go.Figure()
    fig_carbs.add_trace(go.Bar(
        y=top_carbs['food'],
        x=top_carbs['Carbohydrates'],
        orientation='h',
        marker=dict(
            color=top_carbs['Carbohydrates'],
            colorscale='Reds',
            showscale=True,
            colorbar=dict(title="Carbs (g)")
        ),
        text=top_carbs['Carbohydrates'].round(1),
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Carbs: %{x:.1f}g<extra></extra>'
    ))
    
    fig_carbs.update_layout(
        title=dict(text=f'Top {top_n} High-Carb Foods', x=0.5, xanchor='center', font=dict(size=16, color='#2d3436')),
        xaxis_title="Carbohydrates (g)",
        yaxis_title="",
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=11, color='#2d3436'),
        margin=dict(l=10, r=10, t=50, b=40),
        showlegend=False
    )
    
    st.plotly_chart(fig_carbs, use_container_width=True)

st.markdown("---")

# --- Macronutrient Distribution ---
st.markdown("## 📊 Macronutrient Distribution & Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔥 Calorie Distribution")
    
    if chart_type == "Violin Plot":
        fig_dist = px.violin(
            filtered_df,
            y='Caloric Value',
            box=True,
            points="all"
        )
    elif chart_type == "Box Plot":
        fig_dist = px.box(
            filtered_df,
            y='Caloric Value',
            points="all"
        )
    else:  # Histogram
        fig_dist = px.histogram(
            filtered_df,
            x='Caloric Value',
            nbins=30
        )
    
    fig_dist.update_traces(marker=dict(color='#667eea'))
    fig_dist.update_layout(
        title=dict(text='Calorie Distribution', x=0.5, xanchor='center', font=dict(size=16, color='#2d3436')),
        yaxis_title="Calories (kcal)" if chart_type != "Histogram" else "Count",
        xaxis_title="Calories (kcal)" if chart_type == "Histogram" else "",
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=11, color='#2d3436'),
        margin=dict(l=50, r=20, t=50, b=40)
    )
    
    st.plotly_chart(fig_dist, use_container_width=True)

with col2:
    st.markdown("### 💪 Protein vs Calories Correlation")
    
    fig_scatter = px.scatter(
        filtered_df,
        x='Caloric Value',
        y='Protein',
        hover_data=['food'],
        size='Fat',
        color='Carbohydrates',
        color_continuous_scale='Purples'
    )
    
    fig_scatter.update_layout(
        title=dict(text='Protein vs Calories (Size: Fat, Color: Carbs)', x=0.5, xanchor='center', font=dict(size=16, color='#2d3436')),
        xaxis_title="Calories (kcal)",
        yaxis_title="Protein (g)",
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=11, color='#2d3436'),
        margin=dict(l=50, r=20, t=50, b=40)
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("---")

# --- Macronutrient Composition ---
st.markdown("## 🥧 Average Macronutrient Composition")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Create pie chart for macronutrient composition
    macro_values = [avg_protein, avg_fat, avg_carbs]
    macro_labels = ['Protein', 'Fat', 'Carbohydrates']
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=macro_labels,
        values=macro_values,
        hole=0.4,
        marker=dict(colors=['#667eea', '#f093fb', '#4facfe']),
        textinfo='label+percent',
        textfont=dict(size=14, family='Inter', color='white'),
        hovertemplate='<b>%{label}</b><br>Amount: %{value:.1f}g<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig_pie.update_layout(
        title=dict(text='Macronutrient Distribution', x=0.5, xanchor='center', font=dict(size=16, color='#2d3436')),
        height=450,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Inter', size=12, color='#2d3436'),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        margin=dict(l=20, r=20, t=50, b=40)
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# --- Detailed Statistics ---
if show_statistics:
    st.markdown("## 📈 Detailed Nutritional Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    stats_df = filtered_df[['Caloric Value', 'Protein', 'Fat', 'Carbohydrates']].describe()
    
    with col1:
        st.markdown("### 🔥 Calories")
        st.dataframe(stats_df[['Caloric Value']].round(2), use_container_width=True)
    
    with col2:
        st.markdown("### 💪 Protein")
        st.dataframe(stats_df[['Protein']].round(2), use_container_width=True)
    
    with col3:
        st.markdown("### 🥑 Fat")
        st.dataframe(stats_df[['Fat']].round(2), use_container_width=True)
    
    with col4:
        st.markdown("### 🌾 Carbs")
        st.dataframe(stats_df[['Carbohydrates']].round(2), use_container_width=True)
    
    st.markdown("---")

# --- Raw Data Table ---
if show_raw_data:
    st.markdown("## 📋 Complete Food Database")
    st.markdown(f"*Showing {len(filtered_df)} of {len(df)} foods*")
    
    # Add download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name="nutrition_data_filtered.csv",
        mime="text/csv"
    )
    
    st.dataframe(
        filtered_df.style.background_gradient(cmap='Purples', subset=['Caloric Value', 'Protein', 'Fat', 'Carbohydrates']),
        use_container_width=True,
        height=400
    )

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #636e72; font-size: 0.9rem;'>"
    "🥗 NutriVision © 2025 | Made with ❤️ using Streamlit | Data-Driven Nutrition Insights"
    "</p>",
    unsafe_allow_html=True
)
)