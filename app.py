from flask import Flask, render_template, request
import praw

app = Flask(__name__)

reddit = praw.Reddit(
    client_id="2rt7E07Jz8zufkMSOqJCow",
    client_secret="mhoig-kFZSeUm27nQtqha932m2Dz_A",
    user_agent="subreddit image scraper by u/Money_Tangerine1471",
)

@app.route("/", methods=["GET", "POST"])
def index():
    subreddit_name = request.form.get("subreddit")

    if subreddit_name:
        subreddit = reddit.subreddit(subreddit_name)
        submissions = subreddit.top(limit=10)  # You can adjust the limit as needed

        image_urls = []
        for submission in submissions:
            if submission.url.endswith((".jpg", ".jpeg", ".png", ".gif")):
                image_urls.append(submission.url)

        return render_template("index.html", image_urls=image_urls, subreddit_name=subreddit_name)

    return render_template("index.html", image_urls=None, subreddit_name=None)

if __name__ == "__main__":
    app.run(debug=True)
