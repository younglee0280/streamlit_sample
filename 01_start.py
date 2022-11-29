import streamlit as st
import 

st.title('제목')
st.header('헤더')
st.subheader('서브헤더')
st.text('그냥 문자열!')

file_name = './jjangu_list.csv'

df = pd.read_csv(file_name, encoding='UTF-8')