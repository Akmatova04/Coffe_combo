from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Категория аты")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="Слаг (автоматтык)") # URL үчүн

    def save(self, *args, **kwargs):
        if not self.slug:
            
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"

class MenuItem(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=150, verbose_name="Аты")
    description = models.TextField(blank=True, verbose_name="Сүрөттөмөсү")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Баасы (сом)")
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True, verbose_name="Сүрөтү")
    is_special = models.BooleanField(default=False, verbose_name="Өзгөчө сунуш?") # Мисалдагы "Our Special Coffee" үчүн

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню пункту"
        verbose_name_plural = "Меню пункттары"
        ordering = ['category', 'name'] # Категория жана аты боюнча иреттөө