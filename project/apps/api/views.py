import json
import requests
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import LastRequestReposGithubApi
from .githubApiUrls import (
    REPOS_RESOURCE as GITHUB_REPOS_RESOURCE,
    COMMIT_REPOS_RESOURCE as GITHUB_COMMIT_REPOS
)


class RepositoryList(APIView):
    http_method_names = ('get',)

    def saveRequestGithubApi(self, user, githubUser, url, lastTenRepos):
        # Save user and requests
        obj, _ = LastRequestReposGithubApi.objects.get_or_create(
            user=user
        )

        # Add last url
        githubApiUrls = json.loads(obj.githubApiUrls)
        githubApiUrls += [{
            'url': url,
            'date': str(datetime.now())
        }]
        obj.githubApiUrls = json.dumps(githubApiUrls)

        # Add last ten repos
        lastTenReposSent = json.loads(obj.lastTenReposSent)
        lastTenReposSent += [
            {'repo': githubUser+'/'+repo['name']} for repo in lastTenRepos
        ]
        lastTenReposSent = lastTenReposSent[-10:]
        obj.lastTenReposSent = json.dumps(lastTenReposSent)
        obj.save()

    def get(self, request, *args, **kwargs):
        # Get param in url conf
        githubUser = kwargs.get('githubUser')

        # request to Github's Api
        githubApiUrl = GITHUB_REPOS_RESOURCE.format(githubUser)
        GithubApiResponse = requests.get(githubApiUrl)

        if GithubApiResponse.status_code == 200:
            # Obtain Json Response from Github's Api
            data = GithubApiResponse.json()

            # Keys from Github's response
            keyList = ['name', 'created_at']

            # Function to delete unnecessary data
            getData = lambda obj: {key: obj[key] for key in keyList}

            # Map data and send Json Response
            data = map(getData, data)

            repos = list(data)

            self.saveRequestGithubApi(
                user=request.user,
                githubUser=githubUser,
                url=githubApiUrl,
                lastTenRepos=repos[-10:]
            )

            for index, repo in enumerate(repos):
                # Get Commit for each repos
                response = requests.get(
                    GITHUB_COMMIT_REPOS.format(githubUser, repo['name'])
                )
                # Validation for requests exceeded
                # Response if requests exceeded, the rest is empty
                if response.status_code is not 200:
                    break

                # Clear Github's Json Response
                dateLastCommit = response.json()
                dateLastCommit = dateLastCommit['commit']
                dateLastCommit = dateLastCommit['commit']
                dateLastCommit = dateLastCommit['author']
                dateLastCommit = dateLastCommit['date']
                # Add key, value to the data
                repos[index]['last_commit'] = dateLastCommit
            data = repos
        else:
            data = GithubApiResponse.json()
        status = GithubApiResponse.status_code
        return Response(data=data, status=status)
