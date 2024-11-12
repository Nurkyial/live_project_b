CREATE OR REPLACE FUNCTION update_nulls_to_zero(table_name TEXT, column_names TEXT[])
RETURNS VOID AS $$
DECLARE
    column_name TEXT;
BEGIN
    FOREACH column_name IN ARRAY column_names
    LOOP
        EXECUTE format('UPDATE %I SET %I = 0 WHERE %I IS NULL', table_name, column_name, column_name);
    END LOOP;
END;
$$
 LANGUAGE plpgsql;

 -- Function for calculating maximum, minimum, average, median, mode of the given columns
CREATE OR REPLACE FUNCTION calculate_statistics(
	table_name TEXT, 
	column_name_agg TEXT, 
	transactionType_or_paymentMethod TEXT, 
	condition_value INT, 
	currency_column TEXT, 
	currency_condition INT,
	function_type TEXT,
	client_id INT
	)
RETURNS INT AS $$
DECLARE 
	-- results INTEGER[] := '{}';
	resultat INT;
	query TEXT;
BEGIN 
	IF function_type = 'MAX' THEN
		    query := ' SELECT ' ||  function_type || '(' || column_name_agg || ') 
			FROM ' || table_name ||			
			' WHERE ' ||  transactionType_or_paymentMethod || ' = $1 AND '
			|| currency_column || ' = $2 AND client_id = $3' 
			' GROUP BY client_id';
--			query := 'SELECT $7($2) FROM $1
--					  WHERE $3 = $4 
--					  AND $5 = $6 
--					  AND client_id = $8
--					  GROUP BY client_id';
--		EXECUTE query INTO resultat USING table_name, column_name_agg, transactionType_or_paymentMethod,  
--				 condition_value, currency_column, currency_condition, function_type, client_id;	
		EXECUTE query INTO resultat USING condition_value, currency_condition, client_id;
	END IF;
	RETURN resultat;
END;
$$
 LANGUAGE plpgsql;
DROP FUNCTION calculate_statistics;
SELECT client_id,  calculate_statistics(
	'transactions', 
	'amount',
	'transaction_type_id',
	1,
	'currency_id',
	1,
	'MAX',
	client_id)
FROM transactions
GROUP BY client_id
ORDER BY client_id;

SELECT amount FROM transactions
WHERE transaction_type_id = 1 AND currency_id = 1 AND client_id = 1
ORDER BY amount DESC
LIMIT 10;