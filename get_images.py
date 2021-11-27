from PIL import Image
import requests
from io import BytesIO
import pandas as pd

def get_image(uniq_id,name,category,url):
    try:
        # Image
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((250, 250), Image.ANTIALIAS)
        img.save('Dataset/flipkart/images/{}.jpg'.format(uniq_id))
        
        # Metadata
        img_metadata = pd.DataFrame({'id': [uniq_id],
                                     'name': [name],
                                     'category': [category]})
        
        return img_metadata
    except:
        print('fail: {}'.format(url))
        pass