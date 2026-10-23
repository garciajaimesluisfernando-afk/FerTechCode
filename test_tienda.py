# ❌ Nivel Junior: Usar Print() mil veces
# ✅ Nivel Pro: usar pytest

from tienda import aplicar_descuento

def test_descuento_basico():
    # 100 con 20% de descuento TIENE que dar 80
    assert aplicar_descuento(100,20) == 80