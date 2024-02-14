from .image2text import Image2Text, LoadImage2TextModel
from .text2text import Text2Text
from .install import check_and_install


check_and_install("Pillow","PIL")
check_and_install("huggingface_hub")
check_and_install("transformers")
check_and_install("einops")
check_and_install("torchvision")
check_and_install("accelerate")

NODE_CLASS_MAPPINGS = {
    "Text2Text": Text2Text,
    "Image2Text": Image2Text,
    "LoadImage2TextModel": LoadImage2TextModel,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Text2Text": "Text to Text",
    "Image2Text": "Image to Text",
    "LoadImage2TextModel": "Loader Image to Text Model",
}
