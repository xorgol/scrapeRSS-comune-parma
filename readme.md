Quick script for creating an RSS Feed for the [news section of the Comune di Parma](https://www.comune.parma.it/it/novita/notizie).
Right now it completely omits images and the creation dates for each news item.
Only the latest 12 items are read. I should scan the whole archive, or simply append to an existing file.
The result is just printed, I simply use output redirection to get a file.
I'm running this script once an hour on my server, you should be able to point your RSS feed reader there:
https://adrianofarina.it/pyRSS/comune.rss

In order to run the script on a schedule I'm using good old cron. If you want to do the same, just open your crontab with 'crontab -e'
Then write in:
'''0 0 * * * * python path/to/python/script.py > path/to/output.rss'''