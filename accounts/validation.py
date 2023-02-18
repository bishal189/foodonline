from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
    ext=os.path.splitext(value.name)[1]#cover-img.jpg then it will give jpg only
    print(ext)
    valid_extension=['.png','.jpg','.jpeg']
    if not ext.lower() in valid_extension:
        raise ValidationError('unsupported file extension.Allowed extensions :'  + str(valid_extension))

  