import operator
import random
from datetime import datetime
# Instantiating the start time object
start_time = datetime.now()
# Code Workflow
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
# Sequential looping for 500 times for 2 numbers in the range 1-20
for i in range(500):
    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)
    op, fn = random.choice(operators)
    print("{} {} {} = {}".format(num_1, op, num_2, fn(num_1, num_2)))
# Instantiating the end time object
end_time = datetime.now()
print('Execution process duration is: {}'.format(end_time - start_time))

