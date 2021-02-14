from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=128, label='')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mr-sm-2 volny-input'
            visible.field.widget.attrs['placeholder'] = 'Search'