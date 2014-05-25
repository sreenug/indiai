from django.views.generic import CreateView

from models import Award, College, CollegeForm

from school_data.settings import MEDIA_URL
from django.http import HttpResponse
import simplejson
import json
import csv

from school_data.settings import PROJECT_PATH

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

class CreateCollegeView(CreateView):
    model = College
    template_name = 'college.html'
    form_class = CollegeForm
    
    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('image')
        if f:
            data = [{'name': f.name, 'url': MEDIA_URL + "college/" + f.name.replace(" ", "_")}]
        response = JSONResponse("Thank You For Filling the Form", {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = simplejson.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)
