from transaction import *

def input_manager(lines):
    
    transaction_obj = Transaction()
    for line in lines:
        inputs = line.strip().split(" ")

        if inputs[0] == "EXPENSE":
            paid_by = inputs[1]
            total_amount_paid = int(inputs[2])
            no_of_users_involved = int(inputs[3])
            user_involved = []
            exact_amount = []
            percentage = []

            for i in range(no_of_users_involved):
                if paid_by != inputs[i+4]:
                    user_involved.append(inputs[i+4])
            
            next_input_index = 4 + no_of_users_involved
            type_of_expense = inputs[next_input_index]
            next_input_index += 1

            if type_of_expense == "EXACT":
                for i in range(no_of_users_involved):
                   exact = int(inputs[next_input_index + i])
                   exact_amount.append(exact)
            
            if type_of_expense == "PERCENT":
                for i in range(no_of_users_involved):
                   percent_for_user = int(inputs[next_input_index + i])
                   percentage.append(percent_for_user)
        
            transaction_obj.create_expenses(paid_by=paid_by,
                                            amount= total_amount_paid,
                                            type_of_transaction= type_of_expense,
                                            no_of_users_involved= no_of_users_involved,
                                            user_involved= user_involved,
                                            exact_amount= exact_amount,
                                            percentage= percentage)
        elif inputs[0] == "SHOW":
            if len(inputs) > 1:
                user_to_show = inputs[1]
                transaction_obj.get_user_specific_transactions_details(user_to_show)
            else:
                transaction_obj.get_all_transaction_details()
            




        



        