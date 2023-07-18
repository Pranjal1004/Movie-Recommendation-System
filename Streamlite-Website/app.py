import streamlit as st
import pandas as pd
from multiapp import MultiApp
from apps import overview, comments, recommendations # import your app modules here
movie_data = pd.read_csv("movie_data_upto_2022_march.csv")
app = MultiApp()
st.title("Movie Recommendation system")

movie_selected = st.selectbox("Search a movie", movie_data.movie_title.values)
# st.markdown("""
# #
# """)

# Add all your application here
app.add_app("Movie Overview", overview.app)
app.add_app("movie comments", comments.app)
app.add_app("Movie Recommendations", recommendations.app(movie_selected))
# The main app
app.run()
