# Prediction from Under Count (last 20)
st.subheader("Prediction from Under Count (last 20)")
prediction, under_count = predict_from_unders(data, min_unders_for_above=min_unders)
if prediction:
    st.session_state.last_prediction = prediction
    st.write(f"Prediction: **{prediction}** (Under count in last 20 = {under_count})")
else:
    st.write(f"Not enough data yet (need at least {WINDOW} rounds).")

# Prediction from Under Count (last 50)
st.subheader("Prediction from Under Count (last 50)")
prediction_50, under_count_50 = predict_from_unders(
    data, window=50, min_unders_for_above=int(min_unders * 50 / 20)
)
if prediction_50:
    st.write(f"Prediction: **{prediction_50}** (Under count in last 50 = {under_count_50})")
else:
    st.write("Not enough data yet (need at least 50 rounds).")

# Prediction from Under Count (last 100)
st.subheader("Prediction from Under Count (last 100)")
prediction_100, under_count_100 = predict_from_unders(
    data, window=100, min_unders_for_above=int(min_unders * 100 / 20)
)
if prediction_100:
    st.write(f"Prediction: **{prediction_100}** (Under count in last 100 = {under_count_100})")
else:
    st.write("Not enough data yet (need at least 100 rounds).")