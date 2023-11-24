import streamlit as st
from PIL import Image


st.title("天田伊旺俐の卒研結果集")

st.markdown(":green[概要  \n下の選択画面から５つある結果をご参照ください  \nそれぞれの研究結果があります。発表内容と多少前後ずれる場合がありますがご了承ください  \nここに記載されている画像は返答内容をコピペしてワードにそのまま載せたものです。変更などの手は加えていません]")

select_option = st.selectbox("選択してください", ["選択されていません", "結果①(you chat)", "結果②(chat GPT)", "結果③(BING AI)", "結果④(Perplexity AI)","結果⑤(google bard)"])

if select_option == "結果①(you chat)":
    image1 = Image.open('sotuken1.png')
    st.image(image1, caption='研究結果１', use_column_width=True)
    
elif select_option == "結果②(chat GPT)":
    image2 = Image.open('sotuken2.png')
    st.image(image2, caption='研究結果2', use_column_width=True)
    
elif select_option == "結果③(BING AI)":
    image3 = Image.open("sotuken3.png")
    st.image(image3, caption="研究結果３", use_column_width=True)

elif select_option == "結果④(Perplexity AI)":
    image4 = Image.open('sotuken4.png')
    st.image(image4, caption='研究結果4', use_column_width=True)
    
elif select_option == "結果⑤(google bard)":
    image5 = Image.open("sotuken5.png")
    st.image(image5, caption="研究結果５", use_column_width=True)
