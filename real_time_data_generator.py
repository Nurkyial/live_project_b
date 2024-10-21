import project_classes as clas
import project_gen_functions as fun


max_logins_per_client = 10
max_activities_per_login = 10
sleep_time = 60

while True:
    client_id = fun.random.randint(1, 1000)
    client = clas.Client(client_id)
    for _ in range(fun.random.randint(1, max_logins_per_client)):
        login = clas.Login(client_id)
        client.add_login(login)
        for _ in range(fun.random.randint(1, max_activities_per_login)):
            activity = clas.Activity(login)
            client.add_activity(activity)
            if activity.activity_type in ['transfer_funds', 'pay_bill']:
                transaction = clas.Transaction(activity)
                payment = clas.Payment(transaction)
                client.add_transaction(transaction)
                client.add_payment(payment)
    timestamp = fun.datetime.now().strftime("%Y%m%d_%H%M%S")
    data_logins = []
    for _ in client.logins:
        data_logins.append(_.login_data_to_dict())
    login_df = fun.pd.DataFrame(data_logins)
    login_df.to_csv(f'client_logins_{timestamp}.csv', index=False)
    client.generate_anomalous_data()
    break

for _ in client.payments:
    print(_.payment_data_to_dict())
for _ in client.transactions:
    print(_.transaction_data_to_dict())
