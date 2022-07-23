from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.reverse import reverse


# noinspection PyUnresolvedReferences
class ActionListMixin:

    def actions(self, request, *args, **kwargs):
        ret = OrderedDict()
        namespace = request.resolver_match.namespace

        list_actions = (_action for _action in self.get_extra_actions() if not _action.detail)
        for extra_action in list_actions:
            key = extra_action.url_name
            url_name = f'{self.basename}-{extra_action.url_name}'

            if namespace:
                url_name = namespace + ':' + url_name

            ret[key] = reverse(
                url_name,
                args=args,
                kwargs=kwargs,
                request=request,
                format=kwargs.get('format')
            )

        return Response(ret)
