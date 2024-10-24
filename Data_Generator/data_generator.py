import project_gen_functions as fun
import project_classes as clas


num_clients = 10000
max_logins_per_client = 100
max_activities_per_login = 100


for client_id in range(1, num_clients + 1):
    num_logins = fun.random.randint(1, max_logins_per_client)
    data_logins = []
    data_activities = []
    data_transactions = []
    data_payments = []
    data_calls_support = []
    client_data = []

    client = clas.Client(client_id)
    client_data.append(client.client_data_to_dict())

    for _ in range(num_logins):
        num_activities = fun.random.randint(1, max_activities_per_login)
        login = clas.Login(client_id)
        client.add_login(login)
        for _ in range(num_activities):
            activity = clas.Activity(login)
            client.add_activity(activity)
            if activity.activity_type in ['transfer_funds', 'pay_bill']:
                transaction = clas.Transaction(activity)
                payment = clas.Payment(transaction)
                client.add_transaction(transaction)
                client.add_payment(payment)
            if activity.activity_type == 'call_support':
                call_support = clas.CallSupport(activity)
                client.add_call_support(call_support)

    client.generate_anomalous_data()

    for _ in client.logins:
        data_logins.append(_.login_data_to_dict())

    for _ in client.activities:
        data_activities.append(_.activity_data_to_dict())

    for _ in client.transactions:
        data_transactions.append(_.transaction_data_to_dict())

    for _ in client.payments:
        data_payments.append(_.payment_data_to_dict())

    for _ in client.calls_support:
        data_calls_support.append(_.call_support_data_to_dict())

    folder_name = fun.create_folder_if_not_exists('data')

    # dataframe for clients logins
    data_df = fun.pd.DataFrame(data_logins)
    file_path = f'{folder_name}/clients_logins.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)

    # dataframe for clients activities
    data_df = fun.pd.DataFrame(data_activities)
    file_path = f'{folder_name}/clients_activities.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)

    # dataframe for clients transactions
    data_df = fun.pd.DataFrame(data_transactions)
    file_path = f'{folder_name}/clients_transactions.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)

    # dataframe for clients payments
    data_df = fun.pd.DataFrame(data_payments)
    file_path = f'{folder_name}/clients_payments.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)

    # dataframe for clients calls_support
    data_df = fun.pd.DataFrame(data_calls_support)
    file_path = f'{folder_name}/clients_calls_support.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)

    # dataframe for clients data
    data_df = fun.pd.DataFrame(client_data)
    file_path = f'{folder_name}/clients.csv'
    data_df.to_csv(file_path, mode='a', header=not fun.os.path.exists(file_path), index=False)
