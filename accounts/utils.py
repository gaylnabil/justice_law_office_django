from datetime import datetime, timedelta
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.six import text_type
from PIL import Image, ImageOps
from enum import Enum
from django.utils.translation import gettext as _
import pandas as pd


# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             text_type(user.pk) + text_type(timestamp) +
#             text_type(user.is_active)
#         )

# account_activation_token = AccountActivationTokenGenerator()


class Mode(Enum):
    RESIZE = 0
    THUMBNAIL = 1
    FIT = 2
    ZOOM = 3


def resize_image(image_name, size, mode):
    img = Image.open(image_name)

    # ImageOps compatible mode
    if img.mode not in ("L", "RGB"):
        img = img.convert("RGB")

    if mode == Mode.RESIZE:
        img.resize(size, Image.ANTIALIAS)
        # img = img.resize((200,200), Image.ANTIALIAS)
        # imageresize.save('resize_200_200_aa.jpg', 'JPEG', quality=75)

    elif mode == Mode.THUMBNAIL:

        img.thumbnail(size, Image.ANTIALIAS)
        # image.save('thumbnail_200_200_aa.jpg', 'JPEG', quality=75)
    elif mode == Mode.ZOOM:
        img.thumbnail(size, Image.ANTIALIAS)
        img.resize(size, Image.ANTIALIAS)
        # img = ImageOps.fit(img, size,Image.ANTIALIAS)
    else:
        img = ImageOps.fit(img, size, Image.ANTIALIAS)
        # imagefit.save('fit_200_200_aa.jpg', 'JPEG', quality=75)

    return img


def get_time_range(start=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end=(datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"), freq='30T'):

    times = pd.date_range(
        start=start, end=end, freq=freq)
    # times = times.to_series().to_dict()
    # times = times.to_series().strftime('%H:%M')
    times = times.strftime('%H:%M')
    times = tuple((val, val) for val in times)
    # times = list(times)
    # times.insert(0, ('', ''))
    # times = tuple(times)
    return times
