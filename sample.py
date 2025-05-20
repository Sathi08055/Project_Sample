import streamlit as st
import pandas as pd
import numpy as np

# Page title and intro
st.title("🌾 Major Crops in India: A Quick Look")
st.write("Explore key crops grown across India with their growing regions plotted on a map.")

# Crop data
crops_data = {
    'Crop': ['Rice', 'Wheat', 'Maize', 'Sugarcane', 'Cotton', 'Tea', 'Coffee', 'Millets'],
    'Season': ['Kharif', 'Rabi', 'Kharif', 'Kharif', 'Kharif', 'Perennial', 'Perennial', 'Kharif'],
    'Major States': [
        'West Bengal, Punjab, Uttar Pradesh',
        'Punjab, Haryana, Uttar Pradesh',
        'Karnataka, Bihar, Andhra Pradesh',
        'Uttar Pradesh, Maharashtra, Karnataka',
        'Gujarat, Maharashtra, Telangana',
        'Assam, West Bengal, Tamil Nadu',
        'Karnataka, Kerala, Tamil Nadu',
        'Rajasthan, Maharashtra, Karnataka'
    ]
}

df_crops = pd.DataFrame(crops_data)

# Show data table
st.subheader("📊 List of Major Crops and Their Seasons")
st.dataframe(df_crops)

# Generate random locations for demonstration (within India’s lat-lon boundaries)
num_points = 50
india_lat_range = (8.0, 37.0)
india_lon_range = (68.0, 97.0)

map_data = pd.DataFrame({
    'latitude': np.random.uniform(india_lat_range[0], india_lat_range[1], num_points),
    'longitude': np.random.uniform(india_lon_range[0], india_lon_range[1], num_points)
})

# Show map
st.subheader("🗺️ Random Growing Regions (for Demo)")
st.map(map_data)

# Extra content about seasons
st.markdown("""
---
### 🌦️ Crop Seasons in India:
- **Kharif**: Sown with the beginning of the monsoon (June-July) and harvested in autumn (September-October).
- **Rabi**: Sown in winter (October-December) and harvested in spring (March-April).
- **Perennial**: Grown year-round in suitable regions.

**Fun fact:** India ranks **second** worldwide in agricultural production — after China.
""")
