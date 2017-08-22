
from common.database_management_class.db_mamagement import BrowserDBManager
from common.common_configs.db_queries import *
from common.common_steps.common_behave_steps import *


@when('I run "{select_query}" query against "{table}" table in "{db}" database')
def run_query_against_db(context, select_query, db, table):
    context.check_db = BrowserDBManager(dbs_place, db)
    context.element = context.check_db.select_query_trigger(select_db_queries(
        select_query, table, website_url['website']))


@then('the "{url}" should be in the table')
def check_if_entry_exists_in_db(context, url):
    if context.element[0][0] == website_url.get(url):
        print('Entry in the DB')
    else:
        raise Exception('Entry not in DB')
