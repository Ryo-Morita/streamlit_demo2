import textwrap
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit  超入門')

# st.write('Display Image')

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )

#st.write(df)
#st.table(df.style.highlight_max(axis = 0))
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)

# if st.checkbox('Show Image'):
#     img = Image.open('IMG_0261 (2).jpg')
#     st.image(img, caption='mogmog', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11)))
# 'あなたの好きな数字は',option,'です'

# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',text,'です'

# condition = st.slider('あなたの今の調子は？',0,100,50)#min,max,start値
# 'コンディション',condition,'です'

# # st.sidebarって書くと、サイドバーに持っていける
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',text,'です'

# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)#min,max,start値
# 'コンディション',condition,'です'



st.write('プログレスバーの表示')
'Start!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done'





left_columns, right_columns = st.columns(2)
button = left_columns.button('右カラムに文字を表示')
if button:
    right_columns.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

