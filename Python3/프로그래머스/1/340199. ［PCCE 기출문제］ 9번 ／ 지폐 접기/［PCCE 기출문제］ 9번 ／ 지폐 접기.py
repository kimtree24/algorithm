def solution(wallet, bill):
    bill_row = bill[0]
    bill_column = bill[1]
    count = 0
    while True:
        if wallet[0] >= bill_row and wallet[1] >= bill_column:
            return count
        if wallet[0] >= bill_column and wallet[1] >= bill_row:
            return count
        
        if bill_row >= bill_column:
            bill_row = bill_row // 2
            count += 1
        else:
            bill_column = bill_column // 2
            count += 1
        