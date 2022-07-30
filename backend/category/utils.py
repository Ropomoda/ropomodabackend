import uuid


def category_image_path(instance , filename):
    return f'category/images/{instance.uuid}_{uuid.uuid4()}{filename}'
