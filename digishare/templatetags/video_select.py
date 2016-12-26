import random

from django import template
from ..models import _video

register = template.Library()

@register.assignment_tag
def video_select():
    # try:
    #     vid_check = _video.objects.filter(video_id=1).count()
    # except(_video.DoesNotExist):
    #     return "NilDNE"
    # else:
    #     max_id = _video.objects.count()
    #     if max_id==0:
    #         random_id = randint(max_id, 1)
    #     else:
    #         random_id = randint(1, max_id)
    #     vid_pth = _video.objects.values_list('video_path', flat=True).get(video_id=random_id)
    #     return vid_pth
    try:
        vid_check = _video.objects.get(video_id=4)
    except(_video.DoesNotExist):
        return "https://drive.google.com/file/d/0B2UrKVBATwEYYVdJT0dJSFJiUkk/preview"
    else:
        # max_id = _video.objects.count()
        # random_id = randint(1, max_id)
        # vid_pth = _video.objects.get(video_id=random_id)
        return random.choice(list(_video.objects.all())).video_path

