#!/usr/bin/python3
from proxy_sources.proxy_sources import ScraperPlexor
from proxy_checker.proxy_checker import ProxyChecker

# create a bucket for later
proxy_list = list()

# send out the minion
# request is not async yet but return is.
for proxy in ScraperPlexor.get_proxies():
    print( proxy )
    proxy_list.append(proxy)

# de-dupe
proxy_list = list( set(proxy_list) )

# async checks of each result so that the final list only has
# confirmed proxies.  if request takes longer than 1 second it will
# not be added to the list.
for proxy in ProxyChecker.check_proxies(proxy_list, 8):
    print(proxy)