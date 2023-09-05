def main():

    num_males = float(input('Enter number of males: '))
    num_females = float(input('Enter number of females: '))

    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    total = num_males + num_females
    m_perc = total - num_males 
    f_perc = total - num_females 

    print(f'Total number of students: {total}')
    print(f"Total male students: {num_males} Total female students: {num_females}")
    print(f"Percentage of male students: \t {m_perc:.2f} Percentage of female students: \t {f_perc:.2f}")


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
