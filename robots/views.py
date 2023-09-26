from django.http import HttpResponse, FileResponse
from django.views.decorators.http import require_http_methods
import xlsxwriter
import datetime
from django.utils import timezone
from .models import Robot
from django.db.models import Count


@require_http_methods(["GET"])
def robots_report(request):
    FILE_NAME = "robots_report.xlsx"
    COLUMNS = ["Модель", "Версия", "Количество за неделю"]

    unique_models = Robot.objects.values_list("model", flat=True).distinct()
    workbook = xlsxwriter.Workbook(FILE_NAME)

    for model in unique_models:
        sheet = workbook.add_worksheet(model)
        for column_number in range(len(COLUMNS)):
            sheet.write(0, column_number, COLUMNS[column_number])

        versions = Robot.objects.filter(
            created__gte=timezone.now() - datetime.timedelta(days=7), model=model
        ).values("version").annotate(total=Count('version')).order_by('total')

        for i, version in enumerate(versions):
            sheet.write(i + 1, 0, model)
            sheet.write(i + 1, 1, version["version"])
            sheet.write(i + 1, 2, version["total"])
    workbook.close()

    
    return HttpResponse(
        FileResponse(open(FILE_NAME, "rb"),
                     content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )