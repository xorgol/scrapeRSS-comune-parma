Quick script for creating an RSS Feed for the [news section of the Comune di Parma](https://www.comune.parma.it/it/novita/notizie).
Right now it completely omits images and the creation dates for each news item.
Only the latest 12 items are read. I should scan the whole archive, or simply append to an existing file.
The result is just printed, I simply use output redirection to get a file.
I'm running this script twice a day on my server, you should be able to point your RSS feed reader there:
https://adrianofarina.it/pyRSS/comune.rss
However the first run is at 03:00, and I'm not staying up that long :D