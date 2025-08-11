# context_processors.py
def selected_category_context(request):
    return {
        'selected_category': request.session.get('selected_category', None)
    }

