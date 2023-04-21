# Data courtesy of 
# https://www.inaturalist.org/observations?project_id=62152&ttl=900&place_id=any&verifiable=any&view=species

import streamlit as st
import pandas as pd
import plotly.express as px


#df = pd.read_csv("iNaturalist_poppy_2023_observations-316331.csv",index_col=False)
df = pd.read_csv("iNaturalist_flower_202304_organized.csv",index_col=False)

# Need to reorder colors for streamlit's color cycle sequence
label_order = ["Blue dick","Chia","Pimpernel","Violet","Clover","Blue grass","Poppy","Buttercup","Lupine","Fiddleneck","Baby blue eyes"]

new_ordering = []
for name in label_order:
    new_ordering.append( df[ df.new_name == name ])
df_reordered = pd.concat(new_ordering)
df = df_reordered

# ===== Displa
st.markdown("# April 2023 flower sightings")
st.write("#### Data courtesy of citizen naturalist observations on `inaturalist.org`.")
st.write("https://www.inaturalist.org/projects/best-wildflower-bloom-areas-of-california")

#st.map(df)
#fig = px.density_mapbox(df, lat="latitude", lon="longitude",radius=12,
#                        center=dict(lat=34.052235,lon=-118.243683), zoom=8.0,
#                        mapbox_style="stamen-terrain")

dotsize = 1**pd.np.ones_like( df.new_name.values )

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                        center=dict(lat=34.052235,lon=-118.243683), zoom=8.0,
                        size = dotsize.tolist(), size_max = 10,
                        mapbox_style="stamen-terrain",color="new_name")

fig.update_layout(
    width=800,
    height=800,
)
st.plotly_chart(fig, use_container_width=True)

# Histogram
st.markdown("# Most common flower sightings")
st.markdown("#### The top flowers reported below only make up ~16\% of reported flower sightings!")
st.markdown("(there were a few thousand unique species in the data set)")
fig = px.bar(df.new_name.value_counts())
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)

