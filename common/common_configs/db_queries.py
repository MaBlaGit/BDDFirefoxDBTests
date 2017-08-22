
"""DB queries used.
dbs_places - path to folder where browser dbs are stored."""

dbs_place = '/tmp/'


def select_db_queries(select, db_name, item):
    """Function definition which store db queries.
    :param select(str) - key which retrieve db query
    :param db_name(str) - name of database
    :param item(str) - searching target
    :return (str) - database query"""

    db_queries = {
        'select_all': 'SELECT * FROM {0};'.format(db_name),
        'check_if_empty': 'SELECT COUNT(*) FROM {0};'.format(db_name),
        'delete_all': 'DELETE FROM {0};'.format(db_name),
        'find_website_name': 'SELECT url FROM {0} WHERE url="{1}"'.format(db_name, item)
    }
    return db_queries.get('{0}'.format(select))
