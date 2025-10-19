import streamlit as st
import requests
import random

API_BASE = "https://api.genshin.dev/characters"

st.set_page_config(page_title="Genshin Character Explorer", page_icon="✨")

st.title("🌸 Genshin Character Explorer")
st.write("Khám phá thông tin nhân vật Genshin Impact một cách chill 😎")

# Lấy danh sách nhân vật
characters = requests.get(API_BASE).json()
selected_char = st.selectbox("Chọn nhân vật", characters)

if st.button("🎲 Random nhân vật"):
    selected_char = random.choice(characters)

# Lấy dữ liệu chi tiết
data = requests.get(f"{API_BASE}/{selected_char}").json()

# Hiển thị thông tin
st.subheader(f"{data.get('name', selected_char).title()}")
st.image(f"{API_BASE}/{selected_char}/icon.png", width=200)

st.markdown(f"**Vision:** {data.get('vision', 'N/A')}")
st.markdown(f"**Weapon:** {data.get('weapon', 'N/A')}")
st.markdown(f"**Nation:** {data.get('nation', 'N/A')}")
st.markdown(f"**Rarity:** {data.get('rarity', 'N/A')} ⭐")
st.markdown(f"**Description:** {data.get('description', 'Không có mô tả 💤')}")

st.markdown("---")
st.caption("Made with ❤️ by Duy (vọc chơi thôi mà làm đẹp quá 😆)")
