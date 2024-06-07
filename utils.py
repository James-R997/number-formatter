
def prettify(num: str) -> str :

    num: str = str(num)
    num: str = num[::-1]

    result: list[str] = []
    counter: int = 0

    for digit in num:

        counter += 1
        result.append(digit)

        if counter == 3 :
            counter = 0
            result.append(",")

    result: str = "".join(result)
    result: str = result[::-1]

    return result