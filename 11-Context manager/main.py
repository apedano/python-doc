class ContextManager:
    def __enter__(self, *args, **kwargs):
        print("--enter--")

    def __exit__(self, *args):
        print("--exit--")

with ContextManager():
    print("test")
#--enter--
#test
#--exit--