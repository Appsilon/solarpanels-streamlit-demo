from fastai.vision.all import *
import streamlit as st

st.set_page_config(page_title="Solar panels detection by Appsilon")

path = Path(".")
def label_func(fn):
    return path/"labels"/(fn.stem + fn.suffix)

st.header("Where are the solar panels???")
model = load_learner(path / 'models/export.pkl')
model.path = path
model = model.load(file="trained_6epoch")

example_file = st.selectbox(
    "Choose an image to analyze",
    sorted(path.glob("examples/*.png"))
)
uploaded_file = st.file_uploader("Or upload your own!")
st.write("Works best with pictures around 500x500px")

if uploaded_file is not None:
    im = Image.open(uploaded_file).convert("RGB")
else:
    im = Image.open(example_file).convert("RGB")

imageLocation = st.empty()
imageLocation.image(im)
im.save(path/"tmp.png")

mask  = array(model.predict(path/"tmp.png")[0]).astype(np.uint8)

mask[mask == 1] = 255
mask[mask == 0] = 255 // 3

imm = Image.fromarray(mask)
im.putalpha(imm)
imageLocation.image(im)

st.markdown("Find orthophoto image of our neighborhood at:")
st.markdown("https://mapy.geoportal.gov.pl/imap/Imgp_2.html")
