from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200) # 文章網址
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now) # 發表時間

    class Meta:
        # 指定文章顯示的順序
        # pip3 install pytz
        ordering = ('-pub_date',)

    def __unicode__(self):
        # 此類別所產生的資料項目
        return self.title
