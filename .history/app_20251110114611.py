import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Nutrition Insights Dashboard",
    page_icon="🍎",
    layout="wide"  # Use the full page width
)

# --- Data Loading ---
DATA_FILE = 'FOOD-DATA-GROUP1_cleaned.csv'

@st.cache_data  # Cache the data to improve performance
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

# --- Dashboard Title ---
st.title("🍎 Nutrition Insights Dashboard")
st.markdown("---")

# --- KPI Metrics (Top Row) ---
# Calculate the averages, handling potential division by zero if df is empty
if not df.empty:
    avg_calories = df['Caloric Value'].mean()
    avg_protein = df['Protein'].mean()
    avg_fat = df['Fat'].mean()
    avg_carbs = df['Carbohydrates'].mean()
    total_foods = df['food'].nunique()
else:
    avg_calories = avg_protein = avg_fat = avg_carbs = total_foods = 0

# Create 5 columns for the KPI cards
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(label="Total Food Items", value=total_foods)

with col2:
    st.metric(label="Average Calories", value=f"{avg_calories:.0f} kcal")

with col3:
    st.metric(label="Average Protein", value=f"{avg_protein:.1f} g")

with col4:
    st.metric(label="Average Fat", value=f"{avg_fat:.1f} g")

with col5:
    st.metric(label="Average Carbs", value=f"{avg_carbs:.1f} g")

st.markdown("---")

# --- Bar Charts (Middle Row) ---
col1, col2 = st.columns(2)

with col1:
    # Top 10 High-Protein Foods
    st.subheader("Top 10 High-Protein Foods")
    # Sort ascending=True for Plotly horizontal bar to show highest at top
    top_10_protein = df.nlargest(10, 'Protein').sort_values('Protein', ascending=True)
    fig_protein = px.bar(
        top_10_protein,
        x='Protein',
        y='food',
        title='Top 10 High-Protein Foods',
        orientation='h',
        labels={'food': 'Food Item', 'Protein': 'Protein (g)'}
    )
    fig_protein.update_layout(yaxis={'title': ''}) # Remove y-axis label
    st.plotly_chart(fig_protein, use_container_width=True)

with col2:
    # Top 10 High-Carb Foods
    st.subheader("Top 10 High-Carb Foods")
    top_10_carbs = df.nlargest(10, 'Carbohydrates').sort_values('Carbohydrates', ascending=True)
    fig_carbs = px.bar(
        top_10_carbs,
        x='Carbohydrates',
        y='food',
        title='Top 10 High-Carb Foods',
        orientation='h',
        labels={'food': 'Food Item', 'Carbohydrates': 'Carbohydrates (g)'},
        color_continuous_scale='Reds'
    )
    fig_carbs.update_layout(yaxis={'title': ''})
    st.plotly_chart(fig_carbs, use_container_width=True)

st.markdown("---")

# --- Distribution & Scatter Plots (Bottom Row) ---
col1, col2 = st.columns(2)

with col1:
    # Distribution of Calories (using a Violin plot as in your example)
    st.subheader("Distribution of Calories")
    fig_dist = px.violin(
        df,
        y='Caloric Value',
        title='Distribution of Calories',
        box=True,  # Show a box plot inside
        points="all" # Show all data points
    )
    st.plotly_chart(fig_dist, use_container_width=True)

with col2:
    # Protein vs. Calories Scatter Plot
    st.subheader("Protein vs. Calories")
    fig_scatter = px.scatter(
        df,
        x='Caloric Value',
        y='Protein',
        title='Protein vs. Calories',
        hover_data=['food'],  # Show food name on hover
        labels={'Caloric Value': 'Calories (kcal)', 'Protein': 'Protein (g)'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)


# --- Sidebar ---
st.sidebar.header("Options")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Food Nutrition Data")
    st.dataframe(df)

st.sidebar.info(
    "This dashboard provides insights into the food nutrition dataset, "
    "replicating the design from the Power BI screenshot."
)