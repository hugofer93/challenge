import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from .githubApiUrls import REPOS_RESOURCE as GITHUB_REPOS_RESOURCE


class RepositoryList(APIView):
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        # Get param in url conf
        githubUser = kwargs.get('githubUser')

        # request to Github's Api
        GithubApiResponse = requests.get(
            GITHUB_REPOS_RESOURCE.format(githubUser)
        )

        if GithubApiResponse.status_code == 200:
            # Obtain Json Response from Github's Api
            data = GithubApiResponse.json()
            print(GITHUB_REPOS_RESOURCE.format(githubUser))

            # Keys from Github's response
            keyList = ['name', 'created_at']

            # Function to delete unnecessary data
            getData = lambda obj: {key: obj[key] for key in keyList}

            # Map data and send Json Response
            data = map(getData, data)
        else:
            data = data = GithubApiResponse.json()
        status = GithubApiResponse.status_code
        return Response(data=data, status=status)
