import twint


def should_continue():
    # TODO: notify that the current job is being worked on

    # TODO: check if the spot instance doesn't contain metadata for termination time
    #   return requests.get("http://169.254.169.254/latest/meta-data/spot/termination-time").status_code != 200
    return False


class MastersCrawler:
    def __init__(self):
        self.config = twint.Config()
        self.config.Store_object = True
        self.config.User_full = True
        self.config.Username = "barackobama"  # TODO: search for hashtags
        self.config.Hashtags = True
        # self.config.Username = "macz_a"
        self.config.Resume = "resume.txt"
        # self.config.Hide_output = True
        self.config.Should_continue = should_continue
        self.directory = None

    def run(self):
        twint.run.Search(self.config)


crawler = MastersCrawler()
crawler.run()
