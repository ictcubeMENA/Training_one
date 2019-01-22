def seats_in_theater(tot_cols, tot_rows, col, row):
    cols = (tot_cols - col + 1)
    rows = (tot_rows - row)
    return(cols * rows)





def seats_in_theater2(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)