from django.db import models

class details_bio(models.Model):
    bname = models.CharField(max_length = 40)
    bcat = models.CharField(max_length = 40)
    btype = models.CharField(max_length = 40)
    bsymt = models.TextField(max_length = 100)

    def __str__(self):
        return self.bname
        return self.bcat
        return self.btype
        return self.bsymt