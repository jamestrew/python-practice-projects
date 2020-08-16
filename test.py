
big_query = "INSERT INTO post (user_id, post_text) VALUES "
for _ in range(10):
    big_query += "(1, 'test text'), "
big_query = big_query.strip(', ') + ';'

print(big_query)
