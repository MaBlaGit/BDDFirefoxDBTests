
from common.database_management_class.db_mamagement import BrowserDBManager
from common.common_configs.db_queries import *
from common.common_steps.common_behave_steps import *


@when('I run "{find_website_name}" - {query} against "{table}" table in "{db}" database')
def run_query_against_db(context, find_website_name, query, table, db):
    context.check_db = BrowserDBManager(dbs_place, db)
    context.element = context.check_db.select_query_trigger(select_db_queries(
        find_website_name, table, website_url.get(query)))


@then('the {url} web page address should be in the table')
def check_if_entry_exists_in_db(context, url):
    print(context.element)
    if context.element[0][0] == website_url.get(url):
        print('Entry in the DB')
        del context.element
    else:
        raise Exception('Entry not in DB')
