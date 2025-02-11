# def is_palindrome(string: str, _i: int = None, _j: int = None) -> bool:
#     if _i is None:
#         _i = 0
#     if _j is None:
#         _j = len(string) - 1
#     if _i >= _j:
#         return True
#     if string[_i] != string[_j]:
#         return False
#     else:
#         return is_palindrome(string, _i + 1, _j - 1)

def is_palindrome(s: str):
    if len(s) <= 1:
        return True
    i_pos = None
    j_pos = None
    for i in range(len(s)):
        if s[i].isalnum():
            i_pos = i
            break
    for j in range(-1, -len(s), -1):
        if s[j].isalnum():
            j_pos = j
            break
    if s[i_pos].lower() != s[j_pos].lower():
        return False
    return is_palindrome(s[i_pos+1:j_pos])


if __name__ == "__main__":
    print(is_palindrome("ABCDCBA"))  # TRUE
    print(is_palindrome("TAKE U FORWARD"))  # FALSE
