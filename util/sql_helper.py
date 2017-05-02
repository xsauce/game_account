# -*- coding: utf-8 -*-
import MySQLdb
import threading
import tornado.log
from MySQLdb.cursors import DictCursor
import settings

# def transactional(func):
#     @functools.wraps(func)
#     def _wrapper(*args, **kw):
#         with transaction_context:
#             return func(*args, **kw)
#     return _wrapper
from util.pt_tornado_logging import PTTornadoLogger

__all__ = ["SqlHelper", "transaction_context"]


# class __ConnectionManager(threading.local):
#     def __init__(self):
#         self._db_conf = {}
#         self._conn_container = {}
#
#     def _get_conn(self, db_name):
#         if self._conn_container.get(db_name) is None:
#             self._conn_container[db_name] = StandaloneConnection(self._db_conf[db_name]).get_connection()
#         return self._conn_container[db_name]
#
#     def register_db(self, db_name):
#         if db_name not in self._db_conf:
#             self._db_conf[db_name] = settings.DATABASES[db_name]
#
#     def get_cursor(self, db_name, dict_result=False):
#         if dict_result:
#             return self._get_conn(db_name).cursor(cursorclass=DictCursor)
#         else:
#             return self._get_conn(db_name).cursor()
#
#     def close_conn(self, db_name):
#         if self._conn_container.get(db_name) is not None and (not transaction_context.is_in_transaction(db_name)):
#             if self._is_connection_open(db_name):
#                 self._conn_container[db_name].close()
#             self._conn_container[db_name] = None
#
#     def commit(self, db_name):
#         if self._conn_container.get(db_name) is not None:
#             self._conn_container[db_name].commit()
#
#     def rollback(self, db_name):
#         if self._conn_container.get(db_name) is not None:
#             self._conn_container[db_name].rollback()
#
#     def _is_connection_open(self, db_name):
#         if self._conn_container.get(db_name) is not None:
#             try:
#                 self._conn_container[db_name].ping()
#                 return True
#             except:
#                 return False
#
#     def __del__(self):
#         for i in self._conn_container.keys():
#             self.close_conn(i)
#         self._db_conf = None
#         self._conn_container = None


class TransactionContext(threading.local):
    def __init__(self, db_settings):
        self._db_conn = None
        self._transaction_count = 0
        self._db_settings = db_settings

    def get_cursor(self, dict_result=False):
        if dict_result:
            return self._db_conn.cursor(cursorclass=DictCursor)
        else:
            return self._db_conn.cursor()

    def set_db_conf(self, db_settings):
        self._db_settings = db_settings

    def __enter__(self):
        if self._transaction_count == 0:
            self._db_conn = StandaloneConnection(db_conf=self._db_settings).get_connection()
        self._transaction_count += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._transaction_count -= 1
        if self._transaction_count == 0:
            try:
                if exc_type is None:
                    self._db_conn.commit()
                else:
                    # traceback.print_exception(exc_type, exc_val, exc_tb)
                    self._db_conn.rollback()
            finally:
                self._db_conn.close()
                self._db_conn = None


class SqlHelper(object):
    '''
    db_conf sample:
    {
        "NAME": "pt_db_python",
        "HOST": "127.0.0.1",
        "USER": "work",
        "PASSWORD": "pwd",
        "PORT": 3306,
        "TYPE": "mysql"
    }
    '''

    def __init__(self, logger=None):
        self.logger = logger or PTTornadoLogger()
        # self._db_conf = db_conf
        # transaction_context.set_db_conf(db_conf)
        # pass
        # connection_manager.register_db(db)
        # self.db = db

    def _execute(self, sql, args, dict_result_bool=False, is_many_bool=False):
        if args is not None:
            assert isinstance(args, tuple) or isinstance(args, list)
        cur = transaction_context.get_cursor(dict_result=dict_result_bool)
        if not is_many_bool:
            affected_row_count_int = cur.execute(sql, args)
        else:
            affected_row_count_int = cur.executemany(sql, args)
        warns = filter(lambda m: m[0] == MySQLdb.Warning, cur.messages)
        if len(warns) > 0:
            warns_message = ';'.join([w[1][2] for w in warns])
            raise MySQLdb.MySQLError(warns_message)
        return affected_row_count_int, cur

    def query_one(self, sql, val_tuple=None, dict_result_bool=True):
        with transaction_context:
            affected_row_count_int, cur = self._execute(sql, val_tuple, dict_result_bool=dict_result_bool)
            rs = cur.fetchone()
            return rs

    def query_all(self, sql, val_tuple=None, dict_result_bool=True):
        with transaction_context:
            affected_row_count_int, cur = self._execute(sql, val_tuple, dict_result_bool=dict_result_bool)
            rs = cur.fetchall()
            return rs

    def execute(self, sql, val_tuple=None):
        with transaction_context:
            affected_row_count_int, cur = self._execute(sql, val_tuple)
            return affected_row_count_int

    def execute_many(self, sql, val_tuple_list):
        with transaction_context:
            affected_row_count_int, cur = self._execute(sql, val_tuple_list, is_many_bool=True)
            return affected_row_count_int

    def insert(self, sql, val_tuple=None):
        with transaction_context:
            affected_row_count_int, cur = self._execute(sql, val_tuple)
            return affected_row_count_int, cur.lastrowid

    # def close_conn(self):
    #     transaction_context.close_conn()


def import_db_lib(type):
    if type == 'mysql':
        return MySQLdb
    elif type == 'mssql':
        import pymssql
        return pymssql


class StandaloneConnection(object):
    def __init__(self, db_conf):
        self._db_conf = db_conf

    def get_connection(self):
        if self._db_conf['TYPE'] == 'mysql':
            return MySQLdb.connect(
                self._db_conf['HOST'],
                self._db_conf['USER'],
                self._db_conf['PASSWORD'],
                self._db_conf['NAME'],
                self._db_conf['PORT'],
                charset='utf8'
            )
        else:
            raise Exception('unsupport database type:%s' % self._db_conf['TYPE'])


class SqlPool(object):
    def __init__(self, db_conf, maxcached=10, maxshared=10, maxconnections=0):
        '''
        Constructor
        '''
        self.conn = None
        self.maxcached = maxcached
        self.maxshared = maxshared
        self.maxconnections = maxconnections
        from DBUtils.PooledDB import PooledDB
        self.conn_pool = PooledDB(import_db_lib(db_conf['TYPE']),
                                  maxcached=self.maxcached,
                                  maxshared=self.maxshared,
                                  maxconnections=self.maxconnections,
                                  host=db_conf['HOST'],
                                  port=db_conf['PORT'],
                                  user=db_conf['USER'],
                                  passwd=db_conf['PASSWORD'],
                                  db=db_conf['NAME'],
                                  charset="utf8")

    def get_connection(self):
        try:
            return self.conn_pool.connection()
        except Exception as e:
            print e
            raise Exception("failed to connect database")

    def close(self):
        self.conn_pool.close()

# single instance
# connection_manager = __ConnectionManager()
transaction_context = TransactionContext(settings.DATABASES['game_account'])




