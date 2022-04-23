import re
def check_ip(arg):
    print('True' if re.match(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})(\.(?!$)|$)){4}", arg) else 'False')

     