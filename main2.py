amount = int(input("Enter amount need for withdraw:"))

#Number of notes
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

#Printing the notes
print("Number of note_1 =", note_1)
print("Number of note_2 =", note_2)
print("Number of note_3 =", note_3)