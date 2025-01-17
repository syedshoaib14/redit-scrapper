reddit = praw.Reddit(client_id = "uRyb_TFqvN7MbTU0cntBug",
            client_secret = "VAF_xUr-Q6h1JoZG-M8WE2RnLG8XlA",
            username = 'boyboyboi3',
            password = 'redditpassword03',
            redirect_uri = "http://localhost:8080",
            user_agent = "script by u/boyboyboi3",
            check_for_async=False)

def scrape_reddit(subreddit: str, limit = 10, sortby = 'year', show_safe = None):
  sub = reddit.subreddit(subreddit)
  result = []
  sub_itter = sub.top(sortby,limit = limit)
  for submission in tqdm(sub_itter):
    d = {}
    d['id'] = submission.id
    d['title'] = submission.title
    d['num_comments'] = submission.num_comments
    d['score'] = submission.score
    d['upvote_ratio'] = submission.upvote_ratio
    d['date'] = datetime.fromtimestamp(submission.created_utc)
    d['domain'] = submission.domain
    d['nsfw'] = submission.over_18
    try: d['image'] = submission.preview["images"][0]["source"]["url"]
    except: d['image'] = None
    try: d['author'] = submission.author.name
    except: d['author'] = 'Not Found'
    if show_safe == True and d['nsfw'] == True: d={}
    if show_safe == False and d['nsfw'] == False: d={}
    result.append(d)
  result = [item for item in result if item]
  return pd.DataFrame(result)
