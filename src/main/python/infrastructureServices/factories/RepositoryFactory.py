from ..repositories.RepositoryGateway import RepositoryGatewayImpl


def local_repository_gateway(name):
    return RepositoryGatewayImpl(name)


def complete_gateway_not_sync(name, url, queue):
    basic_repo_gw = RepositoryGatewayImpl(name)
    basic_repo_gw.set_remote(url, queue)
    return basic_repo_gw


def complete_gateway_sync(name, url, queue):
    basic_repo_gw = RepositoryGatewayImpl(name)
    basic_repo_gw.set_remote(url, queue)
    basic_repo_gw.sync_remote()
    return basic_repo_gw
