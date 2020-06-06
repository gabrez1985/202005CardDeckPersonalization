from PIL import Image, ImageOps, ImageColor
import os
from ColorFunctionsV02 import *

basewidth = 300
baseheight = int(basewidth * 1.52)
sizefactornum = 1.0  # factor de 0 a 1 en donde 1.0 es el mismo tamano original para el numero
sizepercent = (200, 200)  # tamano para la imagen ubicada en el centro
sizeperesq = (40, 40)  # tamano para la imagen cuando se ubica en las esquinas

distlatalcentro = 35
distbordesup = 3
distseparador = 2

bordersizecard = 10
bordersizepercent = 5
bordesizeperesq = 2

for fileimagenpersonalizado in os.listdir("InputImages"):

    for fileimagennumero in os.listdir("NumberImages"):
        
        imagenpercent = Image.open("InputImages/" + fileimagenpersonalizado)
        imagenpercent.thumbnail(sizepercent)
        anchopercent, largopercent = imagenpercent.size
        coordinate = x, y = int(anchopercent/2), int(largopercent/2)
        color = imagenpercent.getpixel(coordinate)
        colorborde = (color[0], color[1], color[2], 250)
        colorfondo = (color[0], color[1], color[2], 230)
        imagenpercent = ImageOps.expand(imagenpercent, border=bordersizepercent, fill= colorborde)

        imagenbase = create_image(basewidth, baseheight, color = colorfondo)
        anchobase, largobase = imagenbase.size

        imagenperesq = Image.open("InputImages/" + fileimagenpersonalizado)
        imagenperesq.thumbnail(sizeperesq)
        imagenperesq = ImageOps.expand(imagenperesq, border=bordesizeperesq, fill= colorborde)
        anchoperesq, largoperesq = imagenperesq.size

        imagennum = Image.open("NumberImages/" + fileimagennumero)
        imagennum = cambiarcolorfondo(imagennum, color = colorfondo)
        anchonum, largonum = imagennum.size
        imagennum.thumbnail((sizefactornum * anchonum, sizefactornum * largonum))
        
        anchonum, largonum = imagennum.size

        posinicialnumsupizq = (distlatalcentro - int(anchonum / 2), distbordesup)
        posfinalnumsupizq = (distlatalcentro - int(anchonum / 2) + anchonum, distbordesup + largonum)

        posinicialnuminfder = (anchobase - distlatalcentro - int(anchonum/2), largobase - distbordesup - largonum)
        posfinalnuminfder = (anchobase - distlatalcentro - int(anchonum/2) + anchonum, largobase - distbordesup)

        posinicialpersupizq = (distlatalcentro - int(anchoperesq / 2), distbordesup + largonum + distseparador)
        posfinalpersupizq = (distlatalcentro - int(anchoperesq / 2) + anchoperesq, distbordesup + largonum + distseparador + largoperesq)

        posinicialperinfder = (anchobase - distlatalcentro - int(anchoperesq/2), largobase - distbordesup - largonum - distseparador - largoperesq)
        posfinalperinfder = (anchobase - distlatalcentro - int(anchoperesq/2) + anchoperesq, largobase - distbordesup - largonum - distseparador)

        posinicialpercentro = (int((anchobase - anchopercent)/2),
                               int((largobase - largopercent)/2))
        posfinalpercentro = (int((anchobase - anchopercent)/2 + anchopercent),
                             int((largobase - largopercent)/2 + largopercent))

        imagenbase.paste(imagenpercent,
                         (posinicialpercentro[0], posinicialpercentro[1],
                          posfinalpercentro[0] + 2 * bordersizepercent, posfinalpercentro[1] + 2 * bordersizepercent))

        imagenbase.paste(imagennum,
                         (posinicialnumsupizq[0], posinicialnumsupizq[1],
                          posfinalnumsupizq[0], posfinalnumsupizq[1]))

        imagenbase.paste(imagennum.rotate(180),
                         (posinicialnuminfder[0], posinicialnuminfder[1],
                          posfinalnuminfder[0], posfinalnuminfder[1]))

        imagenbase.paste(imagenperesq,
                         (posinicialpersupizq[0], posinicialpersupizq[1],
                          posfinalpersupizq[0], posfinalpersupizq[1]))

        imagenbase.paste(imagenperesq.rotate(180),
                         (posinicialperinfder[0], posinicialperinfder[1],
                          posfinalperinfder[0], posfinalperinfder[1]))

        # el if de abajo da el color del pixel central a todas las imagenes menos las
        # indicadas especificamente en el if, se pueden agregar mas imagenes agregando elif

        imagenbase = ImageOps.expand(imagenbase, border=bordersizecard, fill=colorborde)

        nombrefile = os.path.splitext(fileimagenpersonalizado)[0] + os.path.splitext(fileimagennumero)[0]

        imagenbase.save("OutputDeck/" + nombrefile + ".png")
