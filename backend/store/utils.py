
import uuid 

def product_image_path(instance , filename):
    return f'store/products/images/{instance.id}_{instance.code}_{uuid.uuid4()}{filename}'
