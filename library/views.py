from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Reader, Loan
from datetime import date  # <--- Важно: добавили импорт для даты возврата

# Главная страница (Каталог книг)
def book_list(request):
    books = Book.objects.all()
    # Передаем список читателей для формы выдачи
    readers = Reader.objects.all() 
    return render(request, 'library/book_list.html', {'books': books, 'readers': readers})

# Функция выдачи книги
def issue_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        reader_id = request.POST.get('reader_id')
        reader = get_object_or_404(Reader, id=reader_id)
        
        # Если книги есть в наличии, выдаем
        if book.quantity > 0:
            book.quantity -= 1 # Уменьшаем количество
            book.save()
            # Создаем запись о выдаче
            Loan.objects.create(book=book, reader=reader)
    return redirect('book_list')

# Новая функция для отображения страницы (Журнала выдач)
def loan_list(request):
    # Сортируем: сначала те, что на руках (is_returned=False), потом возвращенные
    loans = Loan.objects.all().order_by('is_returned', '-issue_date')
    return render(request, 'library/loan_list.html', {'loans': loans})

# Функция возврата книги
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)
    if not loan.is_returned:
        loan.is_returned = True
        loan.return_date = date.today() # Фиксируем сегодняшнюю дату возврата
        loan.book.quantity += 1 # Возвращаем книгу на склад (увеличиваем количество)
        loan.book.save()
        loan.save()
    return redirect('loan_list') # После возврата перекидываем на страницу выдач