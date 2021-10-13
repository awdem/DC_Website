from django.urls import re_path

from core.report_helpers.views import MarkdownFileView

app_name = "report_whos_missing"


urlpatterns = [
    re_path(
        r"^$",
        MarkdownFileView.as_view(markdown_file="apps/report_2021/report.md"),
        name="report_whos_missing",
    )
]
