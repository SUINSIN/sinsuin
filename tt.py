import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls')

col1, col2 = st.columns([1, 1])
with col1:
    st.image('수인사진2.jpg', width=260)
with col2:
    st.write('📌안 뽑으시면 후회합니다📌')
    ('')
    ('전화번호📞: 010-1234-5678')
    ('')
    ('이메일📧: xxx123@gmail.com')
    ('')
    ('주소🏚️: 경기도 xxx xxx xxx ')
    ('')
    ('이름🧑🏻: 신수인')
''
'───────────────────────────────────────────'
''
st.title("신수인을 소개합니다.")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write('최종학력: 건양대학교 졸업, 자격증: 위험물산업기사, 산업안전기사, 산업위생관리기사')
with col2:
    st.write('수상경력: 2022국립소방연구원공모전우수상, 2022한국산학기술학회추계학술대회우수논문상, 2023충청남도일반인심폐소생술 최우수상, 2023충청권창업경진대회최우수상, 2023한국산학기술학회추계학술대회캡스톤디자인 아이디어상 수상')
with col3:
    st.write('학점: 3.5/4.5','취미: 헬스, 수영, 스포츠 관람, 독서', '특기: 말하기, 팀 프로젝트' )
''
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    st.image('공모전.png')
with col2:
    st.image('학회.png')
with col3:
    st.image('일반인.png')
with col4:
    st.image('창업.png')
with col5:
    st.image('아이디어상.jpg')
''
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    st.link_button("기사1 💬", "https://www.goodmorningcc.com/news/articleView.html?idxno=277009")
with col2:
    st.link_button("기사2 💬", "https://fire.konyang.ac.kr/cop/bbs/BBSMSTR_000000001240/selectBoardArticle.do?nttId=201443&pageIndex=3&searchCnd=&searchWrd=")
with col3:
    st.link_button("기사3 💬", "https://www.joongdo.co.kr/web/view.php?key=20230413010004025")
with col4:
    st.link_button("기사4 💬", "https://www.ccdailynews.com/news/articleView.html?idxno=2235833")
with col5:
    st.link_button("기사5 💬", "https://fire.konyang.ac.kr/cop/bbs/BBSMSTR_000000001240/selectBoardArticle.do?nttId=246512&pageIndex=1&searchCnd=&searchWrd=")
''
import sys
sys.exit()

fig, ax = plt.subplots()

x = []
y = []
for i in range(-10, 11, 5):
    x.append(i)
    y.append(3*i**3 - 5*i - 7)

col1, col2, col3 = st.columns(3)
with col1:
    aa = st.radio('선의 색을 선택하시오', ('red', 'green', 'blue', 'black'))
with col2:
    bb = st.radio('마커의 형태를 선택하시오', ('s', '^', 'o'))
with col3:
    cc = st.radio('선의 스타일을 선택하시오', ('-', '-.', ':'))

plt.plot(x, y, color = aa, marker = bb, linestyle = cc)
st.pyplot(fig)


import sys
sys.exit()
