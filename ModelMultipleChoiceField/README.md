# 

## 參考網址

- https://medium.com/@alfarhanzahedi/customizing-modelmultiplechoicefield-in-a-django-form-96e3ae7e1a07



### 關於 queryset

有兩個字段可用於表示模型之間的關係：ModelChoiceField和 ModelMultipleChoiceField。這兩個字段都需要一個queryset用於創建字段選擇的參數。表單驗證後，這些字段會將一個模型對象（對於ModelChoiceField）或多個模型對象（對於ModelMultipleChoiceField）放置到cleaned_data表單的 字典中。

對於更複雜的用途，您可以queryset=None在聲明表單字段時指定，然後queryset在表單的__init__() 方法中填充：

```
class FooMultipleChoiceForm(forms.Form):
    foo_select = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foo_select'].queryset = ...
```
- https://docs.djangoproject.com/en/2.2/ref/forms/fields/
- https://stackoverflow.com/questions/738301/how-to-modify-choices-of-modelmultiplechoicefield
