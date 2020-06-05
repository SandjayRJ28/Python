# het importeren van modules in 3 verschillende manieren
# module import als namespace
import Helpers
Helpers.display("geen waarschuwing")

# Import alle funtie van een module in een keer
from Helpers import *
display("Geen waarschuwing")

# Een specifieke funtie uit een module importeren
from Helpers import display
display("Geen Waaarschuwing")

# Installeer inviduele software pakket
pip install colorama

# Installeer pakket van een lijst
pip install -r requirements.txt

# requirements.txt
colorama