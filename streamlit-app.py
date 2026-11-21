import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Key Dental Health Indicators for Public Education (2026)",
    layout="wide",
)

st.title("Key Dental Health Indicators for Public Education (2026)")
st.markdown(
    "A sourced compilation of 13 WHO/CDC/NIDCR figures on dental disease and prevention, "
    "published as an open dataset for public education. Compiled by Masood Ahmad, Editor of "
    "[Dentist in Pico Rivera](https://dentalpicorivera.com/) — a free informational website of "
    "more than 200 plain-English dental guides for families in and around Pico Rivera, California. "
    "It is an education project, not a dental practice."
)
st.markdown(
    "[Dental Health Statistics Explorer](https://dentalpicorivera.com/dental-health-statistics-explorer/) · "
    "[Statistics page](https://dentalpicorivera.com/dental-health-statistics/) · "
    "[Dataset on Mendeley](https://doi.org/10.17632/fjzs5vxtrb.1) · "
    "[Dataset on GitHub](https://github.com/masood2662/key-dental-health-indicators) · "
    "Licence: CC BY 4.0"
)

df = pd.read_csv("dental-health-indicators-2026.csv")
st.subheader("The 13 indicators")
st.dataframe(df, use_container_width=True)

st.subheader("CDC percentages at a glance")
chart = pd.DataFrame(
    {
        "Indicator": [
            "Children 6-8, cavity in baby teeth",
            "Children 5-11, untreated decay",
            "Children 6-11, untreated cavities",
            "Adults, untreated cavities",
            "Adults 20-64, ever had a cavity",
            "Adults 30+, gum disease",
        ],
        "Percent": [52, 20, 16.7, 25, 90, 47.2],
    }
).set_index("Indicator")
st.bar_chart(chart)

comp = pd.read_csv("derived-comparisons-2026.csv")
st.subheader("Derived comparisons")
for _, row in comp.iterrows():
    st.markdown(f"**{row['title']}** — {row['finding']}")

st.markdown(
    "Methodology: only primary publishers were used (WHO for global burden, CDC for the United "
    "States). Values were extracted on 4 November 2026. The five comparisons are arithmetic or "
    "juxtaposition only — no modelling, estimation or extrapolation. Full methodology: see "
    "README-methodology.md in the "
    "[GitHub repository](https://github.com/masood2662/key-dental-health-indicators)."
)
