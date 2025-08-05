"""
Prompt for devis 
"""


def convertisseur(texte:str)->str:
    """
    convertis le devis ecrit par l'humain en html
    """
    devis_formate = open("devis_f",mode="w+")
    
    with open(texte, 'r') as file:
        line = file.readlines()
        nb_line = len(line)

    print(line)

    for nb in range(nb_line):

        if (nb + 1) % 2 == 0:
            devis_formate.write('<div class="white-section">\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<p>\n\t\t\t'+str(line[nb])+'\t\t</p>\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n</div>\n')
        else: 
            devis_formate.write('<div class="yellow-section">\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<p>\n\t\t\t'+str(line[nb])+'\t\t</p>\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n\t<div class="row-devis">\n\t\t<input class="input-devis-facture" type="text">\n\t</div>\n</div>\n')
        

convertisseur("test.txt")


