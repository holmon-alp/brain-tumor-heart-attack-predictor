import streamlit as st

st.set_page_config(
    page_title="Brain tumor and heart attack checker",
    page_icon="❤️️&🧠",
)

st.write("# Welcome to diagnosis app")

st.sidebar.info("Select program above")

st.markdown(
    """
    With the help of this program, you can check brain tumor according to X-ray picture 
    and heart attack susceptibility based on natural and biological data.
    **👈 Select a program from the sidebar** to test programs!
    ### About Brain tumor software:
    The program's model was trained using the image dataset from kaggle.com.
    You can get acquainted with the model notebook and dataset through the following link:
    [Brain tumor model](https://www.kaggle.com/code/holmonalp/brain-tumor)

    ### About Heart Attack Program:
    This program is based on tabular dataset from kaggle.com. 
    You enter information on a given form and the program predicts 
    whether you are more or less likely to have a heart attack.
    If you want to get more information about the model, click on the link below.
    [Code on Github](https://github.com/holmon-alp/heart-attack-predictor.git)


   https://colab.research.google.com/drive/1PWO3Wh582iymliE94Mq14x70GFF6NIzQ?usp=sharing
   
"""
)



# if __name__ == "__main__":
#     pg.braintumor.brain_tumor_checker()
#     # run_parallel([heart_attack, brain_tumor_checker])















