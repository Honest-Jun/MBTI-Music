import streamlit as st
import json

# MBTI별 노래 데이터 불러오기
with open('mbti_songs.json', 'r') as f:
    mbti_songs = json.load(f)

# 앱 타이틀
st.title("MBTI별 노래 추천")

# MBTI 유형 선택
mbti_type = st.selectbox(
    '당신의 MBTI 유형을 선택하세요:',
    ['INTJ', 'ENFP', 'ISFJ', 'ESTP', 'INFJ', 'ENTP', 'ISFP', 'ESTJ', 'INFP', 'ESFP', 'ISTJ', 'ESFJ', 'ISTP', 'ENFJ', 'INTP', 'ISFJ']
)

# MBTI에 맞는 노래 추천
st.header(f"{mbti_type}에 추천하는 노래들:")

# 선택한 MBTI에 맞는 노래 목록 표시
if mbti_type in mbti_songs:
    songs = mbti_songs[mbti_type]
    for song in songs:
        st.write(f"- {song}")
else:
    st.write("추천 노래가 없습니다.")

# 앱 실행 안내
st.write("이 앱은 MBTI 유형에 따라 노래를 추천해주는 웹 애플리케이션입니다. MBTI 유형을 선택하여 좋아하는 노래를 찾으세요!")
