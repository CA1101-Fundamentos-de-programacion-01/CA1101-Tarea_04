
import ejercicio_01

def test_suma(capsys):
    ejercicio_01.suma(10,5)
    captured = capsys.readouterr()
    assert captured.out == "15\n"

def test_resta(capsys):
    ejercicio_01.resta(10,5)
    captured = capsys.readouterr()
    assert captured.out == "5\n"

def test_multiplicacion(capsys):
    ejercicio_01.multiplicacion(10,5)
    captured = capsys.readouterr()
    assert captured.out == "50\n"

def test_division(capsys):
    ejercicio_01.division(10,5)
    captured = capsys.readouterr()
    assert captured.out == "2.0\n"

def test_modulo(capsys):
    ejercicio_01.modulo(10,7)
    captured = capsys.readouterr()
    assert captured.out == "3\n"

def test_potencia(capsys):
    ejercicio_01.potencia(10,5)
    captured = capsys.readouterr()
    assert captured.out == "100000\n"

def test_division_entera(capsys):
    ejercicio_01.division_entera(10,7)
    captured = capsys.readouterr()
    assert captured.out == "1\n"
  