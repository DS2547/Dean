FILE_NAME = 'bit_transactions_2025.csv'
import pandas as pd


def main():
    df = pd.read_csv(FILE_NAME)
    only_credit = df.query("`Credit/Debit` != 'Debit'")  # drop the Debit from the file
    drop_withdrawal_to_bank_account = only_credit.query(
        "`Payment Method` != 'Bank Account'")  # drop the withdrawal to bank account
    drop_declined_deal = drop_withdrawal_to_bank_account.query("Status != 'You declined'")  # only Completed deals
    sum_money_paid = drop_declined_deal.groupby('From/To')[
        'Amount'].sum().reset_index()  # sum the amount by every person
    highest_payer = sum_money_paid.sort_values(by='Amount', ascending=False).head(1)  # give the highest
    print(highest_payer.to_string())


if __name__ == '__main__':
    main()
