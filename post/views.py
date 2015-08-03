import os
import uuid
from django.conf import settings
from django.views.generic import FormView

from post.forms import PostForm

def handle_uploaded_file(f):
    filename = str(uuid.uuid4())
    with open(os.path.join(settings.UPLOADED_FILES_DIR, filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return filename


class PostCreateView(FormView):
    template_name = "post/create.html"
    form_class = PostForm
    # TODO: replace with url named
    success_url = '/thanks/'

    def form_valid(self, form):
        filename = handle_uploaded_file(self.request.FILES['file'])
        form.create_post(filename)

        return super(PostCreateView, self).form_valid(form)
