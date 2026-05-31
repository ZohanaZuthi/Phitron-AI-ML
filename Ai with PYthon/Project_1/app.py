import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_maker


st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")

st.divider()

with st.sidebar:
    st.header("Controls")
    images= st.file_uploader(
        "Upload the images of your notes (up to 3)", type=["jpg", "jpeg", "png"], accept_multiple_files=True
    )
    if images:
        if len(images)>3:
            st.warning("Please upload up to 3 images only.")
        else:
            st.subheader("Uploaded Images")
            col=st.columns(len(images))
            
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
        
# difficulty

    selected_option=st.selectbox("Select Quiz Difficulty", options=["Easy", "Medium", "Hard"], index=None)
    
    if selected_option:
        st.markdown(f"Selected Option: **{selected_option}**")
    else: 
        st.error("Please select a difficulty level for the quiz.")
    pressed=st.button("Click the button",type="primary")

if pressed:
    if not images:
        st.error("Please upload at least one image to generate the quiz.")
    if not selected_option:
        st.error("Please select a difficulty level for the quiz.")
    
            
if pressed and images and selected_option:
    
    with st.container(border=True):    
        note=note_generator(images)
        st.markdown(note)
        
    
    with st.container(border=True):
        st.subheader("Audio Transcription")
        audio_buffer=audio_transcription(note)
        st.audio(audio_buffer)
    
    with st.container(border=True):
        st.subheader("Quiz Questions")
        quiz=quiz_maker(images,selected_option)
        st.markdown(quiz)
        
        
      