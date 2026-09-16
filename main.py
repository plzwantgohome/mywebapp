import streamlit as st
import math

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title="TRIP TONE",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', 'Noto Sans KR', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(225, 231, 255, 0.7), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(255, 232, 240, 0.65), transparent 30%),
        #f8f8f6;
    color: #111111;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

.hero {
    padding: 60px 20px 40px 20px;
    text-align: center;
}

.logo {
    font-size: 13px;
    letter-spacing: 0.35em;
    font-weight: 700;
    color: #666666;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(46px, 8vw, 88px);
    line-height: 0.95;
    letter-spacing: -0.055em;
    font-weight: 700;
    color: #101010;
}

.hero-sub {
    max-width: 610px;
    margin: 28px auto 0 auto;
    color: #727272;
    font-size: 16px;
    line-height: 1.8;
}

.section-title {
    font-size: 13px;
    letter-spacing: 0.16em;
    font-weight: 700;
    color: #777777;
    margin-bottom: 8px;
}

.question {
    font-size: 29px;
    letter-spacing: -0.03em;
    font-weight: 650;
    margin-bottom: 20px;
}

.input-card {
    background: rgba(255,255,255,0.78);
    border: 1px solid rgba(0,0,0,0.06);
    border-radius: 26px;
    padding: 30px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.05);
    backdrop-filter: blur(12px);
    margin-bottom: 26px;
}

.result-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(0,0,0,0.065);
    border-radius: 26px;
    padding: 30px;
    min-height: 240px;
    box-shadow: 0 16px 55px rgba(0,0,0,0.055);
}

.result-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.17em;
    color: #999999;
    margin-bottom: 16px;
}

.result-title {
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.025em;
    line-height: 1.25;
    margin-bottom: 14px;
}

.result-text {
    font-size: 15px;
    line-height: 1.8;
    color: #666666;
}

.chip {
    display: inline-block;
    background: #f1f1ef;
    color: #333333;
    border-radius: 999px;
    padding: 8px 13px;
    margin: 4px 5px 4px 0;
    font-size: 13px;
}

.color-preview {
    width: 100%;
    height: 145px;
    border-radius: 22px;
    margin-bottom: 18px;
    box-shadow: inset 0 0 0 1px rgba(0,0,0,0.06);
}

.summary-card {
    border-radius: 32px;
    padding: 38px;
    margin-top: 24px;
    color: white;
    position: relative;
    overflow: hidden;
}

.summary-card::after {
    content: "";
    position: absolute;
    width: 210px;
    height: 210px;
    border-radius: 50%;
    background: rgba(255,255,255,0.12);
    top: -90px;
    right: -45px;
}

.summary-small {
    font-size: 12px;
    letter-spacing: 0.16em;
    opacity: 0.75;
    font-weight: 700;
}

.summary-title {
    font-size: 34px;
    font-weight: 700;
    letter-spacing: -0.04em;
    margin-top: 9px;
    margin-bottom: 18px;
}

.summary-desc {
    max-width: 720px;
    font-size: 15px;
    line-height: 1.8;
    opacity: 0.9;
}

.footer {
    text-align: center;
    margin-top: 70px;
    font-size: 12px;
    letter-spacing: 0.12em;
    color: #aaaaaa;
}

div[data-testid="stColorPicker"] label,
div[data-testid="stSelectbox"] label {
    font-weight: 600 !important;
}

.stButton > button {
    width: 100%;
    height: 54px;
    border-radius: 999px;
    border: none;
    font-weight: 650;
    font-size: 15px;
    background: #111111;
    color: white;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #333333;
    color: white;
    transform: translateY(-1px);
}

div[data-baseweb="select"] > div {
    border-radius: 15px !important;
    min-height: 50px;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 데이터
# -------------------------------------------------
destinations = {
    "파리 🇫🇷": {
        "mood": "우아하고 클래식한 도시 무드",
        "weather": "레이어드가 쉬운 간결한 스타일",
        "base": ["트렌치코트", "스트레이트 팬츠", "로퍼", "미니멀 숄더백"],
    },
    "도쿄 🇯🇵": {
        "mood": "정교한 미니멀리즘과 도시적인 감성",
        "weather": "깔끔한 레이어링과 디테일 활용",
        "base": ["와이드 팬츠", "깔끔한 셔츠", "스니커즈", "크로스백"],
    },
    "제주 🇰🇷": {
        "mood": "여유롭고 자연스러운 아일랜드 무드",
        "weather": "편안하고 활동적인 스타일",
        "base": ["코튼 셔츠", "데님", "편한 스니커즈", "캔버스백"],
    },
    "뉴욕 🇺🇸": {
        "mood": "선명하고 자신감 있는 시티 스타일",
        "weather": "실용성과 존재감을 동시에 강조",
        "base": ["재킷", "스트레이트 데님", "스니커즈", "구조적인 백"],
    },
    "런던 🇬🇧": {
        "mood": "클래식하면서 살짝 자유로운 무드",
        "weather": "아우터 중심의 레이어드 스타일",
        "base": ["맥코트", "니트", "슬랙스", "로퍼"],
    },
    "로마 🇮🇹": {
        "mood": "따뜻하고 여유로운 클래식 스타일",
        "weather": "가볍고 자연스럽게 떨어지는 소재",
        "base": ["린넨 셔츠", "슬랙스", "플랫 슈즈", "숄더백"],
    },
    "바르셀로나 🇪🇸": {
        "mood": "밝고 자유로운 지중해 감성",
        "weather": "가벼운 소재와 컬러 포인트",
        "base": ["셔츠", "라이트 팬츠", "샌들", "미니백"],
    },
    "코펜하겐 🇩🇰": {
        "mood": "담백하고 세련된 북유럽 미니멀",
        "weather": "심플한 실루엣과 기능적인 아이템",
        "base": ["오버핏 셔츠", "와이드 팬츠", "스니커즈", "토트백"],
    },
}


color_styles = {
    "RED": {
        "rgb": (220, 55, 55),
        "name": "레드",
        "mood": "Bold & Confident",
        "description": "선명한 포인트와 자신감 있는 분위기가 어울리는 컬러입니다.",
        "items": ["레드 니트 또는 톱", "블랙 하의", "실버 액세서리"],
        "pair": "블랙 · 차콜 · 아이보리"
    },
    "ORANGE": {
        "rgb": (238, 135, 55),
        "name": "오렌지",
        "mood": "Warm & Energetic",
        "description": "따뜻하고 활기찬 분위기를 만드는 컬러입니다.",
        "items": ["오렌지 포인트 톱", "크림 팬츠", "브라운 액세서리"],
        "pair": "크림 · 브라운 · 네이비"
    },
    "YELLOW": {
        "rgb": (230, 190, 55),
        "name": "옐로",
        "mood": "Bright & Playful",
        "description": "가볍고 밝은 인상을 주면서 여행 룩에 생기를 더합니다.",
        "items": ["옐로 포인트 아이템", "화이트 셔츠", "연청 데님"],
        "pair": "화이트 · 데님 · 그레이"
    },
    "GREEN": {
        "rgb": (65, 145, 90),
        "name": "그린",
        "mood": "Natural & Calm",
        "description": "자연스럽고 차분하면서도 개성이 느껴지는 컬러입니다.",
        "items": ["그린 셔츠 또는 가디건", "베이지 하의", "브라운 슈즈"],
        "pair": "베이지 · 브라운 · 아이보리"
    },
    "BLUE": {
        "rgb": (55, 105, 205),
        "name": "블루",
        "mood": "Clean & Cool",
        "description": "깨끗하고 시원한 인상을 주는 도시적인 컬러입니다.",
        "items": ["블루 셔츠", "화이트 또는 그레이 하의", "실버 액세서리"],
        "pair": "화이트 · 그레이 · 네이비"
    },
    "PURPLE": {
        "rgb": (135, 80, 185),
        "name": "퍼플",
        "mood": "Artistic & Unique",
        "description": "예술적이고 조금 특별한 분위기를 연출하기 좋은 컬러입니다.",
        "items": ["퍼플 니트 또는 톱", "차콜 팬츠", "블랙 슈즈"],
        "pair": "차콜 · 블랙 · 라이트 그레이"
    },
    "PINK": {
        "rgb": (225, 115, 150),
        "name": "핑크",
        "mood": "Soft & Modern",
        "description": "부드러운 인상에 현대적인 포인트를 더하기 좋은 컬러입니다.",
        "items": ["핑크 셔츠 또는 가디건", "그레이 하의", "화이트 슈즈"],
        "pair": "그레이 · 화이트 · 버건디"
    },
    "BROWN": {
        "rgb": (130, 85, 55),
        "name": "브라운",
        "mood": "Classic & Earthy",
        "description": "차분하고 고급스러운 클래식 무드에 잘 어울립니다.",
        "items": ["브라운 재킷 또는 니트", "크림 하의", "골드 액세서리"],
        "pair": "크림 · 카멜 · 올리브"
    },
    "BLACK": {
        "rgb": (35, 35, 35),
        "name": "블랙",
        "mood": "Chic & Minimal",
        "description": "도시적이고 세련된 미니멀 스타일을 만들기 좋은 컬러입니다.",
        "items": ["블랙 아우터", "모노톤 이너", "메탈 액세서리"],
        "pair": "화이트 · 그레이 · 실버"
    },
    "WHITE": {
        "rgb": (235, 235, 230),
        "name": "화이트",
        "mood": "Clean & Effortless",
        "description": "깔끔하면서도 힘을 뺀 자연스러운 스타일에 어울립니다.",
        "items": ["화이트 셔츠", "베이지 또는 데님 하의", "심플한 슈즈"],
        "pair": "베이지 · 데님 · 네이비"
    },
}


# -------------------------------------------------
# 함수
# -------------------------------------------------
def hex_to_rgb(hex_color):
    """HEX 컬러를 RGB 값으로 변환"""
    hex_color = hex_color.lstrip("#")
    return tuple(
        int(hex_color[i:i + 2], 16)
        for i in (0, 2, 4)
    )


def color_distance(rgb1, rgb2):
    """RGB 공간에서 두 색상의 거리 계산"""
    return math.sqrt(
        sum((a - b) ** 2 for a, b in zip(rgb1, rgb2))
    )


def get_nearest_color(hex_color):
    """사용자가 고른 색과 가장 가까운 컬러 카테고리 찾기"""
    user_rgb = hex_to_rgb(hex_color)

    nearest = None
    smallest_distance = float("inf")

    for key, info in color_styles.items():
        distance = color_distance(user_rgb, info["rgb"])

        if distance < smallest_distance:
            smallest_distance = distance
            nearest = key

    return nearest


def text_color(hex_color):
    """배경색에 따라 흰색/검은색 글자 자동 선택"""
    r, g, b = hex_to_rgb(hex_color)

    brightness = (
        r * 299 +
        g * 587 +
        b * 114
    ) / 1000

    if brightness > 160:
        return "#111111"
    return "#FFFFFF"


# -------------------------------------------------
# Hero
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="logo">TRIP TONE</div>
    <div class="hero-title">
        Find your<br>
        travel color.
    </div>
    <div class="hero-sub">
        좋아하는 색 하나에서 시작하는 여행 스타일.<br>
        여행지의 분위기와 당신의 컬러를 조합해
        가장 어울리는 패션을 추천합니다.
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# 입력 영역
# -------------------------------------------------
st.markdown('<div class="input-card">', unsafe_allow_html=True)

left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown('<div class="section-title">01 · DESTINATION</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="question">어디로 떠나고 싶나요?</div>',
                unsafe_allow_html=True)

    destination = st.selectbox(
        "여행지 선택",
        list(destinations.keys()),
        label_visibility="collapsed"
    )

    info = destinations[destination]

    st.markdown(
        f"""
        <div style="
            margin-top:18px;
            padding:18px 20px;
            border-radius:17px;
            background:#f4f4f1;
        ">
            <div style="
                font-size:12px;
                color:#999;
                margin-bottom:6px;
                letter-spacing:.08em;
            ">
                DESTINATION MOOD
            </div>
            <div style="
                font-size:15px;
                line-height:1.6;
                color:#444;
            ">
                {info['mood']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with right:
    st.markdown('<div class="section-title">02 · COLOR</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="question">당신이 좋아하는 색은?</div>',
                unsafe_allow_html=True)

    favorite_color = st.color_picker(
        "좋아하는 색 선택",
        "#5475D8"
    )

    nearest_key = get_nearest_color(favorite_color)
    color_info = color_styles[nearest_key]

    st.markdown(
        f"""
        <div style="
            width:100%;
            height:105px;
            background:{favorite_color};
            border-radius:18px;
            margin-top:13px;
            border:1px solid rgba(0,0,0,.05);
        "></div>

        <div style="
            margin-top:14px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">
            <div style="font-size:14px;color:#555;">
                {color_info['name']} 계열
            </div>
            <div style="
                font-family:monospace;
                font-size:13px;
                color:#999;
            ">
                {favorite_color.upper()}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)


# -------------------------------------------------
# 추천 버튼
# -------------------------------------------------
recommend = st.button("나만의 여행 스타일 보기 →")


# -------------------------------------------------
# 결과
# -------------------------------------------------
if recommend:

    info = destinations[destination]
    nearest_key = get_nearest_color(favorite_color)
    color_info = color_styles[nearest_key]

    st.markdown(
        """
        <div style="
            margin-top:55px;
            margin-bottom:25px;
        ">
            <div class="section-title">YOUR STYLE</div>
            <div style="
                font-size:38px;
                font-weight:700;
                letter-spacing:-.04em;
            ">
                여행 스타일 추천
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3, gap="large")

    # 컬러 카드
    with c1:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    COLOR MOOD
                </div>

                <div
                    class="color-preview"
                    style="background:{favorite_color};">
                </div>

                <div class="result-title">
                    {color_info['mood']}
                </div>

                <div class="result-text">
                    {color_info['description']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 여행지 카드
    with c2:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    DESTINATION
                </div>

                <div class="result-title">
                    {destination}
                </div>

                <div class="result-text">
                    {info['mood']}<br><br>
                    {info['weather']}을 중심으로 코디하면
                    여행지의 분위기와 자연스럽게 어울릴 수 있습니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 패션 카드
    with c3:

        base_chips = "".join(
            f'<span class="chip">{item}</span>'
            for item in info["base"]
        )

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    KEY ITEMS
                </div>

                <div class="result-title">
                    Pack these.
                </div>

                <div style="margin-top:18px;">
                    {base_chips}
                </div>

                <div class="result-text"
                     style="margin-top:20px;">
                    여기에 <b>{color_info['name']}</b> 컬러를
                    한두 가지 아이템에 포인트로 활용해 보세요.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 코디 구체화
    st.markdown(
        """
        <div style="
            margin-top:35px;
            margin-bottom:20px;
        ">
            <div class="section-title">
                OUTFIT FORMULA
            </div>
            <div style="
                font-size:29px;
                font-weight:700;
                letter-spacing:-.03em;
            ">
                이렇게 입어보세요
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    f1, f2 = st.columns([1.4, 1], gap="large")

    fashion_items = color_info["items"]

    with f1:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    MAIN LOOK
                </div>

                <div class="result-title">
                    {fashion_items[0]}<br>
                    + {info['base'][1]}
                </div>

                <div class="result-text">
                    {destination}의 {info['mood']}에
                    {color_info['name']}의
                    {color_info['mood'].lower()} 무드를 더한 조합입니다.
                    <br><br>
                    좋아하는 색을 전체에 사용하는 것보다
                    상의, 가방, 신발처럼 한 부분에 포인트로 사용하면
                    훨씬 현대적이고 정돈된 스타일을 만들 수 있습니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with f2:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">
                    COLOR PAIRING
                </div>

                <div class="result-title">
                    {color_info['pair']}
                </div>

                <div class="result-text">
                    선택한 컬러와 함께 사용하기 좋은 기본 색상입니다.
                    <br><br>
                    <b>추천 포인트</b><br>
                    {fashion_items[1]}<br>
                    {fashion_items[2]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 최종 요약
    txt_color = text_color(favorite_color)

    st.markdown(
        f"""
        <div class="summary-card"
             style="
                background:{favorite_color};
                color:{txt_color};
             ">

            <div class="summary-small">
                YOUR TRIP TONE
            </div>

            <div class="summary-title">
                {destination} × {color_info['name']}
            </div>

            <div class="summary-desc">
                {destination}의 분위기를 기본으로
                <b>{color_info['name']}</b>을 포인트 컬러로 활용해 보세요.
                기본 아이템은 {", ".join(info['base'][:3])}처럼
                간결하게 구성하고, 선택한 컬러를 상의나 소품에
                한 번 반복하면 전체 룩에 통일감이 생깁니다.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown(
    """
    <div class="footer">
        TRIP TONE · COLOR YOUR JOURNEY
    </div>
    """,
    unsafe_allow_html=True
)
