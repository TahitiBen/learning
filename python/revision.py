def est_valide(prefixe):
    return prefixe >= 0 and prefixe <= 32

prefixe = int(input('Ecrivez un nombre entre 0 et 32: '))

if est_valide(prefixe):
    print('Valide')

else:
    print('Invalide')
