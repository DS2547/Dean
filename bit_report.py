import pandas as pd

FILE_NAME = 'bit_transactions_2025.csv'


def drop_value_from_file(file_name: str, name_of_column: str, value_of_column: str):
    return file_name.query(f"`{name_of_column}` != '{value_of_column}'")


def sum_column_by_another_column(file_name: str, name_of_column: str, name_of_column_sum: str):
    return file_name.groupby(name_of_column)[name_of_column_sum].sum().reset_index()


def sort_and_highest(file_name: str, name_of_column: str, asc_or_desc: bool):
    return file_name.sort_values(by=name_of_column, ascending=asc_or_desc).head(1)


def main():
    df = pd.read_csv(FILE_NAME)
    only_credit = drop_value_from_file(df, 'Credit/Debit', 'Debit')
    drop_withdrawal_to_bank_account = drop_value_from_file(only_credit, 'Payment Method', 'Bank Account')
    drop_declined_deal = drop_value_from_file(drop_withdrawal_to_bank_account, 'Status', 'You declined')
    sum_money_paid = sum_column_by_another_column(drop_declined_deal, 'From/To', 'Amount')
    highest_payer = sort_and_highest(sum_money_paid, 'Amount', False)
    print(highest_payer.to_string())


if __name__ == '__main__':
    main()
