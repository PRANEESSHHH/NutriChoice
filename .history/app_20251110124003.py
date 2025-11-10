import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="NutriChoice",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional UI ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Content Container */
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 100%;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.90) 100%);
        padding: 2rem 2.5rem;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        padding: 0;
    }
    
    .header-subtitle {
        color: #6b7280;
        font-size: 1.1rem;
        font-weight: 400;
        margin-top: 0.5rem;
    }
    
    /* KPI Card Styling */
    .metric-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.90) 100%);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border: 1px solid rgba(255,255,255,0.3);
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .metric-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.95rem;
        color: #6b7280;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Chart Container */
    .chart-container {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.90) 100%);
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        border: 1px solid rgba(255,255,255,0.3);
        margin-bottom: 1.5rem;
    }
    
    .chart-title {
        font-size: 1.3rem;
        font-weight: 600;   
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    /* Sidebar Styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.90) 100%);
    }
    
    .sidebar-content {
        padding: 1rem;
    }
    
    /* Sidebar Text Visibility */
    [data-testid="stSidebar"] label {
        color: #1f2937 !important;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #1f2937 !important;
    }
    
    [data-testid="stSidebar"] p {
        color: #374151 !important;
    }
    
    [data-testid="stSidebar"] h3 {
        color: #1f2937 !important;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] input {
        color: #1f2937 !important;
    }
    
    [data-testid="stSidebar"] .stSlider label {
        color: #1f2937 !important;
    }
    
    [data-testid="stSidebar"] .stCheckbox label {
        color: #1f2937 !important;
    }
    
    [data-testid="stSidebar"] .stTextInput label {
        color: #1f2937 !important;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stTextInput input {
        background-color: white !important;
        color: #1f2937 !important;
        border: 2px solid #d1d5db !important;
        border-radius: 10px !important;
    }
    
    [data-testid="stSidebar"] .stTextInput input::placeholder {
        color: #9ca3af !important;
        opacity: 1 !important;
    }
    
    [data-testid="stSidebar"] .stAlert {
        background-color: rgba(102, 126, 234, 0.1) !important;
        color: #1f2937 !important;
    }
    
    [data-testid="stSidebar"] .stAlert p {
        color: #1f2937 !important;
    }
    
    /* Sidebar Slider Styling */
    [data-testid="stSidebar"] .stSlider > div > div > div {
        background-color: #e5e7eb !important;
    }
    
    [data-testid="stSidebar"] .stSlider > div > div > div > div {
        background-color: #667eea !important;
    }
    
    /* Sidebar Number Display */
    [data-testid="stSidebar"] .stSlider [data-testid="stTickBarMin"],
    [data-testid="stSidebar"] .stSlider [data-testid="stTickBarMax"] {
        color: #1f2937 !important;
    }
    
    /* Remove default Streamlit styling */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Selectbox & Input Styling */
    .stSelectbox>div>div, .stMultiSelect>div>div, .stTextInput>div>div {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
    }
    
    .stTextInput input {
        background-color: white !important;
        color: #1f2937 !important;
        border: 2px solid #d1d5db !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        font-size: 0.95rem !important;
    }
    
    .stTextInput input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    .stTextInput input::placeholder {
        color: #9ca3af !important;
    }
    
    /* DataFrame Styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* Metric Container Override */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: 700;
        color: #667eea;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem;
        color: #6b7280;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        margin: 2rem 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
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

# --- Sidebar Filters ---
with st.sidebar:
    # Control Panel Header with Refresh Icon
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("<h2 style='color: #667eea; margin-bottom: 0;'>🔧 Control Panel</h2>", unsafe_allow_html=True)
    with col2:
        if st.button("🔄", key="refresh_btn", help="Refresh Dashboard"):
            st.cache_data.clear()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Search functionality
    st.markdown("### 🔍 Search Food")
    search_term = st.text_input("Enter food name:", placeholder="e.g., chicken, apple...")
    
    # Calorie filter
    st.markdown("### 🔥 Calorie Range")
    if not df.empty:
        cal_min, cal_max = st.slider(
            "Select calorie range:",
            int(df['Caloric Value'].min()),
            int(df['Caloric Value'].max()),
            (int(df['Caloric Value'].min()), int(df['Caloric Value'].max()))
        )
    
    # Protein filter
    st.markdown("### 💪 Protein Range")
    if not df.empty:
        protein_min, protein_max = st.slider(
            "Select protein range (g):",
            float(df['Protein'].min()),
            float(df['Protein'].max()),
            (float(df['Protein'].min()), float(df['Protein'].max()))
        )
    
    # Visualization options
    st.markdown("### 📊 Visualization Options")
    show_top_n = st.slider("Show top N foods:", 5, 20, 10)
    
    # Data view
    st.markdown("### 📋 Data View")
    show_raw_data = st.checkbox("Show Filtered Data Table")
    
    # Stats
    st.markdown("### 📈 Quick Stats")
    if not df.empty:
        st.info(f"**Total Records:** {len(df)}")
        st.info(f"**Unique Foods:** {df['food'].nunique()}")

# Apply filters
filtered_df = df.copy()
if search_term:
    filtered_df = filtered_df[filtered_df['food'].str.contains(search_term, case=False, na=False)]
if not df.empty:
    filtered_df = filtered_df[
        (filtered_df['Caloric Value'] >= cal_min) & 
        (filtered_df['Caloric Value'] <= cal_max) &
        (filtered_df['Protein'] >= protein_min) & 
        (filtered_df['Protein'] <= protein_max)
    ]

# --- Dashboard Header ---
st.markdown("""
<div class="main-header">
    <h1 class="header-title">NutriChoice</h1>
    <p class="header-subtitle">Advanced Nutritional Intelligence & Food Analytics Platform</p>
</div>
""", unsafe_allow_html=True)

# --- KPI Metrics Section ---
if not filtered_df.empty:
    avg_calories = filtered_df['Caloric Value'].mean()
    avg_protein = filtered_df['Protein'].mean()
    avg_fat = filtered_df['Fat'].mean()
    avg_carbs = filtered_df['Carbohydrates'].mean()
    total_foods = filtered_df['food'].nunique()
    max_calorie_food = filtered_df.loc[filtered_df['Caloric Value'].idxmax(), 'food']
else:
    avg_calories = avg_protein = avg_fat = avg_carbs = total_foods = 0
    max_calorie_food = "N/A"

# Create 5 columns for KPI cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🍽️</div>
        <div class="metric-value">{total_foods}</div>
        <div class="metric-label">Food Items</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🔥</div>
        <div class="metric-value">{avg_calories:.0f}</div>
        <div class="metric-label">Avg Calories (kcal)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">💪</div>
        <div class="metric-value">{avg_protein:.1f}g</div>
        <div class="metric-label">Avg Protein</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🥑</div>
        <div class="metric-value">{avg_fat:.1f}g</div>
        <div class="metric-label">Avg Fat</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🌾</div>
        <div class="metric-value">{avg_carbs:.1f}g</div>
        <div class="metric-label">Avg Carbs</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- Top Foods Comparison ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown(f'<h3 class="chart-title">🏆 Top {show_top_n} High-Protein Foods</h3>', unsafe_allow_html=True)
    
    top_protein = filtered_df.nlargest(show_top_n, 'Protein').sort_values('Protein', ascending=True)
    fig_protein = px.bar(
        top_protein,
        x='Protein',
        y='food',
        orientation='h',
        labels={'food': '', 'Protein': 'Protein (g)'},
        color='Protein',
        color_continuous_scale='Viridis',
        hover_data={'Protein': ':.1f'}
    )
    fig_protein.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        height=400,
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_protein, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown(f'<h3 class="chart-title">🍞 Top {show_top_n} High-Carb Foods</h3>', unsafe_allow_html=True)
    
    top_carbs = filtered_df.nlargest(show_top_n, 'Carbohydrates').sort_values('Carbohydrates', ascending=True)
    fig_carbs = px.bar(
        top_carbs,
        x='Carbohydrates',
        y='food',
        orientation='h',
        labels={'food': '', 'Carbohydrates': 'Carbohydrates (g)'},
        color='Carbohydrates',
        color_continuous_scale='Oranges',
        hover_data={'Carbohydrates': ':.1f'}
    )
    fig_carbs.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        height=400,
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_carbs, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Advanced Visualizations ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">📊 Macronutrient Distribution</h3>', unsafe_allow_html=True)
    
    # Create pie chart for macronutrient totals
    macro_totals = {
        'Protein': filtered_df['Protein'].sum(),
        'Fat': filtered_df['Fat'].sum(),
        'Carbohydrates': filtered_df['Carbohydrates'].sum()
    }
    
    fig_pie = go.Figure(data=[go.Pie(
        labels=list(macro_totals.keys()),
        values=list(macro_totals.values()),
        hole=0.4,
        marker=dict(colors=['#667eea', '#764ba2', '#f093fb']),
        textfont=dict(size=14, family="Inter, sans-serif")
    )])
    
    fig_pie.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        margin=dict(l=0, r=0, t=20, b=0),
        height=400,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">🔬 Protein vs. Calories Relationship</h3>', unsafe_allow_html=True)
    
    fig_scatter = px.scatter(
        filtered_df,
        x='Caloric Value',
        y='Protein',
        size='Fat',
        color='Carbohydrates',
        hover_data=['food'],
        labels={'Caloric Value': 'Calories (kcal)', 'Protein': 'Protein (g)'},
        color_continuous_scale='Plasma'
    )
    
    fig_scatter.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        margin=dict(l=0, r=0, t=20, b=0),
        height=400,
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)')
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Detailed Analytics ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">📈 Caloric Distribution Analysis</h3>', unsafe_allow_html=True)
    
    fig_hist = px.histogram(
        filtered_df,
        x='Caloric Value',
        nbins=30,
        labels={'Caloric Value': 'Calories (kcal)'},
        color_discrete_sequence=['#667eea']
    )
    
    fig_hist.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        margin=dict(l=0, r=0, t=20, b=0),
        height=350,
        showlegend=False,
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', title='Count')
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">🥇 Top Fat Content Foods</h3>', unsafe_allow_html=True)
    
    top_fat = filtered_df.nlargest(show_top_n, 'Fat').sort_values('Fat', ascending=True)
    fig_fat = px.bar(
        top_fat,
        x='Fat',
        y='food',
        orientation='h',
        labels={'food': '', 'Fat': 'Fat (g)'},
        color='Fat',
        color_continuous_scale='Reds',
        hover_data={'Fat': ':.1f'}
    )
    
    fig_fat.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, sans-serif", size=12),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        height=350,
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)'),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_fat, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Nutritional Radar Chart ---
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown('<h3 class="chart-title">🎯 Comparative Nutritional Profile - Top 5 Foods</h3>', unsafe_allow_html=True)

top_5_foods = filtered_df.nlargest(5, 'Caloric Value')

fig_radar = go.Figure()

for idx, row in top_5_foods.iterrows():
    fig_radar.add_trace(go.Scatterpolar(
        r=[row['Protein'], row['Fat'], row['Carbohydrates'], row['Caloric Value']/10],
        theta=['Protein (g)', 'Fat (g)', 'Carbs (g)', 'Calories (kcal/10)'],
        fill='toself',
        name=row['food'][:30]
    ))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, max(filtered_df['Protein'].max(), 
                                                      filtered_df['Fat'].max(), 
                                                      filtered_df['Carbohydrates'].max())])
    ),
    showlegend=True,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family="Inter, sans-serif", size=12),
    height=500,
    legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
)

st.plotly_chart(fig_radar, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Data Table ---
if show_raw_data:
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h3 class="chart-title">📋 Filtered Food Database</h3>', unsafe_allow_html=True)
    st.dataframe(
        filtered_df.style.background_gradient(cmap='Blues', subset=['Caloric Value'])
                         .background_gradient(cmap='Greens', subset=['Protein'])
                         .background_gradient(cmap='Oranges', subset=['Carbohydrates'])
                         .background_gradient(cmap='Reds', subset=['Fat'])
                         .format({'Caloric Value': '{:.0f}', 'Protein': '{:.1f}', 
                                 'Fat': '{:.1f}', 'Carbohydrates': '{:.1f}'}),
        use_container_width=True,
        height=400
    )
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.7); font-size: 0.9rem; padding: 1rem;'>
    <p>🥗 <strong>NutriChoice</strong> | Advanced Food Intelligence Platform</p>
    <p style='font-size: 0.85rem;'>Powered by Streamlit & Plotly | Data-Driven Nutrition Insights</p>
</div>
""", unsafe_allow_html=True)