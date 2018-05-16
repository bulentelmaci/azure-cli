# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import (
    resource_group_name_type, get_resource_group_completion_list,
    get_three_state_flag)

from azure.cli.command_modules.resource._completers import (
    get_policy_set_completion_list, get_policy_completion_list,
    get_policy_assignment_completion_list)

def load_arguments(self, _):
    with self.argument_context('policy event') as c:
        c.argument(
            'management_group_name',
            options_list=('--management-group-name', '-mg'),
            help='Management group name.')
        c.argument(
            'subscription_id',
            options_list=('--subscription-id', '-s'),
            help='Subscription id.')
        c.argument(
            'resource_group_name',
            options_list=('--resource-group-name', '-rg'),
            arg_type=resource_group_name_type,
            completer=get_resource_group_completion_list,
            help='Resource group name.')
        c.argument(
            'resource_id',
            options_list=('--resource-id', '-r'),
            help='Resource id.')
        c.argument(
            'policy_set_definition_name',
            options_list=('--policy-set-definition-name', '-ps'),
            completer=get_policy_set_completion_list,
            help='Policy set definition name.')
        c.argument(
            'policy_definition_name',
            options_list=('--policy-definition-name', '-pd'),
            completer=get_policy_completion_list,
            help='Policy definition name.')
        c.argument(
            'policy_assignment_name',
            options_list=('--policy-assignment-name', '-pa'),
            completer=get_policy_assignment_completion_list,
            help='Policy assignment name.')
        c.argument(
            'from_value',
            options_list=('--from', '-from'),
            help='Timestamp specifying the start time of the interval to query.')
        c.argument(
            'to_value',
            options_list=('--to', '-to'),
            help='Timestamp specifying the end time of the interval to query.')
        c.argument(
            'top_value',
            options_list=('--top', '-top'),
            type=int,
            help='Maximum number of records to return.')
        c.argument(
            'order_by_clause',
            options_list=('--order-by', '-ob'),
            help='Ordering expression using OData notation.')
        c.argument(
            'select_clause',
            options_list=('--select', '-sl'),
            help='Select expression using OData notation.')
        c.argument(
            'filter_clause',
            options_list=('--filter', '-f'),
            help='Filter expression using OData notation.')
        c.argument(
            'apply_clause',
            options_list=('--apply', '-a'),
            help='Apply expression for aggregations using OData notation.')

    with self.argument_context('policy state') as c:
        c.argument(
            'all_results',
            options_list=('--all', '-all'),
            arg_type=get_three_state_flag(),
            help='Within the specified time interval, get all policy states instead of the latest only.')
        c.argument(
            'management_group_name',
            options_list=('--management-group-name', '-mg'),
            help='Management group name.')
        c.argument(
            'subscription_id',
            options_list=('--subscription-id', '-s'),
            help='Subscription id.')
        c.argument(
            'resource_group_name',
            options_list=('--resource-group-name', '-rg'),
            arg_type=resource_group_name_type,
            completer=get_resource_group_completion_list,
            help='Resource group name.')
        c.argument(
            'resource_id',
            options_list=('--resource-id', '-r'),
            help='Resource id.')
        c.argument(
            'policy_set_definition_name',
            options_list=('--policy-set-definition-name', '-ps'),
            completer=get_policy_set_completion_list,
            help='Policy set definition name.')
        c.argument(
            'policy_definition_name',
            options_list=('--policy-definition-name', '-pd'),
            completer=get_policy_completion_list,
            help='Policy definition name.')
        c.argument(
            'policy_assignment_name',
            options_list=('--policy-assignment-name', '-pa'),
            completer=get_policy_assignment_completion_list,
            help='Policy assignment name.')
        c.argument(
            'from_value',
            options_list=('--from', '-from'),
            help='Timestamp specifying the start time of the interval to query.')
        c.argument(
            'to_value',
            options_list=('--to', '-to'),
            help='Timestamp specifying the end time of the interval to query.')
        c.argument(
            'top_value',
            options_list=('--top', '-top'),
            type=int,
            help='Maximum number of records to return.')
        c.argument(
            'order_by_clause',
            options_list=('--order-by', '-ob'),
            help='Ordering expression using OData notation.')
        c.argument(
            'select_clause',
            options_list=('--select', '-sl'),
            help='Select expression using OData notation.')
        c.argument(
            'filter_clause',
            options_list=('--filter', '-f'),
            help='Filter expression using OData notation.')
        c.argument(
            'apply_clause',
            options_list=('--apply', '-a'),
            help='Apply expression for aggregations using OData notation.')

    with self.argument_context('policy state summarize') as c:
        c.ignore('all_results')
        c.ignore('order_by_clause')
        c.ignore('select_clause')
        c.ignore('apply_clause')
