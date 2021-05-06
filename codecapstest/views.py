import os

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import testModel

@csrf_exempt
def index(request):
    tm = testModel.objects.first()
    if not tm or tm.id is None:
        tm = testModel()
        tm.testField = ''
        tm.testField2 = 0
        tm.id = 1
        tm.save()
    fileValue = readFile()
    if request.method == 'POST':
        if 'file' in request.POST:
            writeFile(fileValue + 1)
            fileValue = readFile()
        else:
            tm.testField2 = int(round(float(tm.testField2))) + 1
            tm.save()
    context = {
        "DBValue": int(float(tm.testField2)),
        "FileValue": int(fileValue),
        "FilePath": str(os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt'))
    }
    return render(request, 'index.html', context)

def readFile():
    filePath = os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt')
    if os.path.exists(filePath):
        with open(filePath, 'r') as file:
            val = file.readline()
    else:
        val = 0
    return int(val)

def writeFile(val):
    filePath = os.environ.get("TEXTFILE_URL", './DjangoTestWriteFile.txt')
    with open(filePath, 'w+') as file:
        file.write(str(val))



