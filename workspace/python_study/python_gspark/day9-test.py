import sys
print(-sys.maxsize)

from decimal import getcontext, Decimal
getcontext().prec =1
print(Decimal(0.1)+Decimal(0.2))


