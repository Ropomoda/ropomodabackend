import uuid


def category_image_path(instance , filename):
    return f'category/images/{instance.id}_{uuid.uuid4()}{filename}'
