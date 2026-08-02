def hotes_utilisables(prefixe):
    return (2 ** (32 - prefixe)-2)


for prefixe in range (24,31):
    print (prefixe,"->",hotes_utilisables(prefixe))
   