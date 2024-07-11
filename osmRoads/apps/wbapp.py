import streamlit as st
import geopandas as gpd
import pandas as pd
import altair as alt
import leafmap.foliumap as leafmap

# Page Configuration
st.set_page_config(page_title='Rasta', layout='wide')

# Custom CSS
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .css-1d391kg {
        background-color: #1e3a5f !important;
    }
    .css-qbe2hs {
        color: #ffffff !important;
    }
    .css-1cpxqw2 a {
        color: #1e3a5f !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title('West Bengal Highway Dashboard')

# Sidebar: About Section
st.sidebar.title('About')
st.sidebar.info(
    'Explore the National and State Highway Statistics of different Districts of West Bengal',
    icon=":bar_chart:"
)

# Data URLs
data_url = 'https://github.com/somdeepkundu/geoKosh/raw/main/osmRoads/'
gpkg_file = 'wb_roads.gpkg'
csv_file = 'wb_mejor_roads.csv'

# Data Reading Functions
@st.cache_data
def read_gdf(url, layer):
    return gpd.read_file(url, layer=layer)

@st.cache_data
def read_csv(url):
    return pd.read_csv(url)

# Load Data
gpkg_url = data_url + gpkg_file
csv_url = data_url + csv_file
districts_gdf = read_gdf(gpkg_url, 'wb_district')
nh_gdf = read_gdf(gpkg_url, 'wb_nh')
sh_gdf = read_gdf(gpkg_url, 'wb_sh')
lengths_df = read_csv(csv_url)

# Sidebar: Data Selection
districts = districts_gdf.District.values
district = st.sidebar.selectbox('Select a District', districts)
overlay_nh = st.sidebar.checkbox('Overlay NH')
overlay_sh = st.sidebar.checkbox('Overlay SH')
district_lengths = lengths_df[lengths_df['District'] == district]

# Plotting Chart with Altair
chart = alt.Chart(district_lengths).mark_bar().encode(
    x=alt.X('Category', sort=None, axis=alt.Axis(title=None, labels=False)),
    y=alt.Y('Kilometers', axis=alt.Axis(title='Kilometers')),
    color=alt.Color('Category', scale=alt.Scale(range=['#ff827a', '#4aacff']))
).properties(
    title=f'Length of Highways - {district}',
    width=600,
    height=400
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)

# Display Chart in Sidebar
st.sidebar.altair_chart(chart, use_container_width=True)

# Download Chart
file_name = f'{district}_Highways.png'
chart.save(file_name)
with open(file_name, 'rb') as img:
    st.sidebar.download_button(
        'Download Chart',
        data=img,
        file_name=file_name,
        mime='image/png'
    )

# Credit Section
st.sidebar.markdown('''
---
Created with ❤️ by [Somdeep](https://www.youtube.com/@sthan-kaal-patra/).
''')

# Create the Map
m = leafmap.Map(
    layers_control=True,
    draw_control=False,
    measure_control=False,
    fullscreen_control=False,
)
m.add_basemap('CartoDB.DarkMatter')
m.add_gdf(
    gdf=districts_gdf,
    zoom_to_layer=False,
    layer_name='Districts',
    info_mode='on_click',
    style={'color': '#00d692', 'fillOpacity': 0.2, 'weight': 0.5},
)

# Overlay National Highways
if overlay_nh:
    m.add_gdf(
        gdf=nh_gdf,
        zoom_to_layer=False,
        layer_name='National Highways',
        info_mode=None,
        style={'color': '#4aacff', 'weight': 1.8},
    )  

# Overlay State Highways
if overlay_sh:
    m.add_gdf(
        gdf=sh_gdf,
        zoom_to_layer=False,
        layer_name='State Highways',
        info_mode=None,
        style={'color': '#ff827a', 'weight': 1.6}, #red
    )

# Highlight Selected District
selected_gdf = districts_gdf[districts_gdf['District'] == district]
m.add_gdf(
    gdf=selected_gdf,
    layer_name='Selected District',
    zoom_to_layer=True,
    info_mode=None,
    style={'color': '#f1d600', 'fill': None, 'weight': 2} #yellow
)

# Display Map in Streamlit
m.to_streamlit(height=600)
