import streamlit as st
import streamlit.components.v1 as components

# Streamlit 애플리케이션 설정
st.set_page_config(
    page_title="선수 목록",
    page_icon="🧢",
    layout="wide",
    initial_sidebar_state="expanded")

# 선수 이미지 URL
players = {
    '강효종': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/6a00464c37f059ac3b52898fabd77bad8e7b36f3/pitch_images/%EA%B0%95%ED%9A%A8%EC%A2%85.png',
    '고우석': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B3%A0%EC%9A%B0%EC%84%9D.png',
    '김대현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EB%8C%80%ED%98%84.png',
    '김동규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EB%8F%99%EA%B7%9C.png',
    '김영준': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%98%81%EC%A4%80.png',
    '김유영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%9C%A0%EC%98%81.png',
    '김윤식': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%9C%A4%EC%8B%9D.png',
    '김주완': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%A3%BC%EC%99%84.png',
    '김진성': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EA%B9%80%EC%A7%84%EC%84%B1.png',
    '박명근': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%95%EB%AA%85%EA%B7%BC.png',
    '배재준': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%B0%EC%9E%AC%EC%A4%80.png',
    '백승현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EB%B0%B1%EC%8A%B9%ED%98%84.png',
    '성동현': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%84%B1%EB%8F%99%ED%98%84.png',
    '손주영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%86%90%EC%A3%BC%EC%98%81.png',
    '송은범': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%86%A1%EC%9D%80%EB%B2%94.png',
    '유영찬': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9C%A0%EC%98%81%EC%B0%AC.png',
    '윤호솔': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9C%A4%ED%98%B8%EC%86%94.png',
    '이민호': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EB%AF%BC%ED%98%B8.png',
    '이상규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%83%81%EA%B7%9C.png',
    '이상영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%83%81%EC%98%81.png',
    '이우찬': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%9A%B0%EC%B0%AC.png',
    '이정용': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A0%95%EC%9A%A9.png',
    '이지강': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9D%B4%EC%A7%80%EA%B0%95.png',
    '임정우': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9E%84%EC%A0%95%EC%9A%B0.png',
    '임찬규': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%9E%84%EC%B0%AC%EA%B7%9C.png',
    '정우영': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A0%95%EC%9A%B0%EC%98%81.png',
    '조원태': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A1%B0%EC%9B%90%ED%83%9C.png',
    '진해수': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%A7%84%ED%95%B4%EC%88%98.png',
    '채지선': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B1%84%EC%A7%80%EC%84%A0.png',
    '최동환': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B5%9C%EB%8F%99%ED%99%98.png',
    '최성훈': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%B5%9C%EC%84%B1%ED%9B%88.png',
    '켈리'  : 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%EC%BC%88%EB%A6%AC.png',
    '플럿코': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%ED%94%8C%EB%9F%BF%EC%BD%94.png',
    '함덕주': 'https://raw.githubusercontent.com/Gyeunggeun/Pitch/main/pitch_images/%ED%95%A8%EB%8D%95%EC%A3%BC.png'
}

# 사이드바
pages = ['선수 목록'] + list(players.keys())
selected_page = st.sidebar.selectbox('페이지', pages)

# 선수 목록 페이지 구성
if selected_page == '선수 목록':
    st.title('선수 목록')
    player_list = list(players.keys())
    for i in range(0, len(player_list), 5):  # 5*7 로 총 35명의 선수 이미지 표현
        columns = st.columns(5)
        for j in range(5):
            if i + j < len(player_list):
                player = player_list[i + j]
                with columns[j]:
                    image_url = players[player]
                    components.html(f'''
                        <center>
                            <img src="{image_url}" width="100%">
                            <p style="margin-top: 0px; color: white; font-size: 20px; font-weight: bold">{player}</p>
                        </center>
                    ''', height=200)
else:
    st.title(f'{selected_page}')
    # 선수의 세부 페이지에서 보여줄 정보를 검색하거나 계산
    if selected_page == '강효종':
        st.write('강효종 상세정보')
        # 강효종 선수에 대한 자세한 정보를 표시하는 코드...
    elif selected_page == '고우석':
        st.write('고우석 상세정보')
        # 고우석 선수에 대한 자세한 정보를 표시하는 코드...
    # 기타 선수들에 대한 코드는 elif를 이용하여 추가


