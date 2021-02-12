# Visa plot-kommandon 'inline', behövs bara om ni jobbar i en Jupyter notebook och vill visa figurer som output när ni kör en cell
%matplotlib inline  


# Importera bibliotek
#_____________________________________
import matplotlib.pyplot as plt # Bibliotekt med funktioner för att göra plotar/figurer
import numpy as np  # Numerical python, funktioner för numeriska beräkningar

# Här kan ni importera fler bibliotek med andra funktioner om ni vill
# ...


# PARAMETRAR FÖR FIGURER
#______________________________________
# Nedanstående kod tillåter er att bestämma utseendet på era plottar 

# Uppdatera plt parametrar, textstorlek = fontsize
plt.rcParams["legend.fontsize"]=18  
plt.rcParams["xtick.labelsize"]=22 # textstorlek för ticksen(siffrorna) på x-axeln
plt.rcParams["ytick.labelsize"]=22 # textstorlek för ticksen(siffrorna) på y-axeln
plt.rcParams['lines.linewidth']=2.3 # tjocklek på linjer i plottar
plt.rcParams['lines.markersize']=8  # storlek på markers t.ex. prickar, som markerar datapunkten som plottas

# Om ni vill använda Latex i plottarna
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}',
                                r'\usepackage{helvet}',
                                r'\usepackage{sansmath}',
                                r'\sansmath',
                                r'''\newcommand{
                                \UG}[1]{\text{\unsansmath\ensuremath{#1}\sansmath}}'''
                                r'''\newcommand{
                                \angs}{\text{\normalfont\AA}}'''
                                ]

# Plot parametrar
params = {
"text.usetex": True,  # True == ja använd latex
"font.family": "sans-serif", # använd sans-serif font
"axes.labelsize": 24, # storlek på texten på figur axlarna
"font.size": 24,
'figure.figsize': (8,6) } # bredd och höjd i inches

plt.rcParams.update(params)  # Updatera så att alla valen ovan blir default


# FUNKTIONER
#______________________________________
# Här kan ni defininera funktioner som ni vill ha tillgängliga i hela scriptet
# Nedan finns två exempel på två funktioner som konverterar Celsius till Kelvin och tvärt om



def C_to_K(C):        # def funktion_namn(parameter in):
    K = C + 273.15    # gör något med in parametern, 
    return K          # returnera resultatet

def K_to_C(K):
    C = K  - 273.15
    return C













