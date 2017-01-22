
import matplotlib.pyplot as plt

categoriesList = []
expensesList = []

print("        ------Visualizing Expenses------\n")
file = input("Enter filename if available, otherwise"
      " enter 0: ")
if file != "0":
    fileLines = []
    with open(file) as f:
        for line in f:
            fileLines.append(line)
    count = 0
    for i in fileLines:
        count += 1
        if count % 2 == 0:
            expensesList.append(float(i))
        else:
            categoriesList.append(i)
else:
    numCategories = int(input("\nEnter number of categories: "))
    print()
    for i1 in range(numCategories):
        category = input("Category: ")
        expenses = float(input("Expenses in %s: " % category))
        print()
        categoriesList.append(category)
        expensesList.append(expenses)

numBars = len(categoriesList)
positions = range(1, numBars+1)

plt.axis(xmax=max(expensesList)+1000)
plt.barh(positions, expensesList, align="center")
plt.title("Visualizing Expenses")
plt.yticks(positions, categoriesList)
plt.ylabel("Categories"); plt.xlabel("Amount (Euro)")


plt.show()
