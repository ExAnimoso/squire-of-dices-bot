import re
import random

DICE_DELIMETERS='[dDкК]'

class DiceParser:
    def __init__(self):
        self.expressions = []

    def getValue(self):
        total = 0
        for e in self.expressions:
            total += e.getValue()
        return total

    def parse(self, value):
        expressions = re.split('([+-])', value.replace(' ', ''))
        self.expressions.append(DiceExpression(expressions[0], True))
        for x in range(1, len(expressions), 2):
            positive = expressions[x] == '+'
            if re.search(DICE_DELIMETERS, expressions[x+1]):
                self.expressions.append(DiceExpression(expressions[x+1], positive))
            else:
                self.expressions.append(FlatExpression(expressions[x] + expressions[x+1]))

    def getDescription(self):
        return ("".join(map(self.mapExpression, self.expressions)) + '=' + str(self.getValue()))[1:]

    def mapExpression(self, expression):
        return expression.getDescription()


class DiceExpression:
    def __init__(self, value, positive):
        self.total=0
        self.original = value
        self.calculated = []
        self.positive = positive
        self.mode = 'STR'
        self.dTwentyMode = False

        diceValues = re.split(DICE_DELIMETERS, value)
        if len(diceValues) != 2:
            raise Exception
        if re.search('^1?[dDкК](20)?[!#]?$', value):
            self.dTwentyMode = True
            diceValues[0] = '1'
            diceValues[1] = '20'
            if value.endswith('!'):
                diceValues[0] = '2'
                self.mode = 'ADV'
            if value.endswith('#'):
                diceValues[0] = '2'
                self.mode = 'DIS'
        if diceValues[0] == '':
            diceValues[0] = '1'
        if diceValues[1] == '':
            diceValues[1] = '20'
        if (int(diceValues[0]) > 1000 or int(diceValues[1]) > 1000):
            raise Exception
        for x in range(0, int(diceValues[0])):
            currentRoll = random.randint(1, int(diceValues[1]))
            self.calculated.append(currentRoll)
            self.total += currentRoll

    def getValue(self):
        if self.mode == 'ADV':
            return max(self.calculated[0], self.calculated[1])
        if self.mode == 'DIS':
            return min(self.calculated[0], self.calculated[1])
        return self.total if self.positive else -self.total

    def getDescription(self):
        critIndicator = ''
        if self.dTwentyMode:
            if self.getValue() == 1:
                critIndicator = '☠️'
            if self.getValue() == 20:
                critIndicator = '🔥'
        return ('+' if self.positive else '-') + self.original + '(' + ",".join(map(str, self.calculated)) + ')' + critIndicator


class FlatExpression:
    def __init__(self, value):
        self.value = int(value)
        self.string = value
        if (self.value > 1000):
            raise Exception

    def getValue(self):
        return self.value

    def getDescription(self):
        return ('+' if self.value >= 0 else '') + str(self.value)
