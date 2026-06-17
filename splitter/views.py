from django.shortcuts import render
from django.http import HttpResponse
from .utils import split_excel_to_zip

def index(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        
        try:
            rows_per_file = int(request.POST.get('rows_count', 9998))
        except ValueError:
            rows_per_file = 9998
            
        file_content = excel_file.read()
        zip_data = split_excel_to_zip(file_content, rows_per_file)
        
        if zip_data:
            response = HttpResponse(zip_data, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="splitted_excel_files.zip"'
            return response
        else:
            return render(request, 'splitter/index.html', {'error': 'الملف فارغ أو غير صالح'})
            
    return render(request, 'splitter/index.html')