import ejercicio_03

def test_I(capsys):
  ejercicio_03.repetir_cadena(3, "I")
  captured = capsys.readouterr()
  assert captured.out == "III\n"

def test_Hola(capsys):
  ejercicio_03.repetir_cadena(5, "Hola")
  captured = capsys.readouterr()
  assert captured.out == "HolaHolaHolaHolaHola\n"