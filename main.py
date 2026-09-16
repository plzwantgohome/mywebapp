import streamlit as st
import math
import textwrap


# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="TRIP TONE",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# HTML 출력 함수
# 들여쓰기 때문에 HTML이 코드처럼 보이는 문제 방지
# =========================================================
def html(content):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True
    )


# =========================================================
# CSS
# =========================================================
html("""
<style>

html, body, [class*="css"] {
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        "Noto Sans KR",
        sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(220, 226, 255, 0.65),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(255, 225, 235, 0.55),
            transparent 30%
        ),
        #f8f8f6;
    color: #111111;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}


/* Streamlit 기본 메뉴 숨기기 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* HERO */
.hero {
    padding: 70px 10px 50px 10px;
    text-align: center;
}

.logo {
    font-size: 12px;
    letter-spacing: 0.38em;
    font-weight: 700;
    color: #777;
    margin-bottom: 22px;
}

.hero-title {
    font-size: clamp(48px, 8vw, 86px);
    line-height: 0.98;
    letter-spacing: -0.06em;
    font-weight: 750;
    color: #111;
}

.hero-sub {
    max-width: 590px;
    margin: 28px auto 0 auto;
    font-size: 16px;
    line-height: 1.8;
    color: #747474;
}


/* 공통 카드 */
.card {
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(0,0,0,0.055);
    border-radius: 28px;
    padding: 30px;
    box-shadow:
        0 18px 55px rgba(0,0,0,0.055);
}

.section-label {
    font-size: 11px;
    font-weight: 750;
    color: #999;
    letter-spacing: 0.18em;
    margin-bottom: 13px;
}

.section-title {
    font-size: 30px;
    font-weight: 730;
    letter-spacing: -0.035em;
    margin-bottom: 10px;
    color: #141414;
}

.section-text {
    font-size: 14px;
    color: #777;
    line-height: 1.75;
}


/* 입력 카드 */
.input-card {
    max-width: 680px;
    margin: 0 auto 25px auto;
    padding: 35px;
    background: rgba(255,255,255,0.84);
    border: 1px solid rgba(0,0,0,0.055);
    border-radius: 30px;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.055);
}

.color-preview {
    width: 100%;
    height: 130px;
    border-radius: 22px;
    border: 1px solid rgba(0,0,0,0.06);
    margin-top: 18px;
    margin-bottom: 13px;
}

.color-meta {
    display: flex;
    justify-content: space-between;
    color: #777;
    font-size: 13px;
}


/* 결과 헤더 */
.result-header {
    margin-top: 70px;
    margin-bottom: 25px;
}

.result-big-title {
    font-size: 40px;
    font-weight: 750;
    letter-spacing: -0.045em;
    line-height: 1.1;
}


/* 결과 카드 */
.result-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(0,0,0,0.055);
    border-radius: 28px;
    padding: 30px;
    min-height: 250px;
    box-shadow:
        0 18px 55px rgba(0,0,0,0.055);
}

.result-label {
    font-size: 11px;
    font-weight: 750;
    letter-spacing: 0.18em;
    color: #999;
    margin-bottom: 20px;
}

.result-title {
    font-size: 26px;
    font-weight: 720;
    line-height: 1.35;
    letter-spacing: -0.025em;
    margin-bottom: 14px;
}

.result-text {
    font-size: 14px;
    color: #686868;
    line-height: 1.8;
}


/* 태그 */
.chip {
    display: inline-block;
    padding: 8px 13px;
    margin: 4px 4px 4px 0;
    border-radius: 999px;
    background: #f2f2ef;
    color: #444;
    font-size: 13px;
}


/* 메인 결과 */
.hero-result {
    border-radius: 32px;
    padding: 40px;
    margin-top: 30px;
    overflow: hidden;
    position: relative;
}

.hero-result::after {
    content: "";
    position: absolute;
    width: 270px;
    height: 270px;
    border-radius: 50%;
    background: rgba(255,255,255,0.12);
    right: -90px;
    top: -110px;
}

.hero-result-label {
    font-size: 11px;
    font-weight: 750;
    letter-spacing: 0.2em;
    opacity: 0.7;
}

.hero-result-title {
    font-size: 38px;
    font-weight: 750;
    letter-spacing: -0.04em;
    margin: 10px 0 15px 0;
}

.hero-result-text {
    max-width: 720px;
    font-size: 15px;
    line-height: 1.8;
    opacity: 0.88;
}


/* 버튼 */
.stButton > button {
    width: 100%;
    height: 56px;
    border: 0;
    border-radius: 999px;
    background: #111;
    color: white;
    font-size: 15px;
    font-weight: 650;
    transition: all 0.18s ease;
}

.stButton > button:hover {
    background: #303030;
    color: white;
    border: 0;
    transform: translateY(-1px);
}


/* 컬러피커 */
div[data-testid="stColorPicker"] {
    margin-top: 10px;
}


/* footer */
.custom-footer {
    text-align: center;
    margin-top: 80px;
    color: #aaa;
    font-size: 11px;
    letter-spacing: 0.18em;
}

</style>
""")


# =========================================================
# 색상별 추천 데이터
# =========================================================
color_styles = {

    "RED": {
        "rgb": (220, 55, 55),
        "name": "레드",
        "mood": "Bold & Energetic",

        "destination": "바르셀로나 🇪🇸",
        "destination_desc":
            "강렬한 색채와 자유로운 분위기가 어우러지는 도시입니다. "
            "레드의 활기찬 이미지와 바르셀로나의 밝고 생동감 있는 분위기가 잘 어울립니다.",

        "look": "모던 시티 룩",
        "clothes": [
            "레드 포인트 톱",
            "블랙 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],

        "fashion_desc":
            "레드를 옷 전체에 사용하기보다 상의나 가방처럼 한 부분에 포인트로 사용하면 "
            "강렬하면서도 세련된 스타일을 만들 수 있습니다.",

        "pair": "블랙 · 화이트 · 차콜"
    },


    "ORANGE": {
        "rgb": (235, 135, 55),
        "name": "오렌지",
        "mood": "Warm & Vibrant",

        "destination": "로마 🇮🇹",
        "destination_desc":
            "따뜻한 건축물과 햇빛이 인상적인 도시로, "
            "오렌지의 따뜻하고 활기찬 분위기와 자연스럽게 어울립니다.",

        "look": "웜 클래식 룩",
        "clothes": [
            "오렌지 니트",
            "크림 팬츠",
            "브라운 로퍼",
            "가죽 숄더백"
        ],

        "fashion_desc":
            "오렌지는 크림이나 브라운처럼 따뜻한 중성색과 함께 사용하면 "
            "부담스럽지 않으면서 자연스럽고 고급스럽게 보입니다.",

        "pair": "크림 · 브라운 · 베이지"
    },


    "YELLOW": {
        "rgb": (232, 195, 55),
        "name": "옐로",
        "mood": "Bright & Playful",

        "destination": "제주 🇰🇷",
        "destination_desc":
            "탁 트인 자연과 밝고 편안한 분위기가 특징인 여행지입니다. "
            "옐로의 밝은 이미지가 제주의 자연스러운 분위기와 잘 어울립니다.",

        "look": "라이트 캐주얼 룩",
        "clothes": [
            "옐로 가디건",
            "화이트 티셔츠",
            "연청 데님",
            "캔버스백"
        ],

        "fashion_desc":
            "밝은 옐로를 데님과 화이트에 조합하면 여행지에서 부담 없이 입기 좋은 "
            "산뜻하고 편안한 코디가 완성됩니다.",

        "pair": "화이트 · 데님 · 라이트 그레이"
    },


    "GREEN": {
        "rgb": (65, 145, 90),
        "name": "그린",
        "mood": "Natural & Calm",

        "destination": "코펜하겐 🇩🇰",
        "destination_desc":
            "자연과 도시가 조화를 이루고 차분한 북유럽 감성이 느껴지는 곳입니다. "
            "그린의 안정적이고 자연스러운 느낌과 잘 맞습니다.",

        "look": "내추럴 미니멀 룩",
        "clothes": [
            "그린 셔츠",
            "베이지 팬츠",
            "화이트 스니커즈",
            "브라운 토트백"
        ],

        "fashion_desc":
            "그린은 베이지와 브라운 같은 자연 계열 색상과 함께 사용하면 "
            "차분하면서도 감각적인 스타일을 만들 수 있습니다.",

        "pair": "베이지 · 브라운 · 아이보리"
    },


    "BLUE": {
        "rgb": (60, 105, 205),
        "name": "블루",
        "mood": "Clean & Cool",

        "destination": "도쿄 🇯🇵",
        "destination_desc":
            "깔끔하고 정돈된 도시 풍경과 현대적인 분위기를 가진 여행지입니다. "
            "블루의 시원하고 세련된 이미지와 잘 어울립니다.",

        "look": "클린 미니멀 룩",
        "clothes": [
            "블루 셔츠",
            "그레이 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],

        "fashion_desc":
            "블루를 화이트와 그레이 같은 무채색과 함께 사용하면 "
            "깔끔하고 도시적인 느낌을 강조할 수 있습니다.",

        "pair": "화이트 · 그레이 · 네이비"
    },


    "PURPLE": {
        "rgb": (135, 80, 185),
        "name": "퍼플",
        "mood": "Artistic & Unique",

        "destination": "파리 🇫🇷",
        "destination_desc":
            "예술과 패션의 분위기가 강한 도시로, "
            "퍼플의 독특하고 예술적인 이미지와 잘 어울립니다.",

        "look": "아티스틱 시크 룩",
        "clothes": [
            "퍼플 니트",
            "차콜 슬랙스",
            "블랙 로퍼",
            "미니 숄더백"
        ],

        "fashion_desc":
            "퍼플은 차콜이나 블랙과 조합하면 색의 개성은 유지하면서도 "
            "전체적인 스타일은 차분하고 세련되게 정리할 수 있습니다.",

        "pair": "차콜 · 블랙 · 라이트 그레이"
    },


    "PINK": {
        "rgb": (225, 115, 150),
        "name": "핑크",
        "mood": "Soft & Modern",

        "destination": "파리 🇫🇷",
        "destination_desc":
            "클래식한 건축과 세련된 거리 분위기가 특징인 도시입니다. "
            "핑크의 부드러운 이미지에 도시적인 느낌을 더하기 좋은 여행지입니다.",

        "look": "소프트 모던 룩",
        "clothes": [
            "핑크 가디건",
            "그레이 팬츠",
            "화이트 스니커즈",
            "미니백"
        ],

        "fashion_desc":
            "핑크를 그레이처럼 차분한 색과 함께 사용하면 "
            "지나치게 화려하지 않으면서 부드럽고 현대적인 스타일이 됩니다.",

        "pair": "그레이 · 화이트 · 버건디"
    },


    "BROWN": {
        "rgb": (130, 85, 55),
        "name": "브라운",
        "mood": "Classic & Earthy",

        "destination": "런던 🇬🇧",
        "destination_desc":
            "클래식한 건축과 차분한 거리 분위기를 가진 도시입니다. "
            "브라운의 안정적이고 클래식한 이미지와 잘 어울립니다.",

        "look": "클래식 레이어드 룩",
        "clothes": [
            "브라운 재킷",
            "아이보리 니트",
            "진청 데님",
            "로퍼"
        ],

        "fashion_desc":
            "브라운은 아이보리나 크림 계열과 함께 사용하면 "
            "무겁지 않으면서도 따뜻하고 클래식한 분위기를 만들 수 있습니다.",

        "pair": "아이보리 · 크림 · 네이비"
    },


    "BLACK": {
        "rgb": (35, 35, 35),
        "name": "블랙",
        "mood": "Chic & Minimal",

        "destination": "뉴욕 🇺🇸",
        "destination_desc":
            "빠르고 현대적인 도시 이미지와 강한 개성이 공존하는 여행지입니다. "
            "블랙의 시크하고 미니멀한 분위기와 특히 잘 맞습니다.",

        "look": "올 블랙 시티 룩",
        "clothes": [
            "블랙 재킷",
            "블랙 또는 차콜 팬츠",
            "화이트 이너",
            "실버 액세서리"
        ],

        "fashion_desc":
            "블랙을 중심으로 실루엣을 단순하게 잡고 화이트나 실버를 소량 사용하면 "
            "깔끔하면서도 강한 도시적인 분위기를 만들 수 있습니다.",

        "pair": "화이트 · 차콜 · 실버"
    },


    "WHITE": {
        "rgb": (238, 238, 233),
        "name": "화이트",
        "mood": "Clean & Effortless",

        "destination": "코펜하겐 🇩🇰",
        "destination_desc":
            "간결한 디자인과 여유로운 분위기가 특징인 도시로, "
            "화이트의 깨끗하고 미니멀한 이미지와 잘 어울립니다.",

        "look": "에포트리스 미니멀 룩",
        "clothes": [
            "화이트 셔츠",
            "베이지 팬츠",
            "심플 스니커즈",
            "블랙 미니백"
        ],

        "fashion_desc":
            "화이트를 기본으로 두고 베이지나 블랙처럼 대비가 크지 않은 색을 더하면 "
            "힘을 뺀 듯 자연스러운 미니멀 스타일이 완성됩니다.",

        "pair": "베이지 · 블랙 · 데님"
    }
}


# =========================================================
# 함수
# =========================================================
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")

    return tuple(
        int(hex_color[i:i + 2], 16)
        for i in (0, 2, 4)
    )


def color_distance(rgb1, rgb2):
    return math.sqrt(
        sum(
            (a - b) ** 2
            for a, b in zip(rgb1, rgb2)
        )
    )


def get_nearest_color(hex_color):
    user_rgb = hex_to_rgb(hex_color)

    nearest_color = None
    smallest_distance = float("inf")

    for color_name, color_data in color_styles.items():

        distance = color_distance(
            user_rgb,
            color_data["rgb"]
        )

        if distance < smallest_distance:
            smallest_distance = distance
            nearest_color = color_name

    return nearest_color


def get_text_color(hex_color):
    r, g, b = hex_to_rgb(hex_color)

    brightness = (
        r * 299 +
        g * 587 +
        b * 114
    ) / 1000

    if brightness > 165:
        return "#111111"

    return "#FFFFFF"


# =========================================================
# HERO
# =========================================================
html("""
<div class="hero">

    <div class="logo">
        TRIP TONE
    </div>

    <div class="hero-title">
        Pick a color.<br>
        Find your journey.
    </div>

    <div class="hero-sub">
        당신이 좋아하는 색 하나를 선택해 보세요.<br>
        색이 가진 분위기를 분석해 어울리는 여행지와
        여행 패션을 추천해 드립니다.
    </div>

</div>
""")


# =========================================================
# COLOR INPUT
# =========================================================
html("""
<div class="input-card">

    <div class="section-label">
        01 · YOUR COLOR
    </div>

    <div class="section-title">
        가장 좋아하는 색은 무엇인가요?
    </div>

    <div class="section-text">
        아래 컬러 피커에서 원하는 색을 자유롭게 선택해 주세요.
    </div>

</div>
""")


favorite_color = st.color_picker(
    "좋아하는 색 선택",
    "#5475D8",
    label_visibility="collapsed"
)


nearest_key = get_nearest_color(favorite_color)
color_info = color_styles[nearest_key]


html(f"""
<div class="color-preview"
     style="background:{favorite_color};">
</div>

<div class="color-meta">

    <span>
        {color_info["name"]} 계열
    </span>

    <span>
        {favorite_color.upper()}
    </span>

</div>
""")


st.write("")

recommend = st.button(
    "이 색으로 여행 스타일 찾기 →"
)


# =========================================================
# RESULT
# =========================================================
if recommend:

    color_info = color_styles[
        get_nearest_color(favorite_color)
    ]

    text_color = get_text_color(favorite_color)


    # -----------------------------------------------------
    # 결과 제목
    # -----------------------------------------------------
    html("""
    <div class="result-header">

        <div class="section-label">
            YOUR TRIP TONE
        </div>

        <div class="result-big-title">
            이 색이 안내하는 여행
        </div>

    </div>
    """)


    # -----------------------------------------------------
    # 메인 컬러 결과
    # -----------------------------------------------------
    html(f"""
    <div
        class="hero-result"
        style="
            background:{favorite_color};
            color:{text_color};
        "
    >

        <div class="hero-result-label">
            COLOR MOOD
        </div>

        <div class="hero-result-title">
            {color_info["name"]} ·
            {color_info["mood"]}
        </div>

        <div class="hero-result-text">
            당신이 선택한 색과 가장 가까운 색상 계열은
            <b>{color_info["name"]}</b>입니다.
            이 색의 분위기를 여행지와 패션에 연결해
            하나의 여행 스타일로 구성했습니다.
        </div>

    </div>
    """)


    st.write("")
    st.write("")


    # -----------------------------------------------------
    # 여행지 + 패션
    # -----------------------------------------------------
    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )


    with col1:

        html(f"""
        <div class="result-card">

            <div class="result-label">
                DESTINATION
            </div>

            <div class="result-title">
                {color_info["destination"]}
            </div>

            <div class="result-text">
                {color_info["destination_desc"]}
            </div>

        </div>
        """)


    with col2:

        clothes_html = ""

        for item in color_info["clothes"]:
            clothes_html += (
                f'<span class="chip">{item}</span>'
            )

        html(f"""
        <div class="result-card">

            <div class="result-label">
                FASHION
            </div>

            <div class="result-title">
                {color_info["look"]}
            </div>

            <div style="margin-bottom:18px;">
                {clothes_html}
            </div>

            <div class="result-text">
                {color_info["fashion_desc"]}
            </div>

        </div>
        """)


    # -----------------------------------------------------
    # 컬러 조합
    # -----------------------------------------------------
    st.write("")
    st.write("")

    html(f"""
    <div class="card">

        <div class="section-label">
            COLOR PALETTE
        </div>

        <div class="section-title">
            함께 입으면 좋은 색
        </div>

        <div class="section-text">
            선택한 <b>{color_info["name"]}</b>과
            <b>{color_info["pair"]}</b> 조합을 사용하면
            전체 코디를 보다 자연스럽게 정리할 수 있습니다.
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================
html("""
<div class="custom-footer">
    TRIP TONE · COLOR YOUR JOURNEY
</div>
""")
