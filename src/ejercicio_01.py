def sumar(a, b):
    # En Python, bool es subclase de int, por lo que se valida explícitamente
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Ambos argumentos deben ser estrictamente numéricos (int o float)")
    return a + b
