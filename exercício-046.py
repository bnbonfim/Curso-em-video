from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fim {}'.format(emojize(':party_popper:')))
