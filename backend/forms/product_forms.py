from django import forms

from app.models import Products


class ProductSearchIndexForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ProductSearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Products
        fields = (

        )


class ProductInventorySearchIndexForm(forms.ModelForm):
    product_inventory_search_start_date = forms.DateField(
        label='From date',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-start-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))
    product_inventory_search_end_date = forms.DateField(
        label='To date',
        required=True,
        validators=[],
        input_formats=['%Y-%m-%d', '%d %b %Y'],
        widget=forms.DateInput(
            format='%d %b %Y',
            attrs={
                'type': 'date',
                'id': 'search-input-date-end-date',
                'class': 'form-control',
                'style': 'width:100%;',
                'placeholder': 'Date of Birth',
                'aria-label': 'form-label',
            }
        ))

    def clean_product_inventory_search_start_date(self):
        data = self.cleaned_data['product_inventory_search_start_date']
        return data

    def clean_product_inventory_search_end_date(self):
        data = self.cleaned_data['product_inventory_search_end_date']
        return data

    def clean(self):
        cleaned_data = super(ProductInventorySearchIndexForm, self).clean()
        return cleaned_data

    class Meta:
        model = Products
        fields = (
            'product_inventory_search_start_date',
            'product_inventory_search_end_date',
        )


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
