class CategoryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        category_param = request.GET.get('category')
        if category_param:
            from Store.models import Category  # make sure it's safe
            # Handle direct category name
            if not category_param.isdigit():
                category_obj = Category.objects.filter(Name__icontains=category_param).first()
                if category_obj:
                    request.session['selected_category'] = category_obj.Name
                else:
                    request.session.pop('selected_category', None)
            else:
                # handle by id if digit
                category_obj = Category.objects.filter(id=category_param).first()
                if category_obj:
                    request.session['selected_category'] = category_obj.Name
        elif 'category' in request.GET:
            request.session.pop('selected_category', None)

        return self.get_response(request)

