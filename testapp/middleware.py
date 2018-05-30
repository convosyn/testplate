class Testmiddle(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
       return self.get_response(request)
    
    def parseIt(self, level = "INFO", message = "Default Message"):
        print("[{!s}]: {!s}".format(level, message))

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('-------------testing middleware-----------------')
        self.parseIt(message = request.META)
        self.parseIt(message = view_func)
        self.parseIt(message = view_args)
        self.parseIt(message = view_kwargs)
        return None
