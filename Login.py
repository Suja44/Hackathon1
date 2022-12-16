import streamlit as st
import webbrowser as wb
import func
import time
st.set_page_config(layout="wide",page_title="disease-prediction")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)



def home():
    st.title("WELCOME TO FitOps")
    login, signup = st.columns([2, 2])
    with login:
        st.subheader("LOGIN")
        username = st.text_input("Enter username:",key="username")
        password = st.text_input("Enter a password", type="password")
        # st.text(username)
        # st.text(password)
        creds = func.get_cred()
        usepass = username + password + '\n'
        if st.button('LOGIN'):
            if usepass in creds:
                st.success("login success")
                name=username
                # if username not in st.session_state:
                #     st.session_state["username"]=username
                time.sleep(1)

                wb.open("http://localhost:8502/Dashboard",new=0)

            else:
                st.error("Incorrect username or password,please try again!")

    with signup:
        st.subheader("SIGNUP")
        username = st.text_input("Enter username:", key="usrname")
        password = st.text_input("Enter a password", type="password", key="pasword")
        con_pass = st.text_input("Confirm password", type="password")
        if st.button("SIGNUP"):
            if password != con_pass:
                st.error("Wrong password entered")
            else:
                creds = func.get_cred()
                creds.append(username + password + '\n')
                func.write_cred(creds)
                st.success(f'Welcome {username}')
                time.sleep(1)
                wb.open("http://localhost:8502/Dashboard",new=0)


if __name__ =="__main__":
    home()






