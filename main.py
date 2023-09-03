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
    m_perc = total * num_males / 100
    f_perc = total * num_females / 100

    print(f'Total number of students: {total}')
    print(f"Total number of males: {num_males} Total number of females: {num_females}")
    print(f"Total number of males: \t {m_perc:.2f} Total number of females: \t {f_perc:.2f}")


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
