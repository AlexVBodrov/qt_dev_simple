import sqlalchemy as sqal

DATABASE_NAME = 'sqlite:///sql_alchemy\db_example_1.db'

engine = sqal.create_engine(DATABASE_NAME)
connection = engine.connect()
metadata = sqal.MetaData()

products = sqal.Table('products', metadata,
                      sqal.Column('product_id', sqal.Integer, primary_key=True),
                      sqal.Column('product_name', sqal.Text),
                      sqal.Column('supplier_name', sqal.Text),
                      sqal.Column('price_per_tone', sqal.Integer)
)

metadata.create_all(engine)

# запрос на вставку
insertion_query = products.insert().values([
    {"product_name":"Banana", "supplier_name":"United Banana", "price_per_tone":7000},
    {"product_name":"Apples", "supplier_name":"United Banana", "price_per_tone":6000},
    {"product_name":"Abocado", "supplier_name":"United Abocados", "price_per_tone":12000},
    {"product_name":"Tomatos", "supplier_name":"United Tomatos", "price_per_tone":3100},
])

# connection.execute(insertion_query)


select_all_query = sqal.select([products])
# sql query
# print(select_all_query)

selcect_all_result = connection.execute(select_all_query)

print(selcect_all_result.fetchall()[2][3])

