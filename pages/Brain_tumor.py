import streamlit as st
from os import getcwd
import plotly.express as px
from fastai.vision.all import PILImage, load_learner
import io


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
# Page header
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
        # Display results
        st.markdown(f"#### Diagnosis result according to X-ray: **{predict}**")
        st.info(f"Accuracy: {(prob[pr_id] * 100):.2f}%")
        fig = px.bar(x=custom_label_mapping.values(), y=prob*100)
        st.write("Differences in results")
        st.plotly_chart(fig)
    # else:
        # st.info("Image not foud")

brain_tumor_checker()


# Files(images) for testing model
test1 = PILImage.create("pages/tests/1000.png")
test2 = PILImage.create("pages/tests/100.png")
test3 = PILImage.create("pages/tests/2300.png")

st.markdown("""
            ---
            ```Images for test this app```
        """)

def download_image(image_obj, name: str):
    with io.BytesIO() as buffer:
        image_obj.save(buffer, format="PNG")
        st.download_button(f"Download {name}", buffer.getvalue(), file_name=name)

# Download test images
download_image(test1, "test1.png")
download_image(test2, "test2.png")
download_image(test3, "test3.png")
