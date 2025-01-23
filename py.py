children = [12, 14, 15, 12, 13]

total_sum = 0

length = 0

for child in children:

    total_sum += child  # Corrected this line to add the value of 'child'
    
    length += 1

# Calculate average and print results
average = total_sum / length if length > 0 else 0
print("The total sum of the children is: " + str(total_sum) + " and the total average is: " + str(average))
