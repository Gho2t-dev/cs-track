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