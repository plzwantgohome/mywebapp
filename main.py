import streamlit as st


# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="Trip Tone",
    page_icon="✈️",
    layout="wide"
)


# =========================
# 디자인
# =========================
st.markdown(
    """
<style>
.stApp {
    background: linear-gradient(135deg, #f8f9fc 0%, #f6f3f7 100%);
}

.block-container {
    max-width: 1050px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}

h1 {
    letter-spacing: -2px;
}

h2, h3 {
    letter-spacing: -1px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: rgba(255,255,255,0.82);
    border-radius: 22px;
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 12px 35px rgba(0,0,0,0.05);
}

.stButton > button {
    width: 100%;
    border-radius: 999px;
    height: 52px;
    background-color: #111111;
    color: white;
    border: none;
    font-weight: 600;
    font-size: 16px;
}

.stButton > button:hover {
    background-color: #333333;
    color: white;
    border: none;
}

div[data-testid="stColorPicker"] {
    margin-top: 15px;
}

hr {
    margin-top: 40px;
    margin-bottom: 40px;
}
</style>
""",
    unsafe_allow_html=True
)


# =========================
# 색상 추천 데이터
# =========================
color_data = {
    "RED": {
        "rgb": (220, 60, 60),
        "name": "레드",
        "mood": "강렬하고 자신감 있는 분위기",
        "destination": "바르셀로나 🇪🇸",
        "destination_reason":
            "화려한 색채와 활기찬 거리 분위기가 레드의 에너지와 잘 어울립니다.",
        "style": "Bold City Look",
        "fashion": [
            "레드 포인트 상의",
            "블랙 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],
        "pair": "블랙 · 화이트 · 차콜"
    },

    "ORANGE": {
        "rgb": (235, 140, 55),
        "name": "오렌지",
        "mood": "따뜻하고 생동감 있는 분위기",
        "destination": "로마 🇮🇹",
        "destination_reason":
            "따뜻한 햇빛과 고전적인 건축물이 오렌지의 따뜻한 이미지와 잘 어울립니다.",
        "style": "Warm Classic Look",
        "fashion": [
            "오렌지 니트",
            "크림 팬츠",
            "브라운 로퍼",
            "가죽 숄더백"
        ],
        "pair": "크림 · 브라운 · 베이지"
    },

    "YELLOW": {
        "rgb": (235, 200, 60),
        "name": "옐로",
        "mood": "밝고 경쾌한 분위기",
        "destination": "제주 🇰🇷",
        "destination_reason":
            "밝고 자연스러운 제주의 풍경이 옐로의 산뜻한 분위기와 잘 어울립니다.",
        "style": "Light Casual Look",
        "fashion": [
            "옐로 가디건",
            "화이트 티셔츠",
            "연청 데님",
            "캔버스백"
        ],
        "pair": "화이트 · 데님 · 라이트 그레이"
    },

    "GREEN": {
        "rgb": (70, 145, 90),
        "name": "그린",
        "mood": "차분하고 자연스러운 분위기",
        "destination": "코펜하겐 🇩🇰",
        "destination_reason":
            "자연과 도시가 조화를 이루는 북유럽 분위기가 그린과 잘 어울립니다.",
        "style": "Natural Minimal Look",
        "fashion": [
            "그린 셔츠",
            "베이지 팬츠",
            "화이트 스니커즈",
            "브라운 토트백"
        ],
        "pair": "베이지 · 브라운 · 아이보리"
    },

    "BLUE": {
        "rgb": (60, 105, 205),
        "name": "블루",
        "mood": "깔끔하고 시원한 분위기",
        "destination": "도쿄 🇯🇵",
        "destination_reason":
            "정돈된 도시 이미지와 현대적인 분위기가 블루의 차분함과 잘 맞습니다.",
        "style": "Clean Minimal Look",
        "fashion": [
            "블루 셔츠",
            "그레이 와이드 팬츠",
            "화이트 스니커즈",
            "실버 액세서리"
        ],
        "pair": "화이트 · 그레이 · 네이비"
    },

    "PURPLE": {
        "rgb": (135, 80, 185),
        "name": "퍼플",
        "mood": "독특하고 예술적인 분위기",
        "destination": "파리 🇫🇷",
        "destination_reason":
            "예술과 패션의 도시인 파리가 퍼플의 개성 있는 분위기와 잘 어울립니다.",
        "style": "Artistic Chic Look",
        "fashion": [
            "퍼플 니트",
            "차콜 슬랙스",
            "블랙 로퍼",
            "미니 숄더백"
        ],
        "pair": "차콜 · 블랙 · 라이트 그레이"
    },

    "PINK": {
        "rgb": (225, 115, 155),
        "name": "핑크",
        "mood": "부드럽고 세련된 분위기",
        "destination": "파리 🇫🇷",
        "destination_reason":
            "클래식하면서 세련된 파리의 분위기가 핑크와 자연스럽게 어울립니다.",
        "style": "Soft Modern Look",
        "fashion": [
            "핑크 가디건",
            "그레이 팬츠",
            "화이트 스니커즈",
            "미니백"
        ],
        "pair": "그레이 · 화이트 · 버건디"
    },

    "BROWN": {
        "rgb": (125, 85, 55),
        "name": "브라운",
        "mood": "차분하고 클래식한 분위기",
        "destination": "런던 🇬🇧",
        "destination_reason":
            "고전적인 건축과 차분한 거리 풍경이 브라운의 클래식한 이미지와 잘 맞습니다.",
        "style": "Classic Layered Look",
        "fashion": [
            "브라운 재킷",
            "아이보리 니트",
            "진청 데님",
            "로퍼"
        ],
        "pair": "아이보리 · 크림 · 네이비"
    },

    "BLACK": {
        "rgb": (30, 30, 30),
        "name": "블랙",
        "mood": "시크하고 도시적인 분위기",
        "destination": "뉴욕 🇺🇸",
        "destination_reason":
            "빠르고 현대적인 뉴욕의 분위기가 블랙의 강렬한 도시 이미지와 잘 어울립니다.",
        "style": "Chic City Look",
        "fashion": [
            "블랙 재킷",
            "차콜 팬츠",
            "화이트 이너",
            "실버 액세서리"
        ],
        "pair": "화이트 · 차콜 · 실버"
    },

    "WHITE": {
        "rgb": (240, 240, 235),
        "name": "화이트",
        "mood": "깨끗하고 미니멀한 분위기",
        "destination": "코펜하겐 🇩🇰",
        "destination_reason":
            "간결한 북유럽 디자인과 여유로운 분위기가 화이트의 미니멀한 느낌과 잘 어울립니다.",
        "style": "Effortless Minimal Look",
        "fashion": [
            "화이트 셔츠",
            "베이지 팬츠",
            "심플 스니커즈",
            "블랙 미니백"
        ],
        "pair": "베이지 · 블랙 · 데님"
    }
}


# =========================
# 색상 계산 함수
# =========================
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

        standard_rgb = color_data[name]["rgb"]

        distance = color_distance(
            selected_rgb,
            standard_rgb
        )

        if nearest_distance is None or distance < nearest_distance:
            nearest_distance = distance
            nearest_name = name

    return nearest_name


# =========================
# 상단
# =========================
st.caption("TRIP TONE")

st.title("Pick a color,\nfind your journey.")

st.write(
    "좋아하는 색 하나를 선택하면 "
    "그 색의 분위기에 어울리는 여행지와 패션을 추천해 드립니다."
)

st.write("")


# =========================
# 색 선택
# =========================
with st.container(border=True):

    st.subheader("당신이 좋아하는 색은?")

    st.caption(
        "아래에서 가장 마음에 드는 색을 자유롭게 선택해 주세요."
    )

    selected_color = st.color_picker(
        "색 선택",
        "#5475D8"
    )

    nearest_color = find_nearest_color(
        selected_color
    )

    preview_data = color_data[
        nearest_color
    ]

    # 한 줄짜리 HTML만 사용
    # 코드로 표시되는 문제를 피하기 위함
    st.markdown(
        f'<div style="height:110px;'
        f'background:{selected_color};'
        f'border-radius:18px;'
        f'margin-top:10px;'
        f'margin-bottom:12px;"></div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.caption(
            f"가장 가까운 색상 계열 · "
            f"{preview_data['name']}"
        )

    with col2:
        st.caption(
            f"선택한 색상 · "
            f"{selected_color.upper()}"
        )


st.write("")

show_result = st.button(
    "이 색으로 여행 스타일 찾기"
)


# =========================
# 결과
# =========================
if show_result:

    result_key = find_nearest_color(
        selected_color
    )

    result = color_data[
        result_key
    ]

    st.divider()

    st.caption("YOUR TRIP TONE")

    st.header(
        f"{result['name']}이 안내하는 여행"
    )

    st.write(
        f"선택한 색은 **{result['name']} 계열**과 가장 가깝습니다. "
        f"{result['mood']}을 중심으로 여행지와 패션을 추천했어요."
    )

    st.write("")

    col1, col2 = st.columns(2)

    # 여행지
    with col1:

        with st.container(border=True):

            st.caption("DESTINATION")

            st.subheader(
                result["destination"]
            )

            st.write(
                result["destination_reason"]
            )


    # 패션
    with col2:

        with st.container(border=True):

            st.caption("FASHION")

            st.subheader(
                result["style"]
            )

            for item in result["fashion"]:
                st.write(
                    f"• {item}"
                )


    st.write("")

    # 컬러 조합
    with st.container(border=True):

        st.caption("COLOR PALETTE")

        st.subheader(
            "함께 입으면 좋은 색"
        )

        st.write(
            result["pair"]
        )

        st.write(
            f"**{result['name']}**을 포인트 색으로 사용하고 "
            "나머지 색을 기본색으로 조합하면 "
            "전체 코디가 더 자연스럽게 정리됩니다."
        )


st.write("")
st.write("")
st.caption(
    "TRIP TONE · COLOR YOUR JOURNEY"
)
