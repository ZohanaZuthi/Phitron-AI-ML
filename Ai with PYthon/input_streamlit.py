import streamlit as st

st.title("Input your information", anchor=False)
st.divider()
name=st.text_input("Enter your name ")

st.write("Your name is: ",name)
print(type(name))

st.divider()
age=st.text_input("Enter your age ")

st.write("the age is ", age)

st.divider()
password=st.text_input("Enter your password ", type="password")

st.write("the password is ", password)
st.button("Submit",type="primary")


if password:
    st.success("Your password is correct")  
    
else:
    st.error("Please enter your password")
    
selected=st.selectbox("Choose your profession",(1,2,3,4,5), index=None, accept_new_options=True)

print(type(selected))

st.write("you selected ", selected)