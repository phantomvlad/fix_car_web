from django.utils.html import format_html

def thumbnails(model):
    return format_html(f'<img src="{model.image.url}" height=283px width=283px>')
