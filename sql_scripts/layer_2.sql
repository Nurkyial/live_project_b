CREATE TABLE IF NOT EXISTS name (
	client_id INT,
    name TEXT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO name (client_id, name)
SELECT 
    client_id, client_name AS name
FROM
    ext_clients;
   
SELECT * FROM name;

-- email table
CREATE TABLE IF NOT EXISTS email (
	client_id INT,
    email TEXT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO email (client_id, email)
SELECT 
    client_id, client_email
FROM
    ext_clients;
   
SELECT * FROM email;

-- phone table
CREATE TABLE IF NOT EXISTS phone (
	client_id INT,
    phone TEXT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO phone (client_id, phone)
SELECT 
    client_id, client_phone
FROM
    ext_clients;
   
SELECT * FROM phone;

-- address table
CREATE TABLE IF NOT EXISTS address (
	client_id INT,
    address TEXT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO address (client_id, address)
SELECT 
    client_id, client_address
FROM
    ext_clients;
   
SELECT * FROM address;

-- logins table
CREATE TABLE IF NOT EXISTS logins (
	client_id INT,
    login_id SERIAL,
    login_date TIMESTAMP,
    ip_address TEXT,
    device TEXT,
    login_location TEXT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO logins (client_id, login_date, ip_address, device, login_location)
SELECT 
    client_id, login_date, ip_address, device, location
FROM
    ext_logins;
   
SELECT * FROM logins;


-- activities table
CREATE TABLE IF NOT EXISTS activities (
	client_id INT,
    activity_id SERIAL,
    activity_date TIMESTAMP,
    activity_location TEXT,
    ip_address TEXT,
    device TEXT,
    activity_type_id INT
)
WITH (
	appendoptimized = TRUE,
	orientation = column,
	compresstype = zstd,
	compresslevel = 1
)
DISTRIBUTED BY (client_id);

INSERT INTO activities (client_id, activity_date, activity_location, ip_address, device, activity_type_id)
SELECT 
    client_id, activity_date, activity_location, ip_address, device, 
    CASE activity_type
    	WHEN 'transfer_funds' THEN 1
    	WHEN 'view_account' THEN 2
    	WHEN 'pay_bill' THEN 3
    	WHEN 'chat_support' THEN 4
    	WHEN 'call_support' THEN 5
    END 
FROM
    ext_activities;
   
SELECT * FROM activities;

