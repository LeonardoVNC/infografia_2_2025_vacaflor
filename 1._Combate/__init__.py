from .ViewModel.Ring import Ring
from .View.Console import Console

ring = Ring()
cons = Console()

cons.cls()
print("Inicio del programa\n")
ring.standReady()