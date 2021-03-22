"""
We have a text containing a poem, that is a sequence of verses with rhymes.
The poem is stored in a text file, one verse per line.

We want to analyze the poem to extract its prosodic structure, i.e. the repetition scheme of the poem.

To this aim we need the following definitions:
    - a 'sound element' (SE) is a maximal sequence of 1 or more consonants followed by 1 or more vowels: 
        - first all the consonants
        - then all the vowels (aeioujy)
        - all non-alphabetic chars like spaces, numbers, colon, comma etc. must be ignored
        - all accents from accented letters (e.g. è->e) must be removed
        - differences between uppercase and lowercase letters are disregarded
        NOTICE: the only exceptions are the first and the last SE of a verse, that could contain only vowels
                and only consonants, respectively.
    - a verse is made of a sequence of sound elements, the last of which is called 'final'
        Example:      
        If the verse is "Donàld Duck! wènt, to tHe seas'ìde to swim" 
            - the SEs are           [ 'do', 'na', 'lddu', 'ckwe', 'ntto', 'the', 'sea', 'si', 'de', 'to', 'swi', 'm' ]
            - the final SE is       'm'
            - the verse length is   12
        notice that accents have been removed, letters are lowercase and non-alphabetic chars are ignored.
    - the prosodic structure of the poem is a list of numbers, one for each verse
    - the prosodic structure is obtained considering both the number of SE (#SE) and the final SE of the verses 
    - the first verse is associated with the number 0
    - each one of the following verses are associated:
        - with the same number associated to an earlier verse having the same #SE and final SE
        - or with a new number, obtained adding 1 to the greatest number, already used
    - the period of the verses is the minimum number of verses that repeats with the same schema.

    Example:
        If the poem is the text here below                  its sound elements are                                      #SE final   prosody
        '''
        Dì pestaggio tessessi allarmai, Partenopea!         di pe sta ggio te sse ssia lla rmai pa rte no pea           13  pea         0
        Sembrò svieremo imbarcate, aumentarono usurpai?     se mbro svie re moi mba rca teau me nta ro nou su rpai      14  rpai        1
        Flash privé spirereste? Pentecoste deturpai         fla shpri ve spi re re ste pe nte co ste de tu rpai         14  rpai        1
        scrost, direttamante arrischiai,                    scro stdi re tta ma ntea rri schiai                          8  schiai      2
        odi attuazione vernicera Partenopea.                o dia ttua zio ne ve rni ce ra pa rte no pea                13  pea         0
        Psion trentacinque preesistiti calzascarpe          psio ntre nta ci nque pree si sti ti ca lza sca rpe         13  rpe         3
        nobilt fiacchi vedesti avvertirsi spermatozoi?      no bi ltfia cchi ve de stia vve rti rsi spe rma to zoi      14  zoi         4
        Igloo rubi incassando giurati spermatozoi!          i gloo ru bii nca ssa ndo giu ra ti spe rma to zoi          14  zoi         4
        Saprai reputasse inebriai                           sa prai re pu ta ssei ne briai                               8  briai       5
        man l'ballaste segnaleremo soprascarpe.             ma nlba lla ste se gna le re mo so pra sca rpe              13  rpe         3
        '''
        the list of #SE is              [13,    14,     14,     8,        13,    13,    14,    14,    8,       13   ]
        the list of final SE is         ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe']
        thus the prosodic structure is  [0,     1,      1,      2,        0,     3,     4,     4,     5,       3    ]

        From the prosodic structure you should find the period, i.e. the minimum length of verses that repeats with the same schema.
        In this example the period is 5, in facts the prosody is obtained by repeating twice the [0, 1, 1, 2, 0] schema,
            since the sequence [0, 1, 1, 2, 0] has the same schema of [3, 4, 4, 5, 3]

You have to define a function that analyzes the prosody of a poem stored in a file and returns a tuple with four elements, namely:
    - a list with the prosodic structure of the poem
    - an integer representing the period of the verses
    - a list with the number of Sound Elements (#SE) of each verse
    - a list with the final SE of each verses

    From the above example, the function should return the tuple
          ( [0, 1, 1, 2, 0, 3, 4, 4, 5, 3], 5, [13, 14, 14, 8, 13, 13, 14, 14, 8, 13 ], 
            ['pea', 'rpai', 'rpai', 'schiai', 'pea', 'rpe', 'zoi', 'zoi', 'briai', 'rpe'])

    NOTICE: you cannot use other libraries or open other files.
    TIMEOUT: The timeout for each test is 100ms (0.1 seconds)
"""

def ex1(poem_filename):
    def remove_schar(filename):
    with open(filename, encoding = 'utf-8') as f:
        string = f.read()
    s_char = {228: 97,225: 97,224: 97, 226: 97,227: 97,229: 97,
               235: 101,233: 101,232: 101,234: 101,283: 101,
               239: 105,237: 105,236: 105,238: 105,
               246: 111,243: 111,337: 111,242: 111,244: 111,245: 111,248: 111,
               252: 117, 250: 117,369: 117,249: 117,251: 117,
               255: 121, 253: 121,
               192: 97, 193: 97,194: 97,195: 97,196: 97,197: 97,
               200: 101,201: 101,202: 101,203: 101, 204: 105,205: 105,206: 105,207: 105,
               210: 111,211: 111,212: 111,213: 111,214: 111,216: 111,
               217: 117,218: 117,219: 117,220: 117,221: 121,376: 121,
               65: 97,66: 98,67: 99,68: 100,69: 101, 70: 102,71: 103,72: 104,73: 105,
               74: 106,75: 107,76: 108,77: 109,78: 110,79: 111,80: 112,81: 113,
               82: 114,84: 116,83: 115,85: 117,86: 118,87: 119,88: 120,
               89: 121,90: 122,
               32: '', 33:'', 34:'', 39:'', 44:'', 46:'', 58:'', 59:'', 63:'',
               48:'',49:'',50:'',51:'',52:'',53:'',54:'',55:'',56:'',57:'' ,9:''}
    #[' ', '!', '"', "'", ',', '.', ':', ';', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\t']
    #s_char = str.maketrans('äáàâãåëéèêěïíìîöóőòôõøüúűùûÿýÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖØÙÚÛÜÝŸABCDEFGHIJKLMNOPQRTSUVWXYZ',
    #                      'aaaaaaeeeeeiiiiooooooouuuuuyyaaaaaaeeeeiiiioooooouuuuyyabcdefghijklmnopqrtsuvwxyz')
    #the above dictionary is a translate map with every forbidden character and the equivalent translation
    string = string.translate(s_char)
    return string.split('\n')[:-1]


def prosody_list(escount, finali):
    tuples = list(zip(escount,finali))
    dic = {tupla: i for i,tupla in enumerate(list(dict.fromkeys(tuples)))}
    prosodia = [dic[tupla] for tupla in tuples]
    return prosodia


def divisors(prosodia):
    n = len(prosodia)
    lista = [len(prosodia)]
    for i in range(2, int(n ** 0.5 + 1)):   
        if n % i == 0:
            lista.extend([i, n//i])
    lista = set(lista)
    if 2 in lista:
        lista.remove(2)
    return sorted(list(lista))


def period_calc(prosodia):
    lista = divisors(prosodia)
   
    for d in lista:
        lista1 = prosodia[:d]
        for i in range(1, len(prosodia)):
                listan = prosodia[d*i:d+d*i]
                if len(set(lista1)) != len(set(listan)) or len(set(zip(lista1,listan))) != len(set(lista1))::
                    break
                if d + d*i == len(prosodia):
                    return d
    return d


def ex1(poem_filename):
    lista = remove_schar(poem_filename)
    v_c = ''.maketrans('aeioujybcdfghklmnpqrstvwxz','vvvvvvvccccccccccccccccccc')
    finals = []
    lengths = []
    for verse in lista:
        versetrans = verse.translate(v_c)
        index_fin = versetrans.rfind('vc')
        finals.append(verse[index_fin +1:])
        lengths.append(len(versetrans.split('vc')))
    prosody = prosody_list(lengths,finals)
    period = period_calc(prosody)
    return (prosody,period,lengths,finals)

