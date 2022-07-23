import uuid
import os.path

def generate_uuid4_filename(filename):
    """
    Generates a uuid4 (random) filename, keeping file extension

    :param filename: Filename passed in. In the general case, this will 
                     be provided by django-ckeditor's uploader.
    :return: Randomized filename in urn format.
    :rtype: str
    """
    discard, ext = os.path.splitext(filename)
    basename = uuid.uuid4().urn
    return ''.join(basename, ext)