
miLista = ["Los lunes son los mejores días para programar", 
           "Python es moderno", 
           "Veremos Inteligencia Artificial más adelante",
           "Lambda simplifica el código"]


miLista.sort(key=lambda m:len(m.split()))

print (miLista)