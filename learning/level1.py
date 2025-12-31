'''
	•	Verwende dein Ergebnis (result)
	•	Wenn das Ergebnis größer als 5 ist → gib aus: Greater than 5
	•	Sonst → 5 or less

Regeln
	•	Verwende if / else
	•	Keine neuen Zahlen ausser 5
'''

'''
LEVEL 1 und 2
x = 5
y = 3
result = x + y
print(f"Die summe von x und y ist: {result}")

if result > 5:
    print("Greater than 5")
else:
    print("5 or less")
'''

'''
'Level 5'
nums = [3, 5, 9] 
limit = 4

def numfilter(numbers, lim):
    x = 0
    for n in numbers:
        if n > lim:
            x = x + n
    return x

result = numfilter(nums, limit)
print(result)
'''

'level 7'

'Ziel: Funktion die die grösste zahl aus einer liste zurückgibt ohn max() tool'
'''
numbers = [2, 8, 10, 3, 7]

def findMaxValue(nums):
    x = nums[0]
    for i in nums:
        if i > x:
            x = i
    return x

result = findMaxValue(numbers)
print(result)
'''

'''level 8 index pos der grössten zahl einer liste finden'
numbers = [2, 8, 10, 3, 7]

def IndexOfMaxNum(nums):
    x = nums[0]
    y = 0
    pos = 0
    for i in nums:
        if i > x:
            x = i
            pos = y
        y = y + 1
    return pos

result = IndexOfMaxNum(numbers)
print(result)
'''


'''
'level 9 zweitgrössten wer mit funktion finden'

numbers = [2, 8, 10, 3, 7]



def findSecondMaxValue(nums):
    x = nums[0]                     #Startwert und fortlaufend grösste zahl
    y = nums[0]                     #Startwert und fortlaufend zweitgrösste zahl
    for i in nums:
        if i > x:
            y = x
            x = i
        elif i > y and i < x:
            y = i
    return y

result = findSecondMaxValue(numbers)
print(f"The second largest number in the list is: {result}.") 
'''

'''
# Level 10 Frequency counter, zählen wie oft jedes element vorkommt

nums = [2, 2, 8, 10, 3, 7, 7, 7]

# TODO Input nimmt liste und wandelt alle zahlen in eine counts
# Idee: Prüfen ob die Zahl schon im counts ist, wenn ja dann count +1 und wenn nein dann neuen index erstellen

def FreqCounter(nums):
    FreqDict = {}
    for i in nums:
        if i in FreqDict:
            x = FreqDict[i]
            FreqDict[i] = x + 1
        else:
            FreqDict[i] = 1
    return FreqDict


def MostFrequent(count):
    x = 0
    y = 0
    for i in count:
            if count[i] > x:
                x = count[i]
                y = i
    return y

result = FreqCounter(nums)
maxCount = MostFrequent(result)
print(result)
print(maxCount)
'''
'''
#Level 11 texts zählen 

text = "hello world"

def CharCounter(text):
    counts = {}
    for i in text:
        if i in counts:
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
    return counts

result = CharCounter(text)
print(result)
'''

'''
#Level 12: Wörter Zählen

text = "hello world hello python world"

def wordCounter(text):
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

result = wordCounter(text)
print(result)
'''

# Level 13: Datei lesen -> Wörter zählen

def wordCounterFromFile(path):
    counts = {}
    # Read File
    with open(path) as f:
        text = f.read()
    # text -> wörter umwandeln
    words = text.split()
    # Zählen
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

result = wordCounterFromFile("learning/text.txt")
print(result)
