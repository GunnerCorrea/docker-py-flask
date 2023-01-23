#from flask import request, redirect
from flask import request, redirect

import re

class Redirect:

    def filter(self):

        # get query string (request)
        args = request.args
        url = args.get('url')

        # check if url query not exists
        if url is None:
            return self.redirect_home()

        id = self.get_id(url)

        if(id == -1):
          return self.redirect_home()

        return id

    def redirect_home(self):
        #if env['to_home'] == true:
        return redirect("https://oglobo.globo.com/", code=308)

    def redirect_to(self, url):
        return redirect(url, code=308)

    def get_id(self, url):

        result = re.search('htt.+?-([0-9]{1,})', url)

        id = result.group(1)
        
        if id is None:
            return -1

        return id
