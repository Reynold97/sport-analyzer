import gradio as gr

from tts import transcribe_audio
from llm import analyze_snippet

def pipeline(audio_path):
    """Pipeline to comunicate tts and kg modules"""
    transcription = transcribe_audio(audio_path)
    bullet_points = analyze_snippet(str(transcription))
    return f"Game Analysis:\n {bullet_points}"


iface = gr.Interface(
    fn=pipeline,
    inputs=gr.Audio(sources="microphone", type="filepath", format="wav"),
    outputs="text",
    title="Sports-Analyzer",
)

if __name__ == "__main__":
    iface.launch()
