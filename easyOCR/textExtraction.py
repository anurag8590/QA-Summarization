import easyocr
import pandas as pd
from PIL import Image
import io


reader = easyocr.Reader(['en'], gpu = False)


def create_string(dataframe):
    s = ''
    for col in dataframe.columns:
        for cell in dataframe[col]:
            s += str(cell) + " "
    return s


def read_text(image_path):
    image = Image.open(io.BytesIO(image_path))
    results = reader.readtext(image)
    df_easyocr = pd.DataFrame(results,columns=['bbox','text','conf'])
    df2  = df_easyocr.drop(['bbox','conf'],axis=1)
    df2 = df2.T
    text = create_string(df2)

    return text

