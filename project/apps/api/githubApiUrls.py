# CONTANTS URI's

# REST API GITHUB
API_GITHUB = 'https://api.github.com'

# USERS GITHUB - add Github username
# https://api.github.com
USER_RESOURCE = API_GITHUB + '/users/{}'

# REPOSITORIES USER GITHUB - add Github username
# https://api.github.com/users/{}
REPOS_RESOURCE = USER_RESOURCE + '/repos'

# REPOSITORY DETAIL GITHUB - add Github username and repository's name
# https://api.github.com
DETAIL_REPOS_RESOURCE = API_GITHUB + '/repos/{}/{}'

# COMMITS REPOSITORY GITHUB - add Github username and repository's name
# https://api.github.com/repos/{}/{}
COMMIT_REPOS_RESOURCE = DETAIL_REPOS_RESOURCE + '/branches/master'
