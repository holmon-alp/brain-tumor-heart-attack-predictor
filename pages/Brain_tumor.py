import streamlit as st
from os import getcwd
import plotly.express as px
from fastai.vision.all import PILImage, load_learner

#  Since there were custom label issues when exporting the model, we have included labeling in the app
custom_label_mapping = {
        '1': 'meningioma',
        '2': 'glioma',
        '3': 'pituitary tumor'
    }
# Loading model from file
BT_model = load_learner(f"{getcwd()}/models/brain_tumor.pkl")

st.set_page_config(
    page_title="Brain tumor checker",
    page_icon="🧠",
)

st.divider()
st.title("Program that detects brain tumors using X-ray images")
ftypes = ["png", "jpg"]

def brain_tumor_checker():
    img = st.file_uploader(label="Upload X-ray image", type=ftypes)
    
    if img is not None:
        st.success("Image uploaded successfully")
        st.image(img)  
        pil_img = PILImage.create(img)
        predict, pr_id, prob = BT_model.predict(pil_img)
        predict  = custom_label_mapping.get(predict[0], "Unknown").upper()

        st.markdown(f"Diagnosis result according to X-ray: <b>{predict}</b>")
        st.info(f"Accuracy: {(prob[pr_id] * 100):.2f}%")
        # print(model.dls.vocab, np.array(prob)*100 , sep='\n')
        fig = px.bar(x=custom_label_mapping.values(), y=prob*100)
        st.plotly_chart(fig)
    # else:
        # st.info("Image not foud")

brain_tumor_checker()
