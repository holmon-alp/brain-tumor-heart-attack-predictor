import streamlit as st

st.set_page_config(
    page_title="Brain tumor and heart attack checker",
    page_icon="🧠",
)

st.write("# Welcome to diagnosis app")

st.sidebar.info("Select program above")

st.markdown(
    """
    With the help of this program, you can check brain tumor according to X-ray picture 
    and heart attack susceptibility based on natural and biological data.

    **👈 Select a program from the sidebar** to test programs!

    ---
    ### About Brain tumor software:
    The program's model was trained using the image dataset from kaggle.com.
    You can get acquainted with the model notebook and dataset through the following link:
    
    [Brain tumor model](https://www.kaggle.com/code/holmonalp/brain-tumor)

    ![brain](https://media.istockphoto.com/id/171263511/photo/brain-x-ray.jpg?s=612x612&w=0&k=20&c=nSBx0KQBqWHFSE11fR2QankeeORh6JQfpOclbIYSaMQ=)
    ___
    ### About Heart Attack Program:
    This program is based on tabular dataset from kaggle.com. 
    You enter information on a given form and the program predicts 
    whether you are more or less likely to have a heart attack.
    If you want to get more information about the model, click on the link below.

    [Code on Github](https://github.com/holmon-alp/heart-attack-predictor.git)

    ![heart](https://marvel-b1-cdn.bc0a.com/f00000000229348/www.silversneakers.com/wp-content/uploads/2018/09/SSBlog_HeartAttack_700x525.jpg)

    ***
    
    [Source code of this app](https://github.com/holmon-alp/brain-tumor-heart-attack-predictor.git)

    ---
    ##### Created at 18.02.2023
    #### Created by **Mirjamol Mirislomov**
"""
)
