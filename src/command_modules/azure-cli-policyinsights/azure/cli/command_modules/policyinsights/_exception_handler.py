# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import CLIError

def policy_insights_exception_handler(ex):
    from azure.mgmt.policyinsights.models import QueryFailureException

    if isinstance(ex, QueryFailureException):
        message = '({}) {}'.format(ex.error.error.code, ex.error.error.message)
        raise CLIError(message)
    else:
        import sys
        from six import reraise

        reraise(*sys.exc_info())
