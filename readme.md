Quick script for creating an RSS Feed for the [news section of the Comune di Parma](https://www.comune.parma.it/it/novita/notizie).
Right now it completely omits images and the creation dates for each news item.
Only the latest 12 items are read. I should scan the whole archive, or simply append to an existing file.
The result is just printed, I simply use output redirection to get a file.
I'm running this script once an hour on my server, you should be able to point your RSS feed reader there:
https://adrianofarina.it/pyRSS/comune.rss

In order to run the script on a schedule I'm using good old cron. If you want to do the same, just open your crontab with `crontab -e`
Then write in:
```0 0 * * * * python path/to/python/script.py > path/to/output.rss```

# Different municipalities
It turns out that the government has upgraded most local government websites to this standardized [Bootstrap Italia](https://italia.github.io/bootstrap-italia/) system. That means that they're mostly all the same, so we can scrape the data to get RSS feed from all of them with just a few changes. There are some implementation differences between websites that I should address properly. The whole thing needs a refactor, I need to include temporal information for each item and create proper archives. However, for now I've just added a command line parameter allowing users to specify an URL, of the form https://www.comune.parma.it/it/novita/notizie or https://www.comune.re.it/novita/notizie. Notice that the Reggio version does not have a language nesting level, similar discrepancies are to be expected in each implementation, but the overall scraping seems to work decently enough.

Without command line parameters the script generates the feed for the Comune di Parma. In order to use it for another municipality use the URL of its news page as the first parameter. For example, in order to generate the feed for the Comune di Reggio Emilia use:
```python3 selenium101.py https://www.comune.re.it/novita/notizie > reggio.rss```

I've tested with a handful of sites and I've only had a complete failure with some small mountain municipality which had awful response times, and with Bologna, because they have their own web design. However I've also noticed that some municipalities, like [Piacenza](https://www.comune.piacenza.it/it/feeds) and [Modena](http://www.comune.modena.it/salastampa/comunicati/RSS), do the smart thing, and already have proper RSS feeds. Kudos to them!