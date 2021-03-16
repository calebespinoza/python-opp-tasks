from machine import Machine

m = Machine()
m.register_entrance(12345, "1:39:00")
m.register_entrance(12346, "14:02:55")
m.register_entrance(12347, "00:58:37")
print(m.payment(12346, "15:33:48"))
print(m.payment(12345, "2:00:05"))
print(m.payment(55555, "15:33:48"))
#print(m.print_car_id())
