def format_numbers(phone_number: str) -> str:
    return '+7({0}{1}{2}){3}{4}{5}-{6}{7}-{8}{9}'.format(*[i for i in phone_number if i.isdigit()][1:])