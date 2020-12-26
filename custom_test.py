import twint


class MastersCrawler:
    def __init__(self):
        self.config = twint.Config()
        self.config.Store_object = True
        self.config.User_full = True
        self.config.Username = "barackobama"  # TODO: search for hashtags
        self.config.Resume = "resume.txt"
        self.config.Database = "/private/var/www/masters/storage/tweets.db"  # TODO: dynamic name based on stack and YYYYMM

    def run(self):
        twint.run.Search(self.config)


crawler = MastersCrawler()
crawler.run()
