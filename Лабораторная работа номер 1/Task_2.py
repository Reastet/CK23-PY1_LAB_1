# TODO Найдите количество книг, которое можно разместить на дискете
KB_MB = 1024
val_of_disk = 1.44
val_of_disk_in_Bt = val_of_disk * KB_MB * KB_MB
count_of_pages = 100
count_of_lines = 50
count_of_symb = 25
weight_of_symb = 4
weight_of_book = count_of_pages * count_of_lines * count_of_symb * weight_of_symb
books_on_disk = int(val_of_disk_in_Bt / weight_of_book)
print("Количество книг, помещающихся на дискету:", books_on_disk)
