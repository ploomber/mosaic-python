import streamlit as st
from streamlit_mosaic import mosaic
from specs import basic, flights_10m, vonoroi, stock

st.header("streamlit-mosaic")

st.markdown(
    """
```bash
pip install streamlit-mosaic
```
"""
)


# Create a radio button to switch between plots
plot_choice = st.radio(
    "Choose a plot:",
    ("Penguin Data", "Flights 10M", "Voronoi Diagram", "Stock Prices"),
)

uri = None
# uri = "http://localhost:3000"

# Display the chosen plot
if plot_choice == "Penguin Data":
    mosaic(spec=basic, height=600, uri=uri)
elif plot_choice == "Flights 10M":
    mosaic(spec=flights_10m, height=600, uri=uri)
elif plot_choice == "Voronoi Diagram":
    mosaic(spec=vonoroi, height=680, uri=uri)
else:
    mosaic(spec=stock, height=400, uri=uri)
