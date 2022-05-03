AAPLChange = float(input("Enter percentage change of $AAPL"))
SPX_Volatility = float(input("Enter the volatility of the S&P (0 for weak | 0.5 for normal |  1 for strong)"))
NDAQ_Volatility = float(input("Enter the volatility of the NASDAQ (0 for weak | 0.5 for normal | 1 for strong)"))
SPX_weight = 0.75
NDAQ_weight = 0.65

SPX_anticipated = round((AAPLChange * SPX_weight) + (0.5 * SPX_Volatility), 2) 
NDAQ_anticipated = round((AAPLChange * NDAQ_weight) + (0.75 * NDAQ_Volatility), 2) 

SPX_lev_up = round(SPX_anticipated * 3, 2)
SPX_lev_down = round(SPX_anticipated * 2.8, 2)
NDAQ_lev_up = round(NDAQ_anticipated * 3.2, 2)
NDAQ_lev_down = round(NDAQ_anticipated * 3, 2)

if (AAPLChange > 0):
    #AAPL percentage change on the day is positive.
    print("AAPL is up {0}%, here is the estimated gains contributed:".format(AAPLChange)) 
    print('''
    {0}% from the S&P.
    {1}% from the NASDAQ.
    {2}% from the leveraged LONG S&P index.
    {3}% from the leveraged LONG NASDAQ index.
    '''.format(SPX_anticipated, NDAQ_anticipated, SPX_lev_up, NDAQ_lev_up))

elif (AAPLChange < 0):
    #AAPL percentage change on the day is negative.
    print("AAPL is down {0}%, here is the estimated gains contributed:".format(AAPLChange)) 
    print('''
    {0}% from the S&P.
    {1}% from the NASDAQ.
    {2}% from the leveraged SHORT S&P index.
    {3}% from the leveraged SHORT NASDAQ index.
    '''.format(abs(SPX_anticipated), abs(NDAQ_anticipated), abs(SPX_lev_down), abs(NDAQ_lev_down)))
