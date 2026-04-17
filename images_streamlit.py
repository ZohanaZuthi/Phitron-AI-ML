import streamlit as st

st.title("Input your files ", anchor=False)
st.divider()
image=st.file_uploader("Enter yuur Image ", type=['jpg', 'jpeg','png'])

print(type(image))
if image:
    st.image(image)
    
# to upload multiple images
images=st.file_uploader("Enter your images ", type=['jpg', 'jpeg','png'], accept_multiple_files=True)
# indexing from 0 use enumerate
if images:
    # This creates n vertical containers placed horizontally in a single row.
    col=st.columns(len(images))
    for i,img in enumerate(images):
        with col[i]:
            st.image(img)

