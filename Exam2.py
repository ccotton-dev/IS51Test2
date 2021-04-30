""" PSEUDOCODE 
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