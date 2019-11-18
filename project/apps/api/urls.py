from django.urls import path

from .views import RepositoryList

app_name = 'api'

urlpatterns = [
    path(
        'repository/<githubUser>',
        RepositoryList.as_view(),
        name='repositoryGithubUser'
    )
    #path(
    #    'repository/<githubUser>/<githubRepos>/commits',
    #    CommitsReposDetail.as_view(),
    #    name='commitsRepositoryGithubUser'
    #)
]
