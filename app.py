import streamlit as st

st.set_page_config(page_title="Risk Analytics", page_icon="📊")

st.title("📊 Mines Risk & Probability Calculator")
st.markdown("---")

# Layout for inputs
col_in1, col_in2 = st.columns(2)

with col_in1:
    total_bombs = st.number_input("Total Bombs in Game", min_value=1, max_value=24, value=3)
with col_in2:
    tiles_opened = st.number_input("Tiles Already Opened", min_value=0, max_value=(25 - total_bombs - 1), value=0)

# Calculations
total_tiles = 25
remaining_tiles = total_tiles - tiles_opened
safe_tiles = remaining_tiles - total_bombs

# Probability logic
if remaining_tiles > 0:
    bomb_chance = (total_bombs / remaining_tiles) * 100
    success_chance = (safe_tiles / remaining_tiles)
    fair_multiplier = 1 / success_chance if success_chance > 0 else 0
else:
    bomb_chance = 0
    fair_multiplier = 0

# Visual Results
st.subheader("Statistical Output")
c1, c2 = st.columns(2)
c1.metric("Next Tile Bomb Risk", f"{bomb_probability:.2f}%")
c2.metric("Fair Value Multiplier", f"{fair_multiplier:.3f}x")

st.progress(bomb_probability / 100)

st.write(f"💡 **Analysis:** There are {safe_tiles} safe tiles left out of {remaining_tiles} hidden spots.")
st.caption("Note: This tool uses pure mathematics to show probability. It does not predict outcomes.")
