"""tree1 = float(input("Enter the tree1 value:"))
tree2 = float(input("Enter the tree2 value:"))
tree3 = float(input("Enter the tree3 value:"))
tree4 = float(input("Enter the tree4 value:"))
tree5 = float(input("Enter the tree5 value:"))
tree6 = float(input("Enter the tree6 value:"))
tree7 = float(input("Enter the tree7 value:"))
tree8 = float(input("Enter the tree8 value:"))

sum = tree1 + tree2 + tree3 + tree4 + tree5 + tree6 + tree7 + tree8 
print("The sum of the trees is:", sum)

average =sum/8
print("The average of the trees is:", average)

amount = int(input("Enter amount:"))
notes_of_200 = amount//200
remaining_after_200 = amount%200

notes_of_100 = remaining_after_200//100
remaining_after_100 = remaining_after_200%100

notes_of_50 = remaining_after_100//50
remaining_after_50 = remaining_after_100%50

notes_of_20 = remaining_after_50//20
remaining_after_20 = remaining_after_50%20

notes_of_10 = remaining_after_20//10
remaining_after_10 = remaining_after_20%10

notes_of_5 = remaining_after_10//5
remaining_after_5 = remaining_after_10%5

print("Notes of 200 are",notes_of_200)
print("Notes of 100 are",notes_of_100)
print("Notes of 50 are",notes_of_50)
print("Notes of 20 are",notes_of_20)
print("Notes of 10 are",notes_of_10)
print("Notes of 5 are",notes_of_5)"""


math = int(input("Enter the number: "))
english = int(input("Enter the number: "))
bgs = int(input("Enter the number: "))
science = int(input("Enter the number: "))
bangla =  int(input("Enter the number: "))
religion = int(input("Enter the number: "))
ict = int(input("Enter the number: "))
agriculture = int(input("Enter the number: "))

sum = math + english + bgs + science + bangla + religion + ict + agriculture
percentage = (sum*100)/800
print("The average percentage of all subject is: ",percentage)