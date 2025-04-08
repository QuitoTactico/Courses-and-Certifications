from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook

from elasticsearch import Elasticsearch

"""
Connection Id: elastic_default
Connection type: HTTP
Host: elastic # nombre del servicio en docker
Login: airflow
Password: airflow
Port: 9200
"""

class ElasticHook(BaseHook):

    def __init__(self, conn_id='elastic_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        conn = self.get_connection(conn_id)

        conn_config = {}
        hosts = []

        if conn.host:
            hosts = conn.host.split(',')
        if conn.port:
            # conn_config['port'] = int(conn.port) # deprecated
            hosts = [{"host": host, "port": int(conn.port), "scheme": "http"} for host in hosts]
        if conn.login:
            conn_config['http_auth'] = (conn.login, conn.password)

        print('Hosts:', hosts)

        # hosts debe terminar siendo algo tipo [{"host": "127.0.0.1", "port": 9200}]
        self.es = Elasticsearch(hosts, **conn_config)
        self.index = conn.schema

    def info(self):
        return self.es.info()

    def set_index(self, index):
        self.index = index

    def add_doc(self, index, doc_type, doc):
        self.set_index(index)
        res = self.es.index(index=index, doc_type=doc_type, doc=doc)
        return res

class AirflowElasticPlugin(AirflowPlugin):
    name = 'elastic'
    hooks = [ElasticHook]