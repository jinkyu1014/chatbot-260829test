import streamlit as st
from openai import OpenAI


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Promptly AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

    /* 전체 배경 */
    .stApp {
        background:
            radial-gradient(
                circle at 50% -20%,
                rgba(124, 92, 255, 0.18),
                transparent 40%
            ),
            #09090b;
        color: #f4f4f5;
    }

    /* 기본 컨테이너 */
    .block-container {
        max-width: 1050px;
        padding-top: 40px;
        padding-bottom: 80px;
    }

    /* 헤더 */
    .brand {
        text-align: center;
        margin-top: 25px;
        margin-bottom: 8px;
    }

    .brand-title {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1.5px;
        background: linear-gradient(
            90deg,
            #ffffff,
            #b8a7ff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .brand-subtitle {
        color: #a1a1aa;
        font-size: 16px;
        margin-top: 8px;
    }

    /* 카드 */
    .card {
        background: rgba(24, 24, 27, 0.85);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 26px;
        margin-top: 28px;
        box-shadow:
            0 20px 60px rgba(0,0,0,0.25);
        backdrop-filter: blur(20px);
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .card-description {
        font-size: 13px;
        color: #a1a1aa;
        margin-bottom: 18px;
    }

    /* textarea */
    textarea {
        background: #111113 !important;
        color: #f4f4f5 !important;
        border: 1px solid #27272a !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        line-height: 1.7 !important;
    }

    textarea:focus {
        border: 1px solid #8b5cf6 !important;
        box-shadow: 0 0 0 1px #8b5cf6 !important;
    }

    /* 버튼 */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        border: 0;
        font-size: 15px;
        font-weight: 700;
        background: linear-gradient(
            135deg,
            #7c3aed,
            #8b5cf6
        );
        color: white;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow:
            0 10px 30px rgba(124,58,237,0.35);
    }

    /* 결과 박스 */
    .result-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 14px;
    }

    .result-icon {
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: rgba(139,92,246,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 17px;
    }

    .result-title {
        font-size: 19px;
        font-weight: 700;
    }

    .badge {
        display: inline-block;
        margin-left: 8px;
        padding: 4px 9px;
        border-radius: 20px;
        background: rgba(139,92,246,0.15);
        color: #c4b5fd;
        font-size: 11px;
        font-weight: 600;
    }

    /* 안내 */
    .tip {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 15px 18px;
        color: #a1a1aa;
        font-size: 13px;
        line-height: 1.6;
        margin-top: 20px;
    }

    /* 예시 */
    .example {
        background: rgba(255,255,255,0.025);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 13px 15px;
        margin-top: 8px;
        color: #d4d4d8;
        font-size: 13px;
    }

    /* Streamlit 기본 요소 */
    [data-testid="stToolbar"] {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    /* selectbox */
    div[data-baseweb="select"] > div {
        background: #111113;
        border-color: #27272a;
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)


# ==================================================
# OPENAI
# ==================================================

try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except Exception:
    OPENAI_API_KEY = None


if not OPENAI_API_KEY:

    st.error(
        """
        OpenAI API Key가 설정되지 않았습니다.

        `.streamlit/secrets.toml`에 다음과 같이 설정해주세요.

        `OPENAI_API_KEY = "sk-xxxxxxxx"`
        """
    )

    st.stop()


client = OpenAI(api_key=OPENAI_API_KEY)


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="brand">

    <div class="brand-title">
        ✨ Promptly AI
    </div>

    <div class="brand-subtitle">
        당신의 짧은 아이디어를 강력한 AI 프롬프트로 바꿔드립니다.
    </div>

</div>
""", unsafe_allow_html=True)


# ==================================================
# PROMPT INPUT
# ==================================================

st.markdown("""
<div class="card">

    <div class="card-title">
        📝 프롬프트 입력
    </div>

    <div class="card-description">
        AI에게 요청하고 싶은 내용을 자유롭게 작성해주세요.
        짧게 작성해도 AI가 필요한 내용을 분석해서 보완합니다.
    </div>

</div>
""", unsafe_allow_html=True)


user_prompt = st.text_area(
    "",
    height=190,
    placeholder="""예시:
유튜브 채널 아이디어를 만들어줘

또는

우리 회사의 AI 서비스를 투자자에게 설명하는
PPT를 만들어줘""",
    label_visibility="collapsed"
)


# ==================================================
# SETTINGS
# ==================================================

col1, col2, col3 = st.columns([1.3, 1.3, 1])

with col1:

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


with col2:

    target_ai = st.selectbox(
        "사용할 AI",
        [
            "범용 AI",
            "ChatGPT",
            "Claude",
            "Gemini"
        ]
    )


with col3:

    output_language = st.selectbox(
        "프롬프트 언어",
        [
            "한국어",
            "English"
        ]
    )


# ==================================================
# SYSTEM PROMPT
# ==================================================

SYSTEM_PROMPT = f"""
당신은 세계 최고 수준의 Prompt Engineer입니다.

사용자가 입력한 원본 프롬프트를 분석하고,
사용자의 의도와 목적을 유지하면서
AI가 훨씬 정확하고 높은 품질의 결과를 만들 수 있도록
프롬프트를 확장하고 개선하세요.

현재 설정:

확장 스타일:
{expansion_style}

사용 대상 AI:
{target_ai}

출력 언어:
{output_language}


━━━━━━━━━━━━━━━━━━━━━━━━━━
핵심 원칙
━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 사용자의 원래 의도를 절대 변경하지 마세요.

2. 사용자가 요청하지 않은 내용을 임의의 사실로 만들어내지 마세요.

3. 단순한 요청에는 불필요하게 복잡한 프롬프트를 만들지 마세요.

4. 복잡한 요청이라면 다음 요소를 적절하게 추가하세요.

- Role
- Context
- Goal
- Task
- Target Audience
- Input
- Process
- Output Format
- Constraints
- Evaluation Criteria
- Tone / Style
- Requirements

5. AI가 작업을 수행할 때 필요한 정보가 부족하다면
   사용자가 직접 입력할 수 있도록 [ ] 형태의 placeholder를 사용하세요.

예:

[타겟 고객]
[예산]
[브랜드명]
[서비스 설명]

6. 숫자나 사실을 임의로 만들어내지 마세요.

7. 사용자가 원하는 결과물이 있다면
   결과물의 구조와 형식을 구체적으로 정의하세요.

8. 복잡한 작업이라면 AI가 내부적으로 작업 순서를 고려하도록
   명확한 작업 절차를 정의하세요.

9. 최종 프롬프트는 다른 AI에 그대로 복사해서 사용할 수 있어야 합니다.

10. 실제 작업 결과를 생성하지 마세요.
    당신의 역할은 '프롬프트를 만드는 것'입니다.


━━━━━━━━━━━━━━━━━━━━━━━━━━
출력 형식
━━━━━━━━━━━━━━━━━━━━━━━━━━

반드시 다음 구조로 답변하세요.

### ✨ 확장된 프롬프트

완성된 프롬프트를 작성하세요.

이 부분은 사용자가 그대로 복사해서
다른 AI에 입력할 수 있어야 합니다.


### 🔍 개선된 부분

원본 프롬프트에서 어떤 부분을 보완했는지
핵심적인 내용만 3~5개 설명하세요.


### 💡 사용 팁

이 프롬프트를 사용할 때 도움이 되는
간단한 팁을 1~3개 작성하세요.

불필요하게 장황하게 설명하지 마세요.
"""


# ==================================================
# EXPAND BUTTON
# ==================================================

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

expand_button = st.button(
    "✨ 프롬프트 확장하기"
)


# ==================================================
# API REQUEST
# ==================================================

if expand_button:

    if not user_prompt.strip():

        st.warning(
            "먼저 확장할 프롬프트를 입력해주세요."
        )

    else:

        with st.spinner("AI가 프롬프트를 분석하고 있습니다..."):

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
# RESULT
# ==================================================

if "result" in st.session_state:

    st.markdown("""
    <div class="card">

        <div class="result-header">

            <div class="result-icon">
                ✨
            </div>

            <div class="result-title">
                확장된 프롬프트
                <span class="badge">
                    AI Optimized
                </span>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        st.session_state["result"]
    )


# ==================================================
# EXAMPLE
# ==================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

    <div class="card-title">
        💡 이렇게 입력해보세요
    </div>

    <div class="card-description">
        완벽하게 작성할 필요가 없습니다.
        핵심적인 아이디어만 적어주세요.
    </div>

    <div class="example">
        "AI 스타트업 사업계획서 만들어줘"
    </div>

    <div class="example">
        "20대 여성을 위한 화장품 브랜드 이름 추천해줘"
    </div>

    <div class="example">
        "우리 앱의 마케팅 전략을 만들어줘"
    </div>

    <div class="example">
        "이 논문을 초보자도 이해할 수 있게 설명해줘"
    </div>

</div>
""", unsafe_allow_html=True)


# ==================================================
# FOOTER
# ==================================================

st.markdown("""
<div style="
    text-align:center;
    color:#52525b;
    font-size:12px;
    margin-top:50px;
">
    Promptly AI · Turn simple ideas into powerful prompts.
</div>
""", unsafe_allow_html=True)
