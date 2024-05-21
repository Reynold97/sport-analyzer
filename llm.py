from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

syst_prompt = """
You are an expert sports analyzer with more than 10 years of experience in Australian rugby. Your current task is to help me to understand\
a live game based on poor radio transcriptions snippets. I only want to know important events, actions, player names, team matchup in bullet points,\
with just a few words, as short and concise as possible, that MUST be your answer and nothing else.\
"""

def analyze_snippet(transcription_chunk:str):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": syst_prompt},
        {"role": "user", "content": f"Here is the transcription snippet:{transcription_chunk}"}
    ]
    )
    return completion.choices[0].message.content


