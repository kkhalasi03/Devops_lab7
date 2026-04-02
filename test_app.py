from app import add, subtract, multiply, divide
def test_add():
  assert add(2, 3) == 5
  assert add(5, 3) == 8
def test_subtract():
  assert subtract(5, 3) == 2
  assert subtract(0, 0) == 0
def test_multiply():
   assert multiply(4, 3) == 12
   assert multiply(12, 12) == 144
def test_divide():
   assert divide(10, 2) == 5
   assert divide(10, 0) == 1