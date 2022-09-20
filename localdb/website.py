def check_login(request):
    userid = request.session.get('mobile', None)
    if userid == None:
        return "Redirect to Login Page"
