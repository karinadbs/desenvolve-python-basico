def validar_cpf(cpf_str):
    cpf = cpf_str.replace('.', '').replace('-', '')

    if not (cpf.isdigit() and len(cpf) == 11):
        return "Inválido"

    cpf_base = cpf[:9]
    digitos_verificadores = cpf[9:]

    soma1 = sum(int(d) * f for d, f in zip(cpf_base, range(10, 1, -1)))
    resto1 = soma1 % 11
    digito1 = '0' if resto1 < 2 else str(11 - resto1)

    cpf_com_digito1 = cpf_base + digito1
    soma2 = sum(int(d) * f for d, f in zip(cpf_com_digito1, range(11, 1, -1)))
    resto2 = soma2 % 11
    digito2 = '0' if resto2 < 2 else str(11 - resto2)

    if digito1 + digito2 == digitos_verificadores:
        return "Válido"
    else:
        return "Inválido"

cpf_input = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_input)
print(resultado)