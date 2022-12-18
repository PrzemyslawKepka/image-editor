from io import BytesIO

import streamlit as st
from PIL import Image

from image_editor import multiple_images, textboxes

st.set_page_config(layout="wide")

st.title("Image Editor")

uploaded_img = st.file_uploader(
    "Please upload an image you want to edit",
    type=["png", "jpg", "jfif"],
    accept_multiple_files=False,
)

# FUNCTONALITIES FOR MULTIPLE IMAGES - NOT IMPLEMENTED YET
# if len(uploaded_img) == 1:
#     image = Image.open(uploaded_img[0])
# elif len(uploaded_img) > 1:
#     images = {
#         "image" + str(index): img for index, img in enumerate(uploaded_img)
#     }

# if "images" in locals():
#     st.write(images)
#     multi_img_action = st.radio(
#         "Please select an action for multiple images",
#         ["Combine", "Paste"],
#         horizontal=True,
#     )

#     if multi_img_action == "Combine":
#         image = multiple_images.get_concat_h_resize(
#             uploaded_img[0], uploaded_img[1]
#         )
        # image.save('ssg.jpg')

if uploaded_img:
    # creating object for PIL as well to allow editing it
    # pil_img = Image.open(image)
    pil_img = Image.open(uploaded_img)
    pict_side, config_side = st.columns([2, 1], gap="large")

    with config_side:
        top_text = st.text_input("Top text:")
        with st.expander("Top text parameters:"):
            top = textboxes.TextParams(key="top")
        bottom_text = st.text_input("Bottom text")
        with st.expander("Bottom text parameters:"):
            bot = textboxes.TextParams(key="bot")

    with pict_side:
        top.place_text_on_image(pil_img, top_text, "top")
        line_length = bot.place_text_on_image(pil_img, bottom_text, "bottom")
        displ_img = st.image(pil_img, width=800)

    # allow saving the file
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    byte_image = buf.getvalue()
    download_button = st.download_button(
        label="Download image",
        data=byte_image,
        file_name="image.png",
        mime="image/jpeg",
    )
    if download_button:
        st.success("Image downloaded successfully!")
