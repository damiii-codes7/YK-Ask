import streamlit as st
from groq import Groq
import os

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="YK Ask", page_icon="🤖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Bebas+Neue&display=swap');
.stApp { background-color: #030303 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; }
.stButton > button { background: transparent !important; color: #9B51E0 !important; border: 1px solid #9B51E0 !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; letter-spacing: 0.15em !important; text-transform: uppercase !important; padding: 1rem 2rem !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton > button:hover { background: #9B51E0 !important; color: #030303 !important; }
.stTextInput input { background: #0a0a0a !important; border: 1px solid #181818 !important; color: #ffffff !important; font-family: 'Space Mono', monospace !important; font-size: 0.85rem !important; border-radius: 0 !important; padding: 1rem !important; }
.stTextInput input:focus { border-color: #9B51E0 !important; }
div[data-testid="metric-container"] { background: transparent !important; border: 1px solid #181818 !important; padding: 1.5rem !important; }
div[data-testid="metric-container"] label { font-family: 'Space Mono', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.2em !important; text-transform: uppercase !important; color: #888 !important; }
div[data-testid="metric-container"] div[data-testid="stMetricValue"] { font-family: 'Bebas Neue', sans-serif !important; font-size: 2.5rem !important; color: #ffffff !important; }
.stDownloadButton > button { background: #9B51E0 !important; color: #030303 !important; border: 1px solid #9B51E0 !important; font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important; font-weight: 700 !important; padding: 1rem 2rem !important; }
hr { border-color: #181818 !important; }
.stMarkdown p { color: #888 !important; font-size: 0.8rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@keyframes ringPulse { 0%{opacity:0.15;transform:translate(-50%,-50%) scale(0.3)} 100%{opacity:0;transform:translate(-50%,-50%) scale(1)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
@keyframes slideUp { to{transform:translateY(0)} }
@keyframes marquee { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
</style>
<div style='text-align:center;padding:6vh 2rem 3vh 2rem;position:relative;overflow:hidden;'>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #9B51E0;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease infinite;pointer-events:none;'></div>
<div style='position:absolute;width:500px;height:500px;border-radius:50%;border:1px solid #9B51E0;opacity:0;top:50%;left:50%;transform:translate(-50%,-50%);animation:ringPulse 6s ease 2s infinite;pointer-events:none;'></div>
<div style='display:inline-flex;align-items:center;gap:0.75rem;font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.15em;color:#888;margin-bottom:2rem;padding:0.6rem 1.2rem;border:1px solid #181818;'>
<span style='width:6px;height:6px;background:#9B51E0;border-radius:50%;animation:pulse 2s infinite;display:inline-block;'></span>
AI-Powered &nbsp;|&nbsp; All Indian Laws &nbsp;|&nbsp; Legal-Tech
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.3s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#ffffff;'>YK</div>
</div>
<div style='overflow:hidden;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.5s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(4rem,10vw,8rem);line-height:0.9;color:#9B51E0;'>ASK</div>
</div>
<div style='overflow:hidden;margin-bottom:2rem;'>
<div style='transform:translateY(115%);animation:slideUp 1.2s cubic-bezier(0.16,1,0.3,1) 0.7s forwards;font-family:Bebas Neue,sans-serif;font-size:clamp(1.5rem,4vw,3rem);line-height:0.9;color:#888;'>The expertise You Can Trust</div>
</div>
<div style='display:inline-block;padding:2rem 3rem;border:1px solid #181818;'>
<div style='font-family:Space Mono,monospace;font-size:0.6rem;text-transform:uppercase;letter-spacing:0.2em;color:#9B51E0;margin-bottom:0.5rem;'>SYSTEM STATUS</div>
<div style='font-family:Bebas Neue,sans-serif;font-size:3rem;color:#ffffff;line-height:1;'>READY</div>
<div style='font-family:Space Mono,monospace;font-size:0.65rem;color:#888;'>Transforming Confusion Into Clarity</div>
</div>
</div>
<hr style='border-color:#181818;margin:0;'>
<div style='overflow:hidden;padding:1rem 0;border-bottom:1px solid #181818;'>
<div style='display:flex;width:max-content;animation:marquee 35s linear infinite;font-family:Space Mono,monospace;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#444;white-space:nowrap;'>
<span style='padding:0 2rem;'>IPC 1860</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>CrPC 1973</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Constitution of India</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>GST Act</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Income Tax Act</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Companies Act 2013</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>POSH Act 2013</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Consumer Protection Act</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>RTI Act 2005</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>Indian Contract Act</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>IPC 1860</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
<span style='padding:0 2rem;'>CrPC 1973</span><span style='color:#9B51E0;padding:0 1rem;'>◆</span>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:3rem 0 1rem 0;'>
01 / SELECT LAW CATEGORY
</div>
""", unsafe_allow_html=True)

category = st.selectbox("", [
    "General — Any Indian Law",
    "Criminal Law — IPC, CrPC, BNSS",
    "Constitutional Law",
    "Labour & Employment Law",
    "Contract & Commercial Law",
    "Family & Personal Law",
    "Property Law",
    "Tax Law — GST, Income Tax",
    "Corporate Law — Companies Act",
    "Consumer Protection Law",
    "Cyber Law — IT Act",
    "Environmental Law",
    "RTI & Administrative Law",
    "Intellectual Property Law",
], label_visibility="collapsed")

st.markdown("""
<div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
02 / ASK YOUR QUESTION
</div>
""", unsafe_allow_html=True)

question = st.text_input("",
    placeholder="e.g. What is the punishment for theft under IPC? What are my rights as a tenant?",
    label_visibility="collapsed"
)

if st.button("🤖 GET LEGAL ANSWER →", use_container_width=True):
    if not question.strip():
        st.warning("Please type your question first!")
    else:
        with st.spinner("Researching Indian law..."):

            prompt = f"""You are an expert Indian lawyer with deep knowledge of all Indian laws.

Category: {category}
Question: {question}

Provide a clear, accurate answer under Indian law. Format your response as:

ANSWER:
[Clear direct answer to the question]

RELEVANT LAW:
[Specific act, section, and provision that applies]

EXPLANATION:
[Detailed explanation in simple language]

PRACTICAL ADVICE:
[What the person should do in practice]

DISCLAIMER:
This is general legal information. Consult a qualified lawyer for specific legal advice."""

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content

        st.markdown("""
        <div style='font-family:Space Mono,monospace;font-size:0.65rem;text-transform:uppercase;
        letter-spacing:0.2em;color:#888;margin:2rem 0 1rem 0;'>
        03 / LEGAL ANSWER
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='border:1px solid #181818;padding:2rem;
        font-family:Space Mono,monospace;font-size:0.85rem;
        color:#ffffff;line-height:1.8;'>
        {answer.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#181818;margin:2rem 0;'>", unsafe_allow_html=True)

        st.download_button(
            label="EXPORT ANSWER →",
            data=f"YK ASK — LEGAL ANSWER\n{'='*50}\nQuestion: {question}\nCategory: {category}\n\n{answer}",
            file_name="YKAsk_Answer.txt",
            mime="text/plain",
            use_container_width=True
        )

st.markdown("""
<div style='text-align:center;padding:1rem;font-family:Space Mono,monospace;
font-size:0.55rem;color:#333;text-transform:uppercase;letter-spacing:0.1em;'>
This is general legal information, not legal advice.<br>Adv. Damini Yasodai — YK Legal
</div>
""", unsafe_allow_html=True)
