from django.shortcuts import redirect

def auth_middleware(get_response):
    def middleware(request):
        customer = request.session.get('customer')
        print(f"Customer session: {customer}")
        return_url = request.META.get('PATH_INFO', '/')  # PATH_INFO se aapne kis url pe visit kiya...
        print(f"Requested URL: {return_url}")
        if not customer:
            return redirect(f'/login?return_url={return_url}')
        response = get_response(request)
        return response

    return middleware
