from t_converter import converter



assert converter('30C') == (86, 'F', '86F')
assert converter('30C') == (86, 'F', '86F')
assert converter('12C') == (54, 'F', '54F')
assert converter('0F') == (-18, 'C', '-18C')
try:
    assert converter('10')
except ValueError:
    pass

#another realization

def ass_test():
    c = converter
    assert c('30C') == (86, 'F', '86F')
    assert c('30C') == (86, 'F', '86F')
    assert c('12C') == (54, 'F', '54F')
    assert c('0F') == (-18, 'C', '-18C')


ass_test()