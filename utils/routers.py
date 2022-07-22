from collections import OrderedDict

from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    """
    Enhanced router that can combine multiple routers registries.
    Also provides self documented action lists.
    """

    routes = routers.DefaultRouter.routes[:1] + [
        routers.Route(
            url=r'^{prefix}/actions{trailing_slash}$',
            mapping={
                'get': 'actions',
            },
            name='{basename}-actions',
            detail=False,
            initkwargs={'suffix': 'Actions'}
        ),
    ] + routers.DefaultRouter.routes[1:]

    def extend(self, router: routers.BaseRouter):
        self.registry.extend(router.registry)

    def get_api_root_view(self, api_urls=None):
        # From DefaultRouter
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        actions_name = self.routes[1].name

        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

            # Override
            api_root_dict[f'{prefix} actions'] = actions_name.format(basename=basename)

        # From Default Router
        return self.APIRootView.as_view(api_root_dict=api_root_dict)
