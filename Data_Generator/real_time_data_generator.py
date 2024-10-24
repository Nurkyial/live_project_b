import time
import project_classes as clas
import project_gen_functions as fun

max_clients_per_iteration = 10
max_logins_per_client = 10
max_activities_per_login = 50

max_normal_logins_per_client = 2
max_normal_activities_per_login = 10
sleep_time = 60


while True:
    clients_per_iteration = fun.random.randint(0, max_clients_per_iteration)
    data_logins = []
    data_activities = []
    data_transactions = []
    data_payments = []

    for _ in range(clients_per_iteration):
        client_id = fun.random.randint(1, 10000)
        client = clas.Client(client_id)
        logins_per_iteration = fun.probability_value(max_normal_logins_per_client, max_logins_per_client, 0.9)
        for _ in range(fun.random.randint(1, logins_per_iteration)):
            login = clas.Login(client_id)
            client.add_login(login)
            activities_per_login = fun.probability_value(max_normal_activities_per_login, max_activities_per_login, 0.9)
            for _ in range(fun.random.randint(1, activities_per_login)):
                activity = clas.Activity(login)
                client.add_activity(activity)
                if activity.activity_type in ['transfer_funds', 'pay_bill']:
                    transaction = clas.Transaction(activity)
                    payment = clas.Payment(transaction)
                    client.add_transaction(transaction)
                    client.add_payment(payment)
        
        client.generate_anomalous_data()
        
        for _ in client.logins:
            data_logins.append(_.login_data_to_dict())

        for _ in client.activities:
            data_activities.append(_.activity_data_to_dict())

        for _ in client.transactions:
            data_transactions.append(_.transaction_data_to_dict())
        
        for _ in client.payments:
            data_payments.append(_.payment_data_to_dict())

    timestamp = fun.datetime.now().strftime("%Y%m%d_%H%M%S")

    folder_name = fun.create_folder_if_not_exists('real_time_data')

    # dataframe for clients logins
    data_df = fun.pd.DataFrame(data_logins)
    data_df.to_csv(f'{folder_name}/clients_logins_{timestamp}.csv', index=False)

    # dataframe for clients activities
    data_df = fun.pd.DataFrame(data_activities)
    data_df.to_csv(f'{folder_name}/clients_activities_{timestamp}.csv', index=False)

    # dataframe for clients transactions
    data_df = fun.pd.DataFrame(data_transactions)
    data_df.to_csv(f'{folder_name}/clients_transactions_{timestamp}.csv', index=False)

    # dataframe for clients payments
    data_df = fun.pd.DataFrame(data_payments)
    data_df.to_csv(f'{folder_name}/clients_payments_{timestamp}.csv', index=False)

    time.sleep(sleep_time)
    # break
