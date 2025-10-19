import streamlit as st
import requests
import random

# 👉 Dùng API chính thức từ GenshinDev
API_BASE = "https://raw.githubusercontent.com/genshindev/api-data/main/characters.json"


st.set_page_config(page_title="Genshin Character Explorer", page_icon="✨")

st.title("🌸 Genshin Character Explorer")
st.write("Khám phá thông tin nhân vật Genshin Impact một cách chill 😎")

# --- Lấy danh sách nhân vật ---
try:
    res = requests.get(API_BASE)
    res.raise_for_status()
    characters = res.json()  # Trả về list tên nhân vật
except Exception as e:
    st.error("Không thể tải danh sách nhân vật 😢 (API có thể đang lỗi)")
    st.stop()

# --- Giao diện chọn nhân vật ---
selected_char = st.selectbox("Chọn nhân vật", characters)

if st.button("🎲 Random nhân vật"):
    selected_char = random.choice(characters)

# --- Lấy dữ liệu chi tiết ---
try:
    data = requests.get(f"{API_BASE}/{selected_char}").json()
except Exception as e:
    st.error("Không thể tải thông tin nhân vật 🥲")
    st.stop()

# --- Hiển thị thông tin ---
st.subheader(f"{data.get('name', selected_char).title()}")

# Ảnh đại diện (nếu có)
st.image(f"{API_BASE}/{selected_char}/icon", width=200)

# Các thông tin khác
st.markdown(f"**Vision:** {data.get('vision', 'N/A')}")
st.markdown(f"**Weapon:** {data.get('weapon', 'N/A')}")
st.markdown(f"**Nation:** {data.get('nation', 'N/A')}")
st.markdown(f"**Rarity:** {data.get('rarity', 'N/A')} ⭐")
st.markdown(f"**Description:** {data.get('description', 'Không có mô tả 💤')}")

st.markdown("---")
st.caption("Made with ❤️ by Duy (vọc chơi thôi mà làm đẹp quá 😆)")

