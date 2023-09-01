import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレぐれすばーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expanderA = st.expander('問い合わせA')
expanderA.write('問い合わせAの回答')
expanderB = st.expander('問い合わせB')
expanderB.write('問い合わせBの回答')
expanderC = st.expander('問い合わせC')
expanderC.write('問い合わせCの回答')


