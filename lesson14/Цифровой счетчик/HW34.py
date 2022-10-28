class Counter():

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value
       self.max_max = 0
       self.min_min = 0

   def set_current(self, start):
       self.current = start


   def set_max(self, max_max):
        self.max_max = max_max

   def set_min(self, min_min):
       self.min_min = min_min

   def step_up(self):
       if self.current >= self.max_max:
           raise ValueError("Достигнут максимум")
       self.current += 1

   def step_down(self):
       if self.current <= self.min_min:
           raise ValueError("Достигнут минимум")
       self.current-=1

   def get_current(self):
       return self.current

counter = Counter()
counter.set_max(10)
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())  # 10

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
print(counter.get_current())  # 10


counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())  # 7
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
print(counter.get_current())  # 7
