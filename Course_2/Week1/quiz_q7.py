#
# demystify
#

def demystify(str):
    str = str.replace('l', 'a')
    str = str.replace('1', 'b')
    return str

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))