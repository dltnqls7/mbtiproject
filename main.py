import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 연예인 추천기 🌟",
    page_icon="🎤",
    layout="centered"
)

# MBTI별 연예인 데이터
mbti_celebrity = {
    "INTJ": {
        "celebrities": ["아이유 🎵", "RM (BTS) 📚", "박보검 🎬"],
        "description": "전략적인 사고가! 깊이있고 카리스마 넘치는 당신과 닮은 연예인들이에요! 🧠✨",
        "traits": "🎯 계획적 | 🔮 통찰력 | 👑 독립적",
        "color": "#6A0DAD"
    },
    "INTP": {
        "celebrities": ["슈가 (BTS) 🎹", "아이유 💡", "이동욱 🤔"],
        "description": "논리적인 사색가! 호기심 많고 창의적인 당신과 비슷한 연예인이에요! 🧪📖",
        "traits": "💭 분석적 | 🔬 탐구심 | 🎨 창의적",
        "color": "#4B0082"
    },
    "ENTJ": {
        "celebrities": ["제니 (BLACKPINK) 👑", "유재석 🎤", "공유 🔥"],
        "description": "대담한 통솔자! 카리스마와 리더십을 갖춘 당신과 어울리는 연예인이에요! 💼⚡",
        "traits": "👑 리더십 | 🎯 목표지향 | 💪 강인함",
        "color": "#B22222"
    },
    "ENTP": {
        "celebrities": ["G-DRAGON 🎨", "이효리 ✨", "조세호 🎭"],
        "description": "뜨거운 논쟁가! 재치있고 창의적인 당신과 닮은 연예인이에요! 💡🎉",
        "traits": "💡 창의적 | 🗣️ 토론가 | 🌈 자유로움",
        "color": "#FF8C00"
    },
    "INFJ": {
        "celebrities": ["뷔 (BTS) 🌙", "수지 🌸", "박보영 ✨"],
        "description": "선의의 옹호자! 신비롭고 따뜻한 당신과 어울리는 연예인이에요! 💜🦋",
        "traits": "🌙 신비로움 | 💖 공감능력 | 🎨 예술적",
        "color": "#9370DB"
    },
    "INFP": {
        "celebrities": ["아이유 🌷", "지민 (BTS) 🌸", "박보영 🦋"],
        "description": "열정적인 중재자! 순수하고 감성적인 당신과 닮은 연예인이에요! 🌈💕",
        "traits": "💭 이상주의 | 🎨 감성적 | 🌷 순수함",
        "color": "#FFB6C1"
    },
    "ENFJ": {
        "celebrities": ["진 (BTS) 💖", "장원영 🌟", "차은우 ✨"],
        "description": "정의로운 사회운동가! 따뜻하고 카리스마 있는 당신과 어울리는 연예인이에요! 🤗🌟",
        "traits": "💖 따뜻함 | 🗣️ 영향력 | 🌈 이타적",
        "color": "#32CD32"
    },
    "ENFP": {
        "celebrities": ["제이홉 (BTS) 🌈", "장원영 💖", "유노윤호 ⚡"],
        "description": "재기발랄한 활동가! 밝고 에너지 넘치는 당신과 닮은 연예인이에요! 🎊🌟",
        "traits": "🎉 활발함 | 💡 창의적 | 🌟 긍정적",
        "color": "#FFD700"
    },
    "ISTJ": {
        "celebrities": ["정국 (BTS) 🎯", "손흥민 ⚽", "김연아 ⛸️"],
        "description": "청렴결백한 논리주의자! 성실하고 책임감 강한 당신과 어울리는 연예인이에요! 📚🏆",
        "traits": "📋 성실함 | 🎯 책임감 | 💎 신중함",
        "color": "#4682B4"
    },
    "ISFJ": {
        "celebrities": ["지수 (BLACKPINK) 🌸", "박보영 💝", "이지은 🌻"],
        "description": "용감한 수호자! 헌신적이고 따뜻한 당신과 닮은 연예인이에요! 🤗💐",
        "traits": "💖 헌신적 | 🌷 따뜻함 | 🛡️ 보호본능",
        "color": "#DEB887"
    },
    "ESTJ": {
        "celebrities": ["제니 (BLACKPINK) 💼", "유재석 🎤", "강호동 💪"],
        "description": "엄격한 관리자! 체계적이고 리더십 있는 당신과 어울리는 연예인이에요! 🏆📊",
        "traits": "📋 체계적 | 💪 리더십 | 🎯 실용적",
        "color": "#8B4513"
    },
    "ESFJ": {
        "celebrities": ["로제 (BLACKPINK) 🌹", "트와이스 나연 💕", "이광수 😆"],
        "description": "사교적인 외교관! 친절하고 사람을 좋아하는 당신과 닮은 연예인이에요! 🌈🤗",
        "traits": "💝 친절함 | 🎊 사교적 | 🌟 배려심",
        "color": "#FF69B4"
    },
    "ISTP": {
        "celebrities": ["슈가 (BTS) 🎹", "현빈 🎬", "송중기 ⚔️"],
        "description": "만능 재주꾼! 쿨하고 실용적인 당신과 어울리는 연예인이에요! 🔧😎",
        "traits": "🛠️ 실용적 | 😎 쿨함 | 🎯 독립적",
        "color": "#2F4F4F"
    },
    "ISFP": {
        "celebrities": ["뷔 (BTS) 🎨", "리사 (BLACKPINK) 🌺", "수지 🌷"],
        "description": "호기심 많은 예술가! 감성적이고 자유로운 당신과 닮은 연예인이에요! 🎨🦋",
        "traits": "🎨 예술적 | 🌸 감성적 | 🕊️ 자유로움",
        "color": "#FF7F50"
    },
    "ESTP": {
        "celebrities": ["제이홉 (BTS) 🔥", "이효리 ⚡", "김종국 💪"],
        "description": "모험을 즐기는 사업가! 활동적이고 대담해요!"
