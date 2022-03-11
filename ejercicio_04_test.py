import ejercicio_04

def test_sumatoria_con_3(capsys):
  ejercicio_04.suma_del_saltamontes(2)
  captured = capsys.readouterr()
  assert captured.out == "3\n"

def test_sumatoria_con_8(capsys):
  ejercicio_04.suma_del_saltamontes(8)
  captured = capsys.readouterr()
  assert captured.out == "36\n"