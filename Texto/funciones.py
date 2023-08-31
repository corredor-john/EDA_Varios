def limpieza(objeto_df):
    contenido = objeto_df.content
    #Convertir textos a caracteres en minúsculas
    contenido = contenido.apply(lambda x: x.lower())
    #Remover HTML tags
    contenido = contenido.apply(lambda x: re.sub(r'\<[^<>]*\>','',x))
    #Remover cualquier caracter que no coincida con una letra, un digito o un guion bajo "_" 
    contenido = contenido.apply(lambda x: re.sub(r'^\W+|\W+$',' ',x))
    #Remover espacios, nueva linea, tabulador
    contenido = contenido.apply(lambda x: re.sub(r'\s',' ',x))
    #Remover puntuacion
    contenido = contenido.apply(lambda x: re.sub(r'[^a-zA-Z0-9]',' ',x))
    #Tokenizar los data (https://datapeaker.com/big-data/que-es-la-tokenizacion-metodos-para-realizar-la-tokenizacion/)
    contenido = contenido.apply(lambda x: word_tokenize(x))
    #Remover stopwords
    contenido = contenido.apply(lambda x: [i for i in x if i not in stops])
    return(content)

