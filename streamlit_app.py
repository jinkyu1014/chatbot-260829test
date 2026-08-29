import streamlit as st
from openai import OpenAI


# =========================================================
# 페이지 설정
# =========================================================

st.set_page_config(
    page_title="Promptly AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       전체 앱
    ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 50% -10%,
                rgba(124, 58, 237, 0.16),
                transparent 36%
            ),
            #09090b;

        color: #f4f4f5;
    }

    .block-container {
        max-width: 980px;

        padding-top: 25px;
        padding-bottom: 70px;
    }


    /* =====================================================
       기본 텍스트
    ===================================================== */

    p {
        color: #d4d4d8;
    }

    [data-testid="stCaptionContainer"] {
        color: #a1a1aa !important;
    }


    /* =====================================================
       Hero
    ===================================================== */

    .hero {
        text-align: center;

        padding:
            42px 0
            34px 0;
    }

    .hero-badge {
        display: inline-block;

        padding:
            7px 14px;

        border-radius: 999px;

        background:
            rgba(139, 92, 246, 0.12);

        border:
            1px solid
            rgba(139, 92, 246, 0.28);

        color: #c4b5fd;

        font-size: 11px;
        font-weight: 700;

        letter-spacing: 0.7px;
    }

    .hero-title {
        margin-top: 17px;

        font-size: 48px;
        line-height: 1.1;

        font-weight: 800;

        letter-spacing: -2.2px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #ddd6fe,
                #a78bfa
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        margin-top: 16px;

        color: #a1a1aa;

        font-size: 16px;

        line-height: 1.75;
    }


    /* =====================================================
       섹션 제목
    ===================================================== */

    .section-heading {
        color: #fafafa;

        font-size: 19px;
        font-weight: 750;

        margin-bottom: 5px;
    }

    .section-description {
        color: #a1a1aa;

        font-size: 13px;

        line-height: 1.65;

        margin-bottom: 14px;
    }


    /* =====================================================
       입력 카드
    ===================================================== */

    .input-card {
        background:
            rgba(24, 24, 27, 0.94);

        border:
            1px solid
            rgba(255, 255, 255, 0.08);

        border-radius: 18px;

        padding: 26px;

        margin-top: 8px;

        box-shadow:
            0 16px 45px
            rgba(0, 0, 0, 0.20);
    }


    /* =====================================================
       Text Area
    ===================================================== */

    textarea {
        background: #111113 !important;

        color: #f4f4f5 !important;

        border:
            1px solid
            #303034 !important;

        border-radius:
            12px !important;

        font-size:
            15px !important;

        line-height:
            1.75 !important;

        padding:
            16px !important;

        transition:
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    textarea::placeholder {
        color: #71717a !important;
    }

    textarea:hover {
        border-color:
            #52525b !important;
    }

    textarea:focus {
        border-color:
            #8b5cf6 !important;

        box-shadow:
            0 0 0 1px #8b5cf6,
            0 0 0 4px
            rgba(139, 92, 246, 0.10)
            !important;
    }


    /* =====================================================
       옵션 카드
    ===================================================== */

    .option-card {
        background:
            #111113;

        border:
            1px solid
            rgba(255, 255, 255, 0.07);

        border-radius:
            12px;

        padding:
            15px 16px;

        min-height:
            72px;

        box-sizing:
            border-box;
    }

    .option-label {
        color: #71717a;

        font-size: 12px;

        font-weight: 600;

        margin-bottom: 7px;
    }

    .option-value {
        color: #f4f4f5;

        font-size: 15px;

        font-weight: 700;
    }


    /* =====================================================
       Select Box
    ===================================================== */

    div[data-baseweb="select"] > div {
        background:
            #111113 !important;

        border:
            1px solid
            #303034 !important;

        border-radius:
            10px !important;

        min-height:
            42px;
    }

    div[data-baseweb="select"] > div:hover {
        border-color:
            #52525b !important;
    }


    /* =====================================================
       버튼
    ===================================================== */

    .stButton > button {
        width: 100%;

        min-height: 54px;

        border: none;

        border-radius: 12px;

        background:
            linear-gradient(
                135deg,
                #6d28d9,
                #7c3aed,
                #8b5cf6
            );

        color: white;

        font-size: 15px;

        font-weight: 750;

        box-shadow:
            0 8px 24px
            rgba(124, 58, 237, 0.20);

        transition:
            transform 0.15s ease,
            box-shadow 0.15s ease;
    }

    .stButton > button:hover {
        transform:
            translateY(-1px);

        box-shadow:
            0 12px 30px
            rgba(124, 58, 237, 0.32);
    }


    /* =====================================================
       결과 카드
    ===================================================== */

    .result-card {
        background:
            linear-gradient(
                180deg,
                rgba(30, 27, 45, 0.96),
                rgba(17, 17, 19, 0.96)
            );

        border:
            1px solid
            rgba(139, 92, 246, 0.28);

        border-radius:
            18px;

        padding:
            26px;

        margin-top:
            28px;

        box-shadow:
            0 18px 50px
            rgba(0, 0, 0, 0.24);
    }


    /* =====================================================
       결과 내부
    ===================================================== */

    .result-header {
        color: #fafafa;

        font-size: 19px;

        font-weight: 750;

        margin-bottom: 4px;
    }

    .result-description {
        color: #a1a1aa;

        font-size: 13px;

        line-height: 1.6;

        margin-bottom: 20px;
    }

    .result-content {
        color: #d4d4d8;

        font-size: 14px;

        line-height: 1.8;
    }

    .result-content h3 {
        color: #ddd6fe;

        font-size: 17px;

        margin-top: 25px;
        margin-bottom: 10px;
    }

    .result-content h4 {
        color: #c4b5fd;

        font-size: 15px;

        margin-top: 20px;
    }

    .result-content p {
        color: #d4d4d8;

        line-height: 1.8;
    }

    .result-content li {
        color: #d4d4d8;

        line-height: 1.7;

        margin-bottom: 5px;
    }

    .result-content code {
        background:
            rgba(139, 92, 246, 0.12);

        color: #ddd6fe;

        padding:
            2px 6px;

        border-radius:
            5px;
    }


    /* =====================================================
       예시
    ===================================================== */

    .example-box {
        background:
            #111113;

        border:
            1px solid
            rgba(255, 255, 255, 0.07);

        border-radius:
            10px;

        padding:
            13px 16px;

        margin-bottom:
            8px;

        color:
            #d4d4d8;

        font-size:
            13px;

        line-height:
            1.55;
    }

    .example-box:hover {
        background:
            #18181b;

        border-color:
            rgba(139, 92, 246, 0.25);
    }


    /* =====================================================
       TIP
    ===================================================== */

    .tip {
        margin-top:
            28px;

        padding:
            18px 20px;

        border-radius:
            12px;

        background:
            rgba(139, 92, 246, 0.08);

        border:
            1px solid
            rgba(139, 92, 246, 0.18);

        color:
            #c4b5fd;

        font-size:
            13px;

        line-height:
            1.75;
    }

    .tip strong {
        color:
            #ddd6fe;
    }


    /* =====================================================
       Sidebar
    ===================================================== */

    section[data-testid="stSidebar"] {
        background:
            #111113;

        border-right:
            1px solid
            rgba(255,255,255,0.06);
    }

    section[data-testid="stSidebar"] h2 {
        color:
            #fafafa;

        font-size:
            20px;
    }

    section[data-testid="stSidebar"] h3 {
        color:
            #e4e4e7;

        font-size:
            14px;
    }

    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        color:
            #8f8f98 !important;

        line-height:
            1.55;
    }


    /* =====================================================
       Alert
    ===================================================== */

    div[data-testid="stAlert"] {
        border-radius:
            10px;

        line-height:
            1.6;
    }


    /* =====================================================
       Footer
    ===================================================== */

    .footer {
        text-align:
            center;

        color:
            #52525b;

        font-size:
            12px;

        margin-top:
            50px;
    }


    /* =====================================================
       Streamlit 기본 UI
    ===================================================== */

    #MainMenu {
        visibility:
            hidden;
    }

    footer {
        visibility:
            hidden;
    }

    [data-testid="stToolbar"] {
        visibility:
            hidden;
    }


    /* =====================================================
       모바일
    ===================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left:
                18px;

            padding-right:
                18px;
        }

        .hero {
            padding:
                30px 0 25px;
        }

        .hero-title {
            font-size:
                38px;
        }

        .hero-description {
            font-size:
                14px;
        }

        .input-card,
        .result-card {
            padding:
                20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Header
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-badge">
            ✨ AI PROMPT ENGINEERING
        </div>

        <div class="hero-title">
            Promptly AI
        </div>

        <div class="hero-description">
            당신의 짧은 아이디어를<br>
            더 정확하고 강력한 AI 프롬프트로 만들어드립니다.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.markdown("## ⚙️ 설정")

    st.markdown("### 🔑 OpenAI API Key")

    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-...",
        label_visibility="collapsed"
    )

    st.caption(
        "API Key는 이 앱의 코드에 저장되지 않습니다."
    )

    st.divider()

    st.markdown("### ✨ 확장 설정")

    expansion_style = st.selectbox(
        "확장 스타일",
        [
            "자동",
            "간결하게",
            "상세하게",
            "전문적으로",
            "실행 중심"
        ],
        index=0
    )

    target_ai = st.selectbox(
        "사용할 AI",
        [
            "범용 AI",
            "ChatGPT",
            "Claude",
            "Gemini"
        ],
        index=0
    )

    output_language = st.selectbox(
        "프롬프트 언어",
        [
            "한국어",
            "English"
        ],
        index=0
    )


# =========================================================
# System Prompt
# =========================================================

SYSTEM_PROMPT = f"""
당신은 세계 최고 수준의 Prompt Engineer입니다.

사용자가 작성한 원본 프롬프트를 분석하고,
사용자의 원래 의도와 목적을 유지하면서
AI가 더 정확하고 높은 품질의 결과를 생성할 수 있도록
프롬프트를 확장하고 개선하세요.

현재 설정:

확장 스타일:
{expansion_style}

사용 대상 AI:
{target_ai}

출력 언어:
{output_language}


[핵심 원칙]

1. 사용자의 원래 의도를 절대 변경하지 마세요.

2. 사용자가 요청하지 않은 사실을
   임의로 만들어내지 마세요.

3. 단순한 요청에는 불필요하게
   복잡한 프롬프트를 만들지 마세요.

4. 복잡한 요청에는 필요한 정보를
   구조적으로 보완하세요.

5. 최종 프롬프트는 다른 AI에
   그대로 복사해서 사용할 수 있어야 합니다.


[프롬프트 구성]

요청의 성격에 따라 필요한 요소를 추가하세요.

- Role
- Context
- Goal
- Task
- Target Audience
- Input
- Process
- Output Format
- Constraints
- Requirements
- Evaluation Criteria
- Tone
- Style


[부족한 정보]

정보가 부족한 경우 사실을 만들어내지 마세요.

필요한 경우 placeholder를 사용하세요.

예:

[타겟 고객]
[예산]
[브랜드명]
[서비스 설명]
[목표]
[사용 가능한 데이터]
[원하는 결과물]

단, 불필요한 placeholder는 만들지 마세요.


[복잡한 작업]

복잡한 작업이라면 AI가 작업을
체계적으로 수행할 수 있도록
필요한 작업 절차를 정의하세요.

예:

1. 입력 정보 분석
2. 핵심 요구사항 파악
3. 필요한 정보 정리
4. 결과물 작성
5. 결과 검토
6. 개선사항 반영

모든 요청에 강제로 적용하지 말고
필요한 경우에만 사용하세요.


[결과물]

사용자가 원하는 결과물이 있다면
구체적인 출력 형식을 정의하세요.

예:

- 표
- 목록
- Markdown
- JSON
- 보고서
- 사업계획서
- 발표자료
- 코드
- 이메일
- 광고 카피


[출력 형식]

반드시 다음 형식으로 답변하세요.


### ✨ 확장된 프롬프트

사용자가 그대로 복사해서
다른 AI에 입력할 수 있는
완성된 프롬프트를 작성하세요.


### 🔍 개선된 부분

원본 프롬프트에서 무엇을 개선했는지
핵심적인 내용을 3~5개 설명하세요.


### 💡 사용 팁

이 프롬프트를 더 효과적으로 사용하기 위한
간단한 팁을 1~3개 작성하세요.


[중요]

실제 사용자의 작업 결과를 생성하지 마세요.

당신의 역할은 오직
사용자의 프롬프트를 개선하는 것입니다.

답변은 {output_language}로 작성하세요.
"""


# =========================================================
# API Key 확인
# =========================================================

if not openai_api_key:

    st.info(
        "🔑 왼쪽 사이드바에서 OpenAI API Key를 입력하면 "
        "프롬프트 확장 기능을 사용할 수 있습니다."
    )

    st.markdown(
        """
        <div class="tip">

        💡 <strong>사용 방법</strong><br><br>

        1. 왼쪽에서 API Key를 입력합니다.<br>
        2. 확장 스타일과 사용할 AI를 선택합니다.<br>
        3. 원하는 작업을 간단하게 입력합니다.<br>
        4. "프롬프트 확장하기"를 클릭합니다.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.stop()


# =========================================================
# OpenAI Client
# =========================================================

try:

    client = OpenAI(
        api_key=openai_api_key
    )

except Exception as e:

    st.error(
        "OpenAI Client를 초기화하지 못했습니다."
    )

    st.caption(
        f"오류 내용: {str(e)}"
    )

    st.stop()


# =========================================================
# 원본 프롬프트
# =========================================================

st.markdown(
    """
    <div class="input-card">

        <div class="section-heading">
            📝 원본 프롬프트
        </div>

        <div class="section-description">
            AI에게 원하는 작업을 자유롭게 작성해주세요.
            완벽하게 작성할 필요가 없습니다.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


user_prompt = st.text_area(
    "원본 프롬프트",
    height=210,
    placeholder="""예시:

유튜브 영상 아이디어 만들어줘

또는

우리 회사의 AI 서비스를 투자자에게
설명하는 PPT를 만들어줘

또는

20대 여성을 위한 화장품 브랜드
이름을 추천해줘""",
    label_visibility="collapsed",
    key="user_prompt"
)


# =========================================================
# 확장 옵션
# =========================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-heading">
        ⚙️ 확장 옵션
    </div>

    <div class="section-description">
        현재 선택된 설정입니다.
        실제 변경은 왼쪽 사이드바에서 할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="option-card">

            <div class="option-label">
                ✨ 확장 스타일
            </div>

            <div class="option-value">
                {expansion_style}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="option-card">

            <div class="option-label">
                🤖 사용 AI
            </div>

            <div class="option-value">
                {target_ai}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="option-card">

            <div class="option-label">
                🌐 프롬프트 언어
            </div>

            <div class="option-value">
                {output_language}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 실행 버튼
# =========================================================

st.markdown(
    "<br>",
    unsafe_allow_html=True
)

expand_button = st.button(
    "✨ 프롬프트 확장하기",
    use_container_width=True
)


# =========================================================
# API 호출
# =========================================================

if expand_button:

    # -----------------------------------------------------
    # 입력값 검사
    # -----------------------------------------------------

    if not user_prompt.strip():

        st.warning(
            "📝 먼저 확장하고 싶은 프롬프트를 입력해주세요."
        )

    else:

        # 이전 결과 제거
        if "result" in st.session_state:

            del st.session_state["result"]

        # -------------------------------------------------
        # API 호출
        # -------------------------------------------------

        with st.spinner(
            "✨ AI가 프롬프트를 분석하고 있습니다..."
        ):

            try:

                response = client.responses.create(
                    model="gpt-5.6-terra",
                    instructions=SYSTEM_PROMPT,
                    input=user_prompt.strip()
                )

                result = response.output_text

                # 응답 검사
                if not result or not result.strip():

                    st.error(
                        "AI가 빈 응답을 반환했습니다. "
                        "잠시 후 다시 시도해주세요."
                    )

                else:

                    st.session_state["result"] = result

                    # 화면 새로고침 없이 아래 결과 표시


            except Exception as e:

                st.error(
                    "❌ 프롬프트 생성 중 오류가 발생했습니다."
                )

                st.code(
                    str(e),
                    language="text"
                )


# =========================================================
# 결과
# =========================================================

if "result" in st.session_state:

    st.markdown(
        """
        <div class="result-card">

            <div class="result-header">
                ✨ 확장된 프롬프트
            </div>

            <div class="result-description">
                AI가 원본 프롬프트의 의도를 분석하고
                더 명확한 형태로 구조화했습니다.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state["result"]
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 사용 예시
# =========================================================

st.markdown(
    "<br><br>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section-heading">
        💡 이렇게 입력해보세요
    </div>

    <div class="section-description">
        완벽하게 작성할 필요가 없습니다.
        원하는 작업만 간단하게 적어주세요.
    </div>
    """,
    unsafe_allow_html=True
)


examples = [
    "유튜브 영상 아이디어 10개 만들어줘",
    "스타트업 투자용 PPT 만들어줘",
    "20대 여성을 위한 화장품 브랜드 이름 추천해줘",
    "이 논문을 초보자도 이해할 수 있게 설명해줘",
    "우리 서비스의 마케팅 전략을 만들어줘"
]


for example in examples:

    st.markdown(
        f"""
        <div class="example-box">
            {example}
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TIP
# =========================================================

st.markdown(
    """
    <div class="tip">

        💡 <strong>TIP</strong><br><br>

        프롬프트를 완벽하게 작성할 필요가 없습니다.<br>

        "무엇을 만들고 싶은지"만 작성하면
        Promptly AI가 목적, 역할, 조건,
        결과물 형식 등을 분석해서 보완합니다.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Footer
# =========================================================

st.markdown(
    """
    <div class="footer">
        Promptly AI · Turn simple ideas into powerful prompts.
    </div>
    """,
    unsafe_allow_html=True
)
