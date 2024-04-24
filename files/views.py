from django.shortcuts import render, redirect
from django.views import View
from .models import File

# Create your views here.


class UploadFileView(View):
    model = File
    template_name = "files/index.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        print(request.POST)

        # Get the list of uploaded files
        uploaded_files = request.FILES
        print(uploaded_files)
        if uploaded_files:
            for key in uploaded_files.keys():
                # Get the list of files for each key
                files = uploaded_files.getlist(key)
                # Loop through each file in the list and save it
                for file in files:
                    new_file = File(file=file)
                    new_file.save()

        return render(request, self.template_name)
