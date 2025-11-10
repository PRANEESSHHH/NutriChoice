# 🥗 NutriChoice

**Advanced Nutritional Intelligence & Food Analytics Platform**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Components](#dashboard-components)
- [Data Structure](#data-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

**NutriChoice** is a sophisticated web-based dashboard application designed to provide comprehensive nutritional analysis and food data visualization. Built with modern Python frameworks, it transforms complex nutritional datasets into actionable insights through an intuitive, visually appealing interface.

The platform empowers users—from nutritionists and dietitians to fitness enthusiasts and health-conscious individuals—to make informed dietary decisions based on detailed nutritional analytics.

### Abstract

NutriChoice leverages the power of data visualization to present nutritional information in an accessible and interactive format. The application processes food nutrition data from CSV files and presents it through multiple analytical lenses including macronutrient distributions, caloric analyses, and comparative nutritional profiles. With real-time filtering capabilities and dynamic visualizations, users can explore food data efficiently and discover patterns that inform healthier eating choices.

---

## ✨ Features

### 🎨 **Professional UI/UX**
- Modern gradient design with purple-violet theme
- Glass-morphism cards with subtle shadows
- Responsive layout optimized for all screen sizes
- Custom Inter font family for professional typography
- Smooth hover effects and transitions

### 🔍 **Advanced Filtering & Search**
- **Real-time Food Search** - Find foods instantly by name
- **Calorie Range Filter** - Filter foods within specific calorie ranges
- **Protein Range Filter** - Focus on foods meeting protein requirements
- **Top N Selector** - Customize the number of foods displayed (5-20)

### 📊 **Comprehensive Visualizations**

#### **KPI Metrics Dashboard**
- Total Food Items count
- Average Calories (kcal)
- Average Protein (g)
- Average Fat (g)
- Average Carbohydrates (g)

#### **Interactive Charts**
1. **Top High-Protein Foods** - Horizontal bar chart with Viridis color scale
2. **Top High-Carb Foods** - Horizontal bar chart with Oranges color scale
3. **Macronutrient Distribution** - Donut chart showing proportional breakdown
4. **Protein vs. Calories Relationship** - Multi-dimensional scatter plot
5. **Caloric Distribution Analysis** - Histogram with frequency distribution
6. **Top Fat Content Foods** - Horizontal bar chart with Reds color scale
7. **Comparative Nutritional Profile** - Radar chart for top 5 foods

### 📋 **Data Management**
- Color-coded data table with gradient backgrounds
- Sortable and filterable data grid
- Export-ready filtered datasets
- Cached data loading for optimal performance

### 🔄 **User Controls**
- One-click dashboard refresh
- Persistent filter states
- Quick stats sidebar
- Toggle data table visibility

---

## 🖼️ Demo

### Main Dashboard
The main dashboard features a clean, modern interface with:
- Gradient purple background
- Semi-transparent white cards
- Custom KPI metrics with icons
- Multiple interactive charts

### Control Panel
The sidebar control panel provides:
- Search functionality
- Range sliders for filtering
- Visualization options
- Quick statistics

---

## 🛠️ Tech Stack

### **Core Technologies**
- **Python 3.8+** - Primary programming language
- **Streamlit 1.28+** - Web application framework
- **Plotly 5.0+** - Interactive visualization library
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing

### **UI/UX**
- **Custom CSS** - Professional styling and animations
- **Google Fonts (Inter)** - Modern typography
- **Gradient Design** - Visual aesthetics
- **Glass-morphism** - Modern UI effects

### **Data Processing**
- CSV file handling
- Data caching for performance
- Real-time filtering algorithms
- Statistical computations

---

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/nutrichoice.git
cd nutrichoice
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Prepare Data
Ensure your data file `FOOD-DATA-GROUP1_cleaned.csv` is in the project root directory.

---

## 🚀 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Using the Dashboard

#### **1. Search for Foods**
- Enter food names in the search box
- Results update in real-time

#### **2. Apply Filters**
- Use calorie range slider to filter by calories
- Use protein range slider to focus on protein content
- Adjust "Show top N foods" slider to change display count

#### **3. View Visualizations**
- Scroll through different chart sections
- Hover over charts for detailed information
- Click legend items to toggle data series

#### **4. Access Data Table**
- Check "Show Filtered Data Table" in the sidebar
- View color-coded nutritional values
- Sort and filter data as needed

#### **5. Refresh Dashboard**
- Click "🔄 Refresh Dashboard" button
- Clears cache and reloads all data

---

## 📊 Dashboard Components

### 1. **Header Section**
- Application title with gradient text
- Subtitle describing the platform
- Branded with clean design

### 2. **KPI Metrics Row**
Five custom metric cards displaying:
- 🍽️ Food Items count
- 🔥 Average Calories
- 💪 Average Protein
- 🥑 Average Fat
- 🌾 Average Carbohydrates

### 3. **Top Foods Comparison** (Row 1)
- **Left Chart**: Top N High-Protein Foods
- **Right Chart**: Top N High-Carb Foods

### 4. **Advanced Analytics** (Row 2)
- **Left Chart**: Macronutrient Distribution (Pie Chart)
- **Right Chart**: Protein vs. Calories Scatter Plot

### 5. **Detailed Analysis** (Row 3)
- **Left Chart**: Caloric Distribution Histogram
- **Right Chart**: Top Fat Content Foods

### 6. **Comparative Profile** (Row 4)
- Radar chart comparing top 5 foods across multiple nutrients

### 7. **Data Table** (Optional)
- Filterable, sortable data grid
- Color-gradient backgrounds for easy comparison

### 8. **Footer**
- Branding information
- Technology credits

---

## 📁 Data Structure

### Required CSV Format

Your `FOOD-DATA-GROUP1_cleaned.csv` should have the following columns:

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| `food` | String | Name of the food item |
| `Caloric Value` | Float/Int | Calories in kcal |
| `Protein` | Float | Protein content in grams |
| `Fat` | Float | Fat content in grams |
| `Carbohydrates` | Float | Carbohydrate content in grams |

### Example Data Format
```csv
food,Caloric Value,Protein,Fat,Carbohydrates
Chicken Breast,165,31.0,3.6,0.0
Brown Rice,112,2.6,0.9,23.5
Broccoli,34,2.8,0.4,7.0
Salmon,208,20.4,13.4,0.0
```

---

## 🎨 Customization

### Changing Color Scheme

Edit the CSS gradient in `app.py`:

```python
/* Main Background */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

Replace with your desired colors:
```python
background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
```

### Modifying Chart Colors

Update the `color_continuous_scale` parameter in chart definitions:

```python
fig_protein = px.bar(
    # ... other parameters
    color_continuous_scale='YOUR_SCALE_NAME'  # e.g., 'Blues', 'Greens', 'Reds'
)
```

### Adding New Visualizations

Add custom charts by creating new Plotly figures:

```python
# Example: Adding a box plot
fig_box = px.box(
    filtered_df,
    y='Protein',
    title='Protein Distribution Box Plot'
)
st.plotly_chart(fig_box, use_container_width=True)
```

### Customizing Metrics

Add or modify KPI cards in the metrics section:

```python
with col6:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🎯</div>
        <div class="metric-value">{your_value}</div>
        <div class="metric-label">Your Metric</div>
    </div>
    """, unsafe_allow_html=True)
```

---

## 📦 Project Structure

```
nutrichoice/
│
├── app.py                              # Main application file
├── FOOD-DATA-GROUP1_cleaned.csv       # Food nutrition dataset
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore file
│
└── assets/                             # (Optional) Additional assets
    ├── screenshots/                    # Dashboard screenshots
    └── icons/                          # Custom icons
```

---

## 🔧 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
numpy>=1.24.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
- Use the issue tracker
- Describe the bug in detail
- Include steps to reproduce
- Provide screenshots if applicable

### Suggesting Features
- Open a feature request issue
- Describe the feature and its benefits
- Provide mockups or examples

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 NutriChoice

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🌟 Acknowledgments

- **Streamlit** - For the amazing web app framework
- **Plotly** - For powerful interactive visualizations
- **Pandas** - For robust data manipulation capabilities
- **Google Fonts** - For the Inter font family
- **Community Contributors** - For suggestions and improvements

---

## 📧 Contact

**Project Maintainer:** Your Name

- **Email:** your.email@example.com
- **GitHub:** [@yourusername](https://github.com/yourusername)
- **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)

**Project Link:** [https://github.com/yourusername/nutrichoice](https://github.com/yourusername/nutrichoice)

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Export filtered data to CSV/Excel
- [ ] Meal planning functionality
- [ ] Nutritional goal tracking
- [ ] User authentication and profiles
- [ ] Recipe suggestions based on nutritional needs
- [ ] Mobile app version
- [ ] AI-powered food recommendations
- [ ] Integration with fitness tracking APIs
- [ ] Multi-language support
- [ ] Dark mode toggle
- [ ] Custom data upload functionality
- [ ] Comparison mode for multiple foods
- [ ] Weekly/monthly nutrition reports
- [ ] Food allergen warnings

### Version History
- **v1.0.0** (Current) - Initial release with core features
  - Interactive dashboard
  - 7 visualization types
  - Advanced filtering
  - Professional UI/UX

---

## 📸 Screenshots

### Main Dashboard
*(Add screenshot here)*

### Control Panel
*(Add screenshot here)*

### Data Visualizations
*(Add screenshot here)*

---

## ❓ FAQ

### Q: Can I use my own dataset?
**A:** Yes! Just ensure your CSV file has the required columns: `food`, `Caloric Value`, `Protein`, `Fat`, and `Carbohydrates`.

### Q: How do I change the color theme?
**A:** Edit the CSS gradients in the `st.markdown()` style section of `app.py`.

### Q: Is this project open source?
**A:** Yes, it's licensed under MIT License.

### Q: Can I deploy this on the cloud?
**A:** Yes! You can deploy on Streamlit Cloud, Heroku, AWS, or any platform supporting Python apps.

### Q: How do I add more nutrients to track?
**A:** Add columns to your CSV, then create new visualizations and filters in `app.py`.

---

<div align="center">

**Made with ❤️ using Streamlit and Plotly**

⭐ **Star this repo if you find it helpful!** ⭐

</div>

