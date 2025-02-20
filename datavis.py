import pandas as pd
import altair as alt

import streamlit as st
    
import altair as alt

st.title("Temp/Humidity Data - Blue Paradox")
st.text("""The following is roughly three months of temperature and humidity data
for the Blue Paradox exhibit. Three sensors are shown - one between the Pulse Point
and room 5, one in the main Rotunda (Room 1), and one in the National Geographic
gallery (entryway). See map below.""")

files = [
    {
        "name": "Room 1 (Rotunda)",
        "file": "1 - Rotunda-starts-2023-12-15-09-59-00-ends-2024-01-17-09-55-48.csv"
    },
    {
        "name": "Room 5",
        "file": "2 - BP Room 15-starts-2023-10-15-17-15-00-ends-2024-01-17-09-51-35.csv"
    },
    {
        "name": "Gallery",
        "file": "5 Gallery-starts-2023-11-01-17-20-00-ends-2024-01-17-12-36-30.csv"
    }
]

def make_graph(file_info):
    data = pd.read_csv(file_info['file']).iloc[::5, :]

    base = alt.Chart(data).encode(
        alt.X("Time:T").title(file_info['name'])
    )

    temp = base.mark_line(color="red").encode(
        alt.Y('Temp').title("Temperature (°F)")
    )

    humid = base.mark_line(color="green").encode(
        alt.Y("Humidity").title("Humidity (RH%)")
    )

    second = alt.layer(temp, humid).resolve_scale(y="independent"
        ).configure_axisLeft(titleColor='red'
        ).configure_axisRight(titleColor='green'
        ).interactive()
    st.altair_chart(second, use_container_width=True)

make_graph(files[1])
make_graph(files[0])
make_graph(files[2])
st.image("sensormap3.png")