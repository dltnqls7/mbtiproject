import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 포켓몬 추천기 🎮",
    page_icon="⚡",
    layout="centered"
)

# MBTI별 포켓몬 데이터
mbti_pokemon = {
    "INTJ": {
        "pokemons": ["뮤츠 🧠", "겐가르 👻", "메타그로스 🤖"],
        "description": "전략가! 깊이 사고하고 계획적인 당신에게는 지능적이고 신비로운 포켓몬이 어울려요! 🎯",
        "color": "#6A0DAD"
    },
    "INTP": {
        "pokemons": ["폴리곤 💻", "알라카잠 🔮", "로토무 ⚡"],
        "description": "논리적인 사색가! 호기심 많은 당신에게는 지적인 포켓몬이 딱이에요! 🧪",
        "color": "#4B0082"
    },
    "ENTJ": {
        "pokemons": ["리자몽 🔥", "갸라도스 🐉", "루카리오 ⚔️"],
        "description": "대담한 통솔자! 카리스마 넘치는 당신에게는 강력한 리더 포켓몬이 어울려요! 👑",
        "color": "#B22222"
    },
    "ENTP": {
        "pokemons": ["피카츄 ⚡", "조로아크 🦊", "엑스라이즈 🔄"],
        "description": "뜨거운 논쟁가! 창의적이고 재치있는 당신에게는 변화무쌍한 포켓몬이 어울려요! 💡",
        "color": "#FF8C00"
    },
    "INFJ": {
        "pokemons": ["루나톤 🌙", "가디안 💚", "님피아 🎀"],
        "description": "선의의 옹호자! 따뜻하고 통찰력 있는 당신에게는 신비롭고 우아한 포켓몬이 어울려요! ✨",
        "color": "#9370DB"
    },
    "INFP": {
        "pokemons": ["이브이 🌸", "푸린 🎵", "데덴네 💕"],
        "description": "열정적인 중재자! 순수하고 이상주의적인 당신에게는 사랑스러운 포켓몬이 딱이에요! 🌷",
        "color": "#FFB6C1"
    },
    "ENFJ": {
        "pokemons": ["치코리타 🌿", "행복 💖", "블래키 🌟"],
        "description": "정의로운 사회운동가! 카리스마 있고 따뜻한 당신에게는 친근한 포켓몬이 어울려요! 🤗",
        "color": "#32CD32"
    },
    "ENFP": {
        "pokemons": ["피카츄 ⚡", "마릴 💧", "토게피 🥚"],
        "description": "재기발랄한 활동가! 밝고 에너지 넘치는 당신에게는 귀엽고 활발한 포켓몬이 어울려요! 🎉",
        "color": "#FFD700"
    },
    "ISTJ": {
        "pokemons": ["꼬부기 🐢", "롱스톤 🪨", "갑주무사 🛡️"],
        "description": "청렴결백한 논리주의자! 성실하고 신중한 당신에게는 든든한 포켓몬이 어울려요! 📚",
        "color": "#4682B4"
    },
    "ISFJ": {
        "pokemons": ["치코리타 🌱", "이브이 🤎", "럭키 💝"],
        "description": "용감한 수호자! 헌신적이고 따뜻한 당신에게는 다정한 포켓몬이 딱이에요! 🌻",
        "color": "#DEB887"
    },
    "ESTJ": {
        "pokemons": ["근육몬 💪", "코뿌리 🦏", "다부니 🥊"],
        "description": "엄격한 관리자! 책임감 강하고 체계적인 당신에게는 강인한 포켓몬이 어울려요! 🏆",
        "color": "#8B4513"
    },
    "ESFJ": {
        "pokemons": ["라프라스 🎶", "행복 🌈", "푸린 🎤"],
        "description": "사교적인 외교관! 친절하고 사람을 좋아하는 당신에게는 사랑스러운 포켓몬이 어울려요! 💐",
        "color": "#FF69B4"
    },
    "ISTP": {
        "pokemons": ["스라크 ⚔️", "팬텀 👤", "메깅 🦂"],
        "description": "만능 재주꾼! 대담하고 실용적인 당신에게는 쿨한 포켓몬이 딱이에요! 🔧",
        "color": "#2F4F4F"
    },
    "ISFP": {
        "pokemons": ["이브이 🍃", "버터플 🦋", "샤미드 💧"],
        "description": "호기심 많은 예술가! 감성적이고 자유로운 당신에게는 아름다운 포켓몬이 어울려요! 🎨",
        "color": "#FF7F50"
    },
    "ESTP": {
        "pokemons": ["리자몽 🔥", "괴력몬 💥", "헤라크로스 🦏"],
        "description": "모험을 즐기는 사업가! 활동적이고 대담한 당신에게는 박력있는 포켓몬이 어울려요! 🏍️"
        ,
        "color": "#DC143C"
    },
    "ESFP": {
        "pokemons": ["피카츄 🌟", "이상해풀 🌺", "버터플 🌈"],
        "description": "자유로운 영혼의 연예인! 즐거움을 사랑하는 당신에게는 화려한 포켓몬이 딱이에요! 🎊",
        "color": "#FF1493"
    }
}

# 타이틀
st.title("🎮 MBTI 포켓몬 추천기 ⚡")
st.markdown("### 당신의 MBTI와 찰떡궁합 포켓몬을 찾아드려요! 🔍✨")
st.markdown("---")

# 설명
st.markdown("""
#### 🌟 사용 방법
1. 아래에서 본인의 **MBTI**를 선택해주세요! 🧐  
2. **추천 받기** 버튼을 눌러주세요! 🎯  
3. 당신에게 어울리는 포켓몬을 만나보세요! 💖
""")

st.markdown("---")

# MBTI 선택
col1, col2 = st.columns(2)

with col1:
    ei = st.radio("🗣️ **E** vs **I**", ["E (외향) 🎉", "I (내향) 🌙"])
    sn = st.radio("👀 **S** vs **N**", ["S (감각) 🔍", "N (직관) 💭"])

with col2:
    tf = st.radio("💭 **T** vs **F**", ["T (사고) 🧠", "F (감정) 💖"])
    jp = st.radio("📅 **J** vs **P**", ["J (판단) 📋", "P (인식) 🎨"])

# MBTI 조합
mbti = ei[0] + sn[0] + tf[0] + jp[0]

st.markdown("---")

# 결과 보기 버튼
if st.button("🎲 내 포켓몬 추천 받기! 🎁", use_container_width=True):
    result = mbti_pokemon[mbti]
    
    st.balloons()
    
    # 결과 표시
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {result['color']}, #ffffff); 
                padding: 30px; 
                border-radius: 20px; 
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
        <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            🎊 당신은 {mbti} 유형! 🎊
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    st.success(f"### 💫 {result['description']}")
    
    st.markdown("### 🌟 당신에게 추천하는 포켓몬 BEST 3! 🌟")
    
    # 포켓몬 3개 카드로 표시
    cols = st.columns(3)
    medals = ["🥇", "🥈", "🥉"]
    for idx, (col, pokemon) in enumerate(zip(cols, result['pokemons'])):
        with col:
            st.markdown(f"""
            <div style="background-color: #FFF8DC; 
                        padding: 20px; 
                        border-radius: 15px; 
                        text-align: center;
                        border: 3px solid {result['color']};
                        margin: 10px 0;">
                <h2>{medals[idx]}</h2>
                <h3>{pokemon}</h3>
            </div>
            """, unsafe_allow_html=True)
    
    # 랜덤 응원 메시지
    messages = [
        "🌈 오늘도 포켓몬과 함께 행복한 하루 보내세요!",
        "⚡ 당신의 포켓몬 마스터 여정을 응원해요!",
        "💖 당신은 정말 특별한 트레이너예요!",
        "🎵 포켓몬과 함께라면 무엇이든 할 수 있어요!",
        "🌟 당신의 빛나는 매력이 포켓몬에게도 전해질 거예요!"
    ]
    st.info(random.choice(messages))

# 푸터
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    Made with ❤️ for 당곡고등학교 친구들 | 🎮 Pokemon × MBTI 🎮
</div>
""", unsafe_allow_html=True)
