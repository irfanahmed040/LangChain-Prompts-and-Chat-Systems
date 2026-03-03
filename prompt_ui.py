from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatOpenAI(model="o4-mini-2025-04-16")

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", ["Attention is all you Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style:", ["Beginner-Friendly", "Technical", "Code-Ordiented", "Mathematical"])

length_input = st. selectbox ("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation) "] )

Template = load_prompt('template.json')

#inject values into the prompt
prompt = Template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)