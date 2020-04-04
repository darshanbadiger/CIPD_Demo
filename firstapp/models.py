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


class upload_data(models.Model):
    part_name = models.CharField(max_length = 200)
    species = models.CharField(max_length = 200)
    function_tag = models.TextField()
    geometry = models.FileField(upload_to = 'geometry/')
    mesh = models.FileField(upload_to = 'mesh/')

    def __str__(self):
        return self.part_name
        return self.species
        return self.function_tag