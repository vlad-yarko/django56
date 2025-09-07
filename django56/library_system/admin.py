from django.contrib import admin
from .models import Author, Book, Reader, Loan


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", ]
    search_fields = ["title", ]


class ReaderAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


class LoanAdmin(admin.ModelAdmin):
    list_display = ["reader", ]
    search_fields = ["reader", ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Loan, LoanAdmin)
