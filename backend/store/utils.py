
import uuid 

def product_main_image_path(instance , filename):
    return f'store/products/images/main/{instance.id}_{instance.code}_{uuid.uuid4()}{filename}'

def product_image_path(instance , filename):
    return f'store/products/images/{instance.id}_{uuid.uuid4()}{filename}'