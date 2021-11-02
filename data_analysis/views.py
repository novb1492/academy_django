from django.http.response import HttpResponse


from django.http import HttpResponse
def test(reqest):
    return HttpResponse('test')
