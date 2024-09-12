from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1 style="text-align: center; color: red">VISTA N°1 FLAVIO ARZOLA</h1>'
                        '<p style="background-color: green; font-size: 30">Lorem ipsum dolor sit amet consectetur adipiscing elit tellus enim suscipit, turpis magnis feugiat vivamus sociis senectus dapibus platea netus. Enim aliquam erat tellus nostra venenatis ridiculus id dis etiam nulla maecenas, risus lobortis praesent platea neque imperdiet ultrices bibendum et arcu nisl, proin penatibus per sociis dictum laoreet magna semper ullamcorper dui. Senectus commodo elementum auctor quam vitae hac blandit ante sapien, suscipit ad tortor accumsan vel maecenas cras est taciti potenti, magnis mus nulla dictum phasellus bibendum nascetur donec.</p>'
                        '<a style="font-size: 20" href="https://www.youtube.com">YOUTUBE</a>'
                        
                        
                        )

# Create your views here.
