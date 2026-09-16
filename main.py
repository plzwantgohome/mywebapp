import streamlit as st


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
# 디자인
# =========================================================
st.markdown("""
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
            circle at 12% 15%,
            rgba(225, 231, 255, 0.75),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 12%,
            rgba(255, 230, 240, 0.65),
            transparent 28%
        ),
        #f8f8f6;
    color: #111111;
}

.block-container {
    max-width: 1050px;
    padding-top: 2.8rem;
    padding-bottom: 5rem;
}


/* 기본 Streamlit 요소 정리 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* 메인 제목 */
h1 {
    font-size: clamp(48px, 7vw, 78px) !important;
    line-height: 0.98 !important;
    letter-spacing: -0.055em !important;
    font-weight: 750 !important;
    color: #111111 !important;
    margin-bottom: 1.4rem !important;
}

h2 {
    letter-spacing: -0.035em !important;
    font-weight: 720 !important;
}

h3 {
    letter-spacing: -0.025em !important;
}


/* 카드 */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.86);
    border: 1px solid rgba(0, 0, 0, 0.055);
    border-radius: 26px;
    box-shadow: 0 18px 55px rgba(0, 0, 0, 0.055);
    padding: 10px;
}


/* 캡션 */
.stCaption {
    color: #999999 !important;
    font-size: 11px !important;
    letter-spacing: 0.15em !important;
    font-weight: 700 !important;
    text-transform: uppercase;
}


/* 일반 문장 */
div[data-testid="stMarkdownContainer"] p {
    line-height: 1.75;
}


/* 버튼 */
.stButton > button {
    width: 100%;
    height: 56px;
    border-radius: 999px;
    border: none;
    background: #111111;
    color: #ffffff;
    font-size: 15px;
    font-weight: 650;
    transition: 0.18s ease;
    box-shadow: none;
}

.stButton > button:hover {
    background: #303030;
    color: #ffffff;
    border: none;
    transform: translateY(-1px);
}


/* 컬러피커 */
div[data-testid="stColorPicker"] {
    margin-top: 8px;
}


/* 구분선 */
hr {
    margin-top: 55px !important;
    margin-bottom: 45px !important;
    border-color: rgba(0, 0, 0, 0.07) !important;
}


/* 결과 카드 내부 여백 */
div[data-testid="stVerticalBlockBorderWrapper"]
div[data-testid="stVerticalBlock"] {
    gap: 0.65rem;
}


/* 화면이 좁을 때 */
@media (max-width: 700px) {

    .block-container {
        padding-left: 1.2rem;
        padding-right: 1.2rem;
    }

    h1 {
        font-size: 48px !important;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 색상별 추천 데이터
# =========================================================
color_data = {

    "RED": {
        "rgb": (220, 60, 60),
        "name": "레드",
        "mood": "Bold & Energetic",
        "mood_kr": "강렬하고 자신감 있는 분위기",

        "destination": "바르셀로나 🇪🇸",
        "destination_reason":
            "화려한 색채와 활기찬 거리 분위기가 "
            "레드의 강한 에너지와 자연스럽게 어울립니다.",

        "style": "Bold City Look",
        "fashion": [
            "레드 포인트 상의",
            "블랙 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],

        "fashion_reason":
            "레드를 전체에 사용하기보다 상의나 가방처럼 "
            "한 부분에 포인트로 사용하면 강렬하면서도 "
            "세련된 여행 스타일을 만들 수 있습니다.",

        "pair": "블랙 · 화이트 · 차콜"
    },


    "ORANGE": {
        "rgb": (235, 140, 55),
        "name": "오렌지",
        "mood": "Warm & Vibrant",
        "mood_kr": "따뜻하고 생동감 있는 분위기",

        "destination": "로마 🇮🇹",
        "destination_reason":
            "따뜻한 햇빛과 고전적인 건축물이 "
            "오렌지의 따뜻하고 활기찬 이미지와 잘 어울립니다.",

        "style": "Warm Classic Look",
        "fashion": [
            "오렌지 니트",
            "크림 팬츠",
            "브라운 로퍼",
            "가죽 숄더백"
        ],

        "fashion_reason":
            "오렌지를 크림이나 브라운처럼 따뜻한 중성색과 "
            "함께 사용하면 자연스럽고 고급스러운 분위기가 납니다.",

        "pair": "크림 · 브라운 · 베이지"
    },


    "YELLOW": {
        "rgb": (235, 200, 60),
        "name": "옐로",
        "mood": "Bright & Playful",
        "mood_kr": "밝고 경쾌한 분위기",

        "destination": "제주 🇰🇷",
        "destination_reason":
            "밝고 자연스러운 제주의 풍경이 "
            "옐로의 산뜻하고 가벼운 분위기와 잘 어울립니다.",

        "style": "Light Casual Look",
        "fashion": [
            "옐로 가디건",
            "화이트 티셔츠",
            "연청 데님",
            "캔버스백"
        ],

        "fashion_reason":
            "옐로를 화이트와 데님에 조합하면 "
            "여행지에서 편하게 입기 좋은 밝고 산뜻한 코디가 완성됩니다.",

        "pair": "화이트 · 데님 · 라이트 그레이"
    },


    "GREEN": {
        "rgb": (70, 145, 90),
        "name": "그린",
        "mood": "Natural & Calm",
        "mood_kr": "차분하고 자연스러운 분위기",

        "destination": "코펜하겐 🇩🇰",
        "destination_reason":
            "자연과 도시가 조화를 이루는 북유럽의 분위기가 "
            "그린의 안정적이고 자연스러운 이미지와 잘 어울립니다.",

        "style": "Natural Minimal Look",
        "fashion": [
            "그린 셔츠",
            "베이지 팬츠",
            "화이트 스니커즈",
            "브라운 토트백"
        ],

        "fashion_reason":
            "그린은 베이지와 브라운 같은 자연 계열 색상과 "
            "함께 사용하면 차분하면서도 감각적인 스타일이 됩니다.",

        "pair": "베이지 · 브라운 · 아이보리"
    },


    "BLUE": {
        "rgb": (60, 105, 205),
        "name": "블루",
        "mood": "Clean & Cool",
        "mood_kr": "깔끔하고 시원한 분위기",

        "destination": "도쿄 🇯🇵",
        "destination_reason":
            "정돈된 도시 이미지와 현대적인 분위기가 "
            "블루의 차분하고 시원한 이미지와 잘 맞습니다.",

        "style": "Clean Minimal Look",
        "fashion": [
            "블루 셔츠",
            "그레이 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],

        "fashion_reason":
            "블루를 화이트와 그레이 같은 무채색과 함께 사용하면 "
            "깔끔하고 도시적인 느낌을 강조할 수 있습니다.",

        "pair": "화이트 · 그레이 · 네이비"
    },


    "PURPLE": {
        "rgb": (135, 80, 185),
        "name": "퍼플",
        "mood": "Artistic & Unique",
        "mood_kr": "독특하고 예술적인 분위기",

        "destination": "파리 🇫🇷",
        "destination_reason":
            "예술과 패션의 분위기가 강한 파리가 "
            "퍼플의 개성 있고 예술적인 이미지와 잘 어울립니다.",

        "style": "Artistic Chic Look",
        "fashion": [
            "퍼플 니트",
            "차콜 슬랙스",
            "블랙 로퍼",
            "미니 숄더백"
        ],

        "fashion_reason":
            "퍼플에 차콜이나 블랙을 함께 사용하면 "
            "색의 개성은 유지하면서 전체 스타일은 차분하게 정리할 수 있습니다.",

        "pair": "차콜 · 블랙 · 라이트 그레이"
    },


    "PINK": {
        "rgb": (225, 115, 155),
        "name": "핑크",
        "mood": "Soft & Modern",
        "mood_kr": "부드럽고 세련된 분위기",

        "destination": "파리 🇫🇷",
        "destination_reason":
            "클래식하면서 세련된 파리의 거리 분위기가 "
            "핑크의 부드러운 이미지와 잘 어울립니다.",

        "style": "Soft Modern Look",
        "fashion": [
            "핑크 가디건",
            "그레이 팬츠",
            "화이트 스니커즈",
            "미니백"
        ],

        "fashion_reason":
            "핑크를 그레이처럼 차분한 색과 조합하면 "
            "지나치게 화려하지 않으면서 부드럽고 현대적인 스타일이 됩니다.",

        "pair": "그레이 · 화이트 · 버건디"
    },


    "BROWN": {
        "rgb": (125, 85, 55),
        "name": "브라운",
        "mood": "Classic & Earthy",
        "mood_kr": "차분하고 클래식한 분위기",

        "destination": "런던 🇬🇧",
        "destination_reason":
            "고전적인 건축과 차분한 거리 풍경이 "
            "브라운의 안정적이고 클래식한 이미지와 잘 맞습니다.",

        "style": "Classic Layered Look",
        "fashion": [
            "브라운 재킷",
            "아이보리 니트",
            "진청 데님",
            "로퍼"
        ],

        "fashion_reason":
            "브라운은 아이보리나 크림 계열과 함께 사용하면 "
            "무겁지 않으면서 따뜻하고 클래식한 분위기를 만들 수 있습니다.",

        "pair": "아이보리 · 크림 · 네이비"
    },


    "BLACK": {
        "rgb": (30, 30, 30),
        "name": "블랙",
        "mood": "Chic & Minimal",
        "mood_kr": "시크하고 도시적인 분위기",

        "destination": "뉴욕 🇺🇸",
        "destination_reason":
            "빠르고 현대적인 뉴욕의 분위기가 "
            "블랙의 강렬하고 도시적인 이미지와 잘 어울립니다.",

        "style": "Chic City Look",
        "fashion": [
            "블랙 재킷",
            "차콜 팬츠",
            "화이트 이너",
            "실버 액세서리"
        ],

        "fashion_reason":
            "블랙을 중심으로 실루엣을 단순하게 잡고 "
            "화이트나 실버를 소량 사용하면 세련된 도시 스타일이 완성됩니다.",

        "pair": "화이트 · 차콜 · 실버"
    },


    "WHITE": {
        "rgb": (240, 240, 235),
        "name": "화이트",
        "mood": "Clean & Effortless",
        "mood_kr": "깨끗하고 미니멀한 분위기",

        "destination": "코펜하겐 🇩🇰",
        "destination_reason":
            "간결한 디자인과 여유로운 분위기가 특징인 도시로 "
            "화이트의 깨끗하고 미니멀한 이미지와 잘 어울립니다.",

        "style": "Effortless Minimal Look",
        "fashion": [
            "화이트 셔츠",
            "베이지 팬츠",
            "심플 스니커즈",
            "블랙 미니백"
        ],

        "fashion_reason":
            "화이트를 기본으로 두고 베이지나 블랙을 더하면 "
            "힘을 뺀 듯 자연스러운 미니멀 스타일이 완성됩니다.",

        "pair": "베이지 · 블랙 · 데님"
    }
}


# =========================================================
# 색상 계산
# =========================================================
def hex_to_rgb(hex_color):
    hex_color = hex_color.replace("#", "")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    return r, g, b


def color_distance(color1, color2):

    r1, g1, b1 = color1
    r2, g2, b2 = color2

    return (
        (r1 - r2) ** 2
        + (g1 - g2) ** 2
        + (b1 - b2) ** 2
    )


def find_nearest_color(hex_color):

    selected_rgb = hex_to_rgb(hex_color)

    nearest_name = None
    nearest_distance = None

    for name in color_data:

        distance = color_distance(
            selected_rgb,
            color_data[name]["rgb"]
        )

        if nearest_distance is None or distance < nearest_distance:

            nearest_distance = distance
            nearest_name = name

    return nearest_name


# =========================================================
# HERO
# =========================================================

st.caption("TRIP TONE")

st.title(
    "Find your\ntravel color."
)

st.markdown(
    """
좋아하는 색 하나에서 시작하는 여행 스타일.  
당신이 선택한 색의 분위기를 분석해  
**어울리는 여행지와 패션을 추천합니다.**
"""
)

st.write("")
st.write("")


# =========================================================
# 색 선택
# =========================================================

with st.container(border=True):

    st.caption("01 · COLOR")

    st.header(
        "당신이 좋아하는 색은?"
    )

    st.write(
        "가장 마음에 드는 색을 자유롭게 선택해 주세요."
    )

    selected_color = st.color_picker(
        "좋아하는 색 선택",
        "#5475D8",
        label_visibility="collapsed"
    )

    nearest_color = find_nearest_color(
        selected_color
    )

    preview = color_data[
        nearest_color
    ]

    # 색상 미리보기
    st.markdown(
        f'<div style="width:100%;height:145px;background:{selected_color};border-radius:22px;margin-top:12px;margin-bottom:14px;border:1px solid rgba(0,0,0,0.05);"></div>',
        unsafe_allow_html=True
    )

    info1, info2 = st.columns(2)

    with info1:
        st.caption("COLOR FAMILY")
        st.write(
            f"**{preview['name']} 계열**"
        )

    with info2:
        st.caption("HEX")
        st.write(
            f"`{selected_color.upper()}`"
        )


st.write("")

show_result = st.button(
    "나만의 여행 스타일 보기 →"
)


# =========================================================
# 결과
# =========================================================

if show_result:

    result_key = find_nearest_color(
        selected_color
    )

    result = color_data[
        result_key
    ]

    st.divider()

    st.caption("YOUR STYLE")

    st.header(
        "여행 스타일 추천"
    )

    st.write(
        f"선택한 색은 **{result['name']} 계열**과 가장 가깝습니다. "
        f"{result['mood_kr']}을 바탕으로 여행지와 패션을 골랐어요."
    )

    st.write("")
    st.write("")


    # -----------------------------------------------------
    # 첫 번째 줄
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(
        3,
        gap="large"
    )


    # COLOR MOOD
    with col1:

        with st.container(border=True):

            st.caption(
                "COLOR MOOD"
            )

            st.markdown(
                f'<div style="width:100%;height:120px;background:{selected_color};border-radius:18px;margin-bottom:16px;border:1px solid rgba(0,0,0,0.05);"></div>',
                unsafe_allow_html=True
            )

            st.subheader(
                result["mood"]
            )

            st.write(
                result["mood_kr"]
            )


    # DESTINATION
    with col2:

        with st.container(border=True):

            st.caption(
                "DESTINATION"
            )

            st.subheader(
                result["destination"]
            )

            st.write(
                result["destination_reason"]
            )


    # FASHION
    with col3:

        with st.container(border=True):

            st.caption(
                "KEY ITEMS"
            )

            st.subheader(
                "Pack these."
            )

            for item in result["fashion"]:

                st.markdown(
                    f"`{item}`"
                )


    # -----------------------------------------------------
    # Outfit formula
    # -----------------------------------------------------

    st.write("")
    st.write("")

    st.caption(
        "OUTFIT FORMULA"
    )

    st.header(
        "이렇게 입어보세요"
    )

    st.write("")

    look1, look2 = st.columns(
        [1.35, 1],
        gap="large"
    )


    with look1:

        with st.container(border=True):

            st.caption(
                "MAIN LOOK"
            )

            st.subheader(
                result["style"]
            )

            st.write(
                result["fashion_reason"]
            )

            st.write("")

            st.write(
                f"**추천 조합**  \n"
                f"{result['fashion'][0]} + "
                f"{result['fashion'][1]}"
            )


    with look2:

        with st.container(border=True):

            st.caption(
                "COLOR PAIRING"
            )

            st.subheader(
                result["pair"]
            )

            st.write(
                f"**{result['name']}**을 포인트 컬러로 두고 "
                "이 색들을 기본색으로 함께 사용하면 "
                "전체 코디를 자연스럽게 정리할 수 있습니다."
            )


    # -----------------------------------------------------
    # 마지막 요약
    # -----------------------------------------------------

    st.write("")
    st.write("")

    with st.container(border=True):

        st.caption(
            "YOUR TRIP TONE"
        )

        st.header(
            f"{result['destination']} × {result['name']}"
        )

        st.write(
            f"**{result['mood_kr']}**을 중심으로 한 여행 스타일입니다. "
            f"{result['destination']}의 분위기에 "
            f"{result['name']}을 포인트 컬러로 활용하고, "
            f"{result['pair']} 계열을 함께 매치해 보세요."
        )


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")
st.write("")

st.caption(
    "TRIP TONE · COLOR YOUR JOURNEY"
)
