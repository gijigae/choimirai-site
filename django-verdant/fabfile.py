from __future__ import with_statement
from fabric.api import *

import uuid

env.roledefs = {
    'staging': ['django-staging.torchbox.com'],

    'squid': ['root@rca1.dh.bytemark.co.uk'],
    'db': ['root@rca1.dh.bytemark.co.uk'],
    # All hosts will be listed here.
    'production': ['root@rca2.dh.bytemark.co.uk', 'root@rca3.dh.bytemark.co.uk'],
}
MIGRATION_SERVER = 'rca2.dh.bytemark.co.uk'

@roles('staging')
def deploy_staging():
    with cd('/usr/local/django/verdant-rca/'):
        with settings(sudo_user='verdant-rca'):
            sudo("git pull")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/pip install -r django-verdant/requirements.txt")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py syncdb --settings=verdant.settings.staging --noinput")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py migrate --settings=verdant.settings.staging --noinput")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py collectstatic --settings=verdant.settings.staging --noinput")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py compress --settings=verdant.settings.staging")

        sudo("supervisorctl restart verdant-rca")
        sudo("supervisorctl restart rca-celeryd")
        sudo("supervisorctl restart rca-celerybeat")

        with settings(sudo_user='verdant-rca'):
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py update_index --settings=verdant.settings.staging")

@roles('staging')
def deploy_staging_wagtailsep():
    """Perform the second step of wagtail separation (docs) on staging"""
    with cd('/usr/local/django/verdant-rca/'):
        with settings(sudo_user='verdant-rca'):
            sudo("git pull")
            sudo("psql -Uverdant_rca verdant_rca -f django-verdant/rca/separation_scripts/wagtailsearch.sql")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py collectstatic --settings=verdant.settings.staging --noinput")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py compress --settings=verdant.settings.staging")

        sudo("supervisorctl restart verdant-rca")
        sudo("supervisorctl restart rca-celeryd")
        sudo("supervisorctl restart rca-celerybeat")

        with settings(sudo_user='verdant-rca'):
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py update_index --settings=verdant.settings.staging")


@roles('production')
def deploy():
    with cd('/usr/local/django/verdant-rca/'):
        with settings(sudo_user='verdant-rca'):
            sudo("git pull")
            sudo("/usr/local/django/virtualenvs/verdant-rca/bin/pip install -r django-verdant/requirements.txt")

            if env['host'] == MIGRATION_SERVER:
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py syncdb --settings=verdant.settings.production --noinput")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py migrate --settings=verdant.settings.production --noinput")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py collectstatic --settings=verdant.settings.production --noinput")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py compress --settings=verdant.settings.production")

            run("supervisorctl restart verdant-rca")
            run("supervisorctl restart rca-celeryd")
            if env['host'] == MIGRATION_SERVER:
                run("supervisorctl restart rca-celerybeat")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py update_index --settings=verdant.settings.production")

@roles('production')
def deploy_live_wagtailsep():
    """Perform the second step of wagtail separation (docs) on production. NB: DB updates (separation_scripts/wagtaildocs.sql) need to be done immediately beforehand"""
    with cd('/usr/local/django/verdant-rca/'):
        with settings(sudo_user='verdant-rca'):
            sudo("git pull")

            if env['host'] == MIGRATION_SERVER:
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py collectstatic --settings=verdant.settings.production --noinput")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py compress --settings=verdant.settings.production")

            run("supervisorctl restart verdant-rca")
            run("supervisorctl restart rca-celeryd")
            if env['host'] == MIGRATION_SERVER:
                run("supervisorctl restart rca-celerybeat")
                sudo("/usr/local/django/virtualenvs/verdant-rca/bin/python django-verdant/manage.py update_index --settings=verdant.settings.production")

@roles('squid')
def clear_cache():
    run('squidclient -p 80 -m PURGE http://www.rca.ac.uk')

@roles('db')
def fetch_live_data():
    filename = "verdant_rca_%s.sql" % uuid.uuid4()
    local_path = "/home/vagrant/verdant/%s" % filename
    remote_path = "/root/dumps/%s" % filename

    run('pg_dump -Upostgres -cf %s verdant_rca' % remote_path)
    run('gzip %s' % remote_path)
    get("%s.gz" % remote_path, "%s.gz" % local_path)
    run('rm %s.gz' % remote_path)
    local('dropdb -Upostgres verdant')
    local('createdb -Upostgres verdant')
    local('gunzip %s.gz' % local_path)
    local('psql -Upostgres verdant -f %s' % local_path)
    local ('rm %s' % local_path)
