from behave import given, when, then
from common.database_management_class.db_mamagement import BrowserDBManager
from common.common_configs.db_queries import *


@given('I connect to the "{db_name}" database')
def connect_to_db(context, db_name):
    context.connect_to_db = BrowserDBManager(dbs_place, db_name)


@when('I run "{query}" query against "{db}"')
def run_delete_query_against_db(context, query, db):
    context.connect_to_db.delete_query_trigger(select_db_queries(query, db))


@then('the "{db}" should be empty')
def delete_table_entries(context, db):
    query = select_db_queries('check_if_empty', db)
    check_if_empty = context.connect_to_db.select_query_trigger(query)
    if check_if_empty[0][0] == 0:
        print("{0} is empty".format(db))
    else:
        raise Exception("{0} is not empty!".format(db))
