from ..repositories.RepositoryGateway import RepositoryGatewayImpl


def local_repository_gateway(name):
    """
    Method that create a repository with only the local one set, ignoring the remote
    repository creation
        Parameters:
            name (string): The name of the database to create (or access to)

        Returns:
            repository: the repository created
    """
    return RepositoryGatewayImpl(name)


def complete_gateway_not_sync(name, url, queue):
    """
    Method that create a complete repository (both local and remote) with the
    remote one not synchronized
        Parameters:
            name (string): The name of the database to create (or access to)
            url (string): The url of the remote database location
            queue (queue): The queue to use for the remote repository where to put all the remote requests to send

        Returns:
            repository: the repository created
    """
    basic_repo_gw = RepositoryGatewayImpl(name)
    basic_repo_gw.set_remote(url, queue)
    return basic_repo_gw


def complete_gateway_sync(name, url, queue):
    """
    Method that create a complete repository (both local and remote) with the
    remote one synchronized
        Parameters:
            name (string): The name of the database to create (or access to)
            url (string): The url of the database location
            queue (queue): The queue to use for the remote repository where to put all the remote requests to send

        Returns:
            repository: the repository created
    """
    basic_repo_gw = RepositoryGatewayImpl(name)
    basic_repo_gw.set_remote(url, queue)
    basic_repo_gw.sync_remote()
    return basic_repo_gw
