from DiceParser import DiceParser
import sys
from DiceParser import DiceExpression

dp = DiceParser()
dp.parse(sys.argv[1])
print(dp.getDescription())