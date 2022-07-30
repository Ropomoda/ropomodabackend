
import uuid 

def product_main_image_path(instance , filename):
    return f'store/products/images/main/{instance.uuid}_{instance.code}_{uuid.uuid4()}{filename}'

def product_image_path(instance , filename):
    return f'store/products/images/{instance.uuid}_{uuid.uuid4()}{filename}'