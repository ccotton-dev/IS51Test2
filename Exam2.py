"""Plain English

start 
define function to calculate what percentage of grades lie above the average
    initialize counter and percentage 
    create a loop that iterates through the Final.txt file  
    add 1 to counter that tracks how many grades exist above the average value of the grades
    divide the count of grades above the average by the total number of grades and multiply by 100
    after this number is found, round the number to two decimal places to return the final answer

define a function that calculates the average grade 
    add all of the numbers in the file up and divide by how many grades exist in the file

define main and open the text file to read 
append all of the grades in the file into a list 
call the function that calculates the average grade to determine the avgerage grade

print out values that state the number of grades total, the average grade, and what percentage of grades
lie above the average value
use sep to remove the space between the number and the percentage sign 

call main and execute all of the defined functions in the proper order and print to the user 
the total number of grades, the average grade, and the percentage of grades above average 
end
"""

""" PSUDOCODE 
define calculate_percentage_above_average(avg, grades)
    counter = 0
    create a float percent = 0.0
    for i in grades: 
        if float(i) > avg:
            increment counter by one if above average counter = counter + 1
    solve for the percent = counter/len(grades) * 100
    return the rounded decimal with round(percent, 2)

define average_grade(grades) 
    find value of all grades added, add = sum(grades) 
    set an integer for the length of the file, length = len(grades)
    solve for the average grade, avg = add / length  
    return avg

define main() 
    open the Final.txt file and set a_file equal to it
    define an empty list, grades = [] 
    run a for loop for all values in the file,for i in a_file:
        append the values in the file to a list, grades.append(int(i))
    avg = average_grade(grades)
    print("Number of grades:", len(grades))
    print("Average grade:", avg)
    print("Percentage of grades above average: ", calculate_percentage_above_average(avg, grades)) 
    close the file 

if __name__ == "__main__"
    main()
"""

# Code for sorting grades

def calculate_percentage_above_average(avg, grades):
    counter = 0
    percent = 0.0
    for i in grades:
        if float(i) > avg:
            counter = counter+1
    percent = counter/len(grades) * 100
    return round(percent,2)

def average_grade(grades):
    add = sum(grades)
    length = len(grades)
    avg = add / length
    return avg

def main():
    a_file = open("/Users/CCott_000/Desktop/Spring2021/Test2/Final.txt", "r")
    grades = []
    for i in a_file:
        grades.append(int(i))
    avg = average_grade(grades)
    print("Number of grades:", len(grades))
    print("Average grade:", avg)
    print("Percentage of grades above average: ", calculate_percentage_above_average(avg, grades), "%", sep='')
    
    ##print(a_file.read())
    a_file.close()

if __name__ == "__main__":
    main()
