from import_shims.warn import warn_deprecated_import

warn_deprecated_import('lti_provider.management.commands', 'lms.djangoapps.lti_provider.management.commands')

from lms.djangoapps.lti_provider.management.commands import *
