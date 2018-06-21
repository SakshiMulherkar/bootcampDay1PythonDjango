
class Blog(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)