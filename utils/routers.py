from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    """
    Enhanced router that can combine multiple routers registries.
    """

    def extend(self, router: routers.BaseRouter):
        self.registry.extend(router.registry)
