# Author: Toshio Kuratomi <tkuratom@redhat.com>
# License: GPLv3+
# Copyright: Ansible Project, 2020
"""Parse documentation from ansible plugins using anible-doc."""

import os
import typing as t


#: Clear Ansible environment variables that set paths where plugins could be found.
ANSIBLE_PATH_ENVIRON: t.Dict[str, str] = os.environ.copy()
ANSIBLE_PATH_ENVIRON.update({'ANSIBLE_COLLECTIONS_PATH': '/dev/null',
                             'ANSIBLE_ACTION_PLUGINS': '/dev/null',
                             'ANSIBLE_CACHE_PLUGINS': '/dev/null',
                             'ANSIBLE_CALLBACK_PLUGINS': '/dev/null',
                             'ANSIBLE_CLICONF_PLUGINS': '/dev/null',
                             'ANSIBLE_CONNECTION_PLUGINS': '/dev/null',
                             'ANSIBLE_FILTER_PLUGINS': '/dev/null',
                             'ANSIBLE_HTTPAPI_PLUGINS': '/dev/null',
                             'ANSIBLE_INVENTORY_PLUGINS': '/dev/null',
                             'ANSIBLE_LOOKUP_PLUGINS': '/dev/null',
                             'ANSIBLE_LIBRARY': '/dev/null',
                             'ANSIBLE_MODULE_UTILS': '/dev/null',
                             'ANSIBLE_NETCONF_PLUGINS': '/dev/null',
                             'ANSIBLE_ROLES_PATH': '/dev/null',
                             'ANSIBLE_STRATEGY_PLUGINS': '/dev/null',
                             'ANSIBLE_TERMINAL_PLUGINS': '/dev/null',
                             'ANSIBLE_TEST_PLUGINS': '/dev/null',
                             'ANSIBLE_VARS_PLUGINS': '/dev/null',
                             'ANSIBLE_DOC_FRAGMENT_PLUGINS': '/dev/null',
                             })
try:
    del ANSIBLE_PATH_ENVIRON['PYTHONPATH']
except KeyError:
    # We just wanted to make sure there was no PYTHONPATH set...
    # all python libs will come from the venv
    pass
try:
    del ANSIBLE_PATH_ENVIRON['ANSIBLE_COLLECTIONS_PATHS']
except KeyError:
    # ANSIBLE_COLLECTIONS_PATHS is the deprecated name replaced by
    # ANSIBLE_COLLECTIONS_PATH
    pass


class ParsingError(Exception):
    """Error raised while parsing plugins for documentation."""


def _get_environment(collection_dir: t.Optional[str]) -> t.Dict[str, str]:
    env = ANSIBLE_PATH_ENVIRON.copy()
    if collection_dir is not None:
        env['ANSIBLE_COLLECTIONS_PATH'] = collection_dir
    else:
        # Copy ANSIBLE_COLLECTIONS_PATH and ANSIBLE_COLLECTIONS_PATHS from the
        # original environment.
        for env_var in ('ANSIBLE_COLLECTIONS_PATH', 'ANSIBLE_COLLECTIONS_PATHS'):
            try:
                del env[env_var]
            except KeyError:
                pass
            if env_var in os.environ:
                env[env_var] = os.environ[env_var]
    return env


class AnsibleCollectionDocs:
    # A nested directory structure that looks like:
    #    plugin_type:
    #        plugin_name:  # Includes namespace and collection.
    #            {information from ansible-doc --json.  See the ansible-doc documentation for more
    #             info.}
    plugins: t.Mapping[str, t.Mapping[str, t.Any]]

    # Maps collection name to collection version
    collection_versions: t.Mapping[str, str]

    def __init__(self,
                 plugins: t.Mapping[str, t.Mapping[str, t.Any]],
                 collection_versions: t.Mapping[str, str]):
        self.plugins = plugins
        self.collection_versions = collection_versions
