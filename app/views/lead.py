class LeadCreate(CreateView):
    model = Lead
    template_name = "main/contact_us.html"
    fields = "__all__"
    success_url = reverse_lazy("main")