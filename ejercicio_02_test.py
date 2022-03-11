import ejercicio_02

def test_calcular_3_horas(capsys):
  ejercicio_02.calcular_litros_por_hora(tiempo_de_ciclismo = 3)
  captured = capsys.readouterr()
  assert captured.out == "1.5\n"

def test_calcular_6_p_7_horas(capsys):
  ejercicio_02.calcular_litros_por_hora(tiempo_de_ciclismo = 6.7)
  captured = capsys.readouterr()
  assert captured.out == "3.35\n"


def test_calcular_11_p_8_horas(capsys):
  ejercicio_02.calcular_litros_por_hora(tiempo_de_ciclismo = 11.8)
  captured = capsys.readouterr()
  assert captured.out == "5.9\n"