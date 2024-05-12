
class Transaction:

    def __init__(self):
        self.transactions = {}
    
    def get_transactions(self):
        return self.transactions

    def get_user_expense_key(self, paid_by, need_to_pay):
        return paid_by+"_"+need_to_pay
    
    def settle_reverse_transaction(self, reverse_transaction_key, reverse_amount_to_settle, transactions):
        if reverse_transaction_key in transactions:
            amount_in_transaction = transactions[reverse_transaction_key]
            if amount_in_transaction >= reverse_amount_to_settle:
                amount_in_transaction -= reverse_amount_to_settle
                reverse_amount_to_settle = 0
                transactions[reverse_transaction_key] = amount_in_transaction
            else:
                reverse_amount_to_settle -= amount_in_transaction
                transactions[reverse_transaction_key] = 0

        return reverse_amount_to_settle

    def add_transaction(self, transaction_key, amount):
        if transaction_key not in self.transactions:
            self.transactions[transaction_key] = amount
        else:
            self.transactions[transaction_key] += amount

    def handle_transaction(self, paid_by, need_to_pay, per_user_amount):
        transaction_key = self.get_user_expense_key(paid_by= paid_by,
                                                            need_to_pay= need_to_pay)
        reverse_transaction_key = self.get_user_expense_key(paid_by= need_to_pay,
                                                            need_to_pay= paid_by)
        all_transactions = self.get_transactions()
        remaining_amount_to_settle = self.settle_reverse_transaction(reverse_transaction_key,
                                                                        reverse_amount_to_settle= per_user_amount,
                                                                        transactions= all_transactions)
        
        if remaining_amount_to_settle > 0:
            self.add_transaction(transaction_key, remaining_amount_to_settle)

    def create_expenses(self, 
                        paid_by, 
                        amount, 
                        type_of_transaction,
                        no_of_users_involved,
                        user_involved, 
                        exact_amount=[],
                        percentage= []):
        
        if type_of_transaction == "EQUAL":
            per_user_amount = amount/no_of_users_involved
        
            for user in user_involved:
                self.handle_transaction(paid_by= paid_by,
                                        need_to_pay= user,
                                        per_user_amount = per_user_amount)
                
        elif type_of_transaction == "EXACT":

            for user_index in range(len(user_involved)):
                user = user_involved[user_index]
                per_user_amount = exact_amount[user_index]
                self.handle_transaction(paid_by= paid_by,
                                        need_to_pay= user,
                                        per_user_amount= per_user_amount)
        else:
            for user_index in range(len(user_involved)):
                user = user_involved[user_index]
                user_amount_percentage = percentage[user_index]
                per_user_amount = (amount * user_amount_percentage) / 100
                self.handle_transaction(paid_by= paid_by,
                                        need_to_pay= user,
                                        per_user_amount= per_user_amount)
                
    def get_user_specific_transactions_details(self, user_id):
        
        all_transactions = self.get_transactions()
        unsettled_transaction_exists = False
        for transaction_key, amount in all_transactions.items():
            split_list = transaction_key.split("_")
            paid_by = split_list[0]
            need_to_pay = split_list[1]    
            if (paid_by == user_id or need_to_pay == user_id) and amount != 0:
                unsettled_transaction_exists = True
                print(f"{need_to_pay} owes {paid_by}: ", amount)
        if not unsettled_transaction_exists:
            print("No balances")
    
    def get_all_transaction_details(self):

        all_transactions = self.get_transactions()
        unsettled_transaction_exists = False
        for transaction_key, amount in all_transactions.items():
            split_list = transaction_key.split("_")
            paid_by = split_list[0]
            need_to_pay = split_list[1]    
            if amount != 0:
                unsettled_transaction_exists = True
                print(f"{need_to_pay} owes {paid_by}: ", amount)
        if not unsettled_transaction_exists:
            print("No balances")


                    

