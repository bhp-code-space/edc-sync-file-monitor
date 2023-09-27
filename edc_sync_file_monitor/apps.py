from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_sync_file_monitor'
    base_template_name = 'edc_base/base.html'
    project_name = 'EDC SYNC FILE MONITOR'
    institution = 'Botswana-Harvard AIDS Institute Partnership'

    protocol_sites = {
        'ESR21 Sites': 'esr21_site',
    }


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'EDC SYNC FILE MONITOR'
    institution = 'Botswana-Harvard AIDS Institute'
