
from django import forms



class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        widget=FilteredSelectMultiple("permissions", is_stacked=False),
        # queryset=Permission.objects.all(),
        queryset = Permission.objects.filter(content_type__app_label='knowledge'),
        help_text='此為權限列表，可直接修改model的權限'
    )
    users = forms.ModelMultipleChoiceField(
        widget=FilteredSelectMultiple("users", is_stacked=False),
        queryset=User.objects.all(),
        help_text='此為名單'
    )
    class Meta:
        model = Group
        fields = ["name", "permissions"]
        css = {"all": ("/static/admin/css/widgets.css",)}
        js = ("/admin/jsi18n",)
        help_texts = {
            "name": "請在此輸入權限名單名稱"
        }



    def __init__(self, *args, **kwargs):
        if kwargs.get("instance"):
            initial = kwargs.setdefault("initial", {})
            initial["users"] = [t.pk for t in kwargs["instance"].user_set.all()]
        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self):
        instance = forms.ModelForm.save(self)
        instance.user_set.clear()
        instance.user_set.add(*self.cleaned_data["users"])
        return instance