from django import forms
from .models import Todo


class TodoForm(forms.Form):
    title = forms.CharField(label="Tên sách", max_length=255)

    def save(self):
        try:
            book = Todo()
            book.title = self.cleaned_data['title']
            book.full_clean()  # Validate the book instance before saving
            book.save()
            return book
        except forms.ValidationError as e:
            raise forms.ValidationError(e.message_dict)
        except Exception as e:
            raise e