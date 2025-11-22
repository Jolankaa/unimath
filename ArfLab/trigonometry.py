pi = 3.141592653589793
two_pi = 2 * pi
half_pi = pi / 2

def _normalize_to_0_2pi(x):
    # x mod 2π, sonucu [0, 2π)
    r = x - int(x // two_pi) * two_pi
    if r < 0:
        r += two_pi
    return r

def _sin_taylor(x, eps=1e-15, max_iter=50):
    term = x  # ilk terim
    s = term
    n = 1
    while n < max_iter:
        term *= -x * x / ((2*n) * (2*n + 1))
        s += term
        if abs(term) < eps:
            break
        n += 1
    return s

def _cos_taylor(x, eps=1e-15, max_iter=50):
    # x küçük (|x| <= pi/2) için cos'u Taylor serisi ile hesapla
    term = 1.0
    s = term
    n = 1
    while n < max_iter:
        term *= -x * x / ((2*n-1) * (2*n))
        s += term
        if abs(term) < eps:
            break
        n += 1
    return s

def sin(x):
    """Sinüs (x radyan)."""
    x = _normalize_to_0_2pi(x)
    # quadrant 0..3
    q = int(x // half_pi)  # 0,1,2,3
    theta = x - q * half_pi  # theta in [0, π/2)
    if q == 0:
        return _sin_taylor(theta)
    elif q == 1:
        return _cos_taylor(theta)
    elif q == 2:
        return -_sin_taylor(theta)
    else:  # q == 3
        return -_cos_taylor(theta)

def cos(x):
    """Kosinüs (x radyan)."""
    x = _normalize_to_0_2pi(x)
    q = int(x // half_pi)
    theta = x - q * half_pi
    if q == 0:
        return _cos_taylor(theta)
    elif q == 1:
        return -_sin_taylor(theta)
    elif q == 2:
        return -_cos_taylor(theta)
    else:  # q == 3
        return _sin_taylor(theta)

def tan(x):
    """Tanjant (x radyan). Cos(x) çok küçükse ZeroDivisionError fırlatır."""
    c = cos(x)
    if abs(c) < 1e-15:
        raise ZeroDivisionError("tan: cos(x) ≈ 0, tan tanımsız.")
    return sin(x) / c

def csc(x):
    s = sin(x)
    if abs(s) < 1e-15:
        raise ZeroDivisionError("csc: sin(x) ≈ 0, csc tanımsız.")
    return 1.0 / s

def sec(x):
    c = cos(x)
    if abs(c) < 1e-15:
        raise ZeroDivisionError("sec: cos(x) ≈ 0, sec tanımsız.")
    return 1.0 / c

def cot(x):
    s = sin(x)
    if abs(s) < 1e-15:
        raise ZeroDivisionError("cot: sin(x) ≈ 0, cot tanımsız.")
    return cos(x) / s

def radian_to_degree(radian):
    return (radian*180)/pi