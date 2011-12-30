class Response:
    @classmethod
    def http(self, code, result=""):
        code.write(result)
        return code