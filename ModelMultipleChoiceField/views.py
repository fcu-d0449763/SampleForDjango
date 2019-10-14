class GroupCreateView(PermissionRequiredMixin,CreateView):
    model = Group
    form_class = GroupForm
    permission_required = 'auth.add_group'

    # 新增分類後，轉跳到分類列表
    def get_success_url(self):
        return reverse('knowledge_group_list')