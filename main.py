def main():

    male_students = int(input('Enter number of male students: '))
    female_students = int(input('Enter number of female students: '))

    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    total_students = male_students + female_students
    m_perc = male_students / total_students 
    f_perc = female_students / total_students 

    m_perc = float(m_perc) * 100
    f_perc = float(f_perc) * 100

    print(f"Total number of students: {total_students}")
    print(f"Total male students: {male_students} Total female students: {female_students}")
    print(f"Percentage of male students: \t {m_perc:.2f} Percentage of female students: \t {f_perc:.2f}")


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
