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
    print(f'Total percentage of males: \t {m_perc:.2f}')
    print(f'Total percentage of females: \t {f_perc:.2f}')


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
