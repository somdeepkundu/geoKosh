import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import leafmap.foliumap as leafmap



st.set_page_config(page_title='Rasta', layout='wide')

st.title('West Bengal Highway Dashboard')  

st.sidebar.title(':blue[About]')
st.sidebar.info('Explore the National and State Highway Statistics'\
                ' of different Districts of West Bengal', icon=":material/monitoring:")

data_url = 'https://github.com/somdeepkundu/geoKosh/' \
    'raw/main/osmRoads/'
         
gpkg_file = 'wb_roads.gpkg'
csv_file = 'wb_mejor_roads.csv'

@st.cache_data
def read_gdf(url, layer): 
    gdf = gpd.read_file(url, layer=layer)
    return gdf

@st.cache_data
def read_csv(url):
    df = pd.read_csv(url)
    return df

gpkg_url = data_url + gpkg_file
csv_url = data_url + csv_file
districts_gdf = read_gdf(gpkg_url, 'wb_district')
nh_gdf = read_gdf(gpkg_url, 'wb_nh')
sh_gdf = read_gdf(gpkg_url, 'wb_sh')
lengths_df = read_csv(csv_url)

# Data Selection and backend processing
districts = districts_gdf.District.values
district = st.sidebar.selectbox('Select a District', districts)
overlay_nh = st.sidebar.checkbox('Overlay NH')
overlay_sh = st.sidebar.checkbox('Overlay SH')
district_lengths = lengths_df[lengths_df['District'] == district]

# Plotting Chart
fig, ax = plt.subplots(1, 1)
district_lengths.plot(kind='bar', ax=ax, color=['#ff827a', '#4aacff'], #red, blue
    ylabel='Kilometers', xlabel='Category')
ax.set_title(f'Length of Highways - {district}')
ax.get_xaxis().set_ticklabels([])
ax.set_ylim(0, 402)  # in KM

fig.patch.set_facecolor('#969696') # Chart background color
ax.set_facecolor('#cccccc')

stats = st.sidebar.pyplot(fig)

## Create the map

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


if overlay_nh:
    m.add_gdf(
        gdf=nh_gdf,
        zoom_to_layer=False,
        layer_name='National Highways',
        info_mode=None,
        style={'color': '#4aacff', 'weight': 1.8},
    )  
if overlay_sh:
    m.add_gdf(
        gdf=sh_gdf,
        zoom_to_layer=False,
        layer_name='State Highways',
        info_mode=None,
        style={'color': '#ff827a', 'weight': 1.6}, #red
    )

    
selected_gdf = districts_gdf[districts_gdf['District'] == district]

m.add_gdf(
    gdf=selected_gdf,
    layer_name='Selected District',
    zoom_to_layer=True,
    info_mode=None,
    style={'color': '#f1d600', 'fill': None, 'weight': 2} #yellow
 )


m_streamlit = m.to_streamlit(800, 600)
st.write('*By Somdeep Kundu!* :sunglasses:')


# Download Chart
file_name = f'{district} Highways.png'  
plt.savefig(file_name, format='png')
with open(file_name, 'rb') as img:
    st.sidebar.download_button(
        'Download Chart',
        data=img,
        file_name=file_name,
        mime='image/png')
st.sidebar.markdown('''
---
Created with ❤️ by [Somdeep Kundu](https://www.youtube.com/@sthan-kaal-patra/).
''')
