def main():

    num_males = int(input('Enter number of males: '))
    num_females = int(input('Enter number of females: '))

    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    total = num_males + num_females
    m_perc = total / (float)[num_males]
    f_perc = total / (float)[num_females]

    print(f'Total: {total}')
    print(f"Total number of males: \t {m_perc:.2f} Total number of females: \t {f_perc:.2f}")



    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
