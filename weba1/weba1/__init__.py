from __future__ import absolute_import, unicode_literals

try:
    # This makes Celery available when the dependency is installed,
    # but keeps Django startup working without Celery.
    from .celery_setup import app as celery_app

    celery_app.autodiscover_tasks(None, related_name='aniv')
    celery_app.autodiscover_tasks(None, related_name='import_lote_civ')
    __all__ = ('celery_app',)
except ImportError:
    __all__ = ()

efault_app_config = 'weba1.apps.Weba1Config'
# Permite usar PyMySQL como MySQLdb
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except Exception:
    pass
