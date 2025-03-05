from django.db import models

class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.key = self.key.upper()  # Converte a chave para maiúsculas
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
