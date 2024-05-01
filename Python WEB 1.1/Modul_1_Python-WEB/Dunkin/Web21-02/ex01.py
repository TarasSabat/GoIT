from abc import abstractmethod, ABC


class ApiService(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def invoke(self):
        pass


class AuthService(ABC):
    @abstractmethod
    def auth(self):
        pass
    
# api_service = ApiService()


# print(api_service)

class GitHubService(ApiService, AuthService):
    def connect(self) -> str:
        return "Connect to GitHub"

    def invoke(self):
        return "Invoke something"
    
    def auth(self):
        return "Authenticate to GitHub"


class Bitbucket(ApiService, AuthService):
    def connect(self):
        return "Connect to Bitbucket"
    
    def invoke(self):
        return "Invoke something on Bitbucket"
    
    def auth(self):
        return "Authenticate to Bitbucket"


github = GitHubService()

gh_connect = github.connect()

bitbucket = Bitbucket()

bt_connect = bitbucket.connect()

# print(gh_connect)

# print(bt_connect)

# print(bitbucket.auth())


for service in github, bitbucket:
    print(service.auth())