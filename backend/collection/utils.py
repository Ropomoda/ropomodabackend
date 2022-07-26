import uuid


def collection_image_path(instance , filename):
    return f'collection/images/{instance.id}_{uuid.uuid4()}{filename}'
