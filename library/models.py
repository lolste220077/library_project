from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    year = models.IntegerField(verbose_name="Год издания")
    quantity = models.IntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Reader(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    group_number = models.CharField(max_length=50, verbose_name="Группа")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    issue_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи")
    return_date = models.DateField(null=True, blank=True, verbose_name="Дата возврата")
    is_returned = models.BooleanField(default=False, verbose_name="Возвращена")

    def __str__(self):
        return f"{self.book.title} -> {self.reader.full_name}"

    class Meta:
        verbose_name = "Выдача"
        verbose_name_plural = "Выдачи"