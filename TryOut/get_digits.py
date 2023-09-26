import re


def get_just_digits(src_data: str) -> tuple[int, str] | None:
    src_data = src_data.strip()
    print(f"'{src_data}'")
    digit_pattern = re.compile(r"^\d+")
    result = digit_pattern.match(src_data)
    print(result)
    if result:
        number: int = int(src_data[result.span()[0]:result.span()[1]])
        text: str = src_data[result.span()[1]:].strip()
        return number, text
    return None
s = " 1  пролет (3 фазы) "
a = get_just_digits(s)
print(a)