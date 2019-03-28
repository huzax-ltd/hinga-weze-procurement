from django import forms

from app.models import Products


class ProductExcelImportForm(forms.ModelForm):
    excel_file = forms.FileField(
        label='Excel File',
        required=True,
        validators=[],
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Excel File',
                'aria-label': 'form-label',
                'accept': '.csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            }
        ))

    def clean_excel_file(self):
        excel_file = self.cleaned_data['excel_file']
        return excel_file

    def clean(self):
        cleaned_data = super(ProductExcelImportForm, self).clean()
        return cleaned_data

    class Meta:
        model = Products
        fields = ()
