import streamlit as st
from openai import OpenAI
import textwrap


# ==================================================
# 페이지 설정
# ==================================================

st.set_page_config(
    page_title="Promptly AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CSS
# ==================================================

st.markdown(
    textwrap.dedent("""
    <style>

    /* =========================================
       전체 화면
    ========================================= */

    .stApp {
        background:
            radial-gradient(
                circle at 50% -15%,
                rgba(124, 58, 237, 0.20),
                transparent 38%
            ),
            #09090b;

        color: #f4f4f5;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 35px;
        padding-bottom: 80px;
    }


    /* =========================================
       헤더
    ========================================= */

    .hero {
        text-align: center;
        padding: 30px 0 25px 0;
    }

    .hero-badge {
        display: inline-block;

        padding: 7px 14px;

        border-radius: 30px;

        background: rgba(139, 92, 246, 0.12);

        border: 1px solid rgba(139, 92, 246, 0.25);

        color: #c4b5fd;

        font-size: 11px;

        font-weight: 700;

        letter-spacing: 0.5px;

        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 48px;

        font-weight: 800;

        letter-spacing: -2.5px;

        line-height: 1.1;

        background: linear-gradient(
            90deg,
            #ffffff 20%,
            #c4b5fd 80%
        );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        color: #a1a1aa;

        font-size: 16px;

        line-height: 1.7;

        margin-top: 15px;
    }


    /* =========================================
       카드
    ========================================= */

    .card {
        background: rgba(24, 24, 27, 0.82);

        border: 1px solid rgba(255, 255, 255, 0.07);

        border-radius: 20px;

        padding: 25px;

        margin-top: 20px;

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.22);

        backdrop-filter: blur(20px);
    }

    .card-title {
        font-size: 18px;

        font-weight: 700;

        color: #fafafa;
    }

    .card-description {
        color: #71717a;

        font-size: 13px;

        margin-top: 5px;

        margin-bottom: 18px;

        line-height: 1.6;
    }


    /* =========================================
       Text Area
    ========================================= */

    textarea {
        background: #111113 !important;

        color: #f4f4f5 !important;

        border: 1px solid #27272a !important;

        border-radius: 14px !important;

        font-size: 15px !important;

        line-height: 1.7 !important;

        padding: 15px !important;
    }

    textarea:focus {
        border-color: #8b5cf6 !important;

        box-shadow:
            0 0 0 1px #8b5cf6 !important;
    }


    /* =========================================
       Select Box
    ========================================= */

    div[data-baseweb="select"] > div {
        background: #111113;

        border-color: #27272a;

        border-radius: 10px;
    }


    /* =========================================
       메인 버튼
    ========================================= */

    .stButton > button {
        width: 100%;

        height: 52px;

        border: none;

        border-radius: 13px;

        background: linear-gradient(
            135deg,
            #7c3aed,
            #8b5cf6
        );

        color: white;

        font-size: 15px;

        font-weight: 700;

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 12px 30px rgba(124, 58, 237, 0.30);
    }


    /* =========================================
       결과 카드
    ========================================= */

    .result-card {
        background: rgba(17, 17, 19, 0.92);

        border:
            1px solid rgba(139, 92, 246, 0.22);

        border-radius: 18px;

        padding: 24px;

        margin-top: 25px;

        box-shadow:
            0 15px 45px rgba(0, 0, 0, 0.20);
    }

    .result-title {
        font-size: 20px;

        font-weight: 700;

        color: #fafafa;

        margin-bottom: 5px;
    }

    .result-subtitle {
        color: #71717a;

        font-size: 13px;

        line-height: 1.6;

        margin-bottom: 18px;
    }

    .result-badge {
        display: inline-block;

        padding: 4px 9px;

        margin-left: 7px;

        border-radius: 20px;

        background: rgba(139, 92, 246, 0.14);

        color: #c4b5fd;

        font-size: 10px;

        font-weight: 700;

        vertical-align: middle;
    }


    /* =========================================
       예시
    ========================================= */

    .example {
        background: rgba(255, 255, 255, 0.025);

        border:
            1px solid rgba(255, 255, 255, 0.05);

        border-radius: 11px;

        padding: 13px 15px;

        margin-top: 8px;

        color: #d4d4d8;

        font-size: 13px;

        line-height: 1.5;
    }


    /* =========================================
       Tip
    ========================================= */

    .tip {
        background: rgba(255, 255, 255, 0.025);

        border:
            1px solid rgba(255, 255, 255, 0.06);

        border-radius: 13px;

        padding: 15px 17px;

        margin-top: 18px;

        color: #a1a1aa;

        font-size: 13px;

        line-height: 1.7;
    }


    /* =========================================
       Footer
    ========================================= */

    .footer {
        text-align: center;

        color: #52525b;

        font-size: 12px;

        margin-top: 55px;
    }


    /* =========================================
       Streamlit 기본 UI
    ========================================= */

    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Header
# ==================================================

st.markdown(
    textwrap.dedent("""
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
    """),
    unsafe_allow_html=True
)


# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.markdown("## ⚙️ 설정")

    st.markdown("### 🔑 OpenAI API Key")

    openai_api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="sk-...",
        label_visibility="collapsed"
    )

    st.caption(
        "API Key는 코드에 저장되지 않습니다."
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
        ]
    )

    target_ai = st.selectbox(
        "사용할 AI",
        [
            "범용 AI",
            "ChatGPT",
            "Claude",
            "Gemini"
        ]
    )

    output_language = st.selectbox(
        "프롬프트 언어",
        [
            "한국어",
            "English"
        ]
    )


# ==================================================
# API Key 확인
# ==================================================

if not openai_api_key:

    st.info(
        "왼쪽 사이드바에서 OpenAI API Key를 입력해주세요. 🔑"
    )

    st.stop()


client = OpenAI(
    api_key=openai_api_key
)


# ==================================================
# Prompt Input
# ==================================================

st.markdown(
    textwrap.dedent("""
    <div class="card">

        <div class="card-title">
            📝 원본 프롬프트
        </div>

        <div class="card-description">
            AI에게 원하는 작업을 자유롭게 작성해주세요.
            완벽하게 작성할 필요가 없습니다.
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


user_prompt = st.text_area(
    "prompt",
    height=200,
    placeholder="""예시:

유튜브 영상 아이디어 만들어줘

또는

우리 회사의 AI 서비스를 투자자에게
설명하는 PPT를 만들어줘

또는

20대 여성을 위한 화장품 브랜드 이름 추천해줘""",
    label_visibility="collapsed"
)


# ==================================================
# 설정 표시
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.caption("✨ 확장 스타일")

    st.write(
        expansion_style
    )


with col2:

    st.caption("🤖 사용 AI")

    st.write(
        target_ai
    )


with col3:

    st.caption("🌐 출력 언어")

    st.write(
        output_language
    )


# ==================================================
# System Prompt
# ==================================================

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


━━━━━━━━━━━━━━━━━━━━━━
1. 핵심 원칙
━━━━━━━━━━━━━━━━━━━━━━

- 사용자의 원래 의도를 절대 변경하지 마세요.
- 사용자가 요청하지 않은 사실을 임의로 만들어내지 마세요.
- 단순한 요청에는 불필요하게 복잡한 프롬프트를 만들지 마세요.
- 복잡한 요청에는 필요한 정보를 적극적으로 구조화하세요.
- 최종 프롬프트는 다른 AI에 그대로 복사해서 사용할 수 있어야 합니다.


━━━━━━━━━━━━━━━━━━━━━━
2. 프롬프트 분석
━━━━━━━━━━━━━━━━━━━━━━

사용자의 원본 프롬프트를 먼저 분석하고
다음 요소 중 필요한 항목을 보완하세요.

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


━━━━━━━━━━━━━━━━━━━━━━
3. 부족한 정보
━━━━━━━━━━━━━━━━━━━━━━

정보가 부족한 경우 사실을 임의로 만들어내지 마세요.

필요한 정보는 다음과 같은 placeholder를 사용하세요.

[타겟 고객]
[예산]
[브랜드명]
[서비스 설명]
[목표]
[사용 가능한 데이터]
[원하는 결과물]

단, placeholder가 너무 많이 생기지 않도록
실제로 결과물 생성에 필요한 정보만 추가하세요.


━━━━━━━━━━━━━━━━━━━━━━
4. 작업 과정
━━━━━━━━━━━━━━━━━━━━━━

복잡한 작업이라면 AI가 다음과 같은 방식으로
체계적으로 작업하도록 지시하세요.

1. 입력 정보 분석
2. 핵심 요구사항 파악
3. 필요한 정보 정리
4. 결과물 작성
5. 결과 검토
6. 개선사항 반영

모든 요청에 이 과정을 강제로 적용하지 말고,
필요한 경우에만 사용하세요.


━━━━━━━━━━━━━━━━━━━━━━
5. 결과물
━━━━━━━━━━━━━━━━━━━━━━

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


━━━━━━━━━━━━━━━━━━━━━━
6. 출력 형식
━━━━━━━━━━━━━━━━━━━━━━

반드시 다음 구조로 답변하세요.


### ✨ 확장된 프롬프트

사용자가 그대로 복사해서 다른 AI에 입력할 수 있는
완성된 프롬프트를 작성하세요.


### 🔍 개선된 부분

원본 프롬프트에서 무엇을 개선했는지
핵심적인 내용을 3~5개 설명하세요.


### 💡 사용 팁

이 프롬프트를 더 효과적으로 사용하기 위한
간단한 팁을 1~3개 작성하세요.


━━━━━━━━━━━━━━━━━━━━━━
중요
━━━━━━━━━━━━━━━━━━━━━━

실제 사용자의 작업 결과를 생성하지 마세요.

당신의 역할은 오직
"사용자의 프롬프트를 개선하는 것"입니다.

답변은 {output_language}로 작성하세요.
"""


# ==================================================
# Expand Button
# ==================================================

st.markdown(
    "<div style='height:15px'></div>",
    unsafe_allow_html=True
)

expand_button = st.button(
    "✨ 프롬프트 확장하기"
)


# ==================================================
# API 호출
# ==================================================

if expand_button:

    if not user_prompt.strip():

        st.warning(
            "먼저 확장하고 싶은 프롬프트를 입력해주세요."
        )

    else:

        with st.spinner(
            "AI가 프롬프트를 분석하고 있습니다..."
        ):

            try:

                response = client.responses.create(

                    model="gpt-5.6-terra",

                    instructions=SYSTEM_PROMPT,

                    input=user_prompt

                )

                result = response.output_text

                st.session_state["result"] = result

            except Exception as e:

                st.error(
                    f"오류가 발생했습니다: {str(e)}"
                )


# ==================================================
# 결과
# ==================================================

if "result" in st.session_state:

    st.markdown(
        textwrap.dedent("""
        <div class="result-card">

            <div class="result-title">

                ✨ 확장된 프롬프트

                <span class="result-badge">
                    AI OPTIMIZED
                </span>

            </div>

            <div class="result-subtitle">
                원본 프롬프트의 의도를 분석하고
                AI가 이해하기 쉬운 형태로 구조화했습니다.
            </div>

        </div>
        """),
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state["result"]
    )


# ==================================================
# 사용 예시
# ==================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    textwrap.dedent("""
    <div class="card">

        <div class="card-title">
            💡 이렇게 입력해보세요
        </div>

        <div class="card-description">
            짧게 작성해도 괜찮습니다.
            핵심적인 아이디어만 입력해주세요.
        </div>

        <div class="example">
            유튜브 영상 아이디어 10개 만들어줘
        </div>

        <div class="example">
            스타트업 투자용 PPT 만들어줘
        </div>

        <div class="example">
            20대 여성을 위한 화장품 브랜드 이름 추천해줘
        </div>

        <div class="example">
            이 논문을 초보자도 이해할 수 있게 설명해줘
        </div>

        <div class="example">
            우리 서비스의 마케팅 전략을 만들어줘
        </div>

    </div>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Tip
# ==================================================

st.markdown(
    textwrap.dedent("""
    <div class="tip">

        💡 <strong>TIP</strong><br>

        프롬프트를 완벽하게 작성할 필요가 없습니다.
        <br>
        "무엇을 만들고 싶은지"만 작성하면
        Promptly AI가 목적, 역할, 조건, 결과물 형식 등을 분석해서 보완합니다.

    </div>
    """),
    unsafe_allow_html=True
)


# ==================================================
# Footer
# ==================================================

st.markdown(
    textwrap.dedent("""
    <div class="footer">
        Promptly AI · Turn simple ideas into powerful prompts.
    </div>
    """),
    unsafe_allow_html=True
)
